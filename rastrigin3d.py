from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import math

listax=np.array(np.linspace(-5.12,5.12,200), ndmin=2)
listay=np.array(np.linspace(-5.12,5.12,200), ndmin=2)
listaz=np.array([],dtype=float,ndmin=2)
listat=list()

def rastrigin(*listaf):
		#for n in xrange(1,101):
		fx=sum([(x**2 - (10*np.cos(2 * math.pi * x))) for x in listax])
		fy=sum([(y**2 - (10*np.cos(2 * math.pi * y))) for y in listay])
		fa=20+fx+fy
		listat.append(fa)

		
if __name__== '__main__':
	rastrigin(listax,listay)
	z=np.array(np.append(listat,listaz))
	z=z.reshape(z.shape[0],1)
	x,y=np.meshgrid(listax,listay)
	fig=plt.figure()
	fig.canvas.set_window_title('Evolutionary Computing')
	ax=fig.gca(projection='3d')
	ax.plot_surface(x,y,z,color='g',rstride=1, cstride=1, cmap=cm.viridis, linewidth=0, antialiased=False,label='Optimization') 
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.title("Practice 1: 3D Rastrigin's function ")
	plt.show()
	plt.savefig('test.png')
