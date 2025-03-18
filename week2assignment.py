"""
Week Two Assignment: List and Tuple Operations

Instructions:
1. Create an empty list called my_list.
2. Append the following elements to my_list: 10, 20, 30, 40.
3. Insert the value 15 at the second position in the list.
4. Extend my_list with another list: [50, 60, 70].
5. Remove the last element from my_list.
6. Sort my_list in ascending order.
7. Find and print the index of the value 30 in my_list.

Additionally, this script demonstrates some tuple operations to showcase an understanding of both lists and tuples.
"""

def list_operations():
    # Step 1: Create an empty list called my_list.
    my_list = []
    print("Step 1: Created empty list:", my_list)
    
    # Step 2: Append elements 10, 20, 30, 40 to my_list.
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print("Step 2: After appending 10, 20, 30, 40:", my_list)
    
    # Step 3: Insert the value 15 at the second position (index 1).
    my_list.insert(1, 15)
    print("Step 3: After inserting 15 at second position:", my_list)
    
    # Step 4: Extend my_list with another list: [50, 60, 70].
    my_list.extend([50, 60, 70])
    print("Step 4: After extending with [50, 60, 70]:", my_list)
    
    # Step 5: Remove the last element from my_list.
    removed_element = my_list.pop()  # pop() removes and returns the last element
    print(f"Step 5: Removed the last element ({removed_element}):", my_list)
    
    # Step 6: Sort my_list in ascending order.
    my_list.sort()
    print("Step 6: After sorting in ascending order:", my_list)
    
    # Step 7: Find and print the index of the value 30 in my_list.
    try:
        index_30 = my_list.index(30)
        print("Step 7: The index of 30 in my_list is:", index_30)
    except ValueError:
        print("30 is not in the list.")

def tuple_operations():
    # Demonstrating basic tuple operations.
    # Create a tuple of five favorite fruits.
    my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
    print("\nTuple Operations:")
    print("Created tuple:", my_tuple)
    
    # Access elements using indexing (0-indexed)
    print("First fruit (index 0):", my_tuple[0])
    
    # Slicing: Get the first three fruits
    first_three = my_tuple[:3]
    print("First three fruits (slicing):", first_three)
    
    # Tuples are immutable: the following line would raise an error if uncommented.
    # my_tuple[1] = "blueberry"
    print("Note: Tuples are immutable; elements cannot be changed.")

if __name__ == "__main__":
    print("List Operations:")
    list_operations()
    tuple_operations()
