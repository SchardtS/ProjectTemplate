import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_cell_numbers(file):
    """
    Plots the number of cells over time and the increments in the number of cells over time.

    Parameters:
    file (str): Path to the file containing the processed data.

    Returns:
    None
    """

    # Extract data from the file
    df = pd.read_csv(file)
    Times, Cells = df['Time'], df['Cells']
    Cell_Increments = df['Cell Increments']

    # Choose different colors for the two plots
    color1 = 'tab:red'
    color2 = 'tab:blue'

    # Plot cell numbers over time with y-axis on the left
    plt.figure(figsize=(10, 6))
    plt.plot(Times, Cells, label='Cells', color=color1)
    plt.ylabel('cell number', color=color1, fontsize=14)
    plt.yticks(color=color1, fontsize=14)
    plt.xlabel('time', fontsize=14)

    # Plot cell increments over time with y-axis on the right
    plt.twinx()
    plt.plot(Times, Cell_Increments, label='Cell Increments', color=color2)
    plt.ylabel('cell number increments', color=color2, fontsize=14)
    plt.yticks(color=color2, fontsize=14)

    # Save the figure as a PDF and PNG file
    plt.savefig('Results/Figures/CellNumbers.pdf', dpi=300, bbox_inches='tight', facecolor=None)
    plt.savefig('Results/Figures/CellNumbers.png', dpi=300, bbox_inches='tight', facecolor=None)

    return


def find_data_limits(df):
    """
    Finds the limits of the data in the DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the data.

    Returns:
    tuple: Four floats containing the minimum and maximum x and y values of the data.
    """
    x = df['x-Position'].to_numpy()
    y = df['y-Position'].to_numpy()
    r = df['Radius'].to_numpy()

    # Find the minimum and maximum values of x and y considering the radii of the cells
    x_min = np.min(x - r)
    x_max = np.max(x + r)
    y_min = np.min(y - r)
    y_max = np.max(y + r)

    return x_min, x_max, y_min, y_max


def plot_cell_clusters_at_timestep(file, timestep):
    """
    Plots the cell clusters at a given timestep.

    Parameters:
    file (str): Path to the file containing the data.
    timestep (int): Timestep to plot the cell clusters for.

    Returns:
    None
    """
    # Extract data from the file
    df = pd.read_csv(file)
    df = df[df['Time'] == timestep]

    x = df['x-Position'].to_numpy()
    y = df['y-Position'].to_numpy()
    r = df['Radius'].to_numpy()

    # Plot the cells as circles
    plt.figure(figsize=(10, 10))
    for i in range(len(x)):
        circle = plt.Circle((x[i], y[i]), r[i], color='k', fill=False)
        plt.gca().add_artist(circle)

    # Set the limits of the plot
    x_min, x_max, y_min, y_max = find_data_limits(df)
    plt.xlim(x_min*1.2, x_max*1.2)
    plt.ylim(y_min*1.2, y_max*1.2)
    plt.axis('equal')
    plt.axis('off')

    # Save the figure as a PDF and PNG file
    plt.savefig('Results/Figures/CellClusters_T=' + str(timestep) + '.pdf', dpi=300, bbox_inches='tight', transparent=True)
    plt.savefig('Results/Figures/CellClusters_T=' + str(timestep) + '.png', dpi=300, bbox_inches='tight', transparent=True)

    return

# Plot the number of cells over time and the increments in the number of cells over time
plot_cell_numbers('Results/AnalysisData/CellNumbers.csv')

# Plot the cell clusters at the given timesteps
Times = [0,24,48,72,96]
for T in Times:
    plot_cell_clusters_at_timestep('Data/ExampleData.csv', T)