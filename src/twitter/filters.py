
def combine_filter(word):
    return [word, word.lower(), word.title(), word.upper()]


filters = []

with open('filters', 'r') as f:
    for line in f.readlines():
        filters.extend(combine_filter(line[:-1]))
