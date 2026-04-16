import streamlit as st
import os

# 1. 设置网页标题和图标
st.set_page_config(page_title="HHH电影看板", page_icon="🎬")

st.title("🎬 我的私人电影海报墙")
st.write("这是用 Python 自动抓取的最新资源预览：")

# 2. 指定图片存放的文件夹
img_dir = 'movie_posters'

if os.path.exists(img_dir):
    # 获取文件夹里所有的图片文件名
    images = [f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.png'))]

    if not images:
        st.warning("文件夹里还没图片，快去运行之前的爬虫代码！")
    else:
        # 3. 用网格布局显示图片（每行 3 张）
        cols = st.columns(3)
        for i, img_name in enumerate(images):
            with cols[i % 3]:
                # 显示图片
                img_path = os.path.join(img_dir, img_name)
                st.image(img_path, use_container_width=True)
                # 显示标题（去掉文件名末尾的 .jpg）
                st.caption(img_name.replace('.jpg', ''))
else:
    st.error(f"找不到文件夹 {img_dir}，请确认路径是否正确。")

# 4. 侧边栏加点互动
st.sidebar.header("控制面板")
if st.sidebar.button("刷新数据"):
    st.rerun()

st.sidebar.write("---")
st.sidebar.info("建议配合 Xiaomi 17 Ultra 浏览器食用更佳。")
