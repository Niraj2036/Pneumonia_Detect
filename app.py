import streamlit as st

def main():
    st.title("Pneumonia Detector")

    # Classification and Regression buttons with embedded URLs
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            '''
            <style>
                .custom-button {
                    padding: 10px 20px;
                    background-color: white;
                    color: red;
                    border: 2px solid red;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .custom-button:hover {
                    background-color: red;
                    color: white;
                    border-color: white;
                }
            </style>
            <a href="https://pneumoniadetect1.streamlit.app" style="text-decoration: none; color: red;">
            <button class="custom-button">Self Assesment</button>
            </a>
            ''', 
            unsafe_allow_html=True
        )

    with col2:
        st.write(
            '''
            <style>
                .custom-button {
                    padding: 10px 20px;
                    background-color: white;
                    color: red;
                    border: 2px solid red;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .custom-button:hover {
                    background-color: red;
                    color: white;
                    border-color: white;
                }
            </style>
            <a href="https://pneumoniadetect2.streamlit.app" style="text-decoration: none; color: red;">
            <button class="custom-button">X Ray Detection</button>
            </a>
            ''', 
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
