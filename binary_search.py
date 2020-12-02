def binary(list_arr,number):
    size = len(list_arr)
    start = 0
    end = size-1
    while start <= end:
        mid = (start+end)//2
        if number == list_arr[mid]:
            return mid
        elif number < list_arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1
while True:
  try:
    list_arr= [int(x) for x in input("Please enter your array: ").split(" ")] 
    print("Your input array is: ", list_arr)
    number=int(input("Please enter a value to search: "))
    print("your input is",number)
    break
  except:
    print("Invalid Input")
#print("while loop exited")
result=binary(list_arr,number)
if result !=-1:
  print(f'The index for the number:"{number}" is at {result}')
else:
  print(f'Number:"{number}" is not present in the array')

