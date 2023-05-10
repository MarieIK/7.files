import os

my_file = []

for i in range(1, 4):
    file_name = f'{i}.txt'
    current = os.getcwd()
    folder = 'files'
    result_path = os.path.join(current, folder, file_name)

    with open(result_path, encoding='utf-8') as file:
        my_file.append([file_name, file.readlines()])

my_file = sorted(my_file, key=lambda x: len(x[1]))

with open('result.txt', 'wt', encoding='utf-8') as file:
    for name, lines in my_file:
        file.write(f'{name}\n')
        file.write(f'{len(lines)}\n')
        for line in lines:
            file.write(f'{line}')
        file.write('\n')
