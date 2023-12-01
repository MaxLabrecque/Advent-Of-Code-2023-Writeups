
sum = 0
def main():
    file = open("inputquiz1.txt", "r")
    lines = file.readlines()
    file.close()
    print(lines)
    count = 0
    for line in lines:
        first = 9999
        last = 9999
        for i in range(len(line)):
            try:
                if first == 9999:
                    first = int(line[i])
                    count += 1
                    continue
                last = int(line[i])
            except:
                continue
        if last == 9999:
            last = first

        number = first * 10 + last
        print(number)
        calcSum(number)
    print(sum)

def calcSum(number):
    global sum
    sum += number

if __name__ == "__main__":
    main()
