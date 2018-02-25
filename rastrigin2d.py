import matplotlib.pyplot as plt
import numpy as np
import math

listaf=np.array(np.linspace(-5.12,5.12,700), ndmin=2)
listar=np.array([],dtype=float,ndmin=2)
listat=list()

def rastrigin(*listaf):
		#for n in xrange(1,101):
		f=sum([(n**2 - (10*np.cos(2 * math.pi * n))) for n in listaf])
		fa=10+f
		listat.append(fa)

if __name__== '__main__':
	
	rastrigin(listaf) 
	y=np.append(listat,listar)	
	x=listaf.reshape(700)
	#print (x.ndim)
	#print(y.ndim)
	print x
	print y
	plt.plot(x, y ,'b^',label='Practica1')
	plt.axis([-6,6,-10,50])
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.text(-50,-30,'Pruebas Grafica',fontsize=14, horizontalalignment='left',color='blue')
	plt.title("Practice 1: 2D Rastrigin's function ")
	
	fig=plt.gcf()
	fig.canvas.set_window_title('Evolutionary Computing')
	plt.show()