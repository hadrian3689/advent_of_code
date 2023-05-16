def count(file_name,counter):
    for each_line in file_name:
        each_line = each_line.strip()
        for each_parenthesis in each_line:
            if each_parenthesis == "(":
                counter += 1
            else:
                counter -= 1
        print(counter)

if __name__=="__main__":
    file_name = open("input.txt","r")
    counter = 0
    count(file_name,counter)
    file_name.close()