i = 0 #default loop table
while i <= 10:
    line = "Table de " + str(i) + ":"
    
    j = 0 #default loop result
    while j <= 10:
        line = line + " " + str(i * j)
        j = j + 1  
    print(line)
    
    i = i + 1