def count(file_name,counter,position):
    for each_line in file_name:
        each_line = each_line.strip()
        for each_parenthesis in each_line:
            if counter == -1:
                print(position)
                exit()
            elif each_parenthesis == "(":
                counter += 1
                position += 1
            else:
                counter -= 1
                position += 1

if __name__=="__main__":
    file_name = open("input.txt","r")
    counter = 0
    position = 0
    count(file_name,counter,position)
    file_name.close()