def count(file_name):
    turn = 0
    coordinates_s = [0,0]
    coordinates_r = [0,0]
    final_list_s = [[0,0]]
    final_list_r = [[0,0]]
    for each_line in file_name:
        for each_direction in each_line:
            each_direction = each_direction.strip()
            if each_direction == ">":
                if turn == 0:
                    coordinates_s[0] += 1
                    final_list_s.append(coordinates_s[:])
                    turn += 1
                else:
                    coordinates_r[0] += 1
                    final_list_r.append(coordinates_r[:])
                    turn -= 1               
            elif each_direction == "v":
                if turn == 0:
                    coordinates_s[1] -= 1
                    final_list_s.append(coordinates_s[:])
                    turn += 1
                else:
                    coordinates_r[1] -= 1
                    final_list_r.append(coordinates_r[:])
                    turn -= 1  
            elif each_direction == "<":
                if turn == 0:
                    coordinates_s[0] -= 1
                    final_list_s.append(coordinates_s[:])
                    turn += 1
                else:
                    coordinates_r[0] -= 1
                    final_list_r.append(coordinates_r[:])
                    turn -= 1  
            else:
                if turn == 0:
                    coordinates_s[1] += 1
                    final_list_s.append(coordinates_s[:])
                    turn += 1
                else:
                    coordinates_r[1] += 1
                    final_list_r.append(coordinates_r[:])
                    turn -= 1
                    
    final_list = final_list_s + final_list_r
    remove_duplicates = []
    [remove_duplicates.append(each_item) for each_item in final_list if each_item not in remove_duplicates]
    print(len(remove_duplicates))

if __name__=="__main__":
    file_name = open("input.txt","r")
    count(file_name)
    file_name.close()