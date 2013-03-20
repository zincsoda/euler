#!/usr/bin/python2.6

if __name__=="__main__":
    data = []
    for line in open('triangle.txt'):
        if line.strip():
            data.append(line)

    # build array
    triangle = []
    row_index = 0
    for row in data:
        triangle.append([])
        for col in row.split(' '):
            triangle[row_index].append(int(col))
        row_index += 1
    
    height = len(triangle)    
    for i in range(1, height):
        cur_base = triangle[height - i]
        new_base = triangle[height - i -1]
        for x in range(len(new_base)):
            triangle[height - i -1][x] = new_base[x] + max(cur_base[x], cur_base[x+1])

    print triangle[0][0]
   
