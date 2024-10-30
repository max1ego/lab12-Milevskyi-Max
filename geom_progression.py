def sum_of_n_terms(a, r, n):
    if r == 1:
        return a * n  
    return a * (1 - r ** n) / (1 - r)

def nth_term(a, r, n):
    return a * r ** (n - 1)
