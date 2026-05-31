question1:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

question2:
ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

question3:
Given an integer x, return true if x is a palindrome, and false otherwise.
 question4:
 # Roman to Integer - LeetCode #13

## Problem Description

Roman numerals are represented by seven different symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Given a Roman numeral, convert it to an integer.

## Solution Approach

This solution uses:

* A dictionary to map Roman numeral symbols to their integer values.
* A `while` loop to iterate through the Roman numeral string.
* Comparison of adjacent symbols to determine whether values should be added or subtracted.
* Index skipping when a pair has already been processed.

### Logic

1. Compare the current Roman numeral with the next one.
2. If the current value is smaller than the next value, subtract it from the next value and move two positions forward.
3. If the values are equal, add both values and move two positions forward.
4. If the current value is greater than the next value, add the current value and move one position forward.
5. Handle the final remaining character separately.






