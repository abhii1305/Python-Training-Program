# -*- coding: utf-8 -*-
"""Copy of Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LjfrbZMYH2O4566CK61QIxvIaruBphZr

<div class="markdown-google-sans">
  <h2>What is Colab?</h2>
</div>

Colab, or "Colaboratory", allows you to write and execute Python in your browser, with
- Zero configuration required
- Access to GPUs free of charge
- Easy sharing

Whether you're a **student**, a **data scientist** or an **AI researcher**, Colab can make your work easier. Watch [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI) to learn more, or just get started below!
"""

a=int(input("enter a number"))
if(a==0):
  print("the number is zero:",a)
elif a<0:
  print("the number is negative:",a)
else:
  print(" the number is positive")

age = int(input(Enter your age))





num = 20
if num >= 0:
     if num ==0:
      print("Zero")
     else:
          print("Positive number")

else:
      print("Negative number")









# Declare an integer variable
num1 = 5
num2 = 2.0


# Print the data types of these variables

print(f"{num1} is of type {type(num1)}")
print(f"{num2} is of type {type(num2)}")




# Arithmatic operation
sum = num1 + num2
print(f"Sum: {sum}")

diff = num1 - num2
print(f"Difference: {diff}")

mul = num1 * num2
print(f"Product: {mul}")

div = num1 / num2
print(f"Division: {div}")
