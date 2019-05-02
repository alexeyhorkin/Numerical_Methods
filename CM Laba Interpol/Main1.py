import tkinter as tk
import Functions1 as Func
import matplotlib.pyplot as plt
import math as mt
import Table1 as Tbl
#########################################################
## Some functions
#########################################################

def CreateF(a):
	def f(x):
		if x >= -1 and x <= 0:
			return x ** 3 + 3 * x ** 2
		elif x >= 0 and x <= 1:
			return -x ** 3 + 3 * x ** 2

	def f2(x):
		return mt.exp(x-3)
		#return mt.cos((x ** 2) / 4)
	def f3(x):
		return f2(x)+ mt.cos(100*x)
	if a ==0:
		return f
	elif a ==1:
		return f2
	else:
		return f3

def CreateDF(a):
	def f1(x):
		if x >= -1 and x <= 0:
			return 3 * x ** 2 + 6 * x
		elif x >= 0 and x <= 1:
			return -3 * x ** 2 + 6 * x
	def f2(x):
		return mt.exp(x-3)
	def f3(x):
		return f2(x) - mt.sin(100*x)*100
	if a ==0:
		return f1
	elif a ==1:
		return f2
	else:
		return f3

#########################################################
## GUI
#########################################################


root = tk.Tk()
root.geometry("720x500")
root.title("Лабораторная работа №2")
l1 = tk.Label(root, text = "Write variables", font = "Arial 18")
l1.pack()
f1 = tk.Frame(root)
f1.pack(fill = "x")
f2 = tk.Frame(root)
f2.pack(fill = "x")
f3 = tk.Frame(root)
f3.pack(fill = "x")
f4 = tk.Frame(root)
f4.pack(fill = "x")
f6 = tk.Frame(root)
f6.pack(side = tk.BOTTOM, fill = "x")
f5 = tk.Frame(root)
f5.pack(side = tk.BOTTOM, fill = "x")
f7 = tk.Frame(root)
f7.pack(side = tk.BOTTOM, fill = "x")
f10 = tk.Frame(root)
f10.pack(fill = "x")
f11 = tk.Frame(root)
f11.pack(fill = "x")
f13 = tk.Frame(root)
f13.pack(side = tk.BOTTOM, fill = "x")
f14 = tk.Frame(root)
f14.pack(side = tk.BOTTOM, fill = "x")
f15 = tk.Frame(root)
f15.pack(side = tk.BOTTOM, fill = "x")
''''''


def showtable():
	m1 = 0
	m2 = 0
	n = Func.Initialize(e1)
	if GetMode() ==0:
		start = -1
		end = 1
	if GetMode() ==1:
		start = 0
		end = 5
		if GetMode2()!=0:
			m1 = mt.exp(-3)
			m2 = mt.exp(2)
	if GetMode() ==2:
		start = 0
		end = 5
		if GetMode2() !=0:
			m1 = mt.exp(-3)
			m2 = mt.exp(2)
	f = CreateF(GetMode())
	x = Func.GetGrid(start, end, n)
	array = [f(i) for i in x]
	h = (x[-1] - x[0]) / n  # step of grid
	a, b, c, B = Func.GetFirstMatrix(h, n, array, m1, m2)
	c_coeff = Func.Progonka(a, b, c, B)
	d, b = Func.GetCoeff(array, c_coeff, n, h)
	Tbl.Create_table1(("n","xi", "x i+1","a","b","c","d"),n,x,x[1:],array[1:],b,c_coeff[1:],d)

def showtable2():
	m1= 0
	m2 = 0
	n = Func.Initialize(e1)
	if GetMode() ==0:
		start = -1
		end = 1
	if GetMode() ==1:
		start =0
		end = 5
		if GetMode2()!=0:
			m1 = mt.exp(-3)
			m2 = mt.exp(2)
	if GetMode() ==2:
		start = 0
		end = 5
		if GetMode2()!=0:
			m1 = mt.exp(-3)
			m2 =mt.exp(2) - mt.sin(100*end)*100
	f = CreateF(GetMode())
	fdiff = CreateDF((GetMode()))
	x = Func.GetGrid(start, end, n)
	array = [f(i) for i in x]
	h = (x[-1] - x[0]) / n  # step of grid
	a, b, c, B = Func.GetFirstMatrix(h, n, array, m1, m2)
	c_coeff = Func.Progonka(a, b, c, B)
	d, b = Func.GetCoeff(array, c_coeff, n, h)
	G, y = Func.GetGraph(start, end, array, b, c_coeff, d, n,1)
	y_real = [f(x) for x in G]
	diffrence = [abs(y_real[x] - y[x]) for x in range(len(G))]
	y_real_diff = [fdiff(x) for x in G]
	G,y_diff = Func.GetGraph(start, end, array, b, c_coeff, d, n,0)
	diffrence2 = [abs(y_real_diff[x] - y_diff[x]) for x in range(len(G))]
	Tbl.Create_table2(("n - x","f(x)", "S(x)","|f(x)-S(x)|","f'(x)","S'(x)","|f'(x)-S'(x)|"),len(G),G,y_real,y,diffrence,y_real_diff,y_diff,diffrence2)


def showgraph():
	m1 = 0
	m2 = 0
	if GetMode() == 0:
		start = -1
		end = 1
	if GetMode() == 1:
		start = 0
		end = 5
		if GetMode2()!=0:
			m1 = mt.exp(-3)
			m2 = mt.exp(2)
	if GetMode() == 2:
		start = 0
		end = 5
		if GetMode2()!=0:
			m1 = mt.exp(-3)
			m2 = mt.exp(2) -mt.sin(100*end)*100
	f = CreateF(GetMode())
	fdiff = CreateDF((GetMode()))
	n = Func.Initialize(e1)
	x = Func.GetGrid(start,end,n)
	array = [f(i) for i in x]
	h = (x[-1] - x[0])/n # step of grid
	a,b,c,B = Func.GetFirstMatrix(h,n,array, m1,m2)
	c_coeff = Func.Progonka(a,b,c,B)
	d,b = Func.GetCoeff(array,c_coeff,n,h)
	G,y = Func.GetGraph(start,end,array,b,c_coeff,d,n,1)
	plt.subplot(211)
	plt.plot(x,array,"bo")
	plt.plot(G,y)
	y_real = [f(x) for x in G]
	plt.plot(G,y_real,"r")
	diffrence = [abs(y_real[x]-y[x]) for x in range(len(G))]
	y_real_diff = [fdiff(x) for x in G]
	G, y_diff = Func.GetGraph(start, end, array, b, c_coeff, d, n, 0)
	diffrence2 = [abs(y_real_diff[x] - y_diff[x]) for x in range(len(G))]
	print("max = ", max(diffrence))
	print("max diff = ", max(diffrence2))
	plt.subplot(212)
	plt.plot(G,y_real_diff,"r")
	plt.plot(G,y_diff)
	plt.show()


''''''
l3 = tk.Label(f2,text = "Число разбиений = ", font = "Arial 10")
l3.pack(side = tk.LEFT)
e1 = tk.Entry(f2)
e1.insert(0,"5")
e1.pack(side = tk.RIGHT)

l6 = tk.Label(f11,text = "Справка ", font = "Arial 12")
l6.pack()
t1 = tk.Text(f11,width=60, height=14)
t1.pack(side = tk.LEFT)

var = tk.IntVar()
var.set(0)
def  GetMode():
 return var.get()

var2 = tk.IntVar()
var2.set(0)
def  GetMode2():
 return var2.get()


RButton1 = tk.Radiobutton(f13, text = "Основная задача", variable = var, value = 2, command = GetMode)
RButton2 = tk.Radiobutton(f14, text = "Тестовая задача 2", variable = var, value = 1,command = GetMode)
RButton3 = tk.Radiobutton(f15, text = "Тестовая задача 1", variable = var, value = 0, command = GetMode)
RButton4 = tk.Radiobutton(f15, text = "Естественные ГУ", variable = var2, value = 0, command = GetMode2)
RButton5 = tk.Radiobutton(f15, text = "Точные ГУ", variable = var2, value = 1, command = GetMode2)
RButton4.pack()
RButton5.pack()
RButton1.pack(side = tk.LEFT)
RButton2.pack(side = tk.LEFT)
RButton3.pack(side = tk.LEFT)


b_print_graph = tk.Button(f5,text = "Print_graph", command = showgraph)
b_print_graph.pack(fill = "x")

b_create_table = tk.Button(f6,text = "Print_table1", command = showtable)
b_create_table.pack(fill = "x")

b_print_spec_graph = tk.Button(f7,text = "Print_table2", command = showtable2)
b_print_spec_graph.pack(fill = "x")

root.mainloop()

