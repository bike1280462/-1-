#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      n1280462
#
# Created:     28/10/2020
# Copyright:   (c) n1280462 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

me = [list(map(int,input().split()))]
cnt = int(input())
en = [list(map(int,input().split()))for i in range(cnt)]

for i in range(cnt):
    hf = True
    if (me[0][0] > en[i][0] + en[i][2])\
        or (me[0][0] + me[0][2] < en[i][0])\
        or (me[0][1] > en[i][1] + en[i][3])\
        or (me[0][1] + me[0][3] < en[i][1]):
        hf = False
    if hf == True:
        print("敵機",i+1,"が当たり")
