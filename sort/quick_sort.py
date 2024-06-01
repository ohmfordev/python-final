def quick_sort(name, arr):
    print(f"{name}: {arr}")
    
    if len(arr) <= 1:
        print("Returning:", arr)
        return arr
    
    pivot = arr[0]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print("Left:", left)
    print("Middle:", middle)
    print("Right:", right)
    print("-" * 40)


    sorted_left = quick_sort("left", left)
   

    sorted_right = quick_sort("right", right)

    print("sorted_left :", sorted_left)
    print("middle :", middle)
    print("right :", right)
    
    result = sorted_left + middle + sorted_right
    print(f"Result for {name}: {result}")
    return result

numbers = [64, 34, 25, 12, 22, 11, 90 ,100,200]

print("Sorted data:", quick_sort("start", numbers))
