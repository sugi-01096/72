import math
import streamlit as st
import pandas as pd

st.text("Hello World!")


# 投稿データを保持するリスト
posts = []

# 投稿の作成
def create_post(title, content):
    posts.append({"title": title, "content": content})

# 投稿の表示
def show_posts():
    for post in posts:
        st.write(f"**{post['title']}**")
        st.write(post['content'])
        st.write('---')

# 掲示板アプリのタイトル
st.title("Bulletin Board App")

# 新しい投稿の作成
st.header("Create New Post")
title = st.text_input("Title")
content = st.text_area("Content")
if st.button("Create"):
    create_post(title, content)
    st.success("Post created successfully!")

# 投稿一覧の表示
st.header("Posts")
if len(posts) == 0:
    st.info("No posts yet.")
else:
    show_posts()

#ストリームリットアプリの起動
streamlit run app.py
#junnpei
