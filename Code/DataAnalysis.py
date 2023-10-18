import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def find_cell_number_at_timestep(df, i):

    return len(df[df['Time'] == i])

def find_cell_numbers(df):

    Times = df['Time'].unique()
    Cells = np.empty(Times.shape)
    for i in Times:
        Cells[i] = find_cell_number_at_timestep(df, i)
    
    return Times, Cells

def calculate_cell_number_increments(Cells):
    return np.append(0, np.diff(Cells))

def process_data(raw_data_path, filename):
    df = pd.read_csv(raw_data_path)

    Times, Cells = find_cell_numbers(df)
    Cell_Increments = calculate_cell_number_increments(Cells)

    Data = {'Time': Times, 'Cells': Cells, 'Cell Increments': Cell_Increments}
    processed_df = pd.DataFrame(Data)

    processed_data_path = 'Results/AnalysisData/' + filename + '.csv'
    processed_df.to_csv(processed_data_path)

    create_metadata(processed_df, raw_data_path, filename)

    return

def create_metadata(df, raw_data_path, filename):

    with open('Results/AnalysisData/' + filename + '.md', 'w') as f:

        f.write(f'# ' + filename + ' Metadata\n')

        f.write('## General Information\n\n')
        f.write('- Raw data from: ' + raw_data_path + '\n')
        f.write('- Data processing in: Code/DataAnalysis.py\n')
        f.write('- Researcher: Simon Schardt\n')
        f.write('- Contact: simon.schardt@uni-wuerzburg.de\n')

        f.write('## DataFrame Structure\n')
        f.write(f'- Number of Rows: {df.shape[0]}\n')
        f.write(f'- Number of Columns: {df.shape[1]}\n')
        f.write('- Columns:\n')
        for column in df.columns:
            f.write(f'  - {column}\n')

        f.write('\n## Summary Statistics\n')
        summary = df.describe()
        f.write(summary.to_markdown())

        f.write('\n## Additional Information\n')
        f.write('Python > Julia\n')

    return

process_data('Data/ExampleData.csv', 'CellNumbers')