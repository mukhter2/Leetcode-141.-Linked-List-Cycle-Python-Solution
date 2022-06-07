# Leetcode 141: Linked List Cycle Solution in Python
Problem link : https://leetcode.com/problems/linked-list-cycle/
## Problem Statement
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
## Examples
### Example 1:
![image](https://user-images.githubusercontent.com/19319249/172318379-a6d552f6-89e6-47ea-8b12-0276d227f357.png)

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
### Example 2:
![image](https://user-images.githubusercontent.com/19319249/172318417-f0974e0c-c4b9-4bfd-b286-0f8524c76396.png)

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
### Example 3:
![image](https://user-images.githubusercontent.com/19319249/172318476-dca99276-6eb8-421f-a032-91929dcb2f2c.png)

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
## Constraints
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

## Methodology
Step 1: Declare an empty dictionary for counting number of occurances per head
Step 2: Check if a Linked list is null, if yes, return false
Step 3: Check if a linked list is visited earlier, based on that create/update count on dictionary variable
Step 4: Return true if any head's occurance greater than 1
Step 5: Return false if traversing through linked list is completed
