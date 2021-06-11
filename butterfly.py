import os, sys
import argparse, configparser, logging
import libbutterfly

__version__ = "beta0.0.1-pre"

##Default Settings
conf = {
}

class UI():
    def __init__(self, args):
        self.args = args
    def startUI(self, ui):
        if ui == "auto":
            try:
                return UI.GUI()
            except:
                
                try:
                    return UI.TUI()
                except:
                    return UI.SHELL()
        elif ui == "tui":
            return UI.TUI()
        elif ui == "shell":
            return UI.SHELL()
        elif ui == "gui":
            return UI.GUI()
        elif ui == "socket":
            return UI.SOCKET()
        elif ui == "API":
            return UI.API_SOCKET()
        else:
            return
    class TUI():
        def __init__(self):
            import curses
            curses.wrapper(self.main)
        def main(self):
            pass

    class CUI():
        def __init__(self):
            pass

    class SHELL():
        def __init__(self):
            pass

    class GUI():
        def __init__(self):
            self.logger=logging.getLogger(name="GUI")
            import tkinter
            from tkinter import ttk
            self.root = tkinter.Tk()
            self.root.title("Marusoftware - Butterfly")
            self.logger.info("Started.")
            self.root.mainloop()

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
        self._logging()
        if self.args.daemon:
            pass#todo:daemon start code
        else:
            self.logger.info(f'Starting UI({self.args.ui})...')
            self.ui = UI()
            self.ui.startUI(ui=self.args.ui)
            self.logger.info("UI stopped.")
            self.logger.info("Exit Butterfly. Good Bye!")
    
    def _argparse(self):
        self.arg_parser = argparse.ArgumentParser()
        self.arg_parser.main = self.arg_parser.add_argument_group("MAIN")
        parser = self.arg_parser.main
        parser.add_argument("--disable-pyvercheck", action="store_true", dest="dispyvchk")
        parser.add_argument("--version", action="version", version="")
        self.arg_parser.log = self.arg_parser.add_argument_group("LOG")
        parser.add_argument("-log_dir", action="store", type=str, dest="log_dir")
        parser.add_argument("-log_path", action="store", type=str, dest="log_path")
        parser.add_argument("-log_level", action="store_true", dest="log_level")#todo:stdoutlog
        parser.add_argument("-ui", action="store", type=str, dest="ui", default="auto", choices=["auto","tui","shell","gui","socket","API"])
        parser.add_argument("-daemon", action="store_true", dest="daemon")
        parser.add_argument("command", required=False)
        parser.add_argument("packages", required=False, nargs="*")
        self.args = self.arg_parser.parse_args(self.args)
    def _logging(self):
        if self.args.log_path != None:
            pass
        logging.basicConfig(format='%(levelname)s(%(asctime)s/%(name)s): %(message)s', level=self.args.log_level)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Start Logging")

class ENVIRON():
    def __init__(self):
        pass

if __name__ == "__main__":
    CORE()