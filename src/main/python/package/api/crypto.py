class Cryptographie:
    def __init__(self):
        self.alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t",
                      "u", "v", "w", "x", "y", "z",
                      " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                      "S",
                      "T", "U", "V", "W", "X", "Y",
                      "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "é", "ê", "ô", "?", "î", "û", "â",
                      "(","'",
                      "-", "è", "_", "ç", "à", ")",
                      "=", "^", "$", "ù", "*", ",","€", ";", ":", "!", "<", ">", "~", "#", "{", "[", "|"]
        self.num = ["a", 2, "&", "z", "t", "}", 4, "f", 6, "/", "g", ";", "£", ":", 5, "#", 2, "ç", "g", "_", 5, "è", 5,
                    "-", 8, "<", "€", "w", 3, "¤", "$",
                    "c", 8, "b", 5, "k", 6, "h", 2, "t", "a", 2, "&", "z", "t", "}", 4, "f", 6, "/", "g", ";", "£", ":",
                    5, "#", 2, "ç", "g", "_", 5, "è", 5,
                    "-", 8, "<", "€", "w", 3, "¤", "$", "c", 8, "b", 5, "k", 6, "h", 2, "t", "a", 2, "&", "z", "t", "}",
                    4, "f", 6, "/", "g", ";", "£", ":",
                    5, "#", 2, "ç", "g", "_", 5, "è", 5, "-", 8, "<", "€", "w", 3, "¤", "$", "c", 8, "b", 5, "k", 6,
                    "h",
                    2, "t"]

class Crypter(Cryptographie):

    def __init__(self, chaine, key):
        super().__init__()
        self.chaine = chaine
        self.key = key

    def crypter(self):
        crypted = ""
        cryptedTab = []
        longAlpha = len(self.alpha)
        for i in self.chaine:
            for j in self.alpha:
                if i == j:
                    index_in_alpha = self.alpha.index(j)
                    if (self.key + index_in_alpha) > longAlpha:
                        cryptedTab += self.alpha[index_in_alpha - self.key]
                    elif (self.key + index_in_alpha) < longAlpha:
                        cryptedTab += self.alpha[index_in_alpha + self.key]
                        cryptedTab += str(self.num[index_in_alpha])
                        cryptedTab += str(self.num[index_in_alpha + 1])
                    crypted = "".join(cryptedTab)
        return crypted

    def decryptage(self):
        pass


class Decrypter(Cryptographie):

    def __init__(self, crypt_chaine, key):
        super().__init__()
        self.crypt_chaine = crypt_chaine
        self.key = key
        self.decrypted = ""

    def decryptage(self):
        chaineSlice = self.crypt_chaine[::3]
        decryptedTab = []
        for i in chaineSlice:
            for j in self.alpha:
                if i == j:
                    index_in_alpha = self.alpha.index(j)
                    if (index_in_alpha + self.key) > 0:
                        decryptedTab += self.alpha[index_in_alpha - self.key]
                    elif (index_in_alpha - self.key) < 0:
                        decryptedTab += self.alpha[index_in_alpha - self.key]
                    self.decrypted = "".join(decryptedTab)
        return self.decrypted


if __name__ == '__main__':
    print(Crypter("salute", 3).crypter())
    print(Decrypter("vg_da2o;£x5èw_5ht}", 3).decryptage())


