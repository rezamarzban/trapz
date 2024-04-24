# trapz
Trapezoidal rule to calculating integrals

# usage

`python3 trapz.py expression a b n` calculate integral of expression from a to b with n intervals.

example:

```
python3 trapz.py "sin(x)*cos(x)*tan(x)*cot(x)*log(x)*log10(x)*sqrt(x)*exp(-1*x)*(x**(-1j*x))" 1 10 1000
```

It calculate below integral from x=1 to x=10 with n=1000 intervals

$$
\int \sin(x) \cos(x) \tan(x) \cot(x) \ln(x) \log(x) \sqrt{x} e^{-x} x^{-i x} \ dx
$$ 

# quad

Both of `quad` and `trapz` are numerical method to calculating integrals, But `quad` is so much better than `trapz`, It compute a definite integral. Integrate func from a to b (possibly infinite interval) using a technique from the Fortran library QUADPACK

`python3 quad.py function a b` calculate integral of function from a to b.

example:

```
python3 quad.py "sin(x)*cos(x)*tan(x)*cot(x)*log(x)*log10(x)*sqrt(x)*exp(-1*x)*(x**(-1j*x))" 1 10
```

It calculate below integral from x=1 to x=10

$$
\int \sin(x) \cos(x) \tan(x) \cot(x) \ln(x) \log(x) \sqrt{x} e^{-x} x^{-i x} \ dx
$$ 
