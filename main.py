import streamlit as st

# Function to calculate CRS grade
def calculate_crs_grade(fever, hypotension, hypoxia):
    if fever and not hypotension and not hypoxia:
        return "Grade 1"
    elif fever and hypotension == "responds to fluids" and not hypoxia:
        return "Grade 2"
    elif fever and hypotension == "requires pressors" or hypoxia == "requires oxygen":
        return "Grade 3"
    elif hypotension == "requires multiple pressors" or hypoxia == "requires mechanical ventilation":
        return "Grade 4"
    else:
        return "No CRS"

# Streamlit app
def main():
    st.title("Cytokine Release Syndrome (CRS) Grading Calculator")

    st.write("""
    ## Description
    This app calculates the grade of Cytokine Release Syndrome (CRS) based on user inputs.
    CRS is a systemic inflammatory response that can be triggered by certain therapies,
    and it is important to accurately grade the severity for appropriate management.
    """)

    st.write("### Enter the following information to calculate CRS grade:")
    
    fever = st.checkbox("Fever (≥ 38°C)")
    hypotension = st.selectbox("Hypotension", ["None", "Responds to fluids", "Requires pressors", "Requires multiple pressors"])
    hypoxia = st.selectbox("Hypoxia", ["None", "Requires oxygen", "Requires mechanical ventilation"])

    if st.button("Calculate CRS Grade"):
        grade = calculate_crs_grade(fever, hypotension, hypoxia)
        st.write(f"### The CRS Grade is: {grade}")

if __name__ == "__main__":
    main()
