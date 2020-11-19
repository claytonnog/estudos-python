## funcao do_twice onde f = funcao; e a = argumento;

def do_twice(f, a):
    f(a)
    f(a)

## funcao print_twice onde bruce = argumento;

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print, 'spam')

print(" ")

def do_four(f, a):
    do_twice(f, a)
    do_twice(f, a)

do_four(print, 'spam')