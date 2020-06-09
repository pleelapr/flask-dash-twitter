import pandas as pd
import pprint as pp
import numpy as np
import re
import pandasql as psql

def extract_retweet_from(df):
    for i in range(len(df)):
        m = re.search('RT @(.+?):', df.loc[i, 'text'])
        if m:
            df.loc[i, 'retweet_from_user'] = m.group(1)
        else:
            df.loc[i, 'retweet_from_user'] = np.nan
    return df

# Rank row by rank_col and get top 10 row of index_col
def get_rank_col_by_index_col(df, rank_col, index_col, num_result=10):
    output = df.sort_values(by=[rank_col], ascending=False)
    output.drop_duplicates(subset=[index_col], keep='first', inplace=True)
    output = output.loc[:, [index_col, rank_col]].reset_index(drop=True)
    output = output.head(num_result)
    # print(output)
    return output

def get_top_count_by(df, groupby_col, num_result=10):
    query = "SELECT {}, COUNT(*) AS count FROM df GROUP BY {} ORDER BY count DESC".format(groupby_col, groupby_col)
    output = psql.sqldf(query).head(num_result)
    # output[groupby_col] = output[groupby_col].str.slice(0,30)
    # print(output)
    return output

def get_histogram_of_col(df, col_name, num_bin=10):
    series = df[col_name]
    count, division = np.histogram(series, density=True, bins=num_bin)
    return count, division



