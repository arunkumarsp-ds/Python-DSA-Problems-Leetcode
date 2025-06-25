# Brute force solution:
"""
1) We know that we can trap water only if there are buildings on both sides of the current building.

2) When both the left and right buildings are taller than the current building, we can trap water at that position.

3) So, we loop from the 2nd building to the (n-1)th building (because the first and last buildings can’t trap water).

4) For every building in this range:

     * We find the maximum height to the left (left_max)

     * We find the maximum height to the right (right_max)

     * We take the minimum of left_max and right_max because water will not overflow the smaller side.

     * Then we subtract the current building height from this minimum to get the actual water trapped at that 	      	building.

5) We do this only if both left and right buildings are taller than the current building.

    * Otherwise, if any one of them is smaller, it might give a negative capacity, which doesn’t make sense.
"""

def trap(self, height: List[int]) -> int:
    water = 0
    n = len(height)

    for i in range(1,n-1):
        left_max = max(height[ : i])
        right_max = max(height[i+1: ])
        if left_max > height[i] and right_max >height[i] :
            water += min(left_max,right_max) - height[i]
    return water

"""
Time:O(n^2)
Space: O(1)"""

# optimal solution

"""
1) From the brute-force solution, we know the core logic:

        -We always subtract the current building height from min(left_max, right_max) to calculate trapped water.

	-If we can do this using a single traversal, we can reduce the time complexity to O(n).

2) To achieve that, we use two pointers:

	-One pointer i starting from the left end.

	-Another pointer j starting from the right end.

3) Now, during traversal:

     * If height[i] < height[j], this indicates:

	-There’s a downward slope on the left (i) and possibly an upward slope on the right (j).

	-Water can only be trapped on the downward side.

	-So, we update left_max = max(left_max, height[i])

	-Calculate trapped water at index i using: left_max - height[i]

	-Then move i one step forward.

     * Else if height[j] < height[i], this means:

	-There’s a downward slope on the right.

	-We update right_max = max(right_max, height[j])
	
	-Calculate trapped water at index j using: right_max - height[j]

	-Then move j one step backward.

     * If height[i] == height[j], we can move either pointer, as there’s no effective slope difference.

	 -Our logic will still handle the correct trapped water calculation.

4) In simple terms:

     - i is used to maintain left_max
	
     - j is used to maintain right_max

5) We continue this until i and j meet (i and j are not the same building)."""

def trap(self, height: List[int]) -> int:

    n = len(height)
    water = 0
    left_max = 0
    right_max= 0

    i = 0
    j = n-1

    while i < j:
        if height[i] <= height[j]:
            left_max = max(left_max,height[i])
            water = water + left_max - height[i]
            i += 1
        else:
            right_max = max(right_max,height[j])
            water = water + right_max- height[j]
            j -= 1
    return water

"""
Time: O(n)
space:O(1) """