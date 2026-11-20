with open('about_me.txt', 'r') as file:
    #content = file.read(50)

    #print(content)
    #print(file.readline(10))
    #print(file.readline())

    #for i in range(1, 5):
    #    print(file.readline())

    #print(file.readlines(-1))

    print(file.read(50))
    capture = file.readline()

# 12) both print's only print's a part of the whole text file, only 50 character.
# 14-A) I get a list of all the lines that i have in the text file.
# 14-B) A list of only one line (one item).
# 14-C) same as 14-B
# 14-D) both .readlines(1) and .readlines(10) give the first line as a list.
# 14-E) .readlines(100) return the first four lines as a list
#       .readlines(-1) return all lines as a list.

