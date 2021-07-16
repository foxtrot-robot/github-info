# Filename: main.py
# Purpose: Main source file.
try:
    import requests
    import json
    import os
    import urllib3
    # classes
    from logger import logger
except ImportError as e:
    print(f"Error catched {e}")
    print("Dependency's error please execute following line in your terminal")
    print("pip3 install -r requirements.txt")

with open('config.json') as file:
    config = json.load(file)

# Config
nick = config.get('username')

def fetch_user_data(username):
    r = requests.get(f"https://api.github.com/users/{username}")
    data = r.json()
    # JSON DATA

    login = data['login']
    id = data['id']
    node_id = data['node_id']
    avatar_url = data['avatar_url']
    url = data['url']
    followers_url = data['followers_url']
    following_url = data['following_url']
    gists_url = data['gists_url']
    starred_url = data['starred_url']
    subscriptions_url = data['subscriptions_url']
    organizations_url = data['organizations_url']
    repos_url = data['repos_url']
    events_url = data['events_url']
    received_events_url = data['received_events_url']
    type = data['type']
    company = data['company']
    if company == 'null':
        company = 'Unspecified'
    blog = data['blog']
    location = data['location']
    email = data['email']
    if email == 'null':
        email = 'Unspecified'
    hireable = data['hireable']
    if hireable == 'null':
        hireable = 'Unspecified'
    bio = data['bio']
    #twitter = data['twitter_username']
    public_repos = data['public_repos']
    public_gists = data['public_gists']
    followers = data['followers']
    following = data['following']
    created_at = data['created_at']
    updated_at = data['updated_at']
    # Logger

    logger.find(f"Login: {login}")
    logger.find(f"ID: {id}")
    logger.find(f"Node ID: {node_id}")
    logger.find(f"Avatar URL: {avatar_url}")
    logger.find(f"URL: {url}")
    logger.find(f"Followers URL: {followers_url}")
    logger.find(f"Following URL: {following_url}")
    logger.find(f"Gists URL: {gists_url}")
    logger.find(f"Starred URL: {starred_url}")
    logger.find(f"Subscriptions URL: {subscriptions_url}")
    logger.find(f"Organizations URL: {organizations_url}")
    logger.find(f"Repos URL: {repos_url}")
    logger.find(f"Events URL: {events_url}")
    logger.find(f"Received Events URL: {received_events_url}")
    logger.find(f"Type: {type}")
    if company == 'Unspecified':
        logger.error("Company: unspecified")
    logger.find(f"Blog: {blog}")
    logger.find(f"Location: {location}")
    if email == 'Unspecified':
        logger.error("Email: unspecified")
    logger.find(f"Public Repos: {public_repos}")
    logger.find(f"Public Gists: {public_gists}")
    logger.find(f"Followers: {followers}")
    logger.find(f"Following: {following}")
    logger.find(f"Created at: {created_at}")
    logger.find(f"Updated at: {updated_at}")
if __name__ == "__main__":
    fetch_user_data(nick)