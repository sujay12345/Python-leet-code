class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc]==newColor:
            return image
        self.fill(image,sr,sc, image[sr][sc],newColor)
        return image
    def fill(self,image,sr,sc,color,newColor):
        if (sr <0 or  sr>= len(image) or sc < 0  or sc >=len(image[0]) or image[sr][sc]!= color):
            return
        image[sr][sc]=newColor
        self.fill(image,sr-1,sc,color,newColor)
        self.fill(image,sr+1,sc,color,newColor)
        self.fill(image,sr,sc-1,color,newColor)
        self.fill(image,sr,sc+1,color,newColor)
        
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
        
