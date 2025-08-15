import json

# Load JSON data from files
with open("followers_1.json", "r") as f:
    followers_data = json.load(f)

with open("following.json", "r") as f:
    following_data = json.load(f)

# Extract usernames from followers
followers = {
    entry["string_list_data"][0]["value"]
    for entry in followers_data
    if "string_list_data" in entry and entry["string_list_data"]
}

# Extract usernames from following
following = {
    entry["string_list_data"][0]["value"]
    for entry in following_data["relationships_following"]
    if "string_list_data" in entry and entry["string_list_data"]
}

# Find who you're following that isn't following back
not_following_back = sorted(following - followers)

# Write the result to a file
with open("not_following_back.txt", "w") as outfile:
    outfile.write("Users you're following who don't follow you back:\n")
    for user in not_following_back:
        outfile.write(user + "\n")

print("Done. Check 'not_following_back.txt' for results.")
