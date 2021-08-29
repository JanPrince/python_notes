## Cipher

import string
def rot13(message):
    """

    :param message:  a string
    :returns a string with each letter replaced with a letter 13 letters after it in the alphabets
    Known as ROT13 - an example of Caesar cipher
    """
    empty = []
    alpha = string.ascii_lowercase
    beta = string.ascii_uppercase
    mess_list = list(message)
    copy = mess_list[:]

    for k in copy:
        if k in alpha:
            ind_alpha = alpha.index(k)
            cipher_index = ind_alpha + 13
            if cipher_index > len(alpha):
                cipher_index = cipher_index - len(alpha)
            cipher_letter = alpha[cipher_index]
            empty.append(cipher_letter)
        elif k in beta:
            ind_beta = beta.index(k)
            cipher_index = ind_beta + 13
            if cipher_index > len(beta):
                cipher_index = cipher_index - len(beta)
            cipher_letter = beta[cipher_index]
            print(cipher_letter)
            empty.append(cipher_letter)

    Encoded = "".join(empty)
    print(Encoded)



rot13("test")

