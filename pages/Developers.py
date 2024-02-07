# developers.py

import streamlit as st

def show():
    st.title("Meet the Developers")
    
    # Developer 1
    st.write(
        f"""
        <div style="margin-bottom: 40px;">
            <img src="https://avatars.githubusercontent.com/u/105744567?v=4" alt="Suraj Shinde" style="width: 100px; height: 100px; border-radius: 50%;">
            <div style="display: inline-block; vertical-align: middle;">
                <h3>Suraj Shinde</h3>
                <p><strong>GitHub:</strong> <a href="https://github.com/Suraj3240">Suraj3240</a></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Developer 2
    st.write(
        f"""
        <div style="margin-bottom: 40px;">
            <img src="https://avatars.githubusercontent.com/u/116277146?v=4" alt="Aditya Repe" style="width: 100px; height: 100px; border-radius: 50%;">
            <div style="display: inline-block; vertical-align: middle;">
                <h3>Aditya Repe</h3>
                <p><strong>GitHub:</strong> <a href="https://github.com/AdityaRepe">AdityaRepe</a></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Developer 3
    st.write(
        f"""
        <div style="margin-bottom:40px;">
            <img src="https://avatars.githubusercontent.com/u/100074372?v=4" alt="Ansh Shah" style="width: 100px; height: 100px; border-radius: 50%;">
            <div style="display: inline-block; vertical-align: middle;">
                <h3>Ansh Shah</h3>
                <p><strong>GitHub:</strong> <a href="https://github.com/AnshShah77">AnshShah77</a></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        f"""
        <div style="text-align: center;">
            <h3>Designed during 6 hours Datathon D2K</h3>
            <p><strong>GitHub:</strong> <a href="https://github.com/Suraj3240/D2K_OverReact">D2K_OverReact</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    show()
