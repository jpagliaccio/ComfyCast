# ComfyCast
A ComfyUI node to cast images to chromecast devices 

Install:

    1) Install the pychromecast library 
        eg: pip install pychromecast 

    2) Make the directory "your ComfyUI home"/web/images
        eg: /opt/ComfyUI/web/images
      
    3) Copy the cComfyCast folder to your "your ComfyUI home"/custom_nodes directory  
        eg: /opt/ComfyUI/custom_nodes/ComfyCast

Use:

    Start the ComfyUI server with the --listen option
        eg: python /opt/ComfyUI/main.py --listen
        This (--listen) makes the cast_image.png accessable from the chromecast devices on your network. 

    To test:
        Browse the image file from another machine on your network 
        http://192.168.1.???:8188/images/cast_image.png 

Requirements:

  Pillow
  Numpy
  Pychromecast 
