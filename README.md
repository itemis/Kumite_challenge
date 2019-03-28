# Are you up to the challenge posted below? Hand in your solution and claim your seat at our next #CodingKUMITE event in Hamburg!

Given is a file data.txt. Inside the file you will find balanced lines of random numbers separated by commas, which you should treat as a grid of numbers. (1000 x 1000 numbers)

The challenge is to find certain groups of equal numbers – and we’re only looking for groups with some select properties; such as only groups of 4, 6, 12 and 16 elements to add some spice!

This means, groups of equal numbers which consist of, for instance, 8 elements would not be part of the solution and should be ignored.

## Rules

To get to the solution, you have to stick to all of the rules. Here we’ve comprised a few examples illustrating what counts and what should be ignored!

First of all, a group must go across multiple lines and columns and form a rectangle.

![](/images/img-6-box-vertical.png)

![](/images/img-green-and-red.png)

These groups span across multiple lines and columns, they are groups of 6 elements and they form rectangles – those are the groups we are searching for.

![](/images/img-4-red-horizontal.png)

This group does not span across multiple lines – so it’s not a group that we are searching for.

![](/images/img-red-3-3.png)

This is a group of 9 elements. As we are only searching for groups of 4, 6 ,12 and 16, this one should be ignored. This implies, that this area does not count as a group of 6 or 4 any more.

![](/images/img-green-and-red.png)

Is this a group of 12? Or rather a group of 6 and a group of 8? Without having strict rules how to count groups, there is room for interpretation and we would end up with different results.
Therefore, you should always proceed from left to right starting in the upper left corner, and, going right wins over going down. Therefore, the result would be a group of 6 that we count and a group of 8 that we ignore.

![](/images/img-blue-box.png)

In this case we are looking at two valid groups of 6 elements that we count. Groups must not overlap!

![](/images/img-overlap.png)

Here, the valid group is the green one; the red one is not valid since it overlaps.
Please keep track how many groups of which size you found.

The goal is to create a string that holds this information.

## Example

Let’s say you found 3 groups of 4 elements, 0 of 6 elements, 2 of 12 elements and 1 of 16 elements.
The string that we are looking for would be the concatenation of all those numbers and thus 3021.

Submit your solution by creating a PullRequest against this repository and win an invitation to the kumite. We’re looking forward to getting to know you!

Happy Coding!

