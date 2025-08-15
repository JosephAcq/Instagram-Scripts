import pandas as pd

df = pd.read_csv("final.csv")  # Replace with your actual filename

filtered = df[
    (df['isPrivate'] == True) &
    (df['followingCount'] > df['followersCount'])
]

filtered[['profileUrl']].to_csv("filtered_users.csv", index=False)

