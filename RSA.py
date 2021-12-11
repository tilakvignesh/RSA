'''This Solution Does use Brute force to find the keys, so it probably will be slow for larger numbers'''
def isprime(num):
    flag = 1
    i = 2
    while i<=(num/2):
        if(num%i==0):
            flag = 0
            break
        i = i+1
    return flag



def gcd(num1,num2):
    if(num2==0):
        return num1
    else:
        return gcd(num2,num1%num2)




def public_key(phi):
    e = 2
    x = []
    while e<phi:
        if(gcd(e,phi)==1):
            x.append(e)
            #break
        e = e+1
    return x

def private_key(phi,e):
    '''e*d = 1 mod phi
    which can basically be written as
    e*d =1 + k*phi
    our goal would be to find the smallest k'''
    private = []
    for pub in e:
        k = 1
        while True:
            d = ((1 + k*phi)/pub)
            if(d == int(d)):
                private.append(int(d))
                break
            else:
                k = k+1
    
    return private


        






if __name__ == '__main__':
    print("This program takes  primes p&q and gives u the private and public keys used in RSA")
    p = int(input('Enter A prime: '))
    q = int(input('Enter A prime: '))
    if(isprime(p) and isprime(q) and p!=1 and q!=1):
        n = p*q
        print('We Get n to be: ',n)
        phi = (p-1)*(q-1)
        print('We get phi(n) to be: ',phi)
        e = public_key(phi)
        d = private_key(phi,e)

        print('\n')
        print('For each p and q we an have multiple private and public keys. \n')

        print('We get the public keys(e) to be\n',e)
        print('\n We get the corresponding private keys(d) to be\n',d)
        print('\nNOTE1: THESE ARE NOT THE COMPLETE KEYS, THE PUBLIC KEY IS MADE AS A PAIR OF BOTH e and n(e,n) AND THE PRIVATE KEYS ARE MADE AS A d and n(d,n)\n')
        
        
    else:
        print('numbers are not prime')
        exit()
       