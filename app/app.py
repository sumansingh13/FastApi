from fastapi import FastAPI, HTTPException
from app.schemas import postcreate
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_post = {1:{"title": "New Post", "content": "This is a new post."},
             2:{"title": "Another Post", "content": "This is another post."},
             3:{"title": "Yet Another Post", "content": "This is yet another post."},
             4:{"title": "Final Post", "content": "This is the final post."},
             5:{"title": "Last Post", "content": "This is the last post."},
             6:{"title": "Extra Post", "content": "This is an extra post."},
             7:{"title": "Bonus Post", "content": "This is a bonus post."},
             8:{"title": "Additional Post", "content": "This is an additional post."},
             9:{"title": "More Post", "content": "This is more post."},
             10:{"title": "Even More Post", "content": "This is even more post."}
}

#Query parameter

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_post.values())[:limit]
    return text_post

#http exceptions

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post not found")   
    return text_post[id]

#post creation and validation using pydantic model

@app.post("/posts") 
def create_post(post: postcreate) ->postcreate: #for better documentation so that it will show the request model in the docs
    new_post = {"title": post.title, "content": post.content}
    text_post[max(text_post.keys()) + 1] = new_post
    return new_post


