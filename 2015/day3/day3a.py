def count(file_name):
    coordinates = [0,0]
    final_list = [[0,0]]
    for each_line in file_name:
        for each_direction in each_line:
            each_direction = each_direction.strip()
            if each_direction == ">":
                coordinates[0] += 1
                final_list.append(coordinates[:])
            elif each_direction == "v":
                coordinates[1] -= 1
                final_list.append(coordinates[:])
            elif each_direction == "<":
                coordinates[0] -= 1
                final_list.append(coordinates[:])
            else:
                coordinates[1] += 1
                final_list.append(coordinates[:])
    remove_duplicates = []
    [remove_duplicates.append(each_item) for each_item in final_list if each_item not in remove_duplicates]
    print(len(remove_duplicates))

if __name__=="__main__":
    file_name = open("input.txt","r")
    count(file_name)
    file_name.close()