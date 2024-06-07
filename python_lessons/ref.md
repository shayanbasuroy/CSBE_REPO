~ cd Document
➜ Document mkdir CBSE
➜ Document cd CBSE
➜ CBSE mkdir python_lessons
➜ CBSE cd python_lessons
➜ python_lessons code .
➜ python_lessons

What is a ^ b?
The ^ operator is called the bitwise XOR (exclusive OR) operator. It operates on the binary (bit) representation of numbers. Here's how it works:

It compares each bit of the two numbers.
If the bits are the same (both 0 or both 1), the result is 0.
If the bits are different (one is 0 and the other is 1), the result is 1.
Simple Example
Let's take two numbers, a and b, and see how the bitwise XOR operation works.

a = 6 (which is 0110 in binary)
b = 3 (which is 0011 in binary)
When we perform a ^ b, we compare the bits of a and b:

markdown
Copy code
0110 (a)
^ 0011 (b)

---

0101 (result)
Let's compare each bit from left to right:

The first bit: 0 ^ 0 = 0
The second bit: 1 ^ 0 = 1
The third bit: 1 ^ 1 = 0
The fourth bit: 0 ^ 1 = 1
So, the result in binary is 0101, which is 5 in decimal.
