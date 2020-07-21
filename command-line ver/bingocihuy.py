import random   
import os       
import time     

#todo
#level bot hard
#multiplayer
#check turn perlu dipisah ta gak ?

def Bingo_Create_Table():
    Table = [[0 for Column in range(5)] for Row in range(5)]
    numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    for Row in range (5):
        for Column in range(5):
            numtmp = random.choice(numList)
            Table[Row][Column] = numtmp
            numList.remove(numtmp)

    return Table

def Bingo_Print(Table1, Line1, Table2, Line2, Mode):
    os.system('cls')
    print("BINGO CIHUYYYY")
    print()
    print()
    #Table1
    if (Mode == "CASUAL"):
        print("TABEL LAWAN")
        print()
        for Row in range(5):
            for Column in range(5):
                if not(Table1[Row][Column] == "X" or Table1[Row][Column] == "X "):
                    if (Table1[Row][Column] < 10):
                        print(str(Table1[Row][Column]) + "   ", end="")
                    elif (Table1[Row][Column] >= 10):
                        print(str(Table1[Row][Column]) + "  ", end="")
                elif (Table1[Row][Column] == "X"):
                    print(str(Table1[Row][Column]) + "   ", end="")
                elif (Table1[Row][Column] == "X "):
                    print(str(Table1[Row][Column]) + "  ", end="")
            print()
        print()
        Bingo = "BINGOOOOOOOO"
        Win = ""
        for Row in range(Line1):
            Win = Win + Bingo[Row] + "   "
        print(Win)
        print()
        print()
    #Table2
    print("TABELMU")
    print()
    for Row in range(5):
        for Column in range(5):
            if not(Table2[Row][Column] == "X" or Table2[Row][Column] == "X "):
                if (Table2[Row][Column] < 10):
                    print(str(Table2[Row][Column]) + "   ", end="")
                elif (Table2[Row][Column] >= 10):
                    print(str(Table2[Row][Column]) + "  ", end="")
            elif (Table2[Row][Column] == "X"):
                print(str(Table2[Row][Column]) + "   ", end="")
            elif (Table2[Row][Column] == "X "):
                print(str(Table2[Row][Column]) + "  ", end="")
        print()
    print()
    Bingo = "BINGOOOOOOOO"
    Win = ""
    for Row in range(Line2):
        Win = Win + Bingo[Row] + "   "
    print(Win)
    print()
    print()

def Bingo_Bot_Turn(Table, nums, Level):
    if (Level == "EZ"):
        turn = random.choice(nums)
    elif (Level == "NANGGUNG"):
        if (Table[2][2] != "X" and Table[2][2] != "X "):
            turn = Table[2][2]
        else:
            numsnanggung = []
            Row = 0
            while (Row <= 4):
                Column = 0
                while (Column <= 4):
                    if (Table[Row][Column] != "X" and Table[Row][Column] != "X "):
                        numsnanggung.append(Table[Row][Column])
                    Column += 2
                Row += 2
            turn = random.choice(numsnanggung)
    return turn

def Bingo_Player_Turn():
    turn = input("Masukkan angka: ")
    while(not(turn.isdecimal()) or int(turn) < 1 or int(turn) > 25):
        if (not(turn.isdecimal())):
            print("Masukkan angka")
            turn = input("Masukkan angka: ")
        else:
            if (int(turn) == 999):
                break
            else:
                print("Masukkan angka 1-25!")
                turn = input("Masukkan angka: ")

    return int(turn)

def Bingo_Turn_Check(Table1, Table2, Turn):
    for Row in range(5):
        for Column in range(5):
            if not(Table1[Row][Column] == "X" or Table1[Row][Column] == "X "):
                if (Table1[Row][Column] < 10 and Table1[Row][Column] == Turn):
                    Table1[Row][Column] = "X"
                elif (Table1[Row][Column] >= 10 and Table1[Row][Column] == Turn):
                    Table1[Row][Column] = "X "

    for Row in range(5):
        for Column in range(5):
            if not(Table2[Row][Column] == "X" or Table2[Row][Column] == "X "):
                if (Table2[Row][Column] < 10 and Table2[Row][Column] == Turn):
                    Table2[Row][Column] = "X"
                    return True
                elif (Table2[Row][Column] >= 10 and Table2[Row][Column] == Turn):
                    Table2[Row][Column] = "X "
                    return True

def Bingo_Line_Check(Table):
    Line = 0
    #ngecek baris
    for x in range(5):
        isLine = 0
        for y in range(5):
            if (Table[x][y] == "X" or Table[x][y] == "X "):
                isLine += 1

            if (isLine == 5):
                Line += 1
    ###################################################    
    #ngecek kolom
    for y in range(5):
        isLine = 0
        for x in range(5):
            if (Table[x][y] == "X" or Table[x][y] == "X "):
                isLine += 1

            if (isLine == 5):
                Line += 1
    ###################################################
    #ngecek miring 1
    x = 0
    y = 0
    isLine = 0
    while (x <= 4 and (Table[x][y] == "X" or Table[x][y] == "X ")):
        isLine += 1
        x += 1
        y += 1 
    if (isLine == 5):
        Line += 1
    ###################################################
    #ngecek miring 2
    x = 0
    y = 4
    isLine = 0
    while (x <= 4 and y >= 0 and (Table[x][y] == "X" or Table[x][y] == "X ")):
        isLine += 1
        x += 1
        y -= 1
    if (isLine == 5):
        Line += 1

    return Line


