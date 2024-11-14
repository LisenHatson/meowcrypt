import sys
from gui import MeowCryptGUI
import tkinter as tk

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        from cli import cli
        cli()
    else:
        root = tk.Tk()
        app = MeowCryptGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()
