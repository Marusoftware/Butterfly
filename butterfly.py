import os, sys
import argparse, configparser, logging
import libbutterfly

__version__ = "beta0.0.1-pre"

##Default Settings
conf = {
}

class UI():
    class TUI_CUR():
        def __init__(self):
            pass

    class TUI_CUI():
        def __init__(self):
            if input("!WARN! The outputs of this UI is very long! Do you want to continue? (y or n)") == "y":
                pass

    class CUI_CMD():
        def __init__(self):
            pass

    class CUI_SHELL():
        def __init__(self):
            pass

    class GUI():
        def __init__(self):
            import tkinter
            from tkinter import ttk
            self.root = tkinter.Tk()
            self.root.title("Marusoftware - Butterfly")

    class SOCKET():
        def __init__(self):
            pass

    class API_SOCKET():
        def __init__(self):
            pass

class DAEMON():
    def __init__(self):
        pass

class CORE():
    def __init__(self, args=None):
        self.args = args
        self._argparse()
        if sys.version_info[0] < 3 or sys.version_info[1] < 5: # python version check
            print("Error: Python version is too old! If you want to continue, please use '--disable-pyvercheck'", file=sys.stderr)
            print(sys.version, file=sys.stderr)
            if not self.args.dispyvchk: sys.exit(1)
        if self.args.version:
            print(__version__)
            sys.exit()
        self._logging()#todo:daemon start code
        self.logger.info("Starting UI...")#todo:ui start code
        if self.args.ui == "auto":
            pass
        else:
            self.logger.info("Started UI "+self.args.ui)
    
    def _argparse(self):
        self.arg_parser = argparse.ArgumentParser()
        self.arg_parser.main = self.arg_parser.add_argument_group("MAIN")
        parser = self.arg_parser.main
        parser.add_argument("--disable-pyvercheck", action="store_true", dest="dispyvchk")
        parser.add_argument("--version", action="store_true", dest="version")
        self.arg_parser.log = self.arg_parser.add_argument_group("LOG")
        parser.add_argument("-log_dir", action="store", type=str, dest="log_dir")
        parser.add_argument("-log_path", action="store", type=str, dest="log_path")
        parser.add_argument("-log_level", action="store_true", dest="log_level")#todo:stdoutlog
        parser.add_argument("-ui", action="store", type=str, dest="ui", default="auto")
        self.args = self.arg_parser.parse_args(self.args)
    def _logging(self):
        if self.args.log_path != None:
            pass
        logging.basicConfig(format='%(levelname)s(%(asctime)s,%(name)s): %(message)s', level=self.args.log_level)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Start Logging")

class ENVIRON():
    def __init__(self):
        pass

if __name__ == "__main__":
    CORE()