import os, sys, pickle, json

__version__ = "beta0.0.1-pre"

standaloned=0

class Butterfly():
    def __init__(self):
        pass
class Package():
    def __init__(self):
        self.sptxt = "."
    def version(self, module):
        module = module.split(self.sptxt)
    def install(self, module):
        module = module.split(self.sptxt)
    def uninstall(self, module):
        module = module.split(self.sptxt)
    def addsource(self, source):
        source = source.split(self.sptxt)
    #def build(self, module):
    #    module = module.split(self.sptxt)

class Dir():
    def __init__(self):
        self.base_dir = ""
    def get_module_Dir(self, module_name):
        os.path.join(self.base_dir ,module_name)
    def get_globalconf_Dir(self):
        return 

class Exception():
    class InvalidConfig(Exception): pass

class _Config():
    def __init__(self, module_name, mode="r"):
        global standaloned
        self.mode = mode
        self.module = module_name
        self.userconf={}
        self.bflyconf={}
        self.moduleconf={}
        self.standaloned = os.path.exists("./standalone")
        standaloned = self.standaloned
        if "r" in self.mode:
            if os.path.exists("./bfly_config.pickle"):
                try:
                    conf = pickle.load(open("./bfly_config.pickle", "rb"))
                except:
                    raise 
            elif os.path.exists("./bfly_config.json"):
                conf = json.load(open("./bfly_config.json", "rb"))
            else:
                conf = None
            if conf:
                if "bfly" in conf:
                    self.bflyconf = conf["bfly"]
                    if "userconf" in self.bflyconf:
                        if self.bflyconf["userconf"] == "__this__":
                            self.userconf = conf["user"]
                        elif os.path.exists(self.bflyconf["userconf"]):
                            self.userconf=pickle.load(open(self.bflyconf["userconf"], "r"))
        else:
            raise TypeError
