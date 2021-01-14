try:
    import tkinter
    from tkinter import ttk
except:
    import Tkinter as tkinter
    import ttk
import os, argparse, sys

##Default Settings
conf = {
}

class libs():
    def get_module_Dir(module_name):
        os.path.join("",module_name)
    class Config():
        def __init__(self):
            self.config = open()

class UI():
    class TUI_CUR():
        def __init__(self):
            pass

    class TUI_CUI():
        def __init__(self):
            if input("!WARN! This UI outputs is very long! Do you want to continue? (y or n)") == "y":
                pass

    class CUI_CMD():
        def __init__(self):
            pass

    class CUI_SHELL():
        def __init__(self):
            pass

    class GUI():
        def __init__(self):
            self.root = tkinter.Tk()
            self.root.title("Marusoftware - Butterfly")

    class SOCKET():
        def __init__(self):
            pass

class CORE():
    def __init__(self, args=None):
        self.args = args
        self._argparse()
    def _argparse(self):
        #if self.args == None:
        #    self.args = None
        self.arg_parser = argparse.ArgumentParser()
        self.arg_parser.ui = self.arg_parser.add_argument_group("UI")
        parser = self.arg_parser.ui 
        def arg_ui(i):
            if i[0] == "[":
                return list(i)
            else:
                return str(i)
        parser.add_argument("-ui", action="store", type=arg_ui)
        parser.add_argument("--tui", action="store_true")
        parser.add_argument("--tui_p", action="store_true")
        parser.add_argument("--cui", action="store_true")
        parser.add_argument("--shell", action="store_true")
        parser.add_argument("--socket", action="store_true")
        parser.add_argument("--gui", action="store_false")
        self.arg_parser.parse_args(self.args)
    def _logging(self):
        self.logger

class ENVIRON():        
    class Python2():
        pass
    class Python3():
        pass

if __name__ == "__main__":
    CORE()