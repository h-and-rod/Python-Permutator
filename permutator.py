def fatorate(n):
  if n == 0:
    return 1
  else:
    return n * fatorate(n - 1)
  
def simple_permutation(word):
  letters_set = set()
  for i in word:
    letters_set.add(i)
  number_of_letters = len(letters_set)
  n = fatorate(number_of_letters)
  return n

def subs_permutation:
  


word = input("Digite uma palavra que nao contenha caracteres repetidos: ")
print(f'\nA palavra "{word}" pode ser permutada em {simple_permutation(word)} possibilidades.\n')














# permutation_counter = fatorate(len(permutation(word)))

# print(permutation(word))