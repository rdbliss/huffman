# Huffman Codes

This repository is holds a simple implementation of n-ary [Huffman
coding](https://en.wikipedia.org/wiki/Huffman_coding) in Python.

Huffman coding is a method of encoding messages with variable length,
prefix-free codes that minimizes the average message length. That means that
usually messages sent with Huffman codes are, on average, shorter and fairly
easy to decode. More details can be found in Huffman's original paper, kept
[here](./huffman.pdf).

Without doing much research, binary Huffman codes seem to be familiar to people
in the know, but n-ary Huffman codes seem to be rarer.
[Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding#n-ary_Huffman_coding)
even says that "for n greater than 2, not all sets of source words can
properly form an n-ary tree for Huffman coding" (2016-03-27). Where this is
coming from is a bit of a mystery, because Huffman clearly gives a way to
construct n-ary codes. For more about this, see "Generalization" in
[notes.md](./nodes.md).
