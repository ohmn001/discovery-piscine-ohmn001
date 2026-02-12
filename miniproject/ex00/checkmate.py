#!/usr/bin/env python3

def checkmate(board):
    #แปลง string ที่ user ส่งมาผ่าน main() .ให้กลายเป็น list เพื่อใช้ต่อ
    lines = board.strip().split('\n') #.strip()-->ดักกรณีมีช่องว่าง .split('/n') --> ตัดการเว้นบรรทัดเเล้วเอาไปสรา้ง list
    #.strip()--> ผลที่ได้: "R...\n.K..\n..P.\n...."
    #.split('/n') --> ผลที่ได้: ["R...", ".K..", "..P.", "...."]
    num_rows = len(lines)
    grid = [list(line) for line in lines] #รูปสร้าง ... เเต่ละบรรทัดโดย data type คือ list
    # ผลลัพธ์ grid :
    # [
    #   ['R', '.', '.', '.'],
    #   ['.', 'K', '.', '.'],
    #   ['.', '.', 'P', '.'],
    #   ['.', 'Q', '.', '.']
    # ]
    for  row in grid:
        if len(row) != num_rows: #คิดว่าถ้าความกว้างเเถวไม่เท่าความสูงก็ไม่เหลี่ยม
            print(' not square')
            return
    
    size = len(grid)
    #ผลที่ได้: --> 4

    #หา ตน king(K)
    k_row , k_col = -1,-1 #ต้องระบุ -1 --> บอกว่ามันไม่มีอยู่ในกระดาน
    k_count = 0
    for i_row in range(size): #ลูปหา K เเต่ละ row --> เริ่มนับ 0,1,2,3
        for i_column in range(size): #ลูปหา K เเต่ละ row --> เริ่มนับ 0,1,2,3
            if grid[i_row][i_column] == 'K': 
                k_count = k_count+1
                k_row , k_col = i_row , i_column
                #ผลลัพธ์: k_row , k_col = 1,1
                break

    #ดักกรณีไม่มี king หรือ มี king 2 ตัว
    if k_row == 0 : 
        print('you dont have king !!!')
        return
    if k_row > 1 : 
        print('you have more 1 king !!!')
        return
    #เขียนดักกรณี K สองตัวด้วย


    #อธิบายการทำงานฟังชั่นนี้หน่อย
    def enemy_position(row , column , enemy_type):
        if (0 <= row < size) and (0 <= column < size): #row,column ต้องอยู่ในกระดานเเละไม่ติดลบ
                return grid[row][column] in enemy_type
        return False
    
    is_check = False

    #Pawn(P) --> เดินหน้าสอง
    if enemy_position(k_row+1 , k_col-1 , 'P') or enemy_position(k_row+1 , k_col+1 , 'P'): 
        #ตอนนี้ k_row,k_col คือ ตน.ของK เเล้ว
        #k_row,k_col = 2,0 หรือ k_row,k_col = 2,2 --> K โดนกิน
        is_check = True
    
    #Rook(R) --> เดินเป็นรูป +
    directions_Rook = [(0, 1), (0, -1), (1, 0), (-1, 0)] #ซ้าย-ขวา , ขึ้น-ลง
    for d_row , d_col in directions_Rook:
        curr_row , curr_col = k_row + d_row, k_col + d_col 
        #ใช้ k_row + d_row ตรงๆไม่ได้เพราะมันจะเป็นกาเปลี่ยนค่า
        #k_row,k_col = 2,2 --> curr_r, curr_c = (2,3)
        while (0 <= curr_row < size) and (0 <= curr_col < size):
            if grid[curr_row][curr_col] != '.':
                if grid[curr_row][curr_col] == 'R':
                    is_check = True
                break
            curr_col = curr_col + d_col
            curr_row = curr_row + d_row
    
    #Bishop (B) --> เดินเป็นรูป X
    directions_ฺฺBishop = [(1, 1), (1, -1), (-1, 1), (-1, -1)] #เฉียง
    for d_row , d_col in directions_ฺฺBishop:
        curr_col , curr_row =  k_col + d_col , k_row + d_row
        while (0 <= curr_row < size) and (0 <=  curr_col < size) :
            if grid[curr_row][curr_col] != '.':
                if grid[curr_row][curr_col] == 'B':
                    is_check = True
                break
            curr_col = curr_col + d_col
            curr_row = curr_row + d_row
    
    #Queen(Q) --> เดินเหมือน B ผสม R
    directions_queen = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for d_row , d_col in directions_queen:
        curr_col , curr_row =  k_col + d_col , k_row + d_row
        while (0 <= curr_row < size) and (0 <=  curr_col < size) :
            if grid[curr_row][curr_col] != '.':
                if grid[curr_row][curr_col] == 'Q':
                    is_check = True
                break
            curr_col = curr_col + d_col
            curr_row = curr_row + d_row
            
    if is_check == True:
        print("Success")
    else:
        print("Fail")