#-------------------------------------------------------1 ulesanne (While)-----------------------------------------------------------------------
#t=0 #arvude kogus
#q=0
#while t<15:
	#t+=1
	#a=float(input("Siseta arv__"))
	#if a==round(a): q+=1
#print("Täisarvude kogus:",q)
#----------------------------------------------------------------(FOR)-----------------------------------------------------------------------
#c=0
#q=0
#print("Siseta arv__")
#for c in range(15):
	#c=float(input("Siseta arv__"))
	#q+=1
	#print("Täisarvude kogus:")
#---------------------------------------------------------------2 ulesanne-----------------------------------------------------------------------
#a=10
#s=0
#print("siseta arv__")
#for a in range(1,a+1):
	#s+=a
#print("Summa:",s)
#---------------------------------------------------------------3 Ulesanne-----------------------------------------------------------------------
#from random import *
#korrutis=1
#for i in range(8):
#	B=randint(-100,100)
#	print(B)
#	if B>0: korrutis*=B
#print("Korrutis on ",korrutis)
#---------------------------------------------------------------4 Ulesanne-----------------------------------------------------------------------
#for a in range(10,20):
#	print(a**2)
#_______________________________________________________________5 Ulesanne_______________________________________________________________________
#from random import *
#_______________________________________________________________6 Ulesanne_______________________________________________________________________
#from random import *
#N=int(input("Mitu: "))
#p=n=o=0
#while N>0:
#	N-=1
#	B=randint(-100,100)
#	print(B)
#	if B>0:
#		p+=1
#	elif B<0:
#		n+=1
#	else:
#		o+=1
#print("Positivne:",p)
#print("Negativne:",n)
#print("Nullid",n)
#_______________________________________________________________КУПИ СЛОНА_______________________________________________________________________
#loom=input("Купи слона! ")
#while loom.lower()!="слон":
#	loom=input("Все так говорят "+loom+"! А ты купи!!!")
#print("Слон твой!!!")
#_______________________________________________________________17 ulesanne______________________________________________________________________
#a=int(input("siseta number"))
#for i in range(1,10):
#	print(i,"*",i,"=",a*i)
#_______________________________________________________________15 ulesanne______________________________________________________________________
#for j in range(1,10):
#	for i in range(1,10):
#		print(f"{(j*i):4}",end=" ")
#	print()
#________________________________________________________________16 ulesanne_____________________________________________________________________
#for j in range(1,10):
#	for i in range(1,10):
#		if i==j:
#			print(i,end=" ")
#		else:
#			print("0",end=" ")
#	print()
#________________________________________________________________31 ulesanne_____________________________________________________________________
import random
n=random.randint(0, 10)
while True:
    text = input("Введите число или стоп для выхода: ")
    if text == "стоп":
        print("Выход из программы! До встречи! Загадано было", n)
        break
    elif text == n:
        print("Победа")
    else:
        print("Попробуйте еще")
























































































#print("FOR".center(60,"_"))
#print()
#for i in range(5):
	#print("Hello world!")
#print("WHILE TRUE".center(60,"_"))
#print()
#k=0
#while True:
	#k+=1
	#print("Hello world!")
	#if k==5: break
#print("WHILE TINGIMUSEGA".center(60,"_"))
#k=0
#while k<5:
	#print("Hello World!")
	#k+=1
