from statistics import mean


class School:

    def __init__(self):

        n = int(input())

        self.age = input().split()
        for i in range(0, len(self.age)):
            self.age[i] = int(self.age[i])

        self.height = input().split()
        for j in range(0, len(self.height)):
            self.height[j] = int(self.height[j])

        self.weight = input().split()
        for k in range(0, len(self.weight)):
            self.weight[k] = int(self.weight[k])

    def average(self):
        print("{:.1f}".format(mean(self.age)))
        print("{:.1f}".format(mean(self.height)))
        print("{:.1f}".format(mean(self.weight)))


A = School()
B = School()

A.average()
B.average()

if mean(A.height) > mean(B.height):
    print('A')
if mean(A.height) < mean(B.height):
    print('B')
if mean(A.height) == mean(B.height):
    if mean(A.weight) < mean(B.weight):
        print('A')
    if mean(A.weight) > mean(B.weight):
        print('B')
    if mean(A.weight) == mean(B.weight):
        print('Same')
