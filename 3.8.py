def main():
    pass

if __name__ == '__main__':
    main()
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
print("Set1:",Set1)
print("Set2:",Set2)
print("Set3:",Set3)
Set4=Set1^Set2                                                                                                  # (^) used to find (Union of sets - interesection part in sets)
print("Set of all elements that are in Set1 and Set2 but not both:",Set4)
Set5=Set1^Set2^Set3                                                                                             # (^) used to find (Union of sets - interesection part in sets)
print("Set of all elements that are in only one of the three sets Set1,Set2 and Set3:",Set5)
Set6={1,2,3,4,5,6,7,8,9,10}
print("Set of all integers in the range 1 to 10 that are not in Set1:",Set6-Set1)                               # (-) operator used to find difference of sets
print("Set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3:",Set6-(Set1|Set2|Set3))     # (|) operator used to create union of sets
