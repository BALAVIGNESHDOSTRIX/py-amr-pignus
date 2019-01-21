import os 

def yrDateExtractor(file_name):
    x = list(file_name)
    yrdate = x[:x.index('_'):]
    sx = ''
    for yrs in yrdate:
        sx = sx + yrs
    return str(sx)

def timeSecExtractor(file_name):
    x = list(file_name)
    timex = x[x.index('_') + 1:x.index('-'):]
    cx = ''
    for tim in timex:
        cx = cx + tim 
    return str(cx)

def personNameExtractor(file_name):
    x = list(file_name)
    name = x[x.index('-') + 1:x.index('.'):]
    dx = ''
    for nam in name:
        dx = dx + nam
    return str(dx)

def fileNeedName(file_name):
    x = list(file_name)
    need = x[:x.index('.'):]
    bx = ''
    for neex in need:
        bx = bx + neex
    return str(bx)   




    