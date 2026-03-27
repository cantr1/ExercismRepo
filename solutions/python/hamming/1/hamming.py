def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming = 0

    for i, char in enumerate(strand_a):
        if char != strand_b[i]:
            hamming += 1

    return hamming
