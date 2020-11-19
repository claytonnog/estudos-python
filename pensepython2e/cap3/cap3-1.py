

def right_justify(s):
    extra = 70 - len(s)
    justified = (extra * ' ' + s)
    print(justified)


right_justify('monty')

