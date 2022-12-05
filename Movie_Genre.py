n = int(input())
# n is the number of people who participated in the survey.

list_movie = []

for i in range(n):
    list_movie.extend((input().split()).lower())

# Sample input >>> Action Horror Comedy ... ... ...
# possible genres to choose are : Action , Comdey , History , Horror , Romance , Adventure

print('Action', ':', list_movie.count('action'))
print('Comedy', ':', list_movie.count('comedy'))
print('History', ':', list_movie.count('history'))
print('Horror', ':', list_movie.count('horror'))
print('Romance', list_movie.count('romance'))
print('Adventure', ':', list_movie.count('adventure'))
