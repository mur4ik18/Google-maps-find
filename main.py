import time


def colWidth(sheet, col, size):
    sheet.column_dimensions[col].width = int(size)

def writeExc(sheet,ster,num,inp):
    sheet[ster+str(num)]= inp

def sl(x):
    time.sleep(x)
