for i in range(1,17+1): 
    if i % 3 == 0 or i % 5 == 0:
        print("Fizz" * (i % 3 == 0) +"buzz" * (i % 5 == 0))
    else:
        print(f'{i}')
