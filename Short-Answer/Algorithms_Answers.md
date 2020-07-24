#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

### a) 
```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
- [hint](https://youtu.be/RRItKNx4daY?t=1266)  
- *O(n)*   
- It's not linear because there's multiplaction happening with the `n` within the  `while loop`. Therefore, `n^2` or `n^55` is still is all represented as O(n) if it's still in the condition...  
- The two `n`'s on the bottom cancel out the two `n`'s on the top.  



### b)
```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
- [hint](https://youtu.be/RRItKNx4daY?t=2246)
- *O(n log n)*  
- The loop is O(n)
- And for each itteration happening within that loop, there's another loop causing the time complexity to go to O(n log n) - see the hint for a better explination.




### c)
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
- https://stackoverflow.com/questions/13467674/determining-complexity-for-recursive-functions-big-o-notation#:~:text=The%20time%20complexity%2C%20in%20Big,n)%20%2C%20often%20called%20linear.&text=(Actually%20called%20order%20of%20n,%3D%20O(n)%20).
- *O(n)*  
- The function calls itself, but is still based on linear input, with no crazy shenanigans going on.




## Exercise II

```
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
```

```
if n >= f # Egg breaks
if n < f  # Egg survives  

```
- Trying to figure out the the fastest way to minimize the broken eggs would require a type of searching algorithm. Likely a binary search which would be *[O(log n)](https://www.bigocheatsheet.com/)*.

When trying to find `f`, we need to start with the input of `n`. Use `len(n) // 2` to start dropping eggs. If the egg breaks, go down half the distance to the bottom and try again. Repeat until no broken eggs and do the opposite going up when the first non-broken egg **gently** lands on the ground. This is the fastest, least expensive way to reduce the number of infinite eggs used, broken or not.