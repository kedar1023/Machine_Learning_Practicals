Type "help", "copyright", "credits" or "license" for more information.
>>> a=('a','b')
>>> a
('a', 'b')
>>> type(a)
<class 'tuple'>
>>> a1=('a')
>>> a1
'a'
>>> a,
(('a', 'b'),)
>>> a2,
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a2' is not defined
>>> a=a2,
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a2' is not defined
>>> x,y=a
>>> a
('a', 'b')
>>> x
'a'
>>> y
'b'
>>> a='a','b'
>>> a
('a', 'b')
>>> a[0]=1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> student_cgpa={'K':5,'k1':6,'k2':7}
>>> student_cgpa
{'K': 5, 'k1': 6, 'k2': 7}
>>> type(student_cgpa)
<class 'dict'>
>>> student_cgpa.key
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'key'
>>> x={'a':100,'b':90,'c':80,'a':40}
>>> x
{'a': 40, 'b': 90, 'c': 80}
>>> student_cgpa[d]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> student_cgpa['k2']
7
>>> student_cgpa['k2']=9
>>> student_cgpa[
... student_cgpa
... }
  File "<stdin>", line 3
    }
    ^
SyntaxError: invalid syntax
>>> student_cgpa
{'K': 5, 'k1': 6, 'k2': 9}
>>> student_cgpa['x']=7.8
>>> student_cgpa['x']=7.8
>>> del student_cgpa['x']=7.8
  File "<stdin>", line 1
    del student_cgpa['x']=7.8
                         ^
SyntaxError: invalid syntax
>>> del student_cgpa['x']
>>> student_cgpa
{'K': 5, 'k1': 6, 'k2': 9}
>>> student_cgpa.pop('K')
5
>>> student_cgpa
{'k1': 6, 'k2': 9}
>>> student_cgpa['y]
  File "<stdin>", line 1
    student_cgpa['y]
                   ^
SyntaxError: EOL while scanning string literal
>>> student_cgpa['y']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'y'
>>> 'k1' in  student_cgpa
True
>>> student_cgpa,hasKey('k1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hasKey' is not defined
>>> student_cgpa,hasKey('k1')