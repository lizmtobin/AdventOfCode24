def is_safe(numbers):
  # Loop through the list, stopping one element before the end or line four is out of range
  for i in range(len(numbers) -1):
    a, b = numbers[i], numbers[i+1]
    # Check if the absolute difference between consecutive numbers is between 1 and 3
    if not (1 <= abs(b - a) <= 3):
      return False
    
    # If we are at the second-to-last element, skip the triplet check/end this iteration
    # It will be out of range otherwise and we checked already via line 14
    if i == len(numbers) - 2:
      continue
    
    c = numbers[i+2]
    # Check if the triplet is either strictly increasing or strictly decreasing
    if not a > b > c and not a < b < c:
      return False
  # If all checks pass, return True
  return True

def part1():
  reports = []
  safe_level_reports = 0
  
  with open('python/day_02/puzzle_input.txt') as f:
      reports = f.readlines()
  
  for report in reports:
    numbers = list(map(int,report.split()))
    
    if is_safe(numbers):
      safe_level_reports += 1
      
  print(safe_level_reports)
    
def part2():
  reports = []
  safe_level_reports = 0
  
  with open('python/day_02/puzzle_input.txt') as f:
    reports = f.readlines()
    
  for report in reports:
    numbers = list(map(int,report.split()))
    
    if is_safe(numbers):
      safe_level_reports += 1
    else:
      # if not currently safe -  check if it can be made safe by removing one
      for i in range(len(numbers)):
        # remove one number from the list and check if the new list is safe
        if is_safe(numbers[:i] + numbers[i+1:]):
          safe_level_reports += 1
          break
      
  print(safe_level_reports)
    
if __name__ == '__main__':
  part1()
  part2()
  print('Done running day 2')
  
# Part 1 :
# We have jumbled report data
# one 'report' per line 
# Each report is a list of numbers called 'levels' that are separated by spaces
# We need to figure out which reports are 'safe' and which are 'unsafe'
# safe levels either gradually increasing or gradually decreasing

# Report only counts as safe if both of the following are true:

# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.(adjacent dups would fail!)

# Approach:
# Read the file and get the reports by line
# make each line into a list of numbers
# check if the numbers are increasing or decreasing
# check if the difference between adjacent numbers is between 1 and 3

# Output:
#   Count the number of safe reports

# Part 2:
  
# the problem reports are high but ther is a dampner
# The dampner means a single bad level in a report is tolerable

# Approach:
  # same as above but keep count of bad outcomes instead of straigh to false
  # if bad outcomes are more than 1, then the report is unsafe