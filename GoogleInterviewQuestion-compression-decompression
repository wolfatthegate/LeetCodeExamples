# https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!

def decompress(stri): 
    stack = [] #use stack => last in first out
    s = ""
    
    #we will scan through all the characters in the given string
    for c in stri: 
        if c == ']':
            stack.pop()
            temp = ''
            multiplier = int(stack.pop())
            while multiplier > 0: 
                temp += s
                multiplier -= 1
            s = temp 
            
        else: # if number or '['
            if c.isdigit() or c == '[': 
                stack.append(c)
            else: 
                s += c 
    return s   
    
print(decompress('2[3[abc]d]c'))
