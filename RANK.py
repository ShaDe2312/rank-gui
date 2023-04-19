import numpy
import eel

eel.init('web')
global isvalid

@eel.expose
def rankfinder(data):
	A=data.split(';')
	B=[]
	isvalid=0
	for i in data:
		if (i.isdigit()) or (i==';') or (i==',') or (i==' '):
			isvalid=1
			
		else:
			isvalid=-1
	
	if isvalid==-1:
		eel.jsc_printer("The input is invalid.Please check the input and try again.")
		return 0
	
	for i in A:
		mat=i.split(',')
		B.append(mat)
	print(B)
	if B[-1]==['']:
		B.pop(-1)
	print(B)
	
	for i in range(len(B)):
		B[i]=list(map(int,B[i]))
    
	print("The matrix is:", B)
	the_rank=numpy.linalg.matrix_rank(B)
	print('The rank of the matrix is:',the_rank)
	
	if isvalid==1:
		eel.jsc_printer("The rank of the given matrix is: " + str(the_rank))
		return 0

eel.start('index.html', size=(1000, 600))
