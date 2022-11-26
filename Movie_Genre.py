n = int(input())

list_movie = []
for i in range(n):
    list_movie.extend(input().split())

print('Action', ':', list_movie.count('Action'))
print('Comedy', ':', list_movie.count('Comedy'))
print('History', ':', list_movie.count('History'))
print('Horror', ':', list_movie.count('Horror'))
print('Romance', list_movie.count('Romance'))
print('Adventure', ':', list_movie.count('Adventure'))
