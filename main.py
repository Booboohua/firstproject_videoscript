import streamlit as st
from videoscript import generate_script

st.title("🎬视频脚本生成器")

with st.sidebar:
    openai_api_key=st.text_input("请输入OpenAI API秘钥",type="password")
    st.markdown("[如何获取OpenAI API密钥](https://platform.deepseek.com/api_keys)")

subject=st.text_input("💡请输入视频的主题")
video_length=st.number_input("请输入视频大致时长（单位：分钟）",min_value=0.1,step=0.1)
creativity=st.slider("🌠️请输入视频脚本的创造力（数字越小说明更严谨，数字越大说明更多样)",value=0.5,min_value=0.1,max_value=1.0,step=0.1)

submit=st.button("生成脚本")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit and not video_length >0.1:
    st.info("输入视频时长需要大于0.1分钟")
if submit:
    with st.spinner("AI正在思考中，请稍后"):
         title,script=generate_script(subject,video_length,creativity,openai_api_key)
    st.success("视频脚本已经生成")
    st.subheader("🔥标题：")
    st.write(title)
    st.subheader("📚视频脚本：")
    st.write(script)


