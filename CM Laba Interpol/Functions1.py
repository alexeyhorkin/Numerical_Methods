import numpy as np
import math as mt


def GetMax(l,mode):
	maxx = l[0]
	index = 0
	for i in range(len(l)):
		if maxx <l[i]:
		 maxx = l[i]
		 index = i
	if mode =="index":
	 return index
	else:
	 return maxx 	 


def Progonka(a,b,c,f):
	res = []
	a_arr = []
	b_arr = []
	a_arr.append(-b[0]) #a1
	b_arr.append(f[0])     #b1
	# base of induction
	for i in range(len(f)-2):
		alfa = b[i+1]/(-c[i+1]-a_arr[-1]*a[i])
		betta = (-f[i+1]+b_arr[-1]*a[i])/(-c[i+1]-a_arr[-1]*a[i])
		a_arr.append(alfa)
		b_arr.append(betta)	
	res.append((f[-1]-a[-1]*b_arr[-1])/(1+a_arr[-1]*a[-1])) #add firs elem (yn)
	#back probagation
	for x in range(len(f)-1):
	 res.append(a_arr[len(f)-2-x]*res[-1]+b_arr[len(f)-2-x])
	res = list(reversed(res))
	return res			    
		


def GetGrid(a,b,n):
	return np.linspace(a,b,n+1)


def GetFirstMatrix(h,n,arr_y, m1, m2):
	B = [m1]
	z = arr_y
	for i in range(1,n):
		var = 	6*(arr_y[i+1]-2*arr_y[i]+arr_y[i-1])/h
		B.append(var)
	B.append(m2)
	a1 = []
	b1 = []
	c1 = []
	#цикл по всем промежуточным строкам  i = 1,2,3...n-1; заполнение матрицы
	for i in range(1,n):
	 c1.append(4*h)
	 a1.append(h)
	 b1.append(h)
	# for nature conditions
	c1 = [1] + c1 + [1]
	a1 = a1 + [0]
	b1 = [0] + b1
	return (a1,b1,c1,B)

def Initialize(e1):
    n = e1.get()
    if n != '':
        n = int(n)
    else:
        n = 0.0
        ''''''
    return n

def GetCoeff(a,c,n,h):
	d = []
	b = []
	for i in range(n):
		d.append((c[i+1]-c[i])/h)
	for i in range(n):
		# b.append((a[i+1]-a[i])/h+c[i+1]*0.5*h-d[i]*h*h/6)
		b.append((a[i+1]-a[i])/h+c[i+1]*(1/3)*h+c[i]*h/6)
	return (d,b)


'''
def GetValuefromFunc(start,end,i,a,b,c,d,h,n,acc):
	res = []
	G = GetGrid(start,end,n)
	G_new = GetGrid(start+i*h,end - (n-1-i)*h,acc)
	G_new = G_new[0:-1]
	for z in G_new:
		val = a[i+1] + b[i]*(z-G[i+1]) + c[i+1]*0.5*(z-G[i+1])**2 + (1/6)*d[i]*(z-G[i+1])**3
		res.append(val)
	return res 




def GetGraph(start,end,a,b,c,d,n,h,acc):
	y = []
	for i in range(n):
		y = y + GetValuefromFunc(start,end,i,a,b,c,d,h,n,acc)
	# кастыль
	y.append(a[-1])
	G = GetGrid(start, end, n * acc)
	return (G,y) 

'''
def GetGraph(start,end,a,b,c,d,n, flag):
	acc = 100
	G = GetGrid(start, end, n * acc)
	y = []
	for i in range(n):
		res = []
		for j in list(G[i*acc:(i+1)*acc]):
			Spline = Create_Spine(a[i+1],b[i],c[i+1],d[i],G[(i+1)*acc], flag)
			res.append(Spline(j))
		y = y + res
	if len(a)==1:
		y.append(end)
	else:
		y.append(Create_Spine(a[-1],b[-1],c[-1],d[-1],end,flag)(end)) #latest value
	return (G,y)

















'''
def GetDiffGraph(start,end,a,b,c,d,n,h,acc):
	y = []
	for i in range(n):
		y = y + GetValueForDiff(start,end,i,a,b,c,d,h,n,acc)
	y.append(b[-1])
	G = GetGrid(start, end, n * acc)
	return (G,y)

def GetValueForDiff(start,end,i,a,b,c,d,h,n,acc):
	res = []
	G = GetGrid(start, end, n)
	G_new = GetGrid(start + i * h, end - (n - 1 - i) * h, acc)
	G_new = G_new[0:-1]
	for z in G_new:
		val = b[i] + c[i+1]*(z-G[i+1]) + (1/2)*d[i]*(z-G[i+1])**2
		res.append(val)
	return res	
'''

def Create_Spine(a,b,c,d,xi,flag):
	def spline(x):
		if flag ==1:
			return a + b*(x-xi) + (0.5)*c*(x-xi)**2 + (1/6)*d*(x-xi)**3
		else:
			return b+c*(x-xi) + (1/2)*d*(x-xi)**2
	return spline










