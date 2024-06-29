import pandas as pd

def count_occurrences_in_csv(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Select the first three columns
    selected_columns = df.iloc[:, 0:3]
    
    # Initialize an empty dictionary to store occurrences
    occurrences = {}
    
    # Iterate through each selected column
    for column in selected_columns:
        # Get value counts for each column, dropping NaN values
        column_occurrences = df[column].value_counts(dropna=True).to_dict()
        
        # Update the main occurrences dictionary
        for key, value in column_occurrences.items():
            if key in occurrences:
                occurrences[key] += value
            else:
                occurrences[key] = value
    
    return occurrences

# Example usage with the provided file
file_path = 'pies/data/second_type/sample_2-buy.csv'
occurrences_dict = count_occurrences_in_csv(file_path)
print(occurrences_dict)
