import os
cwd = os.getcwd()
instance = "default"
print os.path.join(cwd, instance, "media")
