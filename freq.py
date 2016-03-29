def str_freq(s):
    """Calculate the relative frequency of every character in the given string.

    The return format is mostly for easy feeding into the Huffman tree creator.

    :s: String.
    :returns: Dictionary of {character: frequency} pairs.

    """

    freqs = dict()

    for c in s:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1

    # Turn the absolute frequencies into relative ones.
    slen = len(s)
    for c in freqs.keys():
        freqs[c] /= slen

    return freqs

def file_freq(name):
    with open(name) as f:
        return str_freq(f.read())
