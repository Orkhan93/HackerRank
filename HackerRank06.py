def mutate_string(s, p, c):
    word = s[0:p] + c + s[p+1::]
    return word
