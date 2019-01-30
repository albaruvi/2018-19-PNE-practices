filename = input('Introduce the name of the file')
with open(filename, 'r') as f:
    sequence = ''
    for line in f:
        line = line.strip('\n')
        line = line.strip('')
        sequence += line
    length = len(sequence)
    sequence = sequence.lower()
    print('The total length is {}'.format(length))
    a = sequence.count('a')
    c = sequence.count('c')
    g = sequence.count('g')
    t = sequence.count('t')
    print('A:', a)
    print('C:', c)
    print('G:', g)
    print('T:', t)
