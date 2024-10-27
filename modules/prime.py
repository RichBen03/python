with open ('prime.txt', 'w') as file:
        
        for x in range(2,251):
            prime=True
            for i in range(2,x):
                if x%i==0:
                    prime=False
                    break
            if prime:
                output=print(f'{x}')
                file.write(f'{x} is a prime number\n')