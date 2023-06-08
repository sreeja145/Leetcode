import sys
def find_pair(arr):
  if len(arr)<2:
    return arr
  low=0
  high=len(arr)-1
  min=sys.maxsize
  i=j=0
  while low<high:
    if abs(arr[low]+arr[high])<min:
      min=abs(arr[low]+arr[high])
      (i,j)=(low,high)
    if min==0:
      break
    if arr[low]+arr[high]<0:
      low=low+1
    else:
      high=high-1
  print("pair is ",arr[i],arr[j])
A=[-5,-4,-3,-2,0,2,4,9]
find_pair(A)
