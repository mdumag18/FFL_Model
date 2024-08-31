import pandas as pd

# Load the CSV files
rb_stats = pd.read_csv('/Users/matti/downloads/FantasyPros_Fantasy_Football_Statistics_RB.csv')
rb_advanced_stats = pd.read_csv('/Users/matti/downloads/FantasyPros_Fantasy_Football_Advanced_Stats_Report_RB.csv')

# Assume 'Player' is the common key column
merged_rb = pd.merge(rb_stats, rb_advanced_stats, on='Player')
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

# Drop duplicate columns if needed
merged_rb.drop(columns=['Rank_y'], inplace=True)
merged_rb.rename(columns={'Rank_x': 'Rank'}, inplace=True)

merged_rb.drop(columns=['ATT_y'], inplace=True)
merged_rb.rename(columns={'ATT_x': 'ATT'}, inplace=True)

merged_rb.drop(columns=['YDS_y'], inplace=True)
merged_rb.rename(columns={'YDS_x': 'YDS'}, inplace=True)

merged_rb.drop(columns=['REC_y'], inplace=True)
merged_rb.rename(columns={'REC_x': 'REC'}, inplace=True)

merged_rb.drop(columns=['TGT_y'], inplace=True)
merged_rb.rename(columns={'TGT_x': 'TGT'}, inplace=True)

merged_rb.drop(columns=['G_y'], inplace=True)
merged_rb.rename(columns={'G_x': 'G'}, inplace=True)

merged_rb.rename(columns={'YDS.1': 'REC_YDS'}, inplace=True)
merged_rb.rename(columns={'TD.1': 'REC_TD'}, inplace=True)
merged_rb.rename(columns={'YACON.1': 'REC_YACON'}, inplace=True)


# Save into consolidated csv
'''merged_rb.to_csv('/Users/matti/PycharmProjects/FFL_Model/all_rb_stats.csv', index=False)'''

# Preview the cleaned DataFrame
print(merged_rb.head())
