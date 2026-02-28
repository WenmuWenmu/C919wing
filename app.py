import streamlit as st
import streamlit.components.v1 as components

# 设置页面标题
st.title("C919机翼选材")

# 读取本地 HTML 文件内容
def load_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        st.error("未找到 HTML 文件，请检查文件路径！")
        return ""
    except Exception as e:
        st.error(f"读取文件出错：{str(e)}")
        return ""

# 加载并展示 HTML 内容
html_content = load_html_file("智能设计优化平台-C919机翼选材.html")  # 替换为你的 HTML 文件名
if html_content:
    # 设置展示区域的宽度和高度（可根据需要调整）
    components.html(html_content, height=800, scrolling=True)