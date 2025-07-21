import time

def powers(x,k):
    if k==0:
        return 1
    elif k%2==0:
        onehalf=powers(x,k//2)
        return onehalf*onehalf
    else:
        return x*powers(x,k-1)
    
def repeated_squaring_poly_eval(n,x):
    result=0
    for k in range(n+1):
        power = powers(x,k)
        if k!=0:
            result+=k*power
        else:
            result = 1
    return result

def runtime():
    n,x = 6,3
    start = time.time()
    running = repeated_squaring_poly_eval(n,x)
    end = time.time()
    print(f"Pn({x}) for n = {n} is {running}")
    print(f"Time: {(end - start) * 1000:.3f} ms\n")
    
    n,x = 3000,10
    start = time.time()
    running = repeated_squaring_poly_eval(n,x)
    end = time.time()
    print(f"Pn({x}) for n = {n} is {running}")
    print(f"Time: {(end - start):.3f} seconds\n")
    
if __name__ == '__main__':
    runtime()