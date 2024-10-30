from geom_progression import sum_of_n_terms, nth_term

a = float(input("Введіть перший член прогресії (a): "))
r = float(input("Введіть знаменник прогресії (r): "))
n = int(input("Введіть кількість членів прогресії (N): "))

sum_n = sum_of_n_terms(a, r, n)
print(sum_n)

nth = nth_term(a, r, n)
print(nth)