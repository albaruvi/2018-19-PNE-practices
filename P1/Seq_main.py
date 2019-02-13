from P1.Seq import Seq

# Information about sequence 1
s1 = Seq(input('Please introduce the first sequence'))
str1 = s1.strbases
print('Sequence 1: {}'.format(str1))

l1 = s1.len()
print('Length: {}'.format(l1))

n_bases1 = s1.count_base()
print('Number of bases: {}'.format(n_bases1))

p_bases1 = s1.perc_bases()
print('Percentage of bases: {}'.format(p_bases1))

# Information about sequence 2
s2 = Seq(input('\nPlease introduce the second sequence'))
str2 = s2.strbases
print('Sequence 2: {}'.format(str2))

l2 = s2.len()
print('Length: {}'.format(l2))

n_bases2 = s2.count_base()
print('Number of bases: {}'.format(n_bases2))

p_bases2 = s2.perc_bases()
print('Percentage of bases: {}'.format(p_bases2))

# Information about sequence 3
s3_str = s1.complement()
print('\nSequence 3: {}'.format(s3_str))
s3 = Seq(s3_str)

l3 = s3.len()
print('Length: {}'.format(l3))

n_bases3 = s3.count_base()
print('Number of bases: {}'.format(n_bases3))

p_bases3 = s3.perc_bases()
print('Percentage of bases: {}'.format(p_bases3))

# Information about sequence 4
s4 = Seq(s3_str)
s4_reverse = s4.reverse()
print('\nSequence 4: {}'.format(s4_reverse))

l4 = s4.len()
print('Length: {}'.format(l4))

n_bases4 = s4.count_base()
print('Number of bases: {}'.format(n_bases4))

p_bases4 = s4.perc_bases()
print('Percentage of bases: {}'.format(p_bases4))
