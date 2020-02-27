# -*- coding: utf-8 -*-


marks=int(input('enter the student marks:'))

if marks>70:
    print('distinction')
elif marks>60 and marks<70:
    print('first class')
elif marks>50 and marks<60:
    print('second class')
elif marks>40 and marks<50:
    print('third class')
else:
    print('fail')