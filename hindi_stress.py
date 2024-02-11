import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('happimynd-3460553cc66f.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets document by its title
spreadsheet = client.open_by_key("1YpIAgkk9nkpczG6U9k-f2aafMy0Tn3Fmu-JJ-O278TY")
worksheet = spreadsheet.get_worksheet(0)  # Assuming the data is in the first worksheet

def categorize_stress_level(total_score):
    if total_score <= 13:
        return "आपका तनाव स्तर कम है। (You have low stress)"
    elif 14 <= total_score <= 26:
        return "आपका तनाव स्तर मध्यम है। (You have moderate stress)"
    else:
        return "आपका तनाव स्तर अत्यधिक है। (You have high perceived stress)"

def submit_survey_data(name, email, mobile_number, company_name, total_score, stress_level):
    data = [name, email, mobile_number, company_name, total_score, stress_level]
    worksheet.append_row(data)
    st.success("Your request is submitted successfully!")
    
def survey_question_1():
    st.markdown("Q1. पिछले महीने, कितनी बार आपने अचानक कुछ होने के कारण  चिड़चिड़ेपन का अहसास किया है?")
    st.markdown("(In the last month, how often have you been upset because of something that happened unexpectedly?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question1")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 0, "लगभग कभी नहीं  (Almost Never)": 1, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 3, "लगभग हमेशा (Very Often)": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_2():
    st.markdown("Q2. पिछले महीने, कितनी बार आपने महसूस किया है कि आप आपने जीवन की महत्वपूर्ण चीजों को नियंत्रित  नहीं कर पा रहे थे?")
    st.markdown("(In the last month, how often have you felt that you were unable to control the important things in your life?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question2")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 0, "लगभग कभी नहीं  (Almost Never)": 1, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 3, "लगभग हमेशा (Very Often)": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_3():
    st.markdown("Q3. पिछले महीने, कितनी बार आपने घबराहट और तनाव महसूस किया है?")
    st.markdown("(In the last month, how often have you felt nervous and stressed?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question3")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 0, "लगभग कभी नहीं  (Almost Never)": 1, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 3, "लगभग हमेशा (Very Often)": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_4():
    st.markdown("Q4. पिछले महीने, कितनी बार आपने अपनी व्यक्तिगत समस्याओं को संभालने की क्षमता के बारे में आत्मविश्वास महसूस किया है?")
    st.markdown("(In the last month, how often have you felt confident about your ability to handle your personal problems?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question4")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 4, "लगभग कभी नहीं  (Almost Never)": 3, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 1, "लगभग हमेशा (Very Often)": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_5():
    st.markdown("Q5. पिछले महीने, कितनी बार आपने महसूस किया है कि चीजें आपके अनुरूप हो रही हैं?")
    st.markdown("(In the last month, how often have you felt that things were going your way?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question5")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 4, "लगभग कभी नहीं  (Almost Never)": 3, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 1, "लगभग हमेशा (Very Often)": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_6():
    st.markdown("Q6. पिछले महीने, कितनी बार आपने महसूस किया है कि जो आपको करना था उन सभी चीजों को आप संभाल नहीं पा रहे थे?")
    st.markdown("(In the last month, how often have you found that you could not cope with all the things that you had to do?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question6")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 0, "लगभग कभी नहीं  (Almost Never)": 1, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 3, "लगभग हमेशा (Very Often)": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_7():
    st.markdown("Q7. पिछले महीने, कितनी बार आप अपने जीवन में  चिड़चिड़ेपन को नियंत्रित कर पाए हैं?")
    st.markdown("(In the last month, how often have you been able to control irritations in your life?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question7")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 4, "लगभग कभी नहीं  (Almost Never)": 3, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 1, "लगभग हमेशा (Very Often)": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_8():
    st.markdown("Q8. पिछले महीने, कितनी बार आपने महसूस किया है कि आपका चीजों पर नियंत्रण है?")
    st.markdown("(In the last month, how often have you felt that you were on top of things?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question8")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 4, "लगभग कभी नहीं  (Almost Never)": 3, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 1, "लगभग हमेशा (Very Often)": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_9():
    st.markdown("Q9. पिछले महीने में, आप कितनी बार उन चीजों के कारण क्रोधित हुए हैं जो आपके नियंत्रण से बाहर थीं?")
    st.markdown("(In the last month, how often have you been angered because of things that happened that were outside of your control?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question9")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 0, "लगभग कभी नहीं  (Almost Never)": 1, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 3, "लगभग हमेशा (Very Often)": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_10():
    st.markdown("Q10. पिछले महीने, कितनी बार आपने यह महसूस किया है कि समस्याएं इतनी  ज़्यादा हैं कि आप उनसे उभर नहीं पा रहे हैं?")
    st.markdown("(In the last month, how often have you felt difficulties piling up so high that you could not overcome them?)")
    options = ["कभी नहीं  (Never)", "लगभग कभी नहीं  (Almost Never)", "कभी-कभी (Sometimes)", "अक्सर (Fairly Often)", "लगभग हमेशा (Very Often)"]
    selected_option = st.radio("", options, index=None, key="question10")

    # Assign scores based on the selected option
    scores = {"कभी नहीं  (Never)": 0, "लगभग कभी नहीं  (Almost Never)": 1, "कभी-कभी (Sometimes)": 2, "अक्सर (Fairly Often)": 3, "लगभग हमेशा (Very Often)": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def get_user_info():
    name = st.text_input("नाम (Name):")
    email = st.text_input("ईमेल आईडी (Email ID):")
    mobile_number = st.text_input("मोबाइल नंबर (Mobile Number):")
    company_name = st.text_input("कंपनी/इंस्टीट्यूट का नाम (Company/Institute Name):")
    
    # Validate that name, email, mobile_number, and company_name are not empty
    if not name.strip() or not email.strip() or not mobile_number.strip() or not company_name.strip():
        st.warning("कृपया सभी विकल्प भरें।")
        return None, None, None, None

    return name, email, mobile_number, company_name    
  
def main():
    st.image("HLS-removebg-preview.png", width = 150)
    st.header("HappiLIFE Screening")
    st.header("तनाव टेस्ट (Stress Test)")
    
    st.subheader("पहला कदम जो आपकी भावनात्मक और मानसिक स्वास्थ्य का  मूल्यांकन करने में आपकी मदद करता है।")
    st.divider()
    
    # First question
    score1 = survey_question_1()
    st.divider()
    
    # Second question
    score2 = survey_question_2()
    st.divider()
    
    # Third question
    score3 = survey_question_3()
    st.divider()
    
    # Fourth question
    score4 = survey_question_4()
    st.divider()
    
    # Fifth question
    score5 = survey_question_5()
    st.divider()
    
    # Sixth question
    score6 = survey_question_6()
    st.divider()
    
    # Seventh question
    score7 = survey_question_7()
    st.divider()
    
    # Eighth question
    score8 = survey_question_8()
    st.divider()
    
    # Ninth question
    score9 = survey_question_9()
    st.divider()
    
    # Tenth question
    score10 = survey_question_10()
    st.divider()
    
    st.markdown("अपना जानकारी हमारे साथ साझा करें ताकि हम आपसे संपर्क कर आपकी सहायता कर सकें।")
    st.markdown("(Share your details so that we can connect and help you)")
    # Collect user information
    name, email, mobile_number, company_name = get_user_info()
    
    
    
    # Handle the case where no option is selected for any question
    if any(score is None for score in [score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, name, email, mobile_number, company_name]):
        st.warning("Please select an option for all questions")
        return

    # Calculate total score
    total_score = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
    
    # Display total score
    st.subheader(f"आपका तनाव स्कोर 40 में से {total_score} है। (Your stress score is {total_score})")

    # Categorize stress level and display result
    stress_level = categorize_stress_level(total_score)
    st.subheader(f"{stress_level}")

# Submit data to Google Sheets
    if st.button("Know more"):
        submit_survey_data(name, email, mobile_number, company_name, total_score, stress_level)


if __name__ == "__main__":
    main()
