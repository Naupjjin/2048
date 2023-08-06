
import numpy as np
import gym
from gym import spaces
import time
import matplotlib.pyplot as plt
import random
import copy
import tkinter 
import math

Object_base=tkinter.Tk()
Object_base.title("地圖")
Object_base.resizable(False,False)
WINDOW=tkinter.Canvas(Object_base,width=500,height=500,bg="#005AB5")
WINDOW.pack()
neko=[
tkinter.PhotoImage(file="IMG/0.png"),
tkinter.PhotoImage(file="IMG/2.png"),
tkinter.PhotoImage(file="IMG/4.png"),
tkinter.PhotoImage(file="IMG/8.png"),
tkinter.PhotoImage(file="IMG/16.png"),
tkinter.PhotoImage(file="IMG/32.png"),
tkinter.PhotoImage(file="IMG/64.png"),
tkinter.PhotoImage(file="IMG/128.png"),
tkinter.PhotoImage(file="IMG/256.png"),
tkinter.PhotoImage(file="IMG/512.png"),
tkinter.PhotoImage(file="IMG/1024.png"),
tkinter.PhotoImage(file="IMG/2048.png")
]
score=0
def key_w_judge():
  global score
  for x in range(0,4):
      for y in range(1,4):
        now_num=map[y][x]
        available=0
        map[y][x]=0
        for i in range(y,-1,-1):
          if map[i][x]==0:
            
            available=i
        ###
        
        map[available][x]=now_num
        if available==0:
          pass
        elif map[available-1][x]==map[available][x] and merge_yn[available-1][x]==0:
          
          merge_yn[available-1][x]=1
          map[available][x]=0
          map[available-1][x]=now_num*2
          score+=now_num*2
  
 

def key_s_judge():
  global score
  for x in range(0,4):
      for y in range(2,-1,-1):
        now_num=map[y][x]
        available=0
        map[y][x]=0
        for i in range(y,4):
          if map[i][x]==0:
            
            available=i
      ##
        map[available][x]=now_num
        if available==3:
          pass
        elif map[available+1][x]==map[available][x] and merge_yn[available+1][x]==0:
          merge_yn[available+1][x]=1
          map[available][x]=0
          map[available+1][x]=now_num*2
          score+=now_num*2

def key_a_judge():
  global score
  for y in range(0,4):
      for x in range(1,4):
        now_num=map[y][x]
        available=0
        map[y][x]=0
        for i in range(x,-1,-1):
          if map[y][i]==0:
            
            available=i
        ###
        
        map[y][available]=now_num
        if available==0:
          pass
        elif map[y][available-1]==map[y][available] and merge_yn[y][available-1]==0:
          merge_yn[y][available-1]=1
          map[y][available]=0
          map[y][available-1]=now_num*2
          score+=now_num*2
  
def key_d_judge():
  global score
  for y in range(0,4):
      for x in range(2,-1,-1):
        now_num=map[y][x]
        available=0
        map[y][x]=0
        for i in range(x,4):
          if map[y][i]==0:
          
            available=i
            
        ###
        map[y][available]=now_num
        if available==3:
          pass
        elif map[y][available+1]==map[y][available] and merge_yn[y][available+1]==0:
          merge_yn[y][available+1]=1
          map[y][available]=0
          map[y][available+1]=now_num*2
          score+=now_num*2

def yn_lost(map):
  for i in range(len(map)):
    for j in range(len(map[0])):
      # Check above
      if i > 0 and map[i][j] == map[i-1][j]:
          return True
      # Check below
      if i < len(map)-1 and map[i][j] == map[i+1][j]:
          return True
      # Check left
      if j > 0 and map[i][j] == map[i][j-1]:
          return True
      # Check right
      if j < len(map[0])-1 and map[i][j] == map[i][j+1]:
          return True
  return False
available_x=[]
available_y=[]

merge_yn=[[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

map=[[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
judge_map=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
rx=random.randint(0,1)
ry=random.randint(0,3)
  
map[ry][rx]=2
rx=random.randint(2,3)
ry=random.randint(0,3)
map[ry][rx]=2
win=False
game_continue=True
while(game_continue):
  

  for y in range(0,4):
  
    for x in range(0,4):
      merge_yn[y][x]=0
  
  judge_map=copy.deepcopy(map)
  #
  for y in range(0,4):
    for x in range(0,4):   
      if map[y][x]==0:
          k=0
      else:
        k=int(math.log(map[y][x],2))
      WINDOW.create_image(70+120*x,70+120*y,image=neko[k])
        
  #
  
  key=input()
  
  if key=="w":
    key_w_judge()
      
 
  elif key=="s":
    key_s_judge()
     
  
  elif key=="a":
    key_a_judge()
     
        ###
  elif key=="d":
    key_d_judge()
   
  else:
    print("無效輸入")
    continue
  

  print("分數",score)

  


  if judge_map==map:
    continue
    #
  available_x=[]
  available_y=[]
  for y in range(0,4):
    for x in range(0,4):
      if map[y][x]==0:
        available_x.append(x)
        available_y.append(y)
  j=random.randint(0,len(available_x)-1)
  
  map[available_y[j]][available_x[j]]=2
  for i in map:
    if 2048 in i:
      win=True
      break
  
  if yn_lost(map)==False:
    break
  


if win==True:
  print("你贏了")
else:
  print("輸了")
Object_base.mainloop() 