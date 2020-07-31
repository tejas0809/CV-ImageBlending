# "CIS581: Computer Vision and Computational Photography" - "Project 1B: Image Gradient Blending"
# Name: Tejas Srivastava

# Objective
The objective of the assignment was to implement Image Blending to seamlessly blend an object from a source image into a target image. 

# Results
![alt text](https://github.com/tejas0809/CV-ImageBlending/blob/master/1_background.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-ImageBlending/blob/master/1_source.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-ImageBlending/blob/master/1_output.png?raw=true)
<br>
![alt text](https://github.com/tejas0809/CV-ImageBlending/blob/master/2_background.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-ImageBlending/blob/master/2_source.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-ImageBlending/blob/master/2_output.jpeg?raw=true)






# File Structure:
- Readme.txt
- script.py 
- seamlessCloningPoisson.py
- createMask.py
- drawMask.py
- getIndexes.py
- getCoefficientMatrix.py
- getSolutionVect.py
- maskImage.py
- reconstructImg.py
- 1_background.jpg (Given)
- 1_source.jpg (Given)
- 1_mask.png (Given)
- 1_output.png - Generated (Minion + Ben Franklin on the bench)
- 2_background.jpg 
- 2_source.jpg
- 2_mask.png
- 2_output.jpeg



# To run the project for the given image, simpy run script.py. 
This will open a pop up to select the mask for the source image, which can then be done by clicking the boundary points of the source image to create the mask. 

# To run the code for other images, 
change the file name as the source image in line number 10 and line number 12 of script.py. Also, update the background image name in line number 11 of script.py.
OffsetX and Offset Y would also have to be changed according to the images selected and the position of the source image in the target image.   

# Description of files:
-script.py: runs the code by reading the source and target images, setting the offsets and calling createMask and seamlessCloningPoisson. 
-getIndexes.py: indexes the replacement pixels in the mask such that each element in x represents one replacement pixel
-getCoefficientMatrix.py: Computes the NxN (N is the number of replacement pixels) matrix A to get the intensities of replacement pixels by solving Ax=b. 
-getSolutionVect.py: generates the solution vector b in the linear system Ax = b.
-seamlessCloningPoisson.py: solves the equation Ax=b, by calling all the above functions for all three channels of the images and further calls reconstructImg
-reconstructImg : basically replaces the calculated replacement pixel intensities in the target image
-createMask.py: used to create the mask for the image    





