from statistics import mean


class School:

    def __init__(self):

        n = int(input())

        self.sen = input().split()
        for i in range(0, len(self.sen)):
            self.sen[i] = int(self.sen[i])

        self.ghad = input().split()
        for j in range(0, len(self.ghad)):
            self.ghad[j] = int(self.ghad[j])

        self.vazn = input().split()
        for k in range(0, len(self.vazn)):
            self.vazn[k] = int(self.vazn[k])

    def miangin_kardan(self):
        print("{:.1f}".format(mean(self.sen)))
        print("{:.1f}".format(mean(self.ghad)))
        print("{:.1f}".format(mean(self.vazn)))


A = School()
B = School()

A.miangin_kardan()
B.miangin_kardan()

if mean(A.ghad) > mean(B.ghad):
    print('A')
if mean(A.ghad) < mean(B.ghad):
    print('B')
if mean(A.ghad) == mean(B.ghad):
    if mean(A.vazn) < mean(B.vazn):
        print('A')
    if mean(A.vazn) > mean(B.vazn):
        print('B')
    if mean(A.vazn) == mean(B.vazn):
        print('Same')
