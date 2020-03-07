'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_helper(word, count):
    index = word.find('th')

    # print(index)

    if index == -1:
        return count

    # print(index)

    word = word[0:index] + word[index+3::]
    # print( word)
    count = count + 1

    return count_helper(word, count)


def count_th(word):

    return count_helper(word, 0)

    # string1 = word
    # string2 = 'th'

    # length_string_uno = len(string1)
    # length_string_dos = len(string2)

    # base case
    # if (length_string_uno == 0 or length_string_uno < length_string_dos):
        # print('S')

    # recursive case
    # checking if the first substring matches
    # if (string1[0:length_string_dos] == length_string_dos):
        # return count_th(string1[length_string_dos-1:]+1)

    # otherwise , return the count from the remaining index
    # return count_th(string1[length_string_dos-1:])


if __name__ == '__main__':

    print(count_th('the'))
