def row(text):
    
    for x in range(text.count('\n')):
        f = text.find('\n')
        text = text.replace('\n', '')

    for x in range(text.count('ʻ')):
        f = text.find('ʻ')
        text = text.replace('ʻ', "'")

    for x in range(text.count('ʼ')):
        f = text.find('ʼ')
        text = text.replace('ʼ', "'")

    # for x in range(text.count("")):
    #     f = text.find('    ')
    #     text = text.replace('   ', "")

    # for x in range(text.count('<n>')):
    #     f = text.find('<n>')
    #     text = text.replace('<n>', "\n")
    

    return text


def bogin(text1, length):
    result = []
    seg = ''
    a = 0
    b = 0

    text = row(text1)

    for x in text:
        if a >= length:
            if text[b-1] == ' ':
                result.append(seg)
                seg = ''
                a = 0
        seg += x
        a += 1
        b += 1

    if b < 27:
        result.append(text)

    elif seg:
        result.append(seg)
    
    return result


def Con(typePaper, *text):
    length = 24
    if typePaper == "Oq list": length = 40
    l = []
    for x in text:
        c = x.count('<n>')
        if c:
            for i in range(c):
                f = x.find('<n>')
                segment = bogin(x[:f], length)
                l.append(segment)
                x = x[f+3:]
            segment = bogin(x, length)
            l.append(segment)
        else:
            segment = bogin(x, length)
            l.append(segment)
    return l

