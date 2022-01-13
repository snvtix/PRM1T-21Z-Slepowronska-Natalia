import numpy

x=0.33
y=1.44
z=-1

def siec(x,y,z):
    wej=numpy.array([[x,y,z]])
    ukr=numpy.array([[1.06, 0.27, 1.27],[0.05, -0.37, 1.1],[0.63, 1.42, 0.48]])
    wyj=numpy.array([0.84,-0.47, 0.98])
    A=numpy.dot(ukr,wej.transpose())
    B=numpy.dot(wyj,A)
    print(f"wynik dzialania sieci: {B[0]}")

siec(x,y,z)

