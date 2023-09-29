import json
from datetime import datetime
import pytz
import urllib.parse
import streamlit as st

# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]

# 投稿を管理するクラス
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
        self.good = 0
        self.bad = 0

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp,
            "good": self.good,
            "bad": self.bad,
        }

# 各投稿を格納するリスト
posts = []

def check_post_content(title, content):
    # 禁止ワードが含まれているかチェック
    for word in banned_words:
        if word in title or word in content:
            st.warning("禁止ワードが含まれています！")
            return None
    return Post(title, content)

def save_post(post):
    with open('posts.json', 'a') as file:
        file.write(json.dumps(post.to_dict()))
        file.write('\n')

def load_posts():
    loaded_posts = []
    with open('posts.json', 'r') as file:
        lines = file.readlines()
        for line in lines:
            post_dict = json.loads(line.strip())
            post = Post(post_dict["title"], post_dict["content"])
            post.timestamp = post_dict["timestamp"]
            post.good = post_dict["good"]
            post.bad = post_dict["bad"]
            loaded_posts.append(post)
    return loaded_posts

def main():
    st.title("掲示板アプリ")

    # 新規投稿の入力
    new_post_content = st.text_area("管理者以外記述厳禁", height=100)
    new_post_title = st.text_input("ページ")

    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:
        new_post = check_post_content(new_post_title, new_post_content)
        if new_post:
            posts.append(new_post)
            save_post(new_post)

    # 投稿一覧を表示
    loaded_posts = load_posts()
    if not loaded_posts:
        st.info("まだ投稿がありません。")
    else:
        for i, post in enumerate(loaded_posts, start=1):
            # 各タイトルにリンクを付けて表示
            post_url = f"<a href='https://maichan-bord-{urllib.parse.quote(post.title)}.streamlit.app'>{post.title}</a>"
            st.subheader(f"{i}. {post.content}")
            st.write(post.timestamp)  # タイムスタンプを表示

            # GoodボタンとBadボタンを追加
            col1, col2 = st.columns(2)
            good_button = col1.button(f"Good ({post.good})", key=f"good_{post.title}")
            bad_button = col2.button(f"Bad ({post.bad})", key=f"bad_{post.title}")
            if good_button:
                post.good += 1
            if bad_button:
                post.bad += 1

            # 評価カウンターを表示
            st.write(f"Good: {post.good}, Bad: {post.bad}")

            st.markdown(post_url, unsafe_allow_html=True)
            st.markdown("---")

if __name__ == "__main__":
    main()
