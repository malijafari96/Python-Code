n = int(input())
# n is the number of people who participated in the survey.

list_movie = []

for i in range(n):
    list_movie.extend(input().split())

# Sample input >>> Action Horror Comedy ... ... ...
# The number of selected genres does not matter, but the first letter of input words must be capitalized
# possible genres to choose are : Action , Comdey , History , Horror , Romance , Adventure

print('Action', ':', list_movie.count('Action'))
print('Comedy', ':', list_movie.count('Comedy'))
print('History', ':', list_movie.count('History'))
print('Horror', ':', list_movie.count('Horror'))
print('Romance', list_movie.count('Romance'))
print('Adventure', ':', list_movie.count('Adventure'))
