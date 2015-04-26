def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)




for i in range(11):
    print(fibonacci(i), end=' ')
print()

print('''
_____________________________________________________________
''')

fib = {0:0, 1:1}
continuar = 's'


while continuar == 's':
    def dict_fib(n):
        if n in fib:
            return fib[n]
        else:
            res = fibonacci(n-1)+fibonacci(n-2)
            fib[n] = res
            return res
    
    
    
    print(dict_fib(int(input('Qual termo: '))))
    print(fib)
    continuar = input('Continuar?(s/n): ')