import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def find_cell_number_at_timestep(df, i):
    """
    Finds the number of cells at a given timestep.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the raw data.
    i (int): Timestep to find the number of cells for.

    Returns:
    int: Number of cells at the given timestep.
    """
    return len(df[df['Time'] == i])

def find_cell_numbers(df):
    """
    Finds the number of cells at each timestep.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the raw data.

    Returns:
    tuple: Two numpy arrays containing the timesteps and the number of cells at each timestep.
    """
    Times = df['Time'].unique()
    Cells = np.empty(Times.shape)
    for i in Times:
        Cells[i] = find_cell_number_at_timestep(df, i)
    
    return Times, Cells

def calculate_cell_number_increments(Cells):
    """
    Calculates the increments in the number of cells.

    Parameters:
    Cells (numpy.ndarray): Array containing the number of cells at each timestep.

    Returns:
    numpy.ndarray: Array containing the increments in the number of cells.
    """
    return np.append(0, np.diff(Cells))

def process_data(raw_data_path, filename):
    """
    Processes the raw data and saves the results to a CSV file.

    Parameters:
    raw_data_path (str): Path to the raw data file.
    filename (str): Name of the file to save the processed data to.

    Returns:
    None
    """
    df = pd.read_csv(raw_data_path)

    # Find cell numbers and calculate increments
    Times, Cells = find_cell_numbers(df)
    Cell_Increments = calculate_cell_number_increments(Cells)

    # Create DataFrame
    Data = {'Time': Times, 'Cells': Cells, 'Cell Increments': Cell_Increments}
    processed_df = pd.DataFrame(Data)

    # Save DataFrame
    processed_data_path = 'Results/AnalysisData/' + filename + '.csv'
    processed_df.to_csv(processed_data_path)

    # Create metadata corresponding to the processed data
    create_metadata(processed_df, raw_data_path, filename)

    return

def create_metadata(df, raw_data_path, filename):
    """
    Creates a metadata file for the processed data.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the processed data.
    raw_data_path (str): Path to the raw data file.
    filename (str): Name of the file to save the metadata to.

    Returns:
    None
    """
    with open('Results/AnalysisData/' + filename + '.md', 'w') as f:
        # Write header
        f.write(f'# ' + filename + ' Metadata\n')

        # Write general information
        f.write('## General Information\n\n')
        f.write('- Raw data from: ' + raw_data_path + '\n')
        f.write('- Data processing in: Code/DataAnalysis.py\n')
        f.write('- Researcher: Simon Schardt\n')
        f.write('- Contact: simon.schardt@uni-wuerzburg.de\n')

        # Write DataFrame structure
        f.write('## DataFrame Structure\n')
        f.write(f'- Number of Rows: {df.shape[0]}\n')
        f.write(f'- Number of Columns: {df.shape[1]}\n')
        f.write('- Columns:\n')
        for column in df.columns:
            f.write(f'  - {column}\n')

        # Write summary statistics
        f.write('\n## Summary Statistics\n')
        summary = df.describe()
        f.write(summary.to_markdown())

        # Write additional information
        f.write('\n## Additional Information\n')
        f.write('Python > Julia\n')

    return

process_data('Data/ExampleData.csv', 'CellNumbers')