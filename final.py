import os
from getpass import getpass

#ATTRIBUTES OF NODE
class attributes:
	def __init__(self,name=None,fathers_name=None,mobile_number=None,email=None,regno=None,gender=None):
		self.name=name
		self.fathers_name=fathers_name
		self.mobile_number=mobile_number
		self.email=email
		self.gender=gender

#NODE OF TREE
class Node:
	def __init__(self,room=None,regno=None,parent=None,left=None,right=None,block=None):
		self.reg_number=regno
		self.block_number=block
		self.room=room
		self.attributes=attributes()
		self.left=left
		self.right=right
		self.parent=parent
		self.flag=0

#TREE
class BST:
	def __init__(self):
		self.root=Node()
			
	#SEARCH FOR SINGLE ROOM (IN TREE1)
	def search(self,k,block):
		temp=self.root
		if temp==None:
			return None
		while temp!=None and temp.room!=None:
			if k==temp.room and temp.block_number==block:
				return temp
			elif (k==temp.room and temp.block_number!=block) or (k>temp.room) :
				temp=temp.right
			else:
				temp=temp.left
		return None
	
	#SEARCH FOR STUDENT BASED ON REG. NUMBER (IN TREE2)
	def search1(self,k):
		temp=self.root
		if temp==None:
			return None
		while temp!=None and temp.reg_number!=None:
			if k==temp.reg_number:
				return temp
			elif k>temp.reg_number:
				temp=temp.right
			else:
				temp=temp.left
		return temp

	#SEARCH FOR DOUBLE ROOM (BASED ON ROOM,BLOCK   IN TREE1)
	def search2(self,k,block):
		x=0
		temp1=None
		temp2=None
		temp=self.root
		if temp==None:
			return None
		while temp!=None:
			if k==temp.room and temp.block_number==block:
				if x==0:
					temp1=temp
					temp=temp.right
					x+=1
				elif x==1:
					temp2=temp
					break
			elif (k==temp.room and temp.block_number!=block) or (k>temp.room) :
				temp=temp.right
			else:
				temp=temp.left
		if temp1==None and temp2==None:
			return None,None			
		else:
			return temp1,temp2

	# SET ATTRIBUTES IN BOTH TREES(TREE1 AND TREE2)
	def setattributes(self,n,room,block,regno,name,gender,fathers_name,mobile_number,email):
		if n==0:
			temp1,temp2=self.search2(room,block)
			if temp1!=None and temp2==None:
				temp1=temp1.attributes
				temp1.name=name
				temp1.fathers_name=fathers_name
				temp1.mobile_number=mobile_number
				temp1.email=email
				temp1.reg_number=regno
				temp1.gender=gender
			
		elif n==1:
			temp2=self.search1(regno)
		if temp2!=None:
			temp2=temp2.attributes
			temp2.name=name
			temp2.fathers_name=fathers_name
			temp2.mobile_number=mobile_number
			temp2.email=email
			temp2.reg_number=regno
			temp2.gender=gender
			
	
	#INSERTION (KEY IS ROOM NUMBER    IN TREE1)
	def insert(self,k1,block,k2):
		temp=T.search(k1,block)
		if temp!=None:
			temp.flag=2

			temp=Node(k1)
			y=None
			x=self.root
			while x!=None and x.room!=None:
				y=x
				if temp.room < x.room:
					x=x.left
				else:
					x=x.right
			temp.parent=y
			if y==None:
				self.root=temp
			elif temp.room < y.room:
				y.left=temp
			else:
				y.right=temp
			temp.block_number=block
			temp.reg_number=k2
			temp.flag=2
		else:
			temp=Node(k1)
			y=None
			x=self.root
			while x!=None and x.room!=None:
				y=x
				if temp.room < x.room:
					x=x.left
				else:
					x=x.right
			temp.parent=y
			if y==None:
				self.root=temp
			elif temp.room < y.room:
				y.left=temp
			else:
				y.right=temp
			temp.block_number=block
			temp.reg_number=k2
			temp.flag=1

	#INSERTION (KEY IS REG. NUMBER   IN TREE2) 
	def insert1(self,k1,block,k2):
		temp=Node(None,k2)
		y=None
		x=self.root
		while x!=None and x.reg_number!=None:
			y=x
			if temp.reg_number < x.reg_number:
				x=x.left
			else:
				x=x.right
		temp.parent=y
		if y==None:
			self.root=temp
		elif temp.reg_number < y.reg_number:
			y.left=temp
		else:
			y.right=temp
		temp.block_number=block
		temp.room=k1	

	#FETCHING DETAILS BASED ON REGNO.  ...(IN TREE2)
	def showdetails1(self,regno):
		temp=self.search1(regno)
		if temp==None:
			print("     sorry no student registered with this registration number")
		else:
			self.printdetails(0,temp)

	#KIND OF FETCHING OF DETAILS BASED ON ROOMNO.,BLOCK  (IN TREE1)
	def showdetails(self,room,block):
		if block==2 or block==4:
			temp1,temp2=self.search2(room,block)
			if (temp1!=None and temp2!=None) and ( temp1.flag==2 or temp2.flag==2):
				self.printdetails(1,temp1)
				self.printdetails(1,temp2)
			elif (temp1!=None and temp1.flag==1 and temp2==None):
				self.printdetails(1,temp1)
			else:
				print('room is not alloted yet')

		elif block==1 or block==3:
			temp=T.search(room,block)
			if temp!=None:
				self.printdetails(1,temp)
			else:
				print('room is not alloted yet')


	#PRINT DETAILS OF STUDENT(OF BOTH TREES)
	def printdetails(self,n,temp):		
					
			if n==0:
				print('details for ',temp.reg_number,' are:')
			else:
				print('details of student(s) in room ',temp.room,' and block ',temp.block_number, ' are:')
			print('Reg_number: ',temp.reg_number)
			print()
			print('Name:',temp.attributes.name)
			print()
			print('Gender: ',temp.attributes.gender)
			print()
			print('Fathers_name:',temp.attributes.fathers_name)
			print()
			print('mobile_number:',temp.attributes.mobile_number)
			print()
			print('email:',temp.attributes.email)
			print()
			print('block number: ',temp.block_number)
			print()
			print('Room number: ',temp.room)
			
#MENU
def menu(f):
	
	flag=0
	while 1:
		print()
		print()
		print("            ***********************************************************************************")
		print()
		print("                                            MENU")
		print()
		print("		1-NEW ADMISSION")
		print("		2-STUDENT DETAIL ")
		print("                3.AVIALABLE ROOMS ACCORDING TO BLOCK NUMBER")		
		print("		4-EXIT")
		print()
		print("		choose required option ",end=" ")

		op=int(input())
		os.system('cls' if os.name == 'nt' else 'clear')

		if op!=1 and op!=2 and  op!=3 and op!=4:
			print("	incorrect input")
		else:
			flag=1	
			break
	if flag==1:
		switch(op,f)

#GO TO APPROPRIATE MENU
def switch(op,f):
	if op==1:
		add_student(f)
		menu(f)
	if op==2:	
		search_detail()
		menu(f)
	if op==3:
		print('       SELECT BLOCK: ')
		print('                                1.single room for boys:')
		print('                                2.Double room for boys:')
		print('                                3.single room for girls:')
		print('                                4.Double room for girls:')	
		print('                                5.For all blocks')
		block=int(input())
		os.system('cls' if os.name == 'nt' else 'clear')
		if block==1 or block==2 or block==3 or block==4:
			avialable(block,f)
		elif block==5:
			room_avialable(f)
		else:
			print('    wrong input')
			switch(3,f)
		menu(f)

	if op==4:
		f.close()
		print("                                THANK YOU")
		exit(0)

def room_avialable(f):
	print('             room avialable in ')
	print('BLOCK 1(single for boys):')
	avialable(1,f)
	print('BLOCK 2(double for boys):')
	avialable(2,f)
	print('BLOCK 3(single for girls):')
	avialable(3,f)
	print('BLOCK 4(double for girls):')
	avialable(4,f)

#SEARCH BASED ON ROOM,BLOCK OR REGISTRATION NUMBER
def search_detail():
	print()
	print("                ##############################STUDENT DETAIL##############################")
	print()
	print("                    1.search by registration number")
	print("                    2.search by room,block number ",end="  ")
	var=int(input())
	if var==1:
		print("                     enter registration number:",end=" ")
		reg_number=int(input())
		T1.showdetails1(reg_number)
	if var==2:
		print("	            enter room number of the student: ",end=" ")
		room_number=int(input())
		print('                  enter block number of the student: ',end=" ")
		block=int(input())
		T.showdetails(room_number,block)
	

def iscorrect(num):
	if(len(num)==10):
		try:
			n=int(num)
		except:
			return False
		else:
			return True
	else:
		return False

def validate(eml):
    for i in range(len(eml)-1,0,-1):
        if(eml[i]=="." and i!=len(eml)-1):
            flag=i
            break
    try:
        for i in range(flag-1,0,-1):
            if(eml[i]=="@"):
                temp=1
                return True
            else:
                temp=0
        if(temp==0):
            return False
    except:
        return False
    else:
        True

# CHECK AVIALABLE ROOMS IN GIVEN BLOCK(IN TREE1):
def avialable(block,f):
	if block==1 or block==3:
		print('Avialable rooms are:')
		for i in range(1,51):
			temp=T.search(i,block)
			if temp==None:
				print(i,end=" ")
		print()
		print()

	elif block==2 or block==4:
		print('aviable rooms (vacant):')
		for i in range(1,51):
			temp=T.search(i,block)
			if temp==None :
				print(i,end=" ")
		print()


		print('avialable rooms with single vacancy:')
		for i in range(1,51):
			temp=T.search(i,block)
			if temp!=None and temp.flag==1:
				print(i,end=" ")
		print()
		print()


	else:
		print('please enter correct input')
		add_student(f)

#NEW ALLOTEMENT
def add_student(f):
	print()
	print()
	print()
	print('               *********************HOSTEL ALLOTMENT FORM****************************           ')
	print()

	#NAME
	print('                                FirstName:',end=" ")
	name=input()
	print()


	#REGNO
	while True:
		try:
			print('                                reg number:',end=" ")
			regno=int(input())
			print()
			temp=T1.search1(regno)
		except ValueError:
			print("                     please enter propper input for registration number")
		else:	
			if temp!=None:
				print('already registered pls enter correct registration_no')
			else:
				break
	print()
	

	#FATHER'S NAME 
	print('                                Fathername:',end=" ")
	fathername=input()
	print()


	#GENDER
	while True:
		print('                                 Gender(M/F): ',end=" ")
		gender=input()
		if gender.capitalize()=="M" or gender.capitalize()=="F":
			break
		else:
			print('		NOT RIGHT FORMAT TRY AGAIN')
			
	print()


	#MOBILE NUMBER
	while True:
		print('                                mobile_number:',end=" ")
		mobile_number=input()
		if (not iscorrect(mobile_number)):
			print('                               Sorry enter correct number')
		else:
			break
	print()
	
	
	#EMAIL
	while(True):
		print('                                Email:',end=" ")
		Email=input()
		if(not validate(Email)):
			print("                                Sorry enter correct E-mail Address")
		else:
			break
		print()




	#BLOCK
	print('##########################PLEASE CHOOSE APPROPRIATE BLOCK####################################')
	print('                                1.single room for boys:')
	print('                                2.Double room for boys:')
	print('                                3.single room for girls:')
	print('                                4.Double room for girls:')
	while True:
		print('                                Block_number: ',end=" ")
		blocknumber=int(input())
		if ((blocknumber==1 or blocknumber==2) and (gender=='F')) or ((blocknumber==3 or blocknumber==4) and (gender=='M')):
			print('PLS CHOOSE RIGHT BLOCK')
		else:
			break
	print()
	
	avialable(blocknumber,f)


	#ROOM_NUMBER
	if blocknumber==2 or blocknumber==4:
		while True:
			print('                                Room_no:',end=" ")
			roomnumber=int(input())
			temp1=T.search(roomnumber,blocknumber)
			if (roomnumber>50) or (temp1!=None and temp1.flag==2):
				print('Room not avialable pls choose other room')
			else:
				break
	elif blocknumber==1 or blocknumber==3:
		while True:
			print('                                Room_no:',end=" ")
			roomnumber=int(input())
			temp1=T.search(roomnumber,blocknumber)
			if roomnumber>50 or temp1!=None:
				print('Room not avialable pls choose other room')
			else:
				break
	
	os.system('cls' if os.name == 'nt' else 'clear')

	print('student added successfully....')
	T.insert(roomnumber,blocknumber,regno)
	T.setattributes(0,roomnumber,blocknumber,regno,name,gender,fathername,mobile_number,Email)
	T1.insert1(roomnumber,blocknumber,regno)
	T1.setattributes(1,roomnumber,blocknumber,regno,name,gender,fathername,mobile_number,Email)
	f.write('%d      '%(roomnumber))
	f.write('%d      '%(blocknumber))
	f.write('%d      '%(regno))
	f.write('%s      '%(name))
	f.write('%s      '%(gender))
	f.write('%s      '%(fathername))
	f.write('%s      '%(mobile_number))
	f.write('%s      '%(Email))
	
	f.write('\r\n\r\n')
	menu(f)

#LOGIN PAGE
def login():				
	default_user_name="admin"
	default_password="123"

	print()
	print()
	print("            *************************************************************************************         ")
	print()
	print("                                     HOSTEL ALLOTMENT SYSTEM")
	print()
	while 1:	
		print("                         enter user name:",end=" ")
		user_name=input()	
		print()
		password=getpass(prompt='                         enter password: ')

		os.system('cls' if os.name == 'nt' else 'clear')

		if password!=default_password or user_name!=default_user_name:
			print()
			print("incorrect user name or password")
			print()
		if password==default_password and user_name==default_user_name:
			break

	print()
	print("successfull logged in...")
	print()	

T=BST()                            #TREE1 (KEY IS ROOM NUMBER)

T1=BST()						   #TREE2 (KEY IS REG.NUMBER)


def main():

	f=open("data.txt","r")
	for line in f:
		line=line.split()

		if len(line)!=8:
			continue
		if len(line)==8:
			T.insert(int(line[0]),int(line[1]),int(line[2]))
			T1.insert1(int(line[0]),int(line[1]),int(line[2]))
			T.setattributes(0,int(line[0]),int(line[1]),int(line[2]),line[3],line[4],line[5],line[6],line[7])
			T1.setattributes(1,int(line[0]),int(line[1]),int(line[2]),line[3],line[4],line[5],line[6],line[7])
	f.close()
	f=open('data.txt','a')
	login()
	menu(f)

main()