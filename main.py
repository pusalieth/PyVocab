"""
 License GPLv3 written by Pusalieth
"""

from tkinter import filedialog
from tkinter import *
import dictionary
import threading


class FILE:
    def __init__(self):
        self.root = Tk()
        self.root.filename = filedialog.askopenfilename(initialdir=".", title="Select file", filetypes=(
            ("text files", "*.txt"), ("comma-seperated-values files", "*.csv"), ("all files", "*.*")))

        frame = Frame(self.root)
        frame.pack()
        button = Button(frame, text="Start", fg="green", command=self.start_Threads)
        button.pack(side=LEFT)
        slogan = Button(frame, text="Stop", fg="red", command=self.breakLoop)
        slogan.pack(side=LEFT)
        self.loop = True
        self.root.mainloop()

    def start_Threads(self):
        self.threads = []
        self.threads.append(threading.Thread(target=self.startLoop))
        self.threads.append(threading.Thread(target=self.breakLoop))
        self.threads[0].start()
        
    def startLoop(self):
        word_list = open(self.root.filename, 'r')
        defined_list = open('%s Defined.txt' % self.root.filename[:-4], 'w')
        lookup = dictionary.GOOGLE_API()
        for line in word_list:
            line = line.rstrip()
            print(line)
            line2write = '%s - %s\n' % (line, lookup.define(line))
            defined_list.write(line2write)
            if(not self.loop):
                break
        word_list.close()
        defined_list.close()

    def breakLoop(self):
        self.loop = False
        self.threads[0].join()


if __name__ == "__main__":
    FILE()
