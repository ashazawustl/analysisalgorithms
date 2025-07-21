import time
longterm = 2**63-1

def simulate_overflow(val):
    if val>longterm:
        print(f"value exceeds 64-bit signed integer: {val}")
        return -1
    elif val< -longterm-1:
        print(f"value is below signed 64-bit minimum: {val}")
        return -1
    else:
        print("handled this large integer without overflow.")
        return val

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
    return simulate_overflow(result)

def runtime():
    n,x = 5,2
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
    
    n, x = 2000,12
    print("Overflow Test")
    try:
        result = repeated_squaring_poly_eval(n, x)
        if result < 0:
            print(f"overflow observed! Pn({x}) for n= {n} is {result}")
        else:
            print(f"Pn({x}) for n= {n} is {result} (No overflow occurred)")
    except Exception as e:
        print(f"Error during overflow simulation: {e}")
    
if __name__ == '__main__':
    runtime()