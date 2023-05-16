def perimeter(smallest_values):
        smallest_side1 = min(smallest_values)
        smallest_values.remove(smallest_side1)
        smallest_side2 = min(smallest_values)
        smallest_values.remove(smallest_side2)
        total_perimeter = 2*int(smallest_side1) + 2*int(smallest_side2)
        return total_perimeter

def count(file_name,counter):
    for each_line in file_name:
        each_line = each_line.strip()
        list_values = each_line.split('x')
        smallest_values = []
        number1 = int(list_values[0])
        smallest_values.append(number1)
        number2 = int(list_values[1])
        smallest_values.append(number2)
        number3 = int(list_values[2])
        smallest_values.append(number3)
        area = number1*number2*number3
        total_perimeter = perimeter(smallest_values)
        total = total_perimeter + area
        counter += total
    print(counter)

if __name__=="__main__":
    file_name = open("input.txt","r")
    counter = 0
    count(file_name,counter)
    file_name.close()