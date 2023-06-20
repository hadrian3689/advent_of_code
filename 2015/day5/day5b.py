def between(each_line):
    length = len(each_line) - 2
    for count in range(0,length):
        if each_line[count] == each_line[count + 2]:
            return True

def double(each_line):
    count = 2
    previous = 0
    while count < len(each_line):
        pair = each_line[previous:count]
        check = each_line[count:]
        if pair in check:
            return True
        else:
            count += 1
            previous += 1

def nice(file_name):
    nice_count = 0
    for each_line in file_name:
        each_line = each_line.strip()
        if double(each_line) and between(each_line):
            nice_count += 1
    print(nice_count)

if __name__=="__main__":
    file_name = open("input.txt","r")
    nice(file_name)