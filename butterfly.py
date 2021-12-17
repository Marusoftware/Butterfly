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
            if self.args.command is None:
                try:
                    return UI.GUI(self.args)
                except:
                    try:
                        return UI.TUI(self.args)
                    except:
                        return UI.SHELL(self.args)
            else:
                UI.CUI(self.args)
        elif ui == "tui":
            return UI.TUI(self.args)
        elif ui == "shell":
            return UI.SHELL(self.args)
        elif ui == "gui":
            return UI.GUI(self.args)
        elif ui == "socket":
            return UI.SOCKET(self.args)
        elif ui == "API":
            return UI.API_SOCKET(self.args)
        else:
            return
    class TUI():
        def __init__(self, args):
            import curses
            curses.wrapper(self.main)
        def main(self):
            pass

    class CUI():
        def __init__(self, args):
            pass

    class SHELL():
        def __init__(self, args):
            pass

    class GUI():
        def __init__(self, args):
            self.logger=logging.getLogger(name="GUI")
            self.args = args
            self.main()
        def main(self):
            import tkinter
            from tkinter import ttk
            self.root = tkinter.Tk()
            self.root.title("Marusoftware - Butterfly")
            self.logger.info("Started.")
            #self.root.iconphoto(True, tkinter.PhotoImage(file="./"))
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
        self._logging()
        if self.args.daemon:
            pass#todo:daemon start code
        else:
            self.logger.info(f'Starting UI({self.args.ui})...')
            self.ui = UI(args=self.args)
            self.ui.startUI(ui=self.args.ui)
            self.logger.info("UI stopped.")
            self.logger.info("Exit Butterfly. Good Bye!")
    
    def _argparse(self):
        self.arg_parser = argparse.ArgumentParser()
        self.arg_parser.main = self.arg_parser.add_argument_group("MAIN")
        parser = self.arg_parser.main
        parser.add_argument("--disable-pyvercheck", action="store_true", dest="dispyvchk")
        parser.add_argument("--version", action="version", version="")
        parser.add_argument("-ui", action="store", type=str, dest="ui", default="auto", choices=["auto","tui","shell","gui","socket","API"])
        parser.add_argument("-daemon", action="store_true", dest="daemon")
        parser.add_argument("command", nargs="?", default=None, type=str)
        parser.add_argument("packages", nargs="*", default=None, type=str)
        self.arg_parser.log = self.arg_parser.add_argument_group("LOG")
        parser=self.arg_parser.log
        parser.add_argument("-log_dir", action="store", type=str, dest="log_dir")
        parser.add_argument("-log_path", action="store", type=str, dest="log_path")
        parser.add_argument("-log_level", action="store", type=int, dest="log_level", default=20)#todo:stdoutlog
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