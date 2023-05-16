def count(file_name,counter):
    for each_line in file_name:
        each_line = each_line.strip()
        list_values = each_line.split('x')
        smallest_side_values = []
        area1 = 2*int(list_values[0])*int(list_values[1])
        area2 = 2*int(list_values[1])*int(list_values[2])
        area3 = 2*int(list_values[0])*int(list_values[2])
        smallest_side_values.append(area1)
        smallest_side_values.append(area2)
        smallest_side_values.append(area3)
        smallest_side = min(smallest_side_values)
        total_area = area1 + area2 + area3 + (smallest_side/2)
        counter += total_area
    print(counter)

if __name__=="__main__":
    file_name = open("input.txt","r")
    counter = 0
    count(file_name,counter)
    file_name.close()