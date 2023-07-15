from tkinter import *
from tkinter import ttk, filedialog
import splitter
import silencer
import converter

def run_silencer():
    try:
        src_dir = filedialog.askdirectory(title="Source Directory")
        dst_dir = filedialog.askdirectory(title="Destination Directory")
        if src_dir != None and dst_dir != None:
            silencer.run(src_dir, dst_dir)
    except Exception as err:
        print(err)
    
def run_splitter():
    try:
        src_dir = filedialog.askdirectory(title="Source Directory")
        splitter.run(src_dir)
    except Exception as err:
        print(err)


def run_converter():
    try:
        src_dir = filedialog.askdirectory(title="Source Directory")
        dst_dir = filedialog.askdirectory(title="Destination Directory")
        if src_dir != None and dst_dir != None:
            converter.run(src_dir, dst_dir)
    except Exception as err:
        print(err)



def main():
    root = Tk()
    root.maxsize(200, 200)
    frm = ttk.Frame(root, padding=10, width=200, height=20)
    # frm.grid()
    splitter_button = ttk.Button(frm, text="Splitter", command=run_splitter)
    splitter_button.pack(padx=10, pady=10)
    silencer_button = ttk.Button(frm, text="Silencer", command=run_silencer)
    silencer_button.pack(padx=10, pady=10)
    converter_button = ttk.Button(frm, text="Converter", command=run_silencer)
    converter_button.pack(padx=10, pady=10)
    frm.pack(padx=10, pady=10)
    root.mainloop()


if __name__ == '__main__':
    main()