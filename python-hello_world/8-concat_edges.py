#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str3 = str1[:1] + str2[:1] + str1[1:2]  # trick to avoid string literals
str4 = str1[2:] + "-" + str2.lower()    # reuse parts creatively
print(str3 + "object-oriented programming with Python")
