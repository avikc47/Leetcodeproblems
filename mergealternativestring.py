def mergeAlternately(word1: str, word2: str) -> str:
    minstr = ''
    maxstr = ''
    merged_string = []
    if len(word1) < len(word2):
        minstr = word1
    else:
        minstr = word2
    for i in range(len(minstr)):
        merged_string += [word1[i], word2[i]]
    if len(word1) > len(minstr):
        merged_string += list(word1[len(minstr):])
    else:
        merged_string += list(word2[len(minstr):])
    return ''.join(merged_string)

print(mergeAlternately('abc', 'pqrs'))
