import itertools

file = open("cardscore.txt", "w")
colors = ["Red", "Blue", "Green", "Yellow", "Orange"]
permuations = list(itertools.permutations(colors))
print(len(list(permuations)))

for perm in permuations:
    file.write(
        f"\n{perm[0]}:10 per container\n{perm[1]}: 5 or 10 per container\n{perm[2]}:6 per container\n{perm[3]}:4 per container\n{perm[4]}: 2 per container\n"
    )

file.close()
