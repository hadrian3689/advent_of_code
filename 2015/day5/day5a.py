def bad_string(each_line):
    bad_string_list = ["ab","cd","pq","xy"]
    for each_bad_string in bad_string_list:
        if each_bad_string in each_line:
            return False
        else:
            continue
    return True

def double_letter(each_line):
    index = 1
    try:
        for each_char in each_line:
            if each_char == each_line[index]:
                return True
            else:
                index += 1
    except IndexError:
        return False

def vowels(each_line):
    vowels = "aeiou"
    counter = 0
    for vowel in vowels:
        for each_char in each_line:
            if each_char == vowel:
                counter += 1
    return counter

def nice(file_name):
    nice_count = 0
    for each_line in file_name:
        each_line = each_line.strip()
        counter = vowels(each_line)
        if counter >= 3 and double_letter(each_line) and bad_string(each_line):
            nice_count += 1
        else:
            continue
    print(nice_count)

if __name__=="__main__":
    file_name = open("input.txt","r")
    nice(file_name)