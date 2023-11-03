import numpy as np
import scipy

##EXERCICE 1

#définition des matrices
A = np.array([[2,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,0],[0,0,-1,2,-1],[0,0,0,-1,2]])
B = np.array([[1,0,0,0,1],[-1,1,0,0,1],[-1,-1,1,0,1],[-1,-1,-1,1,1],[-1,-1,-1,-1,1]])

	#1

#calcul des mineurs principaux de A
mineur = []
for k in range(len(A)):
	mineur.append(np.linalg.det(A[:k+1,:k+1]))
	
print('Mineurs de A = '+str(mineur))

#calcul des mineurs principaux de B
mineur = []
for k in range(len(B)):
	mineur.append(np.linalg.det(B[:k+1,:k+1]))
	
print('Mineurs de B = '+str(mineur))

    #2

#calcul de L tel que A=LL^t
A_cholesky = np.linalg.cholesky(A)
print('A_L = \n'+str(A_cholesky))

    #3
    
#calcul de L et U tel que B=LU
B_L,B_U = scipy.linalg.lu(B)[1],scipy.linalg.lu(B)[2]
print('B_L = \n'+str(B_L))
print('B_U = \n'+str(B_U))