def CColor(n):
    input_color = []
    m = n[1:]
    input_color.append([m[0:2],m[2:4],m[4:6]])
    for i in range(len(input_color)):
        for j in range(3):
            input_color[i][j] = int(input_color[i][j],16)
            input_color[i][j] = 255 - input_color[i][j]
            input_color[i][j] = f'{input_color[i][j]:02X}'
    output = []
    for i in range(len(input_color)):
        m = '#'
        for j in range(3):
            m+=input_color[i][j]
        output.append(m)
    for i in output:
        return i    
        
        
