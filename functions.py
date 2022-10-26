import json

def load_posts(path='posts.json'):
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)

def search_post(substr):
    posts_found = []
    posts =  load_posts()
    for post in posts:
        if substr.lower() in post['content'].lower():
            posts_found.append(post)
    return posts_found


def save_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]

    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        return
    picture.save(f'./uploads/images/{filename}')
    return f'uploads/images/{filename}'

def save_post_to_json(posts,path='posts.json'):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(posts, file, ensure_ascii=False)

def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_post_to_json(posts)
