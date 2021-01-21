import numpy as np
import matplotlib.pyplot as plt



def dir_vec(Q,R):
  return R-Q



#Area using Heron's formula
def tri_hero(q,r,s):
  D = (q+r+s)/2
  area = np.sqrt(D*(D-q)*(D-r)*(D-s))
  return area
def tri_section(Q,R,k):
  V = (k*Q+R)/(k+1)
  return V

#Generate line points
def line_gen(Q,R):
  len =10
  dim = Q.shape[0]
  x_QR = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = Q + lam_1[i]*(R-Q)
    x_QR[:,i]= temp1.T
  return x_QR

#Triangle vertices
def tri_vert(q,r,s):
  w = (q**2 + s**2-r**2 )/(2*q)
  z = np.sqrt(s**2-w**2)
  Q = np.array([w,z])
  R = np.array([0,0])
  S = np.array([q,0])
  return  Q,R,S
def line_dir_pt(m,Q, dim):
  len = 10
  dim = Q.shape[0]
  x_QR = np.zeros((dim,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = Q + lam_1[i]*m
    x_QR[:,i]= temp1.T
  return x_QR

len = 100
degrad = 180/np.pi

#sides of quadrilateral
q = 5 
r = 5.5 
s = 4 
p = 6 
d = 7 

t1 = np.arccos((q**2+d**2-r**2)/(2*q*d))
t2 = np.arccos((p**2+d**2-s**2)/(2*p*d))

print(t1*degrad,t2*degrad)

#Rotation matrix for t1
X = np.array(([np.cos(t1),-np.sin(t1)],[np.sin(t1),np.cos(t1)]) )



#quadrilateral vertices
P,R,S =  tri_vert(q,r,d)
Q1,R1,P1 =  tri_vert(d,s,p)
Q = X@Q1

#Printing coordinates
print(Q1,Q,R,S,P)

#Generating all lines
x_QR = line_gen(Q,R)
x_RS = line_gen(R,S)
x_RP = line_gen(R,P)
x_PQ = line_gen(P,Q)
x_SP = line_gen(S,P)



#Plotting all lines
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RS[0,:],x_RS[1,:],label='$RS$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')
plt.plot(x_SP[0,:],x_SP[1,:],label='$SP$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')


plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.1), Q[1] * (1 - 0.1) , 'Q')

plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 - 0.2), R[1] * (1) , 'R')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 + 0.03), S[1] * (1 - 0.1) , 'S')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')