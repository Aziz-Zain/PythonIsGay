# -*- coding: utf-8 -*-
from engi1020.arduino import *
from time import sleep

def Probability (orderedList):
    A = {'f': 0.769,
         'c': 0.958,
         'v': 0.575,
         'd'}
    
    B = ['v', 'd', 'c', 'f']
    C = ['d', 'v', 'c', 'f']
    
    if orderedList == A:
        p = 0.769*0.958*0.575*1
        print(f'The probability of you having covid is {p}')
        sleep(10)
        print('Please visit the closest doctor')
        
    elif orderedList == B:


def checkdigitalInputs (pin1, pin2):
    val = 0
    if digital_read(pin1) == 1 and digital_read(pin2) == 0:
        val = pin1
    elif digital_read(pin1) == 0 and digital_read(pin2) == 1:
        val = pin2
    
    return val

Answer = ['No', 'Yes']
Questions = [f, c, v, d]
Answers = []
Order = [1, 2, 3, 4]

for q in Questions:
    lcd_print(q)
    while True:
        if checkdigitalInputs(pin1, pin2) == pin1:
            Answers.append(Answer[0])
            break
        elif checkdigitalInputs(pin1, pin2) == pin2:
            Answers.append(Answer[1])
            break
 
Total = {
    'f' : Answers[0],
    'c' : Answers[1],
    'v' : Answers[2],
    'd' : Answers[3],
    }

for i in Total:
    if Total[i] == 'No':
        Total.pop(i)
       
Order = dict.fromkeys(Total.keys())
L = list(Order)
Number = {1: '1st',
          2: '2nd',
          3: '3rd',
          4: '4th'}

#Order of the symptoms
for n in range(1, len(Total) + 1):
    for i in L:
        if Order[i] == None:
            lcd_print(f' is {i} your {Number[n]} symptom ')
            while True:
                if checkdigitalInputs(pin1, pin2) == pin1:
                    break
                elif checkdigitalInputs(pin1, pin2) == pin2:
                    Order.update({i : n})
                    break
        if Order[i] == n:
            break
        
        
sorted_values = sorted(Order.values())
sorted_Order = {}

for i in sorted_values:
    for k in L:
        if Order[k] == i:
            sorted_Order[k] = Order[k]
            break

Final_Order = list(dict.fromkeys(sorted_Order()))               
                
                
                
                
                
                