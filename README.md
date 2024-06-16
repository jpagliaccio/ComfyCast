# ComfyCast
A ComfyUI node to cast images to chromecast devices 


![ComfyCast_cast_images_node_screenshot](https://github.com/jpagliaccio/ComfyCast/assets/7680161/2c482f0a-2b1d-472a-bf5e-7ce3d245d761)


Install:

    1) Install the pychromecast library 
        eg: pip install pychromecast 

    2) Make a web image directory "your ComfyUI home"/web/images
        eg: /opt/ComfyUI/web/images
      
    3) Copy the ComfyCast folder to your "your ComfyUI home"/custom_nodes directory  
        eg: /opt/ComfyUI/custom_nodes/ComfyCast

Use:

    Start the ComfyUI server with the --listen option:
        eg: python /opt/ComfyUI/main.py --listen
        The --listen arg makes the cast_image.png accessable from the chromecast devices on your network.

    Add the node:
        Right-click, "Add Node", "image", "Cast Images" 

    To test:
        Browse the image file from another machine on your network
        eg: http://192.168.1.???:8188/images/cast_image.png 

Requirements:

  * ComfyUI - https://github.com/comfyanonymous/ComfyUI
  * Pychromecast 
