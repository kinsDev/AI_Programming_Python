"""
x = int(input("Enter a number: "))
x += 20
print(x)
"""


"""
camelot_lines  = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())
print(camelot_lines)
"""
import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)
