def count_bases(seq):

    counter_as = 0
    counter_ts = 0
    counter_gs = 0
    counter_cs = 0
    for b in seq:
        if b == 'A':
            counter_as += 1
        if b == 'T':
            counter_ts += 1
        if b == 'G':
            counter_gs += 1
        if b == 'C':
            counter_cs += 1
    dic = {'As': counter_as, 'Ts': counter_ts, 'Gs': counter_gs, 'Cs': counter_cs}
    # Return the dictionary
    return dic


# Main program
s1 = input('Please enter the first sequence:')
s2 = input('Please enter the second sequence')
sequences = [s1, s2]
for s in sequences:

    print('\nSequence', sequences.index(s)+1, 'information:')
    na = count_bases(s)['As']
    nt = count_bases(s)['Ts']
    ng = count_bases(s)['Gs']
    nc = count_bases(s)['Cs']

    # Calculate the total sequence length
    tl = len(s)
    print('The total length of the sequence is: {}'.format(tl))

    # Calculate the number of bases and percentage
    if tl > 0:
        perc_a = round(100.0 * na/tl, 1)
        perc_t = round(100.0 * nt / tl, 1)
        perc_g = round(100.0 * ng / tl, 1)
        perc_c = round(100.0 * nc / tl, 1)
    else:
        perc_a = 0
        perc_t = 0
        perc_g = 0
        perc_c = 0

    # Base A
    print('The number of As is: {}'.format(na))
    print('The percentage of As is {} %'.format(perc_a))

    # Base T
    print('The number of Ts is: {}'.format(nt))
    print('The percentage of Ts is {} %'.format(perc_t))

    # Base G
    print('The number of Gs is: {}'.format(ng))
    print('The percentage of Gs is {} %'.format(perc_g))

    # Base C
    print('The number of Cs is: {}'.format(nc))
    print('The percentage of Cs is {} %'.format(perc_c))
