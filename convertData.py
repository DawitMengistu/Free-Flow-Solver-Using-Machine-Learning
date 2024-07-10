from PIL import Image, ImageDraw, ImageEnhance

import numpy as np
from sklearn.cluster import KMeans


for f in range(30):
    # Load an image from file
    image_path = 'data/blue_pack/66/' + str(30 + f) + '.jpg'
    img = Image.open(image_path)

    # Convert image to numpy array
    img_array = np.array(img)

    # Reshape the array to a 2D array of pixels (rows) by RGB values (columns)
    reshaped_array = img_array.reshape((-1, 3))

    # Perform K-Means clustering
    num_clusters = 10  # Example number of clusters
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    labels = kmeans.fit_predict(reshaped_array)

    # Replace pixel values with cluster centers
    clustered_pixels = kmeans.cluster_centers_[labels]

    # Reshape back to the original image shape
    clustered_img_array = clustered_pixels.reshape(
        img_array.shape).astype(np.uint8)

    # Create PIL image from numpy array
    clustered_img = Image.fromarray(clustered_img_array)

    # Get a drawing context on the image
    draw = ImageDraw.Draw(clustered_img)

    x0, y0 = 35, 29
    ratio = 50
    col = []
    arr = [["" for _ in range(6)] for _ in range(6)]
    index = 1
    for g in range(6):
        for i in range(6):
            x = x0 + i*ratio
            y = y0 + g*ratio
            # draw.point((x, y), fill=(255, 255, 255))
            rgb_value = str(clustered_img.getpixel((x, y)))
            if rgb_value not in col:
                col.append(rgb_value)
            arr[g][i] = col.index(rgb_value)

    # Save or display the clustered image
    # clustered_img.show()
    # print(arr)

    def update_paths(matrix, ind):
        rows = len(matrix)
        cols = len(matrix[0])

        # Create a new matrix to store the updated values
        updated_matrix = [[matrix[i][j]
                           for j in range(cols)] for i in range(rows)]

        # Count occurrences of each number (excluding zeros)
        num_count = {}

        # Iterate through each element in the matrix
        for i in range(rows):
            for j in range(cols):
                current_value = matrix[i][j]

                # Count identical neighbors
                identical_neighbors = 0

                # Check top neighbor
                if i > 0 and matrix[i - 1][j] == current_value:
                    identical_neighbors += 1

                # Check bottom neighbor
                if i < rows - 1 and matrix[i + 1][j] == current_value:
                    identical_neighbors += 1

                # Check left neighbor
                if j > 0 and matrix[i][j - 1] == current_value:
                    identical_neighbors += 1

                # Check right neighbor
                if j < cols - 1 and matrix[i][j + 1] == current_value:
                    identical_neighbors += 1

                # Update the value based on the number of identical neighbors
                if identical_neighbors != 2:
                    updated_matrix[i][j] += 1
                else:
                    updated_matrix[i][j] = 0
                # Check if any number (excluding zeros) appears more than twice
        # Count occurrences of each number (excluding zeros)
        if current_value != 0:
            if current_value in num_count:
                num_count[current_value] += 1
            else:
                num_count[current_value] = 1

        # Check if any number (excluding zeros) appears more than twice
        for num, count in num_count.items():
            if count > 2:
                print(
                    f"Number {num} appears more than twice in the matrix (excluding zeros). At image", ind)
                print(updated_matrix, count)
                exit()

        return updated_matrix

    # Example usage:
    # matrix = [
    #     [0, 0, 0, 0, 1, 0],
    #     [0, 2, 1, 1, 1, 0],
    #     [0, 2, 1, 3, 0, 0],
    #     [0, 2, 1, 3, 0, 4],
    #     [0, 2, 3, 3, 0, 4],
    #     [0, 0, 0, 0, 0, 4]
    # ]

    updated_matrix = update_paths(arr, f)
    # for row in arr:
    #     print(row)

    # for row in updated_matrix:
    #     print(row)

    # Convert the list of lists to a NumPy array
    np_array1 = np.array(updated_matrix)
    np_array2 = np.array(updated_matrix)

    # Save the NumPy array to a file using np.save
    np.save('dsconverted/a-66-' + str(90 + 151 + f) + '.npy', np_array1)
    np.save('dsconverted/g-66-' + str(90 + 151 + f) + '.npy', np_array2)
    print("Done!", f)
    # Save or display the modified image
    # img.show()
