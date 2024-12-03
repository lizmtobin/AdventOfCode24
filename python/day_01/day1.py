# PART 1
def read_file():
  left  = []
  right = []
  
  with open('puzzle_input.txt', 'r') as f:
    for line in f:
      arr = line.split()
      left.append(arr[0])
      right.append(arr[1])
        
  left.sort()
  right.sort()
    
  return left, right
  
def find_difference(left, right):
  difference = 0
  for i in range(len(left)):
    difference += abs(int(left[i]) - int(right[i]))
  
  print(f"The difference between the two lists is: {difference}")

# TODO: 
# pair up the numbers and measure how far apart they are. 
# Pair up the smallest number in the left list with the smallest number in the right list,
# then the second-smallest left number with the second-smallest right number, and so on.

# Approach:
# take each line, place each number in a list, and sort the list.
# compare the numbers in the list to find the difference between them.
# sum up the differences.

# PART 2

# TODO:
# Find the 'similary score'
# the number times a number in the left list appears in the right list.
# multiplied by the number itself
# applies to duplicates as well.

# Approach:
  # it is already sorted, so we can just iterate through the list and compare the numbers.
  # we will need to search for the number in the right list and count the number of times it appears.
  # multiply the number of times it appears by the number itself.
  # sum up the results.
  
def calculate_similarity_score(left_list, right_list):
    # Convert all elements to integers
    left_list = [int(x) for x in left_list]
    right_list = [int(x) for x in right_list]

    # Initialize similarity score
    similarity_score = 0

    # Create a dictionary to count occurrences in the right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Iterate through the left list and calculate the contribution to the similarity score
    for num in left_list:
        if num in right_counts:
            similarity_score += num * right_counts[num]

    print(similarity_score)
 

def main():
  left, right = read_file()
  find_difference(left, right)
  calculate_similarity_score(left, right)
  
if __name__ == "__main__":
  main()
    