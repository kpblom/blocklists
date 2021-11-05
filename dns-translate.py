import idna

with open('output', 'w') as o:
    same = ''
    with open('input', "r") as f:
        for line in f:
            newline = line.strip('\n')
            encoded = idna.encode(newline).decode('utf-8')
            if  newline == encoded:
                same += '*.'+newline+'*\n'
                print('Input: '+newline+' and output: '+encoded+' same')
            else:
                o.write('# '+line)
                o.write('*.'+encoded + '*\n')
    o.write(same)