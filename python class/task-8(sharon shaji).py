import numpy as np

question = """

1. Create 0-D, 1-D, 2-D & 3-D arrays using numpy & demonstrate the following.
a. Print the arrays
b. Do slicing operations
c. Change any array element
d. dtype
e. ndim
f. astype
e. copy
f. view
g. base
h. shape
i. reshape
j. Flatten the array
k. Traverse the array using for loop
l. nditer
m. split
n. join
o. sort
p. where
q. append

"""

def main():
    zero_d_array = np.array(10)

    one_d_array = np.array([10, 20, 30, 40, 50, 60, 70])

    two_d_array = np.array([[10, 20], [100,12], [1211, 2]])

    three_d_array = np.array([ [ [5,6,1], [7,8,1] ], [ [1,2,0], [3,4,0] ] ])


    COLOR_START = "\033[33m"
    COLOR_END = "\033[0m"
    
    #PRINTING
    print(f'1 -> {COLOR_START}PRINTING{COLOR_END}')
    print(zero_d_array)
    print(one_d_array)
    print(two_d_array)
    print(three_d_array, "\n")

    #SLICING
    print(f'2 -> {COLOR_START}SLICING{COLOR_END}')
    sliced_1d = one_d_array[1:3]
    sliced_2d = two_d_array[0, 1:3]
    sliced_3d = three_d_array[1, 0]

    print("Sliced 1-D array:", sliced_1d)
    print("Sliced 2-D array:", sliced_2d)
    print("Sliced 3-D array:", sliced_3d, "\n")

    #MODIFYING
    print(f'3 -> {COLOR_START}MODIFYING{COLOR_END}')
    two_d_array[2,1] = 381
    print("Modified 2-D array:", two_d_array, "\n")   

    #DTYPE
    print(f'4 -> {COLOR_START}DTYPE{COLOR_END}')
    print(" Data type of 1-D array:", one_d_array.dtype, "\n")

    #NDIM
    print(f'5 -> {COLOR_START}NDIM{COLOR_END}')
    print("Dimension of 3-D array: ", three_d_array.ndim, "\n")

    # ASTYPE
    print(f'6 -> {COLOR_START}ASTYPE{COLOR_END}')
    casted_array = one_d_array.astype(np.float32)
    print("Casted 1-D array to float32:", casted_array, "\n")

    # COPY
    print(f'7 -> {COLOR_START}COPY{COLOR_END}')
    copied_array = two_d_array.copy()
    print("Copied 2-D array:", copied_array, "\n")

    # VIEW
    print(f'8 -> {COLOR_START}VIEW{COLOR_END}')
    view_array = two_d_array.view()
    print("View of 2-D array:", view_array, "\n")

    # BASE
    print(f'9 -> {COLOR_START}BASE{COLOR_END}')
    print("Base array of view:", view_array.base, "\n")

    # SHAPE
    print(f'10 -> {COLOR_START}SHAPE{COLOR_END}')

    #splitting for better understanding
    #list_count, element_count = three_d_array.shape
    #print(f"Shape of 2-D array: list count = {list_count}, element count = {element_count}")
    print(f"Shape of 3-D array:{three_d_array.shape} \n")


    # RESHAPE
    print(f'11 -> {COLOR_START}RESHAPE{COLOR_END}')
    reshaped_array = two_d_array.reshape(3,1,2)
    print("Reshaped 2-D array:", reshaped_array, "\n")

    # FLATTEN THE ARRAY
    print(f'12 -> {COLOR_START}FLATTEN THE ARRAY{COLOR_END}')
    flattened_array = three_d_array.flatten()
    print("Flattened 3-D array:", flattened_array, "\n")

    # TRAVERSE THE ARRAY USING FOR LOOP
    print(f'13 -> {COLOR_START}RAVERSE THE ARRAY USING FOR LOOP{COLOR_END}')
    for i in range(three_d_array.shape[0]):
        for j in range(three_d_array.shape[1]):
            print(three_d_array[i, j])
            #for k in range(three_d_array.shape[2]):
                #print(three_d_array[i, j, k])
    print("\n")

    # NDITER
    print(f'14 -> {COLOR_START}NDITER{COLOR_END}')
    for x in np.nditer(three_d_array):
        print(x, end=" ")
    print("\n")

    # SPLIT
    print(f'15 -> {COLOR_START}SPLIT{COLOR_END}')
    split_arrays = np.array_split(two_d_array, 2)
    print("Split 1-D array:", split_arrays, "\n")

    # JOIN
    print(f'16 -> {COLOR_START}JOIN{COLOR_END}')
    joined_array = np.concatenate([split_arrays[0], split_arrays[1]])
    print("Joined array:", joined_array, "\n")

    # SORT
    print(f'17 -> {COLOR_START}SORT{COLOR_END}')
    sorted_array = two_d_array.sort()  # Sorts in-place
    print("Sorted 1-D array:", two_d_array, "\n")

    # WHERE
    print(f'18 -> {COLOR_START}WHERE{COLOR_END}')
    condition = one_d_array > 50
    filtered_array = one_d_array[np.where(condition)]
    print("Elements where condition is True:", filtered_array, "\n")

    # APPEND
    print(f'19 -> {COLOR_START}APPEND{COLOR_END}')
    new_array = np.append(two_d_array, [[1,2,1], [12,122,1]])
    print("Appended array:", new_array, "\n")

if __name__ == "__main__":
    main()
