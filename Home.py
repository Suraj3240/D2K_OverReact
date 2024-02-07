import streamlit as st

def main():
    st.set_page_config(page_title="TextLoc Lens", page_icon=":earth_americas:")

    st.title("TextLoc Lens")
    st.markdown("""
        <div style="display: flex; align-items: center;">
            <div>
                Your tool for exploring textual landscapes and uncovering hidden geographical insights!
            </div>
            <div style="margin-left: auto;">
                <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3VxZ3duaWNwcTZuZnh1MXY0ZjRweWRoeHYwdXZld290aXVteWhiZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/41SIOpeqCfIru/giphy.gif" alt="Animated Globe" width="100" height="100">
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write(
        """
        TextLoc Lens is a user-friendly web application designed to analyze text input and extract contextual locations. 
        By leveraging advanced natural language processing (NLP) techniques, TextLoc Lens identifies locations mentioned 
        within the text and plots them on an interactive map, providing users with a visual representation of the geographical 
        context embedded in their textual data.
        """
    )

    if st.button("Explore TextLoc Lens"):
        st.page_link("pages\Analysis.py", label="Get Started")

    st.write(
        """
        <div style="display: flex; align-items: center; margin-top:150px">
            <div>
                Designed during 6 hours Datathon D2K
            </div>
            <div style="margin-left: auto;">
                <a href="https://github.com/Suraj3240/D2K_OverReact" target="_blank">   
                    <img src="https://img.shields.io/badge/View%20on-GitHub-lightgrey?style=social&logo=github" alt="GitHub Repository" style="height: 25px;">
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True
    )   

if __name__ == "__main__":
    main()
