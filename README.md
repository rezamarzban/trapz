# trapz
Trapezoidal rule to calculating integrals

# usage

`python3 trapz.py expression a b n` calculate integral of expression from a to b with n intervals.

example:

```
python3 trapz.py "2.71**(-1j*x)" 1 1000 10000
```

# quad

`quad` is so much better than `trapz`, It compute a definite integral. Integrate func from a to b (possibly infinite interval) using a technique from the Fortran library QUADPACK

`python3 quad.py expression a b` calculate integral of expression from a to b.

example:

```
python3 quad.py "sin(x)*(2.71**(-1j*x))" 1 10
```
