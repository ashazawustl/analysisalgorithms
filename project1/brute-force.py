import time

def brute_force_poly_eval(n,x):
    result = 0
    for a in range(n+1):
        exp = 1
        for b in range(a):
            exp*= x
        if a!=0:
             result +=x*exp
        else:
            result = 1
    return result

def runtime():
    n,x = 6,3
    start = time.time()
    runtime = brute_force_poly_eval(n,x)
    end = time.time()
    print(f"Pn({x}) for n = {n} is {runtime}")
    print(f"Time: {(end - start) * 1000:.3f} ms\n")
    
    n,x = 6000,30
    start = time.time()
    runtime = brute_force_poly_eval(n,x)
    end = time.time()
    print(f"Pn({x}) for n = {n} is {runtime}")
    print(f"Time: {(end - start):.3f} seconds\n")