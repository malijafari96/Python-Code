from statistics import mean


class School:

    def __init__(self):

        n = int(input())

        self.age = input().split()
        self.age = [int(age) for age in self.age]

        self.height = input().split()
        self.height = [int(height) for height in self.height]

        self.weight = input().split()
        self.weight = [int(weight) for weight in self.weight]

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
