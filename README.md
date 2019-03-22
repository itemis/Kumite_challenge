# The challenge to get to the fabulous coding Kumite

Given is a file data.txt.

Inside the file you will find balanced lines of comma separated random numbers, which you should treat as a grid of numbers. (1000 x 1000 numbers)

The challenge is to find groups of equal numbers - as this would be to easy, we are only searching for groups of 4, 6, 12 and 16 elements.

For instance a group with 8 elements should be ignored.

## Rules

A group must be across multiple lines and columns and form a rectangle

![](/images/img-4-red-horizontal.png)

This group does not span across multiple lines – so it’s not a group that we are searching for.

![](/images/img-6-box-vertical.png)

![](/images/img-green-and-red.png)

This groups span across multiple lines and columns. They are groups of 6 elements and form ractangles – so groups we are searching for.

![](/images/img-red-3-3.png)

This is a group of 9 elements. As we are only searching for groups of 4, 6 ,12 and 16, this one should be ignored. This implies that this area cannot match anymore as a group of 6 or 4.

![](/images/img-green-and-red.png)

You could say there is a group of 12 or you say there is a group of 6 and a group of 8. Without having strict rules for this situation, there is room for interpretation and we end up in different results.

So we always proceed from left to right starting in the upper left corner and going right wins over going down. The result would be a group of 6 that we count and a group of 8 that we ignore.

![](/images/img-blue-box.png)

In this case we are facing two valid groups of 6 elements that we count.

Groups must not overlap!

![](/images/img-overlap.png)

The valid group is the green one. The red one is not valid since it overlaps.

Please keep track how many groups of which size you found.

The goal would be to create a string that holds those informations.

## Example

We have 3 groups of 4 elements, 0 of 6 elements, 2 of 12 elements and 1 of 16 elements.

The string that we are hunting for would be the concatenation of all those numbers.

3021 would be the number we are searching for.

Please take your code, create a PullRequest against this repository and use your result to get an invitation to the kumite. 

Happy Coding!
