import math

def main():
    pass

if __name__ == '__main__':
    main()
    x= float(input("Grade Point:"))
    y = math.floor(x)
    grade_map = {4:'D',5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}
    grade_point_performance = {4:'Poor' , 5:'Below Average', 6:'Average', 7:'Good', 8:'Very Good', 9:'Excellent', 10:'Outstanding'}

    if y in grade_map:
        print("Your Grade is %s and %s performance"% (grade_map[y], grade_point_performance[y]))
    else:
        print("ERROR: OUT OF RANGE")

