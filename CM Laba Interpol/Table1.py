import tkinter.ttk as ttk
import tkinter as tk

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

def Create_table1(headline,n_of_point,l1,l2,l3,l4,l5,l6):
    New_win = tk.Tk()
    New_win.title("Table of variables")
    Rows = []
    for i in range(n_of_point):
        Rows.append([])
    for k in range(n_of_point):
        Rows[k].append(k)
        Rows[k].append(l1[k])
        Rows[k].append(l2[k])
        Rows[k].append(l3[k])
        Rows[k].append(l4[k])
        Rows[k].append(l5[k])
        Rows[k].append(l6[k])

    Rows = tuple(Rows)
    table = Table(New_win, headings=headline, rows=Rows)
    table.pack(expand=tk.YES, fill=tk.BOTH)
    New_win.mainloop()

def Create_table2(headline,n_of_point,l1,l2,l3,l4,l5,l6,l7):
    New_win = tk.Tk()
    New_win.title("Table of variables")
    Rows = []
    for i in range(n_of_point):
        Rows.append([])
    for k in range(n_of_point):
        Rows[k].append("x "+"_"+str(k)+"=" +str("%.4f" % l1[k]))
        Rows[k].append(l2[k])
        Rows[k].append(l3[k])
        Rows[k].append(l4[k])
        Rows[k].append(l5[k])
        Rows[k].append(l6[k])
        Rows[k].append(l7[k])


    Rows = tuple(Rows)
    table = Table(New_win, headings=headline, rows=Rows)
    table.pack(expand=tk.YES, fill=tk.BOTH)
    New_win.mainloop()
