import re
def is_valid_IP(strng):
    print(strng)
    #return not any([ (int(i) <= 0 or int(i) >= 255 or i.startswith('0')) if i.isnumeric() else False for i in strng.split(".")]) # incomplete oneliner, following alternative approach with regex
    return re.search('^(?!\s)(((1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9]?[0-9])\.){3}(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9]?[0-9]))(?!\s)$', strng) != None