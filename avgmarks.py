# -*- coding: utf-8 -*-
"""

"""

kannada,english,hindi,maths,biology=[int(x) for x in input('enter the marks of 5 subjects:').split()]

total_marks_obtained=kannada+english+hindi+maths+biology
average=total_marks_obtained/5
percentage=(total_marks_obtained/525)*100

print(total_marks_obtained,average,percentage)