# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 07:18:36 2019
Brute-force "Backtracking" Sudoku solver
@author: Antiochian
"""

#if you want to import a puzzle inside this code instead of using the console input, scroll down to line 97

import time
import numpy as np

#compares a proposed value with an array "slice"
#these slices are generated by the "check" functions that return a subarray of the larger grid
def testsection(value,gridsection):
    for i in np.nditer(gridsection):
        if value == i:
            return False
    return True

def checkrow(value,grid,ycoord): #this one returns a row vector
    gridsection = grid[ycoord,:]  
    return testsection(value,gridsection)

def checkcol(value,grid,xcoord):  #this one returns a column vector
    gridsection = grid[:,xcoord]
    return testsection(value,gridsection)

def checkbox(value,grid,ycoord,xcoord): #this messy one returns the 3x3 "box" the pointer is in
    if xcoord >= 6 and ycoord <= 2:
        #topright box
        gridsection = grid[:3,6:]
    elif xcoord <= 2 and ycoord <= 2:
        #topleft
        gridsection = grid[:3,:3]
    elif xcoord >= 6 and ycoord >= 6:
        #bottomright
        gridsection = grid[6:,6:]
    elif xcoord <= 2 and ycoord >= 6:
        #bottomleft
        gridsection = grid[6:,:3]       
    elif 3 <= xcoord <= 5 and ycoord <= 2:
        #TOPMIDDLE
        gridsection = grid[:3,3:6]    
    elif 3 <= xcoord <= 5 and ycoord >= 6:
        #BOTTOMMIDDLE
        gridsection = grid[6:,3:6]
    elif xcoord <= 2 and 3 <= ycoord <= 5:
        #LEFTMIDDLE
        gridsection = grid[3:6,:3]
    elif xcoord >= 6 and 3 <= ycoord <= 5:
        #RIGHTMIDDLE
        gridsection = grid[3:6,6:] 
    elif 3 <= xcoord <= 5 and 3 <= ycoord <= 5:
        #MIDDLEMIDDLE
        gridsection = grid[3:6,3:6]    
    else: #somethings gone wrong!
        print("Something's gone wrong!")
        return False #this will throw an error and crash the program
    return testsection(value,gridsection)

def checkeverything(value,grid,xcoord,ycoord): #collates values of previous 3 check functions
    if checkrow(value,grid,ycoord) and checkcol(value,grid,xcoord) and checkbox(value,grid,ycoord,xcoord):
        return True
    else:
        return False
    
def find_next_blank(grid): #finds the (y,x) coordinates of the next blank space (later used as indices)
    for x in range(size):
        for y in range(size):
            if grid[y,x] == 0:
                return (y,x)
    return False #returns Fales if no blanks are found

def sudokusolve(grid):
    if all(0 != grid.flatten()): #Check if sudoku is done - this is quicker than calling the find_next_blank function
        return True
    (y,x) = find_next_blank(grid) #set pointer to a blank location
    for value in range(1,size+1):
        if checkeverything(value,grid,x,y): #if proposed value seems ok, proceed
            grid[y,x] = value #set grid, move on:
            if sudokusolve(grid):
                return True #ideally, program should break here and never come back
            grid[y,x] = 0 #if program executes this line, it implies a failure several steps down the line, so we wipe the pointer location and try again
            
        if value > size: #if we fail to find a single possibility
            print(grid)
            return False #backtrack
    return False #if all items are iterated through unsuccessfully, fail out of everything

def main():
    global size
    size = 9
    """
    If you want to input your sudoku grid in the code instead of in the console, you can do that here.
    Currently it is just a sample placeholder puzzle from Wikipedia.
    """
    spacr=grid = np.array([[5,3,0, 0,7,0, 0,0,0]]) #"spacr" variable is just to keep matrix lined up.
    grid = np.append(grid,[[6,0,0, 1,9,5, 0,0,0]],axis = 0)
    grid = np.append(grid,[[0,9,8, 0,0,0, 0,6,0]],axis = 0)
    #######################---------------------##########
    grid = np.append(grid,[[8,0,0, 0,6,0, 0,0,3]],axis = 0)
    grid = np.append(grid,[[4,0,0, 8,0,3, 0,0,1]],axis = 0)
    grid = np.append(grid,[[7,0,0, 0,2,0, 0,0,6]],axis = 0)
    #######################---------------------##########
    grid = np.append(grid,[[0,6,0, 0,0,0, 2,8,0]],axis = 0)
    grid = np.append(grid,[[0,0,0, 4,1,9, 0,0,5]],axis = 0)
    grid = np.append(grid,[[0,0,0, 0,8,0, 0,7,9]],axis = 0)
    
    print("\nAntioch's Sudoku Solver // 2k19")
    if input("Console input? (y/n): ") == "y": #choose between dataentry modes
        rowtemplate = np.array([[0,0,0, 0,0,0, 0,0,0,]])
        grid =  np.copy(rowtemplate)
        firstrow = input("Enter first row: ") 
        for index in range(size):
            grid[0,index] = int(firstrow[index]) 
        #do 8 subsequent rows and append
        for j in range(1,9): #repeat 8 times
            newrow =  np.copy(rowtemplate)
            rowinput = input("Enter next row:  ") #2 spaces here to make rows line up
            for index in range(size):
                newrow[0,index] = int(rowinput[index])
            grid = np.append(grid,newrow,axis = 0)
    
    print("Starting solve...\n")
    start = time.time() #time how long it takes
    if sudokusolve(grid): #if True, it means all nested versions are true too, which means that its all worked out
        print("Solution found!\n",grid)
    else:
        print("Solving failed.\n")
    print("Time elapsed: ",time.time()-start," seconds") #print time taken

if __name__ == "__main__":
    main()