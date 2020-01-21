Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("Your name is", name)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print ("Your name is", name)
NameError: name 'name' is not defined
>>> name = "Alejandro Stevens"
>>> print ("Your name is", name)
Your name is Alejandro Stevens
>>> 