default_alphabet = "abcdefghijklmnopqrstuvwxyz";

def make_key(initial_key, alphabet):
    result_key = []
    for char in initial_key:
        if char not in result_key:
            result_key.append(char)
            
    for char in alphabet:
        if char not in result_key:
            result_key.append(char)
            
    '''result_dict = {}
    
    for index, item in enumerate(result_key):
        result_dict[item] = index + 1'''
    
    print(result_key)
    
    return result_key #"".join(result_key)

def encode(message, key, initShift):
    #print(len(make_key(key, default_alphabet)))
    full_key = make_key(key, default_alphabet)
    full_key_length = len(full_key)
    
    result_message = []
    
    for letter in message:
        current_encripted_letter = letter
        
        if letter in full_key:
            letter_index = full_key.index(letter)
            current_encripted_letter = full_key[(letter_index + initShift) % full_key_length]
            #print((letter_index + initShift) % full_key_length)
            #print(full_key[(letter_index + initShift) % full_key_length])
            initShift = letter_index + 1
               
        result_message.append(current_encripted_letter)
        
    return "".join(result_message)
    
def decode(message, key, initShift):
    #COULD ALSO BE DONE BY USING THE ENCODING
    
    full_key = make_key(key, default_alphabet)
    full_key_length = len(full_key)
    
    #print(full_key)
    
    result_message = []
    
    for letter in message:
        current_decripted_letter = letter
        
        if letter in full_key:
            letter_index = full_key.index(letter)
            current_decripted_letter = full_key[(letter_index - initShift) % full_key_length]
            #print(letter_index, initShift)
            #print((letter_index - initShift) % full_key_length)
            #print(full_key[(letter_index - initShift) % full_key_length])
            #print(initShift)
            initShift = ((letter_index - initShift) % full_key_length) + 1
               
        result_message.append(current_decripted_letter)
        
    return "".join(result_message)