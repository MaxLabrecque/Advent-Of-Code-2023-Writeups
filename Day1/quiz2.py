# Amelioration to do : with regex

sum = 0
map_number_letter = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

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
                curr = [line[i]]
                for j in range(1, 5):
                    # if the rest of the line is less than i + j, break
                    try:
                        curr.append(line[i+j])
                    except:
                        break

                    if "".join(curr) in map_number_letter:
                        if first == 9999:
                            first = map_number_letter["".join(curr)]
                            count += 1
                            break
                        last = map_number_letter["".join(curr)]
                        break
                    continue
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