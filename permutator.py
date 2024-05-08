def fatorate(n):
  if n == 0:
    return 1
  else:
    return n * fatorate(n - 1)
  
def permutate(word):
  letters_set = set()
  letters_repetition_dict = {}

  for i in word:
    letters_set.add(i)
    try:
      letters_repetition_dict[f"{i}"] += 1
    except KeyError:
      letters_repetition_dict[f"{i}"] = 0

  number_of_letters = len(letters_set)

  k = 1
  
  for i in letters_repetition_dict.values():
    if i != 0:
      number_of_letters += 1
    k *= fatorate(i+1)
  
  n = fatorate(number_of_letters)
  
  if k != 0:
    permutation_result = int(n/k)
  else: 
    permutation_result = n
  
  return permutation_result

word = input("Digite uma sequência de caracteres alfanuméricos para calcular o número de arranjos possiveis: ")
print(f'\n"{word}" pode ser organizada de {permutate(word)} formas diferentes.\n')