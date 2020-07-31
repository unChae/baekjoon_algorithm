import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

#chain
print(list(itertools.chain(letters, booleans, decimals)))

#product
print(list(itertools.product('ABCD', repeat=2)))

#permutations
print(list(itertools.permutations('ABCD', 2)))

#combinations
print(list(itertools.combinations('ABCD', 2)))

#combinations_with_replacement
print(list(itertools.combinations_with_replacement('ABCD', 2)))