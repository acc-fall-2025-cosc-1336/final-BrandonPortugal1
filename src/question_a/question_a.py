def create_multiplication_table():
    table = []
    for row in range(1, 6):
        current_row = []
        for col in range(1, 11):
            current_row.append(row * col)
        table.append(current_row)
    return table


def display_multiplication_table(table):
    for row in table:
        print(" ".join(str(num) for num in row))
    print()