# Objective

Recursion is unintuitive, so this assignment is practice to be comfortable **applying the rules of recursion**.

During this phase of learning computational thinking, **avoid using** the following Python features (if you are aware of/familiar with them):
- `break` (instead, `return` from a function or use a `while` loop)
- `continue` (instead, use a `while` loop or filter the range of iteration)

----------

# Recursion Practice: Palindrome, Permutations, Paths

## Task 1: Check if a String is a Palindrome
Write a function, `is_palindrome(s: str) -> bool`, that:
- takes in a string `s`
- returns `True` if `s` is a palindrome, and `False` otherwise

A **palindrome** is a string that reads the same forward and backward (like a word that's a mirror of itself).

Examples:
```python
is_palindrome("racecar")  # Output: True
is_palindrome("hello")    # Output: False
is_palindrome("a")        # Output: True  (single character)
is_palindrome("")         # Output: True  (empty string)
```

<details>
<summary><b>Algorithm</b></summary>
<p>To check if a string is a palindrome using recursion, follow these steps:</p>
<ol>
  <li>If the string consists of a single character, it is a palindrome.</li>
  <li>If the first and last characters of the string are not the same, the string is not a palindrome.</li>
  <li>If the first and last characters match, the string is a palindrome if the remaining characters form a palindrome.</li>
</ol>
</details>

<details>
<summary><b>Tips</b></summary>
<p>Did you miss out empty string as a base case?</p>
<p>Translate the above requirements into recursion steps:</p>
<ol>
  <li>What is/are your base case(s)?</li>
  <li>Where will you need your recursive call?</li>
  <li>How will you bring the recursive call closer to the base case?</li>
</ol>
</details>

<details>
<summary><b>Challenge</b></summary>
<p>For very long strings, this algorithm will require a lot of memory space, because string slicing creates a new copy of the string. Is it possible to implement an algorithm that does not involve string slicing, or otherwise creating a new copy of the string? (You may modify the function definition if necessary.)</p>
</details>

## Task 2: Generate Permutations of a String
Write a function, `generate_permutations(s: str) -> list[str]`, that:
- takes in a string `s`
- returns a list of all permutations of `s`

A **permutation** is an arrangement of all the characters of a string in every possible order.

Examples:
```python
generate_permutations("abc")   # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
generate_permutations("ab")    # Output: ['ab', 'ba']
generate_permutations("a")     # Output: ['a']
generate_permutations("")      # Output: ['']
```

<details>
<summary><b>Algorithm</b></summary>
<p>To generate permutations of a string using recursion, follow these steps:</p>
<ol>
  <li>If the string is empty, return a list containing an empty string.</li>
  <li>For each character in the string, remove the character and generate all permutations of the remaining string.</li>
  <li>Concatenate the removed character with each permutation of the remaining string and add it to the result list.</li>
</ol>
</details>

<details>
<summary><b>Challenge</b></summary>
<p>How would you implement this iteratively?</p>
<p>Compare the iterative and recursive implementations. Which do you prefer? Why?</p>
</details>

<details>
<summary><b>Tips</b></summary>
<p>Translate the above requirements into recursion steps:</p>
<ol>
  <li>What is your base case?</li>
  <li>How will you bring the recursive call closer to the base case?</li>
  <li>What does your recursive call represent? How will you add the character you removed back to the result</li>
</ol>
</details>

## Task 3: Count Number of Paths from A to B, Moving Only Rightwards or Upwards
Write a function, `num_paths(m: int, n: int) -> int`, that:
- takes in two integers `m` and `n` representing the dimensions of a grid
- returns the number of ways to go from the bottom-left corner (0, 0) to the top-right corner (m, n), moving only rightwards or upwards

Examples:
```python
num_paths(2, 2)  # Output: 6
num_paths(1, 1)  # Output: 2
num_paths(3, 2)  # Output: 10
num_paths(0, 5)  # Output: 1
```

<details>
<summary><b>Algorithm</b></summary>
<p>To count the number of ways to go from A to B using recursion, follow these steps:</p>
<ol>
  <li>If either `m` or `n` is `0`, return `1` (only one way to move in a single row or column).</li>
  <li>Otherwise, the number of ways to reach the top-right corner is the sum of the number of ways to reach the cell to the left and the number of ways to reach the cell below.</li>
</ol>
</details>

<details>
<summary><b>Tips</b></summary>
<p>You may wish to draw a diagram to better illustrate the problem for yourself.</p>
<p>Translate the above requirements into recursion steps:</p>
<ol>
  <li>What are your base cases?</li>
  <li>Where will you need your recursive calls?</li>
  <li>How will you bring the recursive call closer to the base case?</li>
</ol>
</details>

<details>
<summary><b>Challenge</b></summary>
<p>The algorithm described above involves a lot of repeated calculation for results that have already been previously computed. How can we avoid unnecessary computation?</p>
</details>

----------

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
