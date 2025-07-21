import time


def horners_rule_poly_eval(n,x):
    result=n
    for k in range(n-1,0,-1):
        result= (result+k)*x
    result+=1
    return result

def runtime():
    n,x = 6,3
    start = time.time()
    runtime = horners_rule_poly_eval(n,x)
    end = time.time()
    print(f"Pn({x}) for n = {n} is {runtime}")
    print(f"Time: {(end - start) * 1000:.3f} ms\n")
    
    n,x = 6000,30
    start = time.time()
    runtime = horners_rule_poly_eval(n,x)
    end = time.time()
    print(f"Pn({x}) for n = {n} is {runtime}")
    print(f"Time: {(end - start):.3f} seconds\n")