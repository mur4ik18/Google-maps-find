import time
import datetime

def colWidth(sheet, col, size):
    sheet.column_dimensions[col].width = int(size)

def writeExc(sheet,ster,num,inp):
    sheet[ster+str(num)]= inp

def sl(x):
    time.sleep(x)

def error(f, log, num, err):
    f.write('==============================================================')
    f.write('\n')
    f.write(str(datetime.datetime.now())+ '  \|/  ' + log)
    f.write('\n')
    f.write(num)
    f.write('\n')
    f.write(err)
    f.write('\n')



def speed(internet):
    if internet == 'good':
        return 50
    elif internet == 'normal':
        return 30
    else :
        return 15