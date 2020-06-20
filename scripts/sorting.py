import pandas as pd


def get_mac_duplicates():
	csv_df = pd.read_csv('file.csv', encoding='utf-8')
	shaw_df = csv_df.copy()
	comcast_df = csv_df.copy()
	shaw_df.drop(['Comcast'], axis=1, inplace=True)
	comcast_df.drop(["Shaw"], axis=1, inplace=True)
	shaw_df.rename(columns={"Shaw": "mac_address"}, inplace=True)
	comcast_df.rename(columns={"Comcast":"mac_address"}, inplace=True)
	duplicate_mac_df = pd.merge(shaw_df, comcast_df, on="mac_address", how="inner")
	duplicate_mac_df.to_csv('duplicates.csv', index=False)
