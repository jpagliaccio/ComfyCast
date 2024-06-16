from .comfy_cast import comfy_cast 

NODE_CLASS_MAPPINGS = {
    "Cast Image": comfy_cast,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Cast Image": "Cast Images",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
