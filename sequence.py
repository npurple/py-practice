#coding=utf8
import sys
import os
import dis
from common.tools import *

# 自定义切片(命名)
def defineSlice():
    invoice = """
    0.....6................................40........52...55........
    1909  Pimoroni PiBrella                 $17.50      3    $52.50
    1489  6mm Tactile Switch x20             $4.95      2    $9.90
    1510  Panavise Jr. - PV-201i            $28.00      1    $28.00
    1601  PiTFT Mini Kit 320x240            $34.95      1    $34.95
    """
    lines = invoice.split('\n')[2:]

    p(invoice)
    p(lines)

    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)

    for line in lines:
        p(line[UNIT_PRICE], line[DESCRIPTION])

# 切片赋值 
def setValue():
    al = [1,2,3,4,5,6,7,8]

    al [3:] = [88]
    p(al)
    '''
    [1, 2, 3, 88]  
    '''

# 切片运算
def operation():
    al = [1,2,3]
    bl = [11,22,33]
    p(al*3)
    p(al+bl)

# 序列解包(PEP 448+)
def unpack():
    al = *range(5), # ,不能少 
    p('*range(5)        =>', al)
    al = [*range(5)]
    p('[*range(5)]      =>', al)
    al = list(range(5))
    p('list(range(5))   =>', al)

# 多维数组
def multiDimention():
    board = [['_']*3 for i in range(3)]
    p(board)
    for secList in board:
        p(id(secList))
        for x in secList:
            p(id(x))
    board[1][2] = 'New Year'
    p(board)

    # 注意，第二维的每一个数组都指向同一个内存 
    board2 = [['_']*3]*3
    p(board2)
    #p([id(b) for b in board2])
    for secList in board2:
        p(id(secList))
        for x in secList:
            p(id(x))
    board2[1][2] = 'New Year'
    p(board2)

# 修改元组中的可变序列
'''
    不要在元组里加入可变序列
'''
def puzzle():
    t = (1, 2, [30, 40])
    try:
        t[2] += [50, 60]
    except Exception as e:
        p(e)
        p(t)
        '''
            'tuple' object does not support item assignment
            (1, 2, [30, 40, 50, 60])
        '''

if __name__ == '__main__':
    #operation()
    #unpack()
    #multiDimention()
    #dis.dis('a=range(5)')
    puzzle()
