import numpy as np

# Directory containing the .npy files
directory = 'path/to/your/npy/files'

# Initialize lists to hold the puzzles and answers
puzzles = []
answers = []

# Load each .npy file
for i in range(0):  # assuming you have 100 files named 1.npy, 2.npy, ..., 100.npy

    puzzle = np.load("ds/g-66-" + str(i) + ".npy")
    answer = np.load("ds/a-66-" + str(i) + ".npy")
    
    puzzles.append(puzzle)
    answers.append(answer)

# Convert lists to NumPy arrays
puzzles_array = np.array(puzzles)
answers_array = np.array(answers)


finalOutput = np.load("ds/g-66-" + str(i) + ".npy")
# Save the combined arrays to a single .npz file
np.savez('free_flow_ds.npz', puzzles=puzzles_array, answers=answers_array)

print("Data saved successfully!")
