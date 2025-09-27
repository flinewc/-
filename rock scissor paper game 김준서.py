from tkinter import *
from random import *
win = Tk()

win.title("Rock Paper Scissors Game")

basic_img = PhotoImage(file = "ready.png")
def change_img(user) :
  List = ["scisors.png", "rock.png", "paper.png"]
  com = randint(0,2)

  com_img = PhotoImage(file = List[com])
  user_img = PhotoImage(file = List[user])
  lbl_com['image'] = com_img
  lbl_com.image = com_img
  lbl_user[image] = user_img
  lbl_user.image = user_img
def game(com,user) :

  
lbl_com = Label(win, image = basic_img)
lbl_user = Label(win, image = basic_img)

lbl_res = Label()

lbl_name1 = Label(text = "computer")
lbl_name2 = Label(text = "user")

btn_scissor = Button(text = "scissor")
btn_rock = Button(text = "rock")
btn_paper = Button(text = "paper")

lbl_com.grid(row = 0, column = 0)
lbl_user.grid(row = 0, column = 2)
btn_scissor.grid(row = 2, column = 0)
btn_rock.grid(row = 2, column = 1)
btn_paper.grid(row = 2, column = 2)
lbl_name1.grid(row = 1, column = 0)
lbl_name2.grid(row = 1, column = 2)


win.mainloop()





















90
