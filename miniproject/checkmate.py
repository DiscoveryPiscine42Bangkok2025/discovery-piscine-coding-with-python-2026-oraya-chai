#!/usr/bin/env python3

def checkmate(board_str=None):

    # 1 กรณีที่ไม่มีinput
    if board_str is None: 
        print("Error")
        return

    # 2 กรณีinputไม่ใช่string 
    if not isinstance(board_str, str):
        print("Error")
        return 
    
    rows = board_str.splitlines() 
    # ['', 'R...', '.K..', '..P.', '....'] โดย '' มาจากnewlineตัวแรกในtripple quoteเพราะมีการกดขึ้นบรรทัดใหม่เลยเป็นงั้น
    # ไม่มีที่ตัวสุดท้ายเพราะ splitlines() ไม่สร้างสมาชิกว่างจากnewlineตัวสุดท้าย
    rows = [row for row in rows if row.strip() != ""]
    # ['R...', '.K..', '..P.', '....']
    
    # 3 กรณีกระดานว่าง (board = " ")
    if len(rows) == 0:
        print("Error") 
        return

    # 4 กรณีไม่เป็นสี่เหลี่ยมจตุรัส
    n = len(rows)
    for row in rows:
        if len(row) != n:
            print("Error")
            return
        
    # 5 กรณีไม่มีKing/kingมากกว่า1
    king_position = None # ไว้เก็บตำแหน่งคิงในรูปของ(row, col)
    king_count = 0 # นับจำนวนคิงที่เจอมีกี่ตัว
    # n ตัวบอกว่าจตุรัสเท่าไร / n=4 -> 0 1 2 3
    # i = แถว
    # j = column
    for i in range(n):
        for j in range(n):
            if rows[i][j] == "K":
                king_position = (i, j)
                king_count += 1
    if king_count > 1:
        print("Error")
        return 
    elif king_count == 0:
        print("Error")
        return
    king_row, king_col = king_position

    # 5 กรณีเช็คหมากเดินเลยขอบ
    def in_bounds(ro, co):
        return 0 <= ro < n and 0 <= co < n

    # 6 ตรวจหมากบนกระดาน
    for i in range(n):
        for j in range(n):
            piece = rows[i][j]
            # คัดเฉพาะหมาก R/B/Q/P ถ้าไม่ใช่ก็ให้ข้ามไปช่องถัดไป
            if piece not in ("R", "B", "Q", "P"):
                continue

            # ROOK
            if piece == "R":
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                # ลง (1,0) row + 1, col +0
                # ขึ้น (-1,0) row -1, col +0
                # ขวา (0,1) row +0, col +1
                # ซ้าย (0,-1) row +0, col -1

            # BISHOP
            elif piece == "B":
                directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
                # ขวาล่าง (1,1) row +1, col +1
                # ซ้ายล่าง (1,-1) row +1, col -1
                # ขวาบน (-1,1) row -1, col 1
                # ซ้ายบน (-1,-1) row -1, col -1
            
            # QUEEN
            elif piece == "Q":
                directions = [
                    (1,0), (-1,0), (0,1), (0,-1),
                    (1,1), (1,-1), (-1,1), (-1,-1)]
                # Queen = R + B

            # PAWN
            elif piece == "P":
                pawn_attacks = [(-1, -1), (-1, 1)]
                # ซ้ายบน (-1,-1) row -1, col-1
                # ขวาบน (-1,1) row -1, col 1

                # ตรวจเส้นทางเดินpawn -> ให้มีการตรวจทั้ง2ฝั่ง 
                for dr, dc in pawn_attacks:
                    # ซ้ายบน dr = -1, dc = -1
                    # ขวาบน dr = -1, dc = 1 
                    # มาคำนวณช่องที่ pawn โจมตีได้
                    ro = i + dr 
                    co = j + dc
                    if in_bounds(ro, co) and (ro, co) == (king_row, king_col):
                        # เช็คว่ายังอยู่ในกระดาน
                        # เช็คช่องที่ Pawn โจมตี = ช่องที่ King อยู่
                        # ถ้าใช่ก็คือ king โดนตี
                        print("Success")
                        return
                # ตรวจpawn เสร็จแล้ว ข้ามไปดูช่องถัดไปในกระดาน
                continue
            # ตรวจเส้นทางของ R/B/Q
            for dr, dc in directions:
                ro, co = i + dr, j + dc

                # ยังไม่หลุดกระดานก็ให้เดินต่อไปเรื่อยๆ
                while in_bounds(ro, co):
                    if rows[ro][co] == "K":
                        # kingโดนตี
                        print("Success")
                        return
                    # เจอหมากตัวอื่นขวางให้หยุด -> หมากกินข้ามตัวอื่นไม่ได้
                    elif rows[ro][co] in ("R", "B", "Q", "P"):
                        break
                    # เลื่อนไปอีก1ช่องในทิศทางเดิม จนกว่าจะหลุดขอบ
                    ro += dr
                    co += dc
    # kingไม่โดนตี
    print("Fail")
    return



