import os, sys

__version__ = "beta0.0.1-pre"

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

class Config():
    def __init__(self, ftype, module, fmode="default"):
        self.type = ftype
        self.module = module
        self._permition()
        if ftype == "pickle":
            pass
        elif ftype=="ini":
            pass
        else:
            raise TypeError
    def setPermittion(self, to):
        #if
        pass 
    def _permition(self):
        return 1
    class _Pickle():
        def __init__(self):
            self.config = open()
