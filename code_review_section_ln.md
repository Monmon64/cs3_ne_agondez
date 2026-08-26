Annex C

Code Quality Assessment Worksheet

Section: Neon	                                                        Score: _________
C# / Name: Monvic Gnel E. Agondez, Ysabella Andrea "Sunny" E. Rogers  Date: 08/26/2026

Instructions:

The problem: Search for a Number in a Sorted List

For example: Both algorithms could search: 
numbers = [5, 12, 18, 23, 31, 47, 56, 68, 74, 90]
target = 47

Implementation 1

def linear_search(numbers, target):
   for i in range(len(numbers)):
       if numbers[i] == target:
           return i
           
   return -1


Implementation 2

def binary_search(numbers, target):
   low = 0
   high = len(numbers) - 1

   while low <= high:
       middle = (low + high) // 2

       if numbers[middle] == target:
           return middle
       elif numbers[middle] < target:
           low = middle + 1
       else:
           high = middle - 1

   return -1







Questions with Checklists

1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

Implementation 2 is faster when the list is very large because it reduces the search area by about half after each check. Meanwhile, Implementation 1 searches through the numbers one by one and may need to check every single element.

Checklist to guide your answer:

Implementation 1
☑ How many elements might the algorithm need to check? Every single element in the worst case.
☑ Does the algorithm reduce the search area as it runs? No.
☑ Does the algorithm still work efficiently with a very large list? Not as efficient.

Implementation 2
☑ How many elements might the algorithm need to check? Far fewer elements.
☑ Does the algorithm reduce the search area as it runs? Yes.
☑ Does the algorithm still work efficiently with a very large list? Yes.


2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?

Implementation 1, Linear Search, is easier to understand at first glance because the code is simple and straightforward. It checks each number one by one until it finds the target. The variable names are easy to understand, and there are fewer conditions to follow compared to Implementation 2.

Checklist to guide your answer:

Implementation 1
☑ How meaningful are the variable names? The variables are meaningful because the names: numbers, target, and i are simple and easy to understand. 
☑ How simple is the logic? The logic is very simple because it checks each number one by one until it finds the target.
☑ How concise is the code? The code is short and contains only the necessary steps for searching.
☑ How easy is it to follow the search process? It is very easy to follow because the algorithm starts at the beginning of the list and checks each number in order.

Implementation 2
☑ How meaningful are the variable names? The variable names numbers, target, low, high, and middle are meaningful and describe their purpose clearly.
☑ How simple is the logic? The logic is more complicated because it uses low, high, and middle and has multiple conditions to decide which part of the list to search.
☑ How concise is the code? The code is fairly concise, but it has more lines and steps than Linear Search.
☑ How easy is it to follow the search process? It is somewhat harder to follow because you need to understand how Binary Search repeatedly divides the search area.


3. Maintainability
If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

Implementation 1 may be easier to maintain because it's structure is simpler and more straightforward. It only loops through the list and checks each number, so adding or changing steps would be easier to follow. Implementation 2 has more variables and conditions, which could make modifications more complicated.

Checklist to guide your answer:

Implementation 1
☑ Is the structure straightforward? Yes.
☑ Would adding new steps break the code easily? Less likely.
☑ Is there less chance of errors when updating? Yes.

Implementation 2
☑ Is the structure straightforward? No, it is more complicated.
☑ Would adding new steps break the code easily? Yes, there will be more things to consider
☑ Is there less chance of errors when updating? No, there will be more chances of errors.


4. Testability
Which algorithm is easier to test with different inputs? Why?

Implementation 1 is easier to test. It can be tested easily with small lists, such as when the target is at the beginning, middle, end, or not present. It's output is also straightforward and predictable.

Checklist to guide your answer:

Implementation 1
☑ Can you test with small lists easily? Yes.
☑ Does the algorithm have fewer conditions to check? Yes. 
☑ Is the output predictable and clear? Yes.

Implementation 2
☑ Can you test with small lists easily? Yes. 
☑ Does the algorithm have fewer conditions to check? No.
☑ Is the output predictable and clear? Yes.


5. Reliability and Input Validation
What should the algorithm check to avoid errors when receiving input from a user?

The algorithm should check if the list is empty and make sure the user enters valid numbers instead of letters or other invalid values. It should also handle unusual inputs without crashing. For Binary Search, the program must make sure the list is sorted because Binary Search only works correctly with a sorted list. While Linear Search does not require the list to be sorted.

Checklist to guide your answer:

Implementation 1
☑ Does the algorithm check if the list is empty? No.
☑ Does it handle invalid inputs (like letters instead of numbers)? No.
☑ Does it avoid crashing when inputs are unusual? No.
☑ Does it check that the list is sorted before using Linear Search? No, because it doesn't need to.

Implementation 2
☑ Does the algorithm check if the list is empty? No.
☑ Does it handle invalid inputs (like letters instead of numbers)? No.
☑ Does it avoid crashing when inputs are unusual? No.
☑ Does it check that the list is sorted before using Binary Search? No, but the list must be sorted for it to work correctly.


6. Final Answer
Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

I would choose Implementation 2, Binary Search, for this problem because it is faster and more efficient when searching for a number in a very large sorted list. It reduces the search area by about half after each check, so it can find the target much faster than Linear Search. However, Implementation 1, Linear Search, would be more suitable for small lists or when the list is not sorted. Linear Search is also simpler, easier to understand, maintain, and test.






