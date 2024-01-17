import requests

def count_words(subreddit, word_list, after=None, count_dict={}):
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                count = title.count(word.lower())
                if count > 0:
                    if word in count_dict:
                        count_dict[word] += count
                    else:
                        count_dict[word] = count
        
        after = data['data']['after']
        if after is not None:
            count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return
