#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def ap(arr):
    if len(arr)==1:
        return [arr] 
    else:
        a=arr[0] #берем 1 "болт, сотню кротов, два ведра селикона, 2 стопки картона, 12 шестеренок,
                 # 3 крышки от пива и шутку админа, охапку дров - французский танк готов"
        p=ap(arr[1:])
        r=[]  
        for k in p: #цикл для пребора начального числа
            for i in range(len(k)):#цикл для перебора всех позиций 1
                t=k[0:i]+[a]+k[i:] #делаем разрез куда вставляем 1
                r.append(t) #добавляем новую комбинацию в список комбинаций
            r.append(k+[a])    
        return r

if __name__ == '__main__':
    n=int(input("n="))        
    print(ap([i for i in range(1,n+1)]))
    