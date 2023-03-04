import csv

data = [
    ['ID', 'X', 'Y'],
    [1, 2, 3],
    [4, 2, 1],
    [0, 9, 3]
]

with open('data_write_test.csv', 'w', newline='') as new_file:
    fieldnames = ['ID', 'X', 'Y']
    #csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
    csv_writer = csv.writer(new_file, delimiter=',')
    #csv_writer.writeheader()

    for line in data:
        csv_writer.writerow(line)
