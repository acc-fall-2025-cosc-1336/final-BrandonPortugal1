from question_c import get_most_likely_ancestor_consensus

while True:
    dna_string1 = input("Enter a DNA string (9–16 characters): ").upper()
    dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").upper()

    if not (9 <= len(dna_string1) <= 16):
        continue

    if len(dna_string2) != 4:
        continue

    result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

    if result:
        print(*result)
    else:
        print("No occurrences found")

    if input("Continue? (y/n): ").lower() != "y":
        break