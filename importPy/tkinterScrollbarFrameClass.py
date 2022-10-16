from tkinter import *
from tkinter import ttk

class ScrollbarFrame():
    def __init__(self, parent, v_select, btnList):
        self.v_select = v_select
        self.btnList = btnList
        
        self.frame = ttk.Frame(parent)
        self.frame.pack(expand=True, fill=BOTH)

        self.tree = ttk.Treeview(self.frame, selectmode="browse")

        self.scrollbar_x = ttk.Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=lambda f, l: self.scrollbar_x.set(f, l))
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        self.scrollbar_y = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=lambda f, l: self.scrollbar_y.set(f, l))
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        self.tree.pack(expand=True, fill=BOTH)
        self.tree.bind("<<TreeviewSelect>>", self.treeSelect)

        csvExtractBtn = self.btnList[4]
        csvLoadAndSaveBtn = self.btnList[5]
        headerFileEditBtn = self.btnList[6]
        
        csvExtractBtn["state"] = "normal"
        csvLoadAndSaveBtn["state"] = "normal"
        headerFileEditBtn["state"] = "normal"
    def treeSelect(self, event):
        selectId = self.tree.selection()[0]
        selectItem = self.tree.set(selectId)

        editLineBtn = self.btnList[0]
        insertLineBtn = self.btnList[1]
        deleteLineBtn = self.btnList[2]
        copyLineBtn = self.btnList[3]
        
        editLineBtn["state"] = "normal"
        insertLineBtn["state"] = "normal"
        deleteLineBtn["state"] = "normal"
        copyLineBtn["state"] = "normal"
        
        self.v_select.set(selectItem["番号"])
