from tkinter import *
root = Tk()

# console part of calculator ......

console = Entry(root, width = 35 , borderwidth = 5)
console.grid(row = 0, column = 0, columnspan = 3, padx = 30)

list_of_numbers = []
last = ''

#funtion to get numbers
def number_input(number):
    cur = console.get()
    console.delete(0,END)
    console.insert(0,str(cur) + str(number))

#function to clear the console
def clear():
    console.delete(0,END)
    while len(list_of_numbers) > 0:
        list_of_numbers.pop()


#Arithmetic functions
def sign_add():
    num = console.get()
    if len(list_of_numbers) == 0:
        list_of_numbers.insert(0,num + '+')
    else:
        s = list_of_numbers.pop()
        list_of_numbers.append(s + num + '+')
    console.delete(0,END)

def sign_sub():
    num = console.get()
    if len(list_of_numbers) == 0:
        list_of_numbers.insert(0,num + '-')
    else:
        s = list_of_numbers.pop()
        list_of_numbers.append(s + num + '-')
    console.delete(0,END)

def sign_mul():
    num = console.get()
    if len(list_of_numbers) == 0:
        list_of_numbers.insert(0,num + '*')
    else:
        s = list_of_numbers.pop()
        list_of_numbers.append(s + num + '*')
    console.delete(0,END)

def sign_div():
    num = console.get()
    if len(list_of_numbers) == 0:
        list_of_numbers.insert(0, num + '/')
    else:
        s = list_of_numbers.pop()
        list_of_numbers.append(s + num + '/')
    console.delete(0,END)


#funtion to display
def equal():
    num = console.get()
    list_of_numbers[0] = list_of_numbers[0] + num
    def helper(a, b, sign):
        if sign == '+':
            return str(int(a) + int(b))
        elif sign == '-':
            return str(int(a) - int(b))
        elif sign == '*':
            return str(int(a) * int(b))
        else:
            return str(int(int(a) / int(b)))

    def calc(s):
        stack = []
        last = ''
        num = ''
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            else:
                if last == '':
                    stack.append(num)
                    last = s[i]
                    num = ''
                else:
                    cur = stack.pop()
                    val = helper(cur, num, last)
                    stack.append(val)
                    last = s[i]
                    num = ''
        if last == '':
            stack.append(num)
        else:
            cur = stack.pop()
            val = helper(cur, num, last)
            stack.append(val)
        return stack[0]
    ans = calc(list_of_numbers.pop())
    console.delete(0,END)
    console.insert(0,ans)
    while len(list_of_numbers) > 0:
        list_of_numbers.pop()

# Buttons 0-9,add,subtract,multiply,divide,equals,clear ......

butn7 = Button(root, text = '7', padx = 40 , pady = 20, command = lambda : number_input(7)).grid(row = 1 , column = 0)
butn8 = Button(root, text = '8', padx = 40 , pady = 20, command = lambda : number_input(8)).grid(row = 1 , column = 1)
butn9 = Button(root, text = '9', padx = 40 , pady = 20, command = lambda : number_input(9)).grid(row = 1 , column = 2)
butn4 = Button(root, text = '4', padx = 40 , pady = 20, command = lambda : number_input(4)).grid(row = 2 , column = 0)
butn5 = Button(root, text = '5', padx = 40 , pady = 20, command = lambda : number_input(5)).grid(row = 2 , column = 1)
butn6 = Button(root, text = '6', padx = 40 , pady = 20, command = lambda : number_input(6)).grid(row = 2 , column = 2)
butn1 = Button(root, text = '1', padx = 40 , pady = 20, command = lambda : number_input(1)).grid(row = 3 , column = 0)
butn2 = Button(root, text = '2', padx = 40 , pady = 20, command = lambda : number_input(2)).grid(row = 3 , column = 1)
butn3 = Button(root, text = '3', padx = 40 , pady = 20, command = lambda : number_input(3)).grid(row = 3 , column = 2)
butn0 = Button(root, text = '0', padx = 40 , pady = 20, command = lambda : number_input(0)).grid(row = 4 , column = 0)
butn_add = Button(root, text = '+', padx = 40 , pady = 20, command = sign_add).grid(row = 4 , column = 1)
butn_sub = Button(root, text = '-', padx = 40 , pady = 20, command = sign_sub).grid(row = 4 , column = 2)
butn_div = Button(root, text = '/', padx = 40 , pady = 20, command = sign_div).grid(row = 5 , column = 0)
butn_mul = Button(root, text = '*', padx = 40 , pady = 20, command = sign_mul).grid(row = 5 , column = 1)
butn_equal = Button(root, text = '=', padx = 40 , pady = 20, command = equal).grid(row = 5 , column = 2)
butn_clr = Button(root, text = 'clr', padx = 40 , pady = 20, command = clear).grid(row = 6 , column = 0)

root.mainloop()

## end .....
