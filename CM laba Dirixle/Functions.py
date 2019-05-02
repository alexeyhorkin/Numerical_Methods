import numpy as np
import math as mt
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D # This import has side effects required for the kwarg projection
from tqdm import tqdm
def f_test_real(x,y):
	return 1 - x**2-y**2

def f_test(var):
	a = -1
	b = 1
	c = -1
	d = 1
	def f(x,y):
		return -4
	def m1(y):
		return -y**2
	def m2(y):
		return -y**2
	def m3(x):
		return -x**2
	def m4(x):
		return -x**2
	if var ==-1:
		return (a,b,c,d)
	if var ==0:
		return f
	if var ==1:
		return m1
	if var ==2:
		return m2
	if var ==3:
		return m3
	if var ==4:
		return m4

def f_main(var):
	a = -1
	b = 1
	c = -1
	d = 1
	def f(x,y):
		return 	abs((mt.sin(mt.pi*x*y))**3)
	def m1(y):
		return -y**2 +1
	def m2(y):
		return -y**2 + 1
	def m3(x):
		return abs(mt.sin(mt.pi*x))
	def m4(x):
		return abs(mt.sin(mt.pi*x))
	if var ==-1:
		return (a,b,c,d)
	if var ==0:
		return f
	if var ==1:
		return m1
	if var ==2:
		return m2
	if var ==3:
		return m3
	if var ==4:
		return m4

def Init_arr(a,b,c,d,Funk,n,m):
	x_arr = GetGrid(a,b,n)
	y_arr = GetGrid(c,d,m)
	V2 = np.zeros((n+1,m+1))
	for i in range(n+1):
		for j in range(m+1):
			V2[i][j] = Funk(x_arr[i],y_arr[j])
	return V2

def GetMax(V,V2):
	Z = []
	V2 = V2[::2]
	for i in range(len(V2)):
		z = V2[i][::2]
		Z.append(z)
	Z = np.array(Z)
	return np.amax(np.abs(V-Z))

def GetMax2(V,V2):
	n = len(V)-1
	m = len(V[0])-1
	n_edge =int(n/2)
	m_edge = int(m/2)
	Mask = np.ones((n+1,m+1))
	for i in range(n_edge):
			for j in range(m_edge):
				Mask[i][j] = 0
	print(Mask)
	return np.amax(np.abs((V-V2)*Mask))


def GetGrid(a,b,n):
	return np.linspace(a,b,n+1)


def GetEigenValues(n,m,h,k):
	l_min = (4/h**2)*(mt.sin(mt.pi/(2*n)))**2+(4/k**2)*(mt.sin(mt.pi/(2*m)))**2
	l_max = (4/h**2)*(mt.sin(mt.pi*(n-1)/(2*n)))**2+(4/k**2)*(mt.sin(mt.pi*(m-1)/(2*m)))**2
	return (l_min,l_max)


def GetTay(l_min,l_max):
	return 2/(l_max+l_min)

def Yakobi(a,b,c,d,n,m,f,m1,m2,m3,m4,eps, N_max):
	N=0
	r = np.array(())
	eps_curr= 100
	h = (b-a)/n
	k = (d-c)/m
	h1 = 1/h**2
	k1 = 1/k**2
	y_arr = GetGrid(c,d,m)
	x_arr = GetGrid(a, b, n)
	A = -2*(h1+k1)
	V = np.zeros((n+1,m+1))
	for j in range(m+1):
		V[0][j]= m1(y_arr[j])
		V[-1][j] = m2(y_arr[j])
	for i in range(n + 1):
		V[i][0] = m3(x_arr[i])
		V[i][-1] = m4(x_arr[i])
	VS = V.copy()
	for i in tqdm(range(N_max)):
		if (eps_curr>eps and N<N_max):
			r = np.array(())
			for i in range(1,n):
				for j in range(1,m):
					V[i][j] = (1/A)*(f(x_arr[i],y_arr[j])-h1*(VS[i-1][j]+VS[i+1][j])-k1*(VS[i][j-1]+VS[i][j+1]))
					r =np.append(r,abs(V[i][j]-VS[i][j]))
			eps_curr = max(r)
			N+=1
			VS = V.copy()
	print("eps - ", eps_curr)
	print("count of steps - ", N)
	return V


def SimplyIteration(a,b,c,d,n,m,f,m1,m2,m3,m4,eps, N_max):
	N=0
	r = np.array(())
	eps_curr= 100
	h = (b-a)/n
	k = (d-c)/m
	h1 = 1/h**2
	k1 = 1/k**2
	y_arr = GetGrid(c,d,m)
	x_arr = GetGrid(a, b, n)
	A = -2*(h1+k1)
	l_min , l_max =GetEigenValues(n,m,h,k) 
	t = GetTay(l_min,l_max)
	V = np.zeros((n+1,m+1))
	for j in range(m+1):
		V[0][j]= m1(y_arr[j])
		V[-1][j] = m2(y_arr[j])
	for i in range(n + 1):
		V[i][0] = m3(x_arr[i])
		V[i][-1] = m4(x_arr[i])
	VS = V.copy()
	for i in tqdm(range(N_max)):
		if (eps_curr>eps and N<N_max):
			r = np.array(())
			for i in range(1,n):
				for j in range(1,m):
					V[i][j] = VS[i][j] - t*(f(x_arr[i],y_arr[j])-h1*(VS[i-1][j]+VS[i+1][j])-A*VS[i][j]-k1*(VS[i][j-1]+VS[i][j+1]))
					r =np.append(r,abs(V[i][j]-VS[i][j]))
			eps_curr = max(r)
			N+=1
			VS = V.copy()
	print("eps - ", eps_curr)
	print("count of steps - ", N)
	return V


def SimplyIteration_var2(a,b,c,d,n,m,f,m1,m2,m3,m4,eps, N_max):
	N=0
	r = np.array(())
	eps_curr= 100
	h = (b-a)/n
	k = (d-c)/m
	h1 = 1/h**2
	k1 = 1/k**2
	y_arr = GetGrid(c,d,m)
	x_arr = GetGrid(a, b, n)
	A = -2*(h1+k1)
	l_min , l_max =GetEigenValues(n,m,h,k) 
	t = GetTay(l_min,l_max)
	n_edge = int(n/2)
	m_edge = int(m/2)
	V = np.zeros((n+1,m+1))
	for j in range(m+1):
		V[n_edge][j] = f_test_real(x_arr[n_edge],y_arr[j])
		V[-1][j] = m2(y_arr[j])
	for i in range(n + 1):
		V[i][m_edge] = f_test_real(x_arr[i],y_arr[m_edge])
		V[i][-1] = m4(x_arr[i]) 
	for j in range(m_edge,m+1):
		V[0][j] = m1(y_arr[j])
	for i in range(n_edge,n+1):
		V[i][0] = m3(x_arr[i])
	VS = V.copy()

	for i in tqdm(range(N_max)):
		if (eps_curr>eps and N<N_max):
			r = np.array(())
			for i in range(1,n):
				for j in range(1,m):
					if i <n_edge and j<m_edge:
						pass
					else:  
						V[i][j] = VS[i][j] - t*(f(x_arr[i],y_arr[j])-h1*(VS[i-1][j]+VS[i+1][j])-A*VS[i][j]-k1*(VS[i][j-1]+VS[i][j+1]))
						r =np.append(r,abs(V[i][j]-VS[i][j]))
			eps_curr = max(r)
			N+=1
			VS = V.copy()
	print("eps - ", eps_curr)
	print("count of steps - ", N)
	return V








