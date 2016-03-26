from tree import TreeNode
import bisect

def huffman_initial_count(message_count, digits):
    """
    Return the number of messages that must be grouped in the first layer for
    Huffman Code generation.

    See the section "Generalization" in ./notes.md for details.

    :message_count: Positive integral message count.
    :digits: Integer >= 2 representing how many digits are to be used in codes.
    :returns: The number of messages that _must_ be grouped in the first level
              to form a `digit`-ary Huffman tree.

    """

    if message_count <= 0:
        raise ValueError("cannot create Huffman tree with <= 0 messages!")
    if digits <= 1:
        raise ValueError("must have at least two digits for Huffman tree!")

    if message_count == 1:
        return 1

    return 2 + (message_count - 2) % (digits - 1)

def combine_and_replace(nodes, n):
    """
    Combine n nodes from the front of the low-to-high list into one whose key is
    the sum of the merged nodes. The new node's data is set to None, then
    inserted into its proper place in the list.

    Note: The sum of keys made here is the smallest such combination.

    In the contradictory style of Huffman, if any set of nodes were chosen
    except for the first n, then changing a node not in the first n to one that
    is from the first n would reduce the sum of their keys. thus the smallest
    sum is made from the last n nodes.

    :nodes: A list of TreeNodes.
    :n: Integer < len(nodes).
    :returns: High-to-low list that combines the last n nodes into one.

    """
    group = nodes[:n]
    combined = TreeNode(sum(node.key for node in group), None, group)
    nodes = nodes[n:]
    bisect.insort(nodes, combined)

    return nodes

def huffman_nary_tree(probabilities, digits):
    """Return a Huffman tree using the given number of digits.

    This `digits`-ary tree is always possible to create. See ./notes.md.

    :probabilities: List of tuples (symbol, probability) where probability is
                    any floating point and symbol is any object.
    :digits: Integral number of digits to use in the Huffman encoding. Must be
             at least two.
    :returns: TreeNode that is the root of the Huffman tree.

    """
    tree = None

    # TreeNode does rich comparison on key value (probability), so we can
    # pass this right to sorted().
    probabilities = [TreeNode(freq, symbol) for (symbol, freq) in probabilities]
    probabilities = sorted(probabilities)

    if len(probabilities) == 1:
        return Tree(probabilities[0])

    # Grab the required first set of messages.
    initial_count = huffman_initial_count(len(probabilities), digits)
    probabilities = combine_and_replace(probabilities, initial_count)

    # If everything is coded correctly, this loop is guarenteed to terminate
    # due to the initial number of messages merged.
    while len(probabilities) != 1:
        # Have to grab `digits` nodes from now on to meet an optimum code requirement.
        probabilities = combine_and_replace(probabilities, digits)

    if probabilities[0].key != 1:
        print("The probabilities don't sum up to 1...")

    return probabilities.pop()

def huffman_nary_dict(probabilities, digits):
    """Return a dictionary that decodes messages from the nary Huffman tree.

    :probabilities: List of tuples (symbol, probability) where probability is
                    any floating point and symbol is any object.
    :digits: Integral number of digits to use in the Huffman encoding. Must be
             at least two.
    :returns:  A dictionary of {code: message} keys, where "code" is a string
               of digits representing the Huffman encoding for the given
               message.

    """
    def indicies_to_code(path):
        ret = ""
        for index in path:
            if index < 0:
                raise ValueError("Cannot accept negative path indicies (what went wrong?)")
            elif index >= 10:
                raise ValueError("Cannot currently make digits greater than 9")

            ret += str(index)

        return ret

    def visit(node, path, decoding_dict):
        # The goal here is to visit each node, passing the path taken to get there
        # as well. When we reach a leaf, then we now that we're at a message, so
        # we can turn the path into digits (in an arbitrary but consistant way) and
        # add it to the dict.
        # Here, the "path" is the list of indicies for children that we have to
        # access to get to the needed node. In binary, paths would be lists of
        # 0s and 1s.
        # We modify the passed in dictionary, so no returning is needed.
        # See: https://stackoverflow.com/questions/986006.
        if len(node.children) == 0:
            code = indicies_to_code(path)
            decoding_dict[code] = node.data
        else:
            for k, child in enumerate(node.children):
                path.append(k)
                visit(child, path, decoding_dict)
                path.pop()

    root = huffman_nary_tree(probabilities, digits)
    decoding_dict = dict()
    visit(root, [], decoding_dict)

    return decoding_dict

def p(l):
    print([(n.data, n.key) for n in l])

if __name__ == "__main__":
    # Do the thing.
    from freq import file_freq
    freqs = file_freq("test.txt")

    probabilities = list(freqs.items())
    test = [TreeNode(freq, sym) for (sym, freq) in probabilities]
    print(probabilities)
    root = huffman_nary_tree(probabilities, 2)
    decoding_dict = huffman_nary_dict(probabilities, 2)
