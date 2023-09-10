import numpy as np
import matplotlib.pyplot as plt


# Read the twelve-column text file
data = np.loadtxt(r'H:\netdefect\论文\Stress\P-Stress\all.txt')

# Calculate the probability density for each column
num_cols = data.shape[1]  # Get the number of columns

# Define the bin width
bin_width = 0.5
x_range = (0, 50)
# Calculate the maximum value among all columns
max_value = np.max(data)

# Calculate the number of bins based on the maximum value and bin width
num_bins = int(np.ceil(max_value / bin_width))

# Create an array to store the density results
density = np.zeros((num_bins, num_cols + 1))

# Calculate the probability density for each column
for i in range(num_cols):
    col_data = data[:, i]  # Extract column data

    # Calculate the histogram of the column data
    hist, bin_edges = np.histogram(col_data, bins=num_bins, range=(0, max_value))

    # Calculate the midpoints of the bins
    bin_midpoints = (bin_edges[1:] + bin_edges[:-1]) / 2

    # Store the density results in the array
    density[:, i + 1] = hist / np.sum(hist)
    density[:, 0] = bin_midpoints

# Plot the density results
plt.figure()

for i in range(num_cols):
    plt.plot(density[:, 0], density[:, i + 1], label=f'Column {i + 1}')

plt.xlabel('Midpoints')
plt.ylabel('Probability Density')
plt.legend()
plt.xlim(x_range)
plt.grid(True)
plt.show()

# Save the density results to a text file
np.savetxt(r'H:\netdefect\论文\Stress\P-Stress\density_all.txt', density, delimiter='\t')
