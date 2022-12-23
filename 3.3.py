def main():
    pass

if __name__ == '__main__':
    main()

N=int(input("Enter number of elements in list:"))                               #to take input of number of terms in list
i=1
LIST=[]
while(i<=N):                                                                    #loop run from 1 to N
  INPUT=int(input("Enter a number:"))                                           #to take input of a number
  SQ= INPUT*INPUT                                                               #to store square of number that is given as input in INPUT
  t=(INPUT,SQ)                                                                  #to create a tuple
  LIST.append(t)                                                                #tuple added in list
  i+=1                                                                          #updating statement
print("The tuples are :")
print(LIST)
