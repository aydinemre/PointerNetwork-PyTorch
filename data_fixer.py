with open('data/data_my.csv', 'r') as f:
    lines = f.readlines()

with open('data/my_fixed_data.csv', 'w+') as f:
    temp_lines = []
    max_in_seq_len = -1
    for line in lines:
        temp_lines.append(line.replace('\n', '').lstrip())
        if 'output' in line:
            f.write(' '.join(temp_lines) + '\n')
            in_seq_len = ' '.join(temp_lines).split('output')[0].count(' ')
            if in_seq_len > max_in_seq_len:
                max_in_seq_len = in_seq_len
            temp_lines = []

    print("max_in_seq_len : {}".format(max_in_seq_len))
