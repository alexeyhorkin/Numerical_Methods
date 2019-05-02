import tkinter as tk
import matplotlib.pyplot as plt
import Table as Tbl
import numpy as np
from Functions import *

def Initialize(e1,e2,e3,e4):
	n = e1.get()
	m = e2.get()
	eps = e3.get()
	N_MAX = e4.get()
	if n !='':
		n = int(n)
	else:
		n = 0
	if m!='':
		m = int(m)
	else:
		m = 0.0
	
	if eps!='':
		eps = float(eps)
	else:
		eps = 0.0
	
	if N_MAX!='':
		N_MAX = int(N_MAX)
	else:
		N_MAX = 0.0
	return (n,m,eps,N_MAX)


root = tk.Tk()
root.configure(background='#9cb8e5')
root.geometry("680x700")
root.title("DIRIXLE")
l1 = tk.Label(root, text = "Write variables", font = "Arial 18",background='#9cb8e5')
l1.pack()

f1 = tk.Frame(root,background='#9cb8e5')
f1.pack(fill = "x")

f2 = tk.Frame(root,background="#9cb8e5")
f2.pack(fill = "x")

f3 = tk.Frame(root,background="#c2c4c6", bd = 3)
f3.pack(fill = "x")


f5 = tk.Frame(root,background='#9cb8e5', bd = 3)
f5.pack(fill= "x")
f6 = tk.Frame(root,background='#9cb8e5', bd = 3)
f6.pack(fill= "x")


f_inside = tk.Frame(f3,height=300, bd =4 )
f_inside.pack(fill = tk.BOTH)


f3 = tk.Frame(root)
f3.pack(fill = "x", side = tk.BOTTOM)

l3 = tk.Label(f1,text = "eps,n = ", font = "Arial 10", background='#9cb8e5')
l3.pack(side = tk.LEFT)

l4 = tk.Label(f2,text = "N_MAX,m = ", font = "Arial 10", background='#9cb8e5')
l4.pack(side = tk.LEFT)

e1 = tk.Entry(f1, bd = 2)
e1.insert(0,"10")
e1.pack(side = tk.RIGHT)

e2 = tk.Entry(f2, bd = 2)
e2.insert(0,"10")
e2.pack(side = tk.RIGHT)

e3 = tk.Entry(f1, bd = 2)
e3.insert(0,"0.001")
e3.pack(side = tk.RIGHT)

e4 = tk.Entry(f2, bd = 2)
e4.insert(0,"100")
e4.pack(side = tk.RIGHT)

var1 = tk.IntVar()
var1.set(0)
def  GetMode():
	return var1.get()

var2 = tk.IntVar()
var2.set(0)
def  GetMode2():
	return var2.get()


RButton1 = tk.Radiobutton(f5, text = "Тестовая задача", variable = var1, value = 0,bg = "#9cb8e5")
RButton1.pack(side = tk.LEFT)
RButton2 = tk.Radiobutton(f5, text = "Основная задача", variable = var1, value = 1,bg = "#9cb8e5")
RButton2.pack(side = tk.LEFT)
RButton3 = tk.Radiobutton(f6, text = "Тестовая, вырезанная область, метод простой итерации", variable = var1, value = 3,bg = "#9cb8e5")
RButton3.pack(side = tk.LEFT)
RButton4 = tk.Radiobutton(f5, text = "Метод Якоби", variable = var2, value = 0,bg = "#9cb8e5")
RButton4.pack(side = tk.LEFT)
RButton5 = tk.Radiobutton(f5, text = "Метод простой итерации", variable = var2, value = 1,bg = "#9cb8e5")
RButton5.pack(side = tk.LEFT)


n,m,eps,N_MAX  = Initialize(e1,e2,e3,e4)

Main_table = Tbl.Table(f_inside, ("№","случайная величина"))
def showtable():
	n,m,eps,N_MAX  = Initialize(e1,e2,e3,e4)
	global Main_table
	Main_table.destroy()
	if GetMode() ==0:
		a,b,c,d = f_test(-1)
		if GetMode2()==0:
			V = Yakobi(a,b,c,d,n,m,f_test(0),f_test(1),f_test(2),f_test(3),f_test(4),eps,N_MAX)
		if GetMode2()==1:
			print("Метод простой итерации:")
			V = SimplyIteration(a,b,c,d,n,m,f_test(0),f_test(1),f_test(2),f_test(3),f_test(4),eps,N_MAX)
		V2 = Init_arr(a,b,c,d,f_test_real,n,m)
		print("Погрешность - ", np.amax(np.abs(V-V2)))
	if GetMode() ==1:
		a,b,c,d = f_main(-1)
		if GetMode2()==0:
			V = Yakobi(a,b,c,d,n,m,f_main(0),f_main(1),f_main(2),f_main(3),f_main(4),eps,N_MAX)
			V2 = SimplyIteration(a,b,c,d,2*n,2*m,f_main(0),f_main(1),f_main(2),f_main(3),f_main(4),eps,N_MAX)
		if GetMode2()==1:
			print("Метод простой итерации:")
			V = SimplyIteration(a,b,c,d,n,m,f_main(0),f_main(1),f_main(2),f_main(3),f_main(4),eps,N_MAX)
			V2 = SimplyIteration(a,b,c,d,2*n,2*m,f_main(0),f_main(1),f_main(2),f_main(3),f_main(4),eps,N_MAX)
		print("Погрешность - ", GetMax(V,V2))
	if GetMode() ==3:
		print("Метод простой итерации:")
		a,b,c,d = f_test(-1)
		if GetMode2()==0:
			V = SimplyIteration_var2(a,b,c,d,n,m,f_test(0),f_test(1),f_test(2),f_test(3),f_test(4),eps,N_MAX)
		V2 = Init_arr(a,b,c,d,f_test_real,n,m)
		print("Погрешность - ", GetMax2(V,V2))
	Main_table = Tbl.Table(f_inside,tuple(map(str,range(n+1))),V)
	Main_table.pack(expand=tk.YES, fill=tk.BOTH)


def GetGraph():
	pass



b_print_graph = tk.Button(f3,text = "RUN TABLE", command = showtable)
b_print_graph.pack(fill = "x")
b_Gr = tk.Button(f3,text = "PrintGraph", command = GetGraph)
b_Gr.pack(fill = "x")

root.mainloop()

