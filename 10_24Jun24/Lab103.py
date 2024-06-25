letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}
# Filter the vowels
# a,e,i,o,u

def filter_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

# result = filter_vowel('a')
# print(result)


filtered_words = filter(filter_vowel, letters_list)
print(list(filtered_words))


