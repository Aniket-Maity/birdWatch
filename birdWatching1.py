# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:46:43 2020

@author: Aniket Maity
"""



def main():
    n = int(input())
    a=list(map(int,input().split()))

    my_dict = {i:a.count(i) for i in a}
    
    
    print(sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))[0][0])

if __name__ == '__main__':
   main()