os.system('cls')
print("BINGO CIHUYYYY")
print()
print()

#input play
time.sleep(1)
Bingo_Play = input("Main?(Y/N) ").upper()
while not (Bingo_Play == "Y" or Bingo_Play == "N"):
    os.system('cls')
    print("BINGO CIHUYYYY")
    print()
    print()
    print("Masukkan (Y/N)!")
    time.sleep(2)
    Bingo_Play = input("Mau main(Y/N)? ").upper()
print()
###################################################

#play
while (Bingo_Play == "Y"):
    #pilih level
    os.system('cls')
    print("BINGO CIHUYYYY")
    print()
    print()
    time.sleep(1)
    print("EZ       : Bot easy.")
    print("Nanggung : Bot medium.")
    print("More levels soon! gausah bimbang.")
    time.sleep(1)
    Bingo_Level = input("Level?(EZ/Nanggung) ").upper()
    while not (Bingo_Level == "EZ" or Bingo_Level == "NANGGUNG"):
        print("Masukkan (EZ/Nanggung)!")
        time.sleep(2)
        print("EZ       : Bot easy.")
        print("Nanggung : Bot medium.")
        print("More levels soon! gausah bimbang.")
        time.sleep(1)
        Bingo_Level = input("Level?(EZ/Nanggung) ").upper()
    ###################################################

    #pilih mode
    os.system('cls')
    print("BINGO CIHUYYYY")
    print()
    print()
    time.sleep(1)
    print("Casual   : Kedua tabel pemain ditampilkan.")
    print("Pro      : Hanya tabel pemain ditampilkan.")
    time.sleep(1)
    Bingo_Mode = input("Mode?(Casual/Pro) ").upper()
    while not (Bingo_Mode == "CASUAL" or Bingo_Mode == "PRO"):
        print("Masukkan (Pro/Casual)!")
        time.sleep(2)
        print("Casual   : Kedua tabel pemain ditampilkan.")
        print("Pro      : Hanya tabel pemain ditampilkan.")
        Bingo_Mode = input("Mode?(Casual/Pro) ").upper()
    ###################################################

    #buat tabel baru
    Player_Table = Bingo_Create_Table()
    Player_Line = 0
    Bot_Table = Bingo_Create_Table()
    Bot_Line = 0

    #cetak tabel awal
    Bingo_Print(Bot_Table, Bot_Line, Player_Table, Player_Line, Bingo_Mode)
    ###################################################

    #play
    num_Bot = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    while (Bot_Line < 5 and Player_Line < 5):
        Player_Turn = Bingo_Player_Turn()
        if (Player_Turn == 999):
            for Row in range(5):
                for Column in range(5):
                    Player_Table[Row][Column] = "X"
            Player_Line = 12
        else:
            is_Availaible = False
            is_Availaible = Bingo_Turn_Check(Player_Table, Bot_Table, Player_Turn)
            while (not(is_Availaible)):
                print("Angka", Player_Turn, "sudah dimasukkan!")
                Player_Turn = Bingo_Player_Turn()
                is_Availaible = Bingo_Turn_Check(Player_Table, Bot_Table, Player_Turn)
            num_Bot.remove(Player_Turn)

            #cek line
            Bot_Line = Bingo_Line_Check(Bot_Table)
            Player_Line = Bingo_Line_Check(Player_Table)

            #jika line belom 5
            if (Bot_Line < 5 and Player_Line < 5):
                Bingo_Print(Bot_Table, Bot_Line, Player_Table, Player_Line, Bingo_Mode)
                print("Player 1 memilih angka", Player_Turn)
                time.sleep(2)
                ###################################################

                #turn bot
                print("Bot..")
                time.sleep(2)
                print("...")
                time.sleep(5)

                Bot_Turn = Bingo_Bot_Turn(Bot_Table, num_Bot, Bingo_Level)
                num_Bot.remove(Bot_Turn)
                is_Availaible = Bingo_Turn_Check(Player_Table, Bot_Table, Bot_Turn)

                #cek line
                Bot_Line = Bingo_Line_Check(Bot_Table)
                Player_Line = Bingo_Line_Check(Player_Table)

                #cetak tabel
                Bingo_Print(Bot_Table, Bot_Line, Player_Table, Player_Line, Bingo_Mode)
                print("Bot memilih angka", Bot_Turn)
                time.sleep(2)
                ###################################################

    #Bot_Line atau Player_Line sudah ada yang lebih dari 5
    Bingo_Print(Bot_Table, Bot_Line, Player_Table, Player_Line, "CASUAL")

    if (Player_Line > Bot_Line):
        print("Kamu menang!")
    else:
        print("Kamu kalah!")
    ###################################################

    #input play
    time.sleep(1)
    Bingo_Play = input("Main lagi?(Y/N) ").upper()
    while not (Bingo_Play == "Y" or Bingo_Play == "N"):
        print("Masukkan (Y/N)!")
        time.sleep(2)
        Bingo_Play = input("Main lagi?(Y/N) ").upper()
    print()
    ###################################################

os.system('cls')
print("BINGO CIHUYYYY")
print()
print()
print()
print()
print("MAKASIH DAH MAEN")