#DSA-Exer-21

def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    low=0
    high=len(num_list)-1
    if high==low:
        return num_list
    else:
        mid=(high+low)//2
        lis1=merge_sort(num_list[low:mid+1])
        lis2=merge_sort(num_list[mid+1:high+1])
        fin=merge(lis1,lis2)
        return fin

def merge(left_list,right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i=j=0
    sorted_list=[]
    while(i<len(left_list) and j<len(right_list)):
        if(left_list[i]<=right_list[j]):
            sorted_list.append(left_list[i])
            i=i+1
        else:
            sorted_list.append(right_list[j])
            j=j+1
    if i<=len(left_list)-1:
        for num in range(i,len(left_list)):
            sorted_list.append(left_list[num])
    if j<=len(right_list)-1:
        for num in range(j,len(right_list)):
            sorted_list.append(right_list[num])
    return sorted_list

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)
