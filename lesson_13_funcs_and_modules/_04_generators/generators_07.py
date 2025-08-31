def read_file_gen(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


if __name__ == '__main__':
    for line in read_file_gen(r'students\students.txt'):
        print(line)
