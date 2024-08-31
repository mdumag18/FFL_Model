import pandas as pd

# Load the CSV files
qb_stats = pd.read_csv('/Users/matti/downloads/FantasyPros_Fantasy_Football_Statistics_QB.csv')
qb_advanced_stats = pd.read_csv('/Users/matti/downloads/FantasyPros_Fantasy_Football_Advanced_Stats_Report_QB.csv')

# Assume 'Player' is the common key column
merged_qb = pd.merge(qb_stats, qb_advanced_stats, on='Player')
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
# Drop duplicate columns if needed
merged_qb.drop(columns=['Rank_y'], inplace=True)
merged_qb.rename(columns={'Rank_x': 'Rank'}, inplace=True)

merged_qb.drop(columns=['ATT_y'], inplace=True)
merged_qb.rename(columns={'ATT_x': 'PASS_ATT'}, inplace=True)

merged_qb.drop(columns=['PCT_y'], inplace=True)
merged_qb.rename(columns={'PCT_x': 'PCT'}, inplace=True)

merged_qb.drop(columns=['YDS_y'], inplace=True)
merged_qb.rename(columns={'YDS_x': 'Pass_YDS'}, inplace=True)

merged_qb.drop(columns=['Y/A_y'], inplace=True)
merged_qb.rename(columns={'Y/A_x': 'Y/A'}, inplace=True)

merged_qb.drop(columns=['G_y'], inplace=True)
merged_qb.rename(columns={'G_x': 'G'}, inplace=True)

merged_qb.rename(columns={'ATT.1': 'Rush_ATT'}, inplace=True)
merged_qb.rename(columns={'YDS.1': 'Rush_YDS'}, inplace=True)
merged_qb.rename(columns={'TD.1': 'Rush_TD'}, inplace=True)

# Save into consolidated csv
merged_qb.to_csv('/Users/matti/PycharmProjects/FFL_Model/all_qb_stats.csv', index=False)

# Preview the cleaned DataFrame
print(merged_qb.head())
