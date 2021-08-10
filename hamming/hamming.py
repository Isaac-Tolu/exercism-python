def distance(strand_a, strand_b):
    
    if len(strand_a) != len(strand_b):
        raise ValueError('The two strands must have the same length')

    dist = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]: dist += 1

    return dist
