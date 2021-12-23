import requests
import random
import sys
from pprint import pprint


def user_info():
    user_id = int(input("Enter id: "))
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    max_id = max(r.json(), key=lambda item: item['id'])
    if 1 <= user_id <= max_id["id"]:
        for user in r.json():
            if user["id"] == user_id:
                pprint(user, sort_dicts=False)
    else:
        print(f"Wrong id. Max id: {max_id['id']}")


def user_posts():
    option = input("Choose action:\n1. Get user posts\n2. Get post by id\n: ")
    if option == '1':
        user_id = int(input("Enter user id: "))
        r = requests.get("https://jsonplaceholder.typicode.com/posts", {'userId': user_id})
        for post in r.json():
            print(f"id: {post['id']}  title: {post['title']}")
    elif option == '2':
        post_id = int(input("Enter post id: "))
        posts = requests.get("https://jsonplaceholder.typicode.com/posts", {'id': post_id})
        comments = requests.get("https://jsonplaceholder.typicode.com/comments", {'postId': post_id})
        comment_ids = []
        for post in posts.json():
            for comment in comments.json():
                comment_ids.append(comment["id"])
            result = {'id': post['id'], 'title': post['title'], 'text': post['body'],
                      'comments': len(comment_ids), 'comment_ids': comment_ids}
            pprint(result, sort_dicts=False)
    else:
        print("Wrong input")


def todo_list():
    option = input("Choose action:\n1. Get uncompleted tasks\n2. Get completed tasks\n: ")
    if option == '1':
        uncompleted = []
        r = requests.get("https://jsonplaceholder.typicode.com/todos", {"completed": "false"})
        for task in r.json():
            uncompleted.append(task["title"])
        pprint(uncompleted)
    elif option == '2':
        completed = []
        r = requests.get("https://jsonplaceholder.typicode.com/todos", {"completed": "true"})
        for task in r.json():
            completed.append(task["title"])
        pprint(completed)
    else:
        print("Wrong input")


def get_url():
    imgs = requests.get("https://jsonplaceholder.typicode.com/photos")
    max_id = max(imgs.json(), key=lambda item: item['id'])
    img_id = random.randint(1, max_id['id'])
    for img in imgs.json():
        if img['id'] == img_id:
            return img['url']


def start():
    action = input("Choose action:\n1. Get user info\n2. Get posts\n3. Get ToDo list\n4. Get picture URL\n"
                   "5. Exit\n: ")
    if action == "1":
        user_info()
    elif action == "2":
        user_posts()
    elif action == "3":
        todo_list()
    elif action == "4":
        print(get_url())
    elif action == "5":
        sys.exit()
    else:
        print("Wrong input. Please, try again")
        start()


start()