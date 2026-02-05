\# Basic Logic and Control Flow



This folder contains beginner-level algorithm problems implemented in Python.

Each problem includes a clear problem statement, algorithm, and Python solution.



---



\## Problem 01: Find the Largest of Three Numbers



\*\*Input:\*\*  

Three numbers a, b, c



\*\*Output:\*\*  

The largest number among a, b, c



\*\*Algorithm:\*\*

1\. Read values a, b, and c

2\. If a >= b AND a >= c, print a

3\. Else if b >= a AND b >= c, print b

4\. Else print c



\*\*Python File:\*\*  

`01\_largest\_of\_three.py`



---

## Problem 02: Check whether a number is even or odd

**Input:**  
One integer a

**Output:**  
Indicates whether the number is even or odd

**Algorithm:**
1. Read integer a
2. If a mod 2 = 0, print "Even"
3. Else print "Odd"

**Python File:**  
`02_even_or_odd.py`

---

## Problem 03: Check whether a number is prime

**Input:**  
One integer a

**Output:**  
"Prime" if the number is prime, otherwise "Not Prime"

**Algorithm:**
1. Read integer a
2. If a < 2, print "Not Prime" and stop
3. For each number i from 2 to √a (inclusive):
   - If a mod i = 0, print "Not Prime" and stop
4. If no divisor is found, print "Prime"

**Python File:**  
`03_prime_or_not.py`

---

## Problem 04: Count digits in a number

**Input:**  
One integer a

**Output:**  
Number of digits in the given number

**Algorithm:**
1. Read integer a
2. If a = 0, print 1 and stop
3. Convert a to its absolute value
4. Initialize count = 0
5. While a > 0:
   - Divide a by 10 using integer division
   - Increment count by 1
6. Print count

**Python File:**  
`04_count_digits.py`

## Problem 05: Reverse the number

**Input:**  
One integer n

**Output:**  
The reverse of the given number

**Algorithm:**
1. Read integer n  
2. If n = 0, print 0 and stop  
3. If n is negative, store sign = -1; otherwise store sign = 1  
4. Convert n to its absolute value  
5. Initialize reverse = 0  
6. While n > 0:  
   - Extract last digit using n % 10  
   - Update reverse = (reverse × 10) + digit  
   - Divide n by 10 using integer division  
7. Multiply reverse by sign  
8. Print reverse  

**Python File:**  
`05_reverse_the_number.py`


## Problem 06: Check if a number is a palindrome

**Input:**  
One integer n

**Output:**  
Print whether the given number is a palindrome or not

**Algorithm:**
1. Read integer n  
2. If n is negative, print "not a palindrome" and stop  
3. If n is equal to 0, print "palindrome" and stop  
4. Store the value of n in a temporary variable temp  
5. Initialize reverse = 0  
6. While temp > 0:  
   - Extract the last digit using temp % 10  
   - Update reverse = (reverse × 10) + digit  
   - Divide temp by 10 using integer division  
7. Compare reverse with the original number n  
8. If both are equal, print "palindrome"; otherwise print "not a palindrome"  

**Python File:**  
`06_palindrome_or_not.py`



