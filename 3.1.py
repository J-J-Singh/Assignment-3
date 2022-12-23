def main():
    pass

if __name__ == '__main__':
 main()
x=str(input("Sentence:"))
y=str(input("Character/Word to be counted:"))

count_word = dict()
count_char = dict()

words = x.split()

print(x.count(y))
