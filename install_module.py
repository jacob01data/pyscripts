# havent used python in a long time so there might be errors
# ive been using LuaU/Lua alot

import importlib # built in
__import__ = importlib.import_module

def installer(module):
  module_or_none = None
  try:
    module_or_none = __import__(module)
  except Exception as e:
    # install it with os.system
    os = __import__("os") # built in btw
    # check to see if it is invalid module name
    try:
      os.system("pip install " + module)
    except Exception as e:
      print("Invalid module Name!")
      return None
    # once complete set
    module_or_none = __import__(module)
  return module_or_none
