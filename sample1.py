Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: /Users/gaddamabhithareddy/Documents/python/sample.py ========
>>> import sample
>>> sample.a
100
>>> sample.b
'abhi'
>>> sample.y()
my name is abhitha
>>> print(sample.y(10,20))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(sample.y(10,20))
TypeError: y() takes 0 positional arguments but 2 were given
>>> print(sample.z(10,2))
20
>>> from sample import*
>>> print(a)
100
>>> print(b)
abhi
>>> y()
my name is abhitha
>>> print(z(10,3))
30
>>> from sample import a,b,z
>>> print(a)
100
>>> print(b)
abhi
>>> print(z(10,4))
40
import sample as nithi
print(nithi.a)
100
print(nithi.b)
abhi
y()
my name is abhitha
print(z(10,5))
50
