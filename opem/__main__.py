# -*- coding: utf-8 -*-

from .Static.Amphlett import Static_Analysis as Amphlett_Analysis
from .Static.Larminie_Dicks import Static_Analysis as Larminiee_Analysis
from .Static.Chamberline_Kim import Static_Analysis as Chamberline_Kim_Analysis
from .Dynamic.Padulles1 import Dynamic_Analysis as Padulles1_Analysis
from art import tprint
import doctest
import sys
import argparse
from .gui.mainwindow import *

Version=0.3

def parse_args():
    parser = argparse.ArgumentParser(description="This is OPEM")
    parser.add_argument(
        '-g', '--gui',
        help='Using this option will show GUI for the OPEM',
        action='store_true'
    )
    parser.add_argument(
        '-t', '--test',
        help='Run the test cases',
        action='store_true'
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    app = None
    Menu={"Amphlett_Analysis (Static)":Amphlett_Analysis,"Larminiee_Analysis (Static)":Larminiee_Analysis,
          "Chamberline_Kim_Analysis (Static)":Chamberline_Kim_Analysis,"Padulles_Analysis I (Dynamic)":Padulles1_Analysis}
    MenuKeys = list(Menu.keys())

    MenuKeys.sort()

    if args.test:   # RUN Test
        doctest.testfile("test.py", optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    elif args.gui:  # RUN With GUI
        app = QApplication(sys.argv)
        a = MainWindow(Menu)
        a.show()
    else:           # RUN Normal
        ExitFlag = False
        while not ExitFlag:
            tprint("OPEM")
            tprint("v" + str(Version))
            for i, item in enumerate(MenuKeys):
                print(str(i + 1) + "-" + item)
            # noinspection PyBroadException
            try:
                AnalysisIndex = int(input("Please Choose Analysis : "))
            except:
                AnalysisIndex = -1
            if AnalysisIndex - 1 in range(len(MenuKeys)):
                Menu[MenuKeys[AnalysisIndex - 1]]()
                InputIndex = input("Press [R] to restart OPEM or any other key to exit.")
                if InputIndex.upper() != "R":
                    ExitFlag = True

    if app is not None:
        sys.exit(app.exec_())
