#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import huffman
import freq
import textwrap

with open("./test.txt") as f:
    in_str = f.read()

freq_dict = freq.str_freq(in_str) # Create frequency dictionary.
freqs = list(freq_dict.items()) # HuffmanCode requires (symbol, freq) pairs.

binary_huffman = huffman.HuffmanCode(freqs, 2) # Usual base 2 Huffman coding.
hexadecimal_huffman = huffman.HuffmanCode(freqs, 16) # Or maybe base 16.

ascii_encoding = huffman.ascii_encode(in_str) # 8-bit ascii encoding.
binary_encoding = binary_huffman.encode(in_str)
hexadecimal_encoding = hexadecimal_huffman.encode(in_str)

print("ascii encoding:")
print(textwrap.fill(ascii_encoding))
print()
print("binary encoding:")
print(textwrap.fill(binary_encoding))
print()
print("hex encoding:")
print(textwrap.fill(hexadecimal_encoding))
print()

print("Decoding hex:")
print(hexadecimal_huffman.decode(hexadecimal_encoding))

print("Sizes relative to ascii:")
print("\t ascii:", len(ascii_encoding)/len(ascii_encoding))
print("\tbinary:", len(binary_encoding)/len(ascii_encoding))
print("\t   hex:", len(hexadecimal_encoding)/len(ascii_encoding))
