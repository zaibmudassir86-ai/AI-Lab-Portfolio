"""
Lab 5: Hand-readable bottom-up Minimax trace for the padded supplied tree.
"""
leaves = [3, 5, 2, 9, 0, 7, 0, 0]
print("Leaf utilities:", leaves)

max_values = [max(leaves[i], leaves[i + 1]) for i in range(0, 8, 2)]
print("MAX layer:", max_values)

min_values = [min(max_values[i], max_values[i + 1]) for i in range(0, 4, 2)]
print("MIN layer:", min_values)

root = max(min_values)
print("Root MAX value:", root)
print("Chosen root branch: left MIN subtree, value 5")
print("Chosen leaf in left MIN subtree: first MAX child has value 5")
