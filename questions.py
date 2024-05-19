import streamlit as st

def check_pneumonia():
    st.title("Pneumonia Self-Assessment")

    # Initialize session state variables
    if 'responses' not in st.session_state:
        st.session_state.responses = {}
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'completed' not in st.session_state:
        st.session_state.completed = False

    questions = [
        "Do you have a cough that produces phlegm?",
        "Do you have a high fever?",
        "Do you experience chest pain that worsens with deep breathing or coughing?",
        "Do you have shortness of breath even while resting?",
        "Do you feel very tired or weak?",
        "Do you experience nausea, vomiting, or diarrhea?",
        "Are you experiencing confusion (especially if you are an older adult)?",
        "Do you have muscle pain?",
        "Do you have a headache?",
        "Are you experiencing chills or sweating?"
    ]

    def display_question(question, index):
        st.write(question)
        response = st.radio(f"Select your answer for question {index + 1}", ('Yes', 'No'), key=index)
        return response

    # Display all answered questions so far
    for i in range(st.session_state.current_question):
        st.write(f"{questions[i]} - {st.session_state.responses.get(i, '').capitalize()}")

    # Display the current question
    if st.session_state.current_question < len(questions):
        current_question = st.session_state.current_question
        response = display_question(questions[current_question], current_question)
        if st.button("Next"):
            st.session_state.responses[current_question] = response.lower()
            st.session_state.current_question += 1
            st.experimental_rerun()
    else:
        st.session_state.completed = True

    # Display result after all questions are answered
    if st.session_state.completed:
        # Define conditions that indicate a higher risk of pneumonia
        high_risk_conditions = [
            "Do you have a high fever?",
            "Do you experience chest pain that worsens with deep breathing or coughing?",
            "Do you have shortness of breath even while resting?",
            "Do you experience confusion (especially if you are an older adult)?"
        ]
        
        # Count the number of high-risk symptoms
        high_risk_count = sum(
            1 for i, q in enumerate(questions) if q in high_risk_conditions and st.session_state.responses.get(i) == 'yes'
        )

        # Define a threshold for suggesting a chest X-ray
        if high_risk_count >= 2 or (high_risk_count == 1 and len(st.session_state.responses) > 5):
            st.write("You should get a chest X-ray and upload it.")
        else:
            st.write("Congratulations, you don't have pneumonia.")

        if st.button("Restart"):
            st.session_state.responses = {}
            st.session_state.current_question = 0
            st.session_state.completed = False
            st.experimental_rerun()

if __name__ == "__main__":
    check_pneumonia()
