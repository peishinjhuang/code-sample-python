import tkinter as tk
import random

def click():
    global flag
    if(flag == 0):  #假如未答對
        setRandomNum() #產生隨機答案"串列"
        rdans="" 
        for i in rdAnswer:   #印出答案以供對照
            rdans+=str(i)
        resulttext.set(rdans) 
        
        global rows #新增及設定使用者的答案
        colstext = []
        for i in range(3):
            coltext = tk.StringVar()
            colstext.append(coltext)
            cols = tk.Label(win, textvariable=coltext,font=("calibri", 20))
            cols.grid(row=rows, column=i)
        rows+=1

        global count
        count +=1
        colstext[0].set(count)
        colstext[1].set(entrytext.get())
    
        result = compareNums() #比對答案串列
        colstext[2].set(result)

        if (flag == 1): #若第一次就答對, 則印出"贏得遊戲"
            cols = tk.Label(win, text="You win the game!",
                            font=("calibri", 20), fg="brown")
            cols.grid(row=rows, column=0, columnspan=3)
            #flagtext.set(flag)
            return


def setRandomNum():         #產生隨機答案"串列"(其元素為"數值")
    if(len(rdAnswer)==0):       #首次答案串列為0, 需產生"數字不重複"的答案串列
        numList = list(range(10))
        for i in range(4):
            rdNum = random.choice(numList)
            numList.remove(rdNum)
            rdAnswer.append(rdNum)

def compareNums():      #比對答案串列
    userInput = entrytext.get()
    inputAry = list(userInput)      #將使用者答案轉成串列(其元素為"字串")
    inputIntAry=[]      #將串列裡的元素轉成"數值", 才能與"答案串列"比對
    for k in inputAry:
        inputIntAry.append(int(k))
    correctloc=0        #計算正確位置的個數
    correctNum=0        #計算正確數字的個數
    for i in range(4):
        if (rdAnswer[i]==inputIntAry[i]):
            correctloc +=1
        for j in range(4):
            if(inputIntAry[i] == rdAnswer[j]):
                correctNum +=1
    if(correctloc == 4):        #若4個位置皆正確, 則判斷答對
        global flag
        flag = 1
    return(str(correctloc)+"A"+str(correctNum)+"B")         #回答結果(*A*B的形式)

#------------code starting-----------

rdAnswer = []  #隨機產生的答案

count=0 #使用者的輸入次數
rows = 4 #印出使用者答案的起始列數

flag = 0 #判斷是否答對

win = tk.Tk()

lblrow1 = tk.Label(win, text="please input 4 different numbers: ")
lblrow1.grid(row=0, column=0)

entrytext = tk.StringVar() #讀取使用者輸入的數字
entry = tk.Entry(win, textvariable=entrytext)
entry.grid(row=0, column=1, columnspan=2)

btn = tk.Button(win, text="Guess the number!",  #按鈕
                bg="aliceblue", fg="mediumblue",
                font=("calibri", 20), command = click)
btn.grid(row=1, column=0, columnspan=3)

lblrow2 = tk.Label(win, text="The answer is: ")
lblrow2.grid(row=2, column=0, columnspan=2)

resulttext = tk.StringVar() #隨機產生的答案(供對照, 以確保程式無錯誤)
ans = tk.Label(win, textvariable=resulttext)
ans.grid(row=2, column=1)

rowstring = ["Times","Your Number","Hint"]
times=0
for i in rowstring:
    lblrow3 = tk.Label(win, text=i, font=("calibri", 12))
    lblrow3.grid(row=3, column=times)
    times += 1


#flagtext = tk.StringVar() #判斷是否答對(答對時, flag=1)
#flaglbl = tk.Label(win, textvariable=flagtext)
#flaglbl.grid(row=3, column=0, columnspan=3)
#flagtext.set(flag)

win.mainloop()
