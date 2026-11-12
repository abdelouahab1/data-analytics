films = ['The Shawshank Redemption (1994)', 'The Godfather (1972)', 'The Dark Knight (2008)', 'The Godfather Part II (1974)', 'The Lord of the Rings: The Return of the King (2003)']

length = len(films)
print(f'The list [films] includes my top {length} favorite movies')
print(films)

print(sorted(films))
# I noticed that the sorted function sorted the films titeles alphabiticly.

films.sort()
print(films)
# I get the same result using the .sort and sorted().

films.append('12 Angry Men (1957)')
print(films)