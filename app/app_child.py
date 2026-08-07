from fastapi import FastAPI, HTTPException


ReyApp = FastAPI()

text_posts = {
    1: {"title": "Debugging Tip", "content": "Print statements are great, but learning to use a proper debugger saves hours."},
    2: {"title": "Dev Humor", "content": "There are 10 types of people in the world: those who understand binary, and those who don't."},
    3: {"title": "Learning Goal", "content": "Focusing on mastering Docker and Kubernetes best practices this month."},
    4: {"title": "Clean Code", "content": "Functions should do one thing, do it well, and do it only."},
    5: {"title": "Quick Reminder", "content": "Don't forget to commit your code before ending your work session today!"},
    6: {"title": "Web Dev Note", "content": "CSS Grid is incredible for layout structures, while Flexbox shines for alignment within items."},
    7: {"title": "Database Tip", "content": "Always index foreign keys and columns that are frequently used in WHERE clauses."},
    8: {"title": "Coffee Thought", "content": "Coding is 10% writing syntax and 90% figuring out why it isn't working as expected."},
    9: {"title": "Tech Reflection", "content": "Refactoring old code is terrifying until unit tests pass completely green."},
    10: {"title": "Community Check-in", "content": "What was the very first programming language you learned?"}
}

# text_posts = {
#     1: {
#         "title": "Debugging Tip",
#         "content": "Print statements are great, but learning to use a proper debugger saves hours.",
#     },
#     2: {
#         "title": "Dev Humor",
#         "content": "There are 10 types of people in the world: those who understand binary, and those who don't.",
#     },
#     3: {
#         "title": "Learning Goal",
#         "content": "Focusing on mastering Docker and Kubernetes best practices this month.",
#     },
#     4: {
#         "title": "Clean Code",
#         "content": "Functions should do one thing, do it well, and do it only.",
#     },
#     5: {
#         "title": "Quick Reminder",
#         "content": "Don't forget to commit your code before ending your work session today!",
#     },
#     6: {
#         "title": "Web Dev Note",
#         "content": "CSS Grid is incredible for layout structures, while Flexbox shines for alignment within items.",
#     },
#     7: {
#         "title": "Database Tip",
#         "content": "Always index foreign keys and columns that are frequently used in WHERE clauses.",
#     },
#     8: {
#         "title": "Coffee Thought",
#         "content": "Coding is 10% writing syntax and 90% figuring out why it isn't working as expected.",
#     },
#     9: {
#         "title": "Tech Reflection",
#         "content": "Refactoring old code is terrifying until unit tests pass completely green.",
#     },
#     10: {
#         "title": "Community Check-in",
#         "content": "What was the very first programming language you learned?",
#     },
# }

@ReyApp.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        # return text_posts[:limit]
        return list(text_posts.values())[:limit]
    return text_posts

@ReyApp.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not Found")

    return text_posts.get(id)

# @ReyApp.get("/posts/{post_id}")
# def get_post(post_id: int):
#     if post_id not in text_posts:
#         raise HTTPException(status_code=404,detail="Post not Found")

#     return text_posts.get[post_id]