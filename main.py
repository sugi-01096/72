import math
import streamlit as st
import pandas as pd

st.text("ヤッハロー")
#         ↑ガハマすこ

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
st.title("舞チャン")

# 新しい投稿の作成
st.header("新しい投稿を作成")
title = st.text_input("スレタイトル")
content = st.text_area("内容")
if st.button("作成！"):
    create_post(title, content)
    st.success("作成完了！")

# 投稿一覧の表示
st.header("スレタイトル一覧")
if len(posts) == 0:
    st.info("まだ投稿はありません")
else:
    show_posts()

