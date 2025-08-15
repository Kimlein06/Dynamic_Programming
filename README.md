# Dynamic_Programming
### Introduction to Dynamic Programming 
- exercises from LeetCode
- Experiment with different algorithms to see the changes in the time complexity
- Demonstration with the Fibonacci series 

Recursion, memoization, and the bottom-up approach are different ways to solve problems like the Fibonacci sequence, each with trade-offs in terms of efficiency and clarity.

## Recursion
Recursion is a programming technique where a function calls itself to solve a smaller instance of the same problem. For the Fibonacci series, a recursive function would calculate F(n) by calling itself to find F(n−1) and F(n−2), then adding the results.

## Memoization
Memoization is a technique that optimizes recursive algorithms by storing the results of expensive function calls and returning the cached result when the same inputs occur again. It's a form of dynamic programming.

In the context of the Fibonacci series, a memoized solution would still utilize recursion but also employ a data structure (such as an array or dictionary) to store the Fibonacci numbers as they are calculated. Before making a recursive call, it checks if the value is already in the cache. If it is, it returns the stored value; otherwise, it computes the value, stores it, and then returns the stored value. 

## Bottom-Up 
The bottom-up approach, also a dynamic programming technique, solves the problem iteratively from the base cases up to the desired result. Instead of using recursion, it builds the solution from the ground up.

For the Fibonacci series, this method starts with the known values for F(0) and F(1) and then iteratively computes each subsequent Fibonacci number up to F(n) by adding the previous two.

This approach avoids the overhead of recursive function calls, making it generally more efficient in practice than memoization, although both have the same time complexity of O(n). By using an array to store all intermediate results, it can be slightly less space-efficient than an optimized iterative approach that only stores the last two values, which would have a space complexity of O(1).

