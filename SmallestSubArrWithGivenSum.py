#Time Complexity is O(N + N) = O(N)
def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  window_sum = 0                        #Subtract max_sum
  min_length = math.inf                 #Added
  window_start = 0
  
  for window_end in range(len(arr)):
      window_sum += arr[window_end]     
    
      while window_sum >=s:                   
        min_length = min(min_length, window_end - window_start +1) #Added
        window_sum -= arr[window_start]
        window_start += 1
    if min_length == math.inf:  #Added
        return 0                #Added
    return min_length           #Added
  

'''
def smallest_subarray_with_given_sum(s, arr):
  window_sum = 0
  min_length = math.inf
  window_start = 0

  for window_end in range(0, len(arr)):
    window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start + 1)
      window_sum -= arr[window_start]
      window_start += 1
  if min_length == math.inf:
    return 0
  return min_length
'''

