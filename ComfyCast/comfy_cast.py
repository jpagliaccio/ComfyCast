import os
import sys
import time
import json
import pychromecast

from PIL import Image
from PIL.PngImagePlugin import PngInfo
import numpy as np

# sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

from comfy.cli_args import args
import folder_paths

class comfy_cast:

    def __init__(self):
        self.type = "output"
        self.server_url = ""
        self.cast_device = ""
        self.wait = 2
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    {"images": ("IMAGE", ),
                     "server_url": ("STRING", {"default": "http://192.168.1.103:8188"}),
                     "cast_device": ("STRING", {"default": "Office display"}),
                     "wait": ("INT", {"default": 2}),
                     "debug_info": ("BOOLEAN", {"default": False})
                    },
                }

    @classmethod
    # ---------------------------------------------------------------------------------
    # Cast each image to the chromecast device 
    # ---------------------------------------------------------------------------------
    def cast_to_chromecast(self, image_url, chromecast_name, wait=2, sleep=False):

        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[chromecast_name])

        if not chromecasts:
            print("Chromecast device '{}' not found.".format(chromecast_name))
            return

        cast_device = chromecasts[0]
        cast_device.wait()
        cast_device.quit_app() # or it will hang 
        cast_device.wait()
        mc = cast_device.media_controller
        mc.play_media(image_url + "?_=" + str(int(time.time())) , "image/png")
        mc.block_until_active() # Don't mc.stop() - let run till timeout 
        
        if sleep:
            time.sleep(wait)
        pass 


    RETURN_TYPES = ()
    FUNCTION = "cast_images"
    OUTPUT_NODE = True
    CATEGORY = "image"

    # --------------------------------------------------------------------------------------------------------------
    # For each image returned save the web cast image and then call the cast 
    # --------------------------------------------------------------------------------------------------------------
    def cast_images(self, images, server_url, cast_device="not set", wait=2, debug_info=False, prompt=None, extra_pnginfo=None):
    
        results = list()

        for (batch_number, image) in enumerate(images):

            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = None
            if not args.disable_metadata:
                metadata = PngInfo()
                if prompt is not None:
                    metadata.add_text("prompt", json.dumps(prompt))
                if extra_pnginfo is not None:
                    for x in extra_pnginfo:
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))

            if debug_info:
                print(f"The batch number {batch_number}") 

            try: 
                home_dir = os.path.dirname(folder_paths.get_output_directory()) # the parent of the current 

                if debug_info:
                    print("ComfyUI home is", home_dir)

                web_dir = os.path.join(home_dir, "web/images")

                if os.path.exists(web_dir):
                    if debug_info:
                        print("The img file will be copied to the web_dir:", web_dir)
                else:
                    print("*** error: remember to create the web image directory:", web_dir)

            except Exception as e:
                print("*** We had an error:", e)
                pass

            file = "cast_image.png"
            if debug_info:
                print("Image file:", file)
           
            # Save the image to a web directory for http access  
            # ------------------------------------------------------------
            img.save(os.path.join(web_dir, file), pnginfo=metadata, compress_level=self.compress_level)

            if debug_info:
                print("Cast device", cast_device, "Image count", len(images)) 

            image_url = server_url + "/images/" + file

            if batch_number < len(images)-1:
                sleep = True
            else:
                sleep = False

            # The cast 
            # ------------------------------------------------------------
            self.cast_to_chromecast(image_url, cast_device, wait, sleep)
            
            results.append({
                "filename": file,
                "cast_device": self.cast_device,
                "type": self.type
            })
          
        return { }

