# (Attempt #1) Teaching a Neural Network to Solve Free Flow Puzzles

![image](https://github.com/user-attachments/assets/3f85b130-d897-46a9-8a8a-f25bde2b8dd9)


To play Free Flow, connect matching colors with a pipe to create a Flow®. Pair all colors and cover the entire board to solve each puzzle. Ensure the entire board is filled with pipes that do not cross or overlap, Successfully connect all colors and cover the board to complete the puzzle. Enjoy the challenge of creating your Flow!

## Collecting data

![image](https://github.com/user-attachments/assets/c326757e-bfca-4443-847b-cbf57cf78105)

I discovered a site with solutions for all levels of Flow Free® and downloaded the solutions for various grid sizes (5x5 to 9x9) in regular, green, bonus, and blue packs, plus an additional 150 levels for the 6x6 grid.

For training, I chose the 6x6 images and now have 270 of them. Initially, I considered sampling equally spaced points from the images and converting those values to a range of 1-n (where n is the number of different colors). However, the RGB values in the images were not uniform. Applying K-Means clustering solved the issue and allowed me to convert the images into usable data.

![image](https://github.com/user-attachments/assets/31250c5d-8623-47bf-a3b1-f6613dd9e896) ![image](https://github.com/user-attachments/assets/e82bd641-1aa2-4217-b7ac-6ce4554ab4e8)


There are multiple levels, like 5x5, 6x6, 7x7, 8x8, and some irregular sizes like 5x7 and 6x9. For this attempt I used the 6*6, 270 patterns which turn out to be a very small amount (I think). The Result was not satisfying as expected.



## Want To Try It?

Clone the repository

```
cd Web
```
```
npm install
```

```
nodemon app.js
```

# What's Next

This was a supervised learning approach, and next, I'll explore other machine learning methods. I'll also experiment with different grid sizes, rather than focusing solely on the 6x6 grid as I did for training.
