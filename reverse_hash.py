def reverse_hash(inp):
    """
    This function takes hash integer as an argument and converts it into original string.
    """
    h = 7
    letters = "acdegilmnoprstuw"
    res = ''
    while inp > h:
        pos = inp % 37
        res += letters[pos]
        inp = inp / 37
    return res[::-1]


if __name__ == "__main__":
    inp = input("Enter the hash number:\n")
    print 'Reverse Hash: ', reverse_hash(inp)
