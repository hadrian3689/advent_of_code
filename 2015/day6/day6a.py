import re

def instructions(input):
    light_track = set()
    for line in input:
        numbers = re.findall('(0|[1-9]{1}[0-9]{0,2})',line.strip())
        x1,x2,y1,y2 = numbers[0],numbers[2],numbers[1],numbers[3]
        if "turn on" in line.strip():
            for x in range(int(x1),(int(x2) + 1)):
                for y in range(int(y1),(int(y2) + 1)):
                    coordinates = str(x) + "," + str(y)
                    if coordinates in light_track:
                        continue
                    else:
                        light_track.add(coordinates)

        elif "turn off" in line.strip():
            for x in range(int(x1),(int(x2) + 1)):
                for y in range(int(y1),(int(y2) + 1)):
                    coordinates = str(x) + "," + str(y)
                    light_track.discard(coordinates)
                    if coordinates in light_track:
                        light_track.discard(coordinates)
                    else:
                        continue

        else:
            for x in range(int(x1),(int(x2) + 1)):
                for y in range(int(y1),(int(y2) + 1)):
                    coordinates = str(x) + "," + str(y)
                    if coordinates in light_track:
                        light_track.discard(coordinates)
                    else:
                        light_track.add(coordinates)

    print(len(light_track))

if __name__=="__main__":
    input = open('input.txt','r')
    instructions(input)