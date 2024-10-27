insulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

dict1={z:insulin.count(z) for z in ['m','w','l','v']}
print(dict1)

# Creating a new dictionary to count occurrences of specific amino acids
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Print the seqCount dictionary
print(seqCount)