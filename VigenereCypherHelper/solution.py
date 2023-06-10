class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key
        self.key_shifts = []
        print(alphabet)
        for letter in self.key:
            self.key_shifts.append(self.alphabet.find(letter)) #temporal coupling?
    
    def encode(self, text):
        encoded = ""
        for i, letter in enumerate(text):
            letter_alphabet_index = self.alphabet.find(letter)
            if(letter_alphabet_index == -1):
                encoded += letter
                continue
            encoded += self.alphabet[ ( (letter_alphabet_index + self.key_shifts[i % len(self.key)]) % len(self.alphabet) ) ]
        return encoded
    
    def decode(self, text):
        decoded = ""
        for i, letter in enumerate(text):
            letter_alphabet_index = self.alphabet.find(letter)
            if(letter_alphabet_index == -1):
                decoded += letter
                continue
            #print((letter_alphabet_index - self.key_shifts[i % len(self.key)]))
            #More detailed alternative: ( (letter_alphabet_index + len(self.alphabet) - self.key_shifts[i % len(self.key)]) % len(self.alphabet) )
            decoded += self.alphabet[ ( (letter_alphabet_index + len(self.alphabet) - self.key_shifts[i % len(self.key)]) % len(self.alphabet) ) ]
            
        return decoded
        