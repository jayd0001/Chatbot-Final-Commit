from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

## Init Flask APp
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
  ## GEt user message
    user_msg = request.values.get('Body', '').lower()
    ## Init bot response
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    # Applying bot logic
    if 'hello'   in user_msg:
        bot="Hi there welcome to Gndec Chatbot! How may I help you?"
        msg.body(bot)
        responded = True

    elif 'eligibility'   in user_msg:
        bot=("*Eligibility Criteria for BTech First Year*" + "\n\n JEE mains with 10+2 with Physics and Mathematics as compulsory along with chemistry/ Biotechnology/ Computer Science/ Biology"
        + "\n\n*Eligibility Criteria for BTech Second Year(LEET)*" + "\n\nAll those candidates who have passed Diploma examination from an AICTE approved Institution and have obtained at least 45% marks"
        + "\n\n*Eligibility Crteria for MTech*" + "\n\n GATE with BE/BTech in particular Branch with at least 50 % marks"
        + "\n\n*Eligibility Criteria for BCA*" + "\n\n The minimum eligibility criteria for BCA program is 10+2. in any discipline"
        + "\n\n *Elgibility Criteria for MCA*" + "\n\n All those candidates who have passed bachler degree of minimum 3 years duration in BCA or equivalent \n\n"
        + "\n\n*Eligibility Criteria for BBA*" + "\n\nAll those candidates who have passed the 10+2 or its equivalent examination in any stream conducted by a recognized Board / University."
        + "\n\n*Eligibility Criteria for MBA*" + "\n\nPreference given to the students having CMAT ranking (conducted by AICTE, New Delhi), other entrance examinations (CAT, MAT etc.)"
        + "\n\n*Eligibility Criteria for PHD. Program*" + "\n\nCandidates for admission to the PhD programme shall have a Masters degree in the relevant discipline wirth 55% marks")
        msg.body(bot)
        responded = True
        
    elif 'admission'  in user_msg:
        bot=("All the admission process is done under affiliated university  Punjab Technical university  centeralized counseling"
        + "\n\n for more Info visit university Website:- ptu.ac.in" + "\n\n then after which seats were left will be filled by Gndec itself (direct counseling)"
        + "\n\n for direct counseling Schedule visit our college website:- gndec.ac.in")
        msg.body(bot)
        responded = True
    
    elif 'rural' in user_msg:
        bot=("Reservation of seats for candidates belonging to Gill  village or rural area. over all 70% seats shall be filled by students hailing from rural area in punjab under rural quota"
        + "\n\n for more information on rural quota visit our  college website:- gndec.ac.in")
        msg.body(bot)
        responded = True
    
    elif 'btech' in user_msg:
        bot=("These are The BTech courses currently we are offering into our college\n\n"+
        "\n *BTech* *Courses*\n\n" + "\nBTech Information Technology" + "\nBTech Computer Science Engineering"
        + "\nBTech Mechanical Engineering" + "\nBTech Civil Engineering" + "\nBTech Electrical Engineering"
        + "\nBTech Electronics and Communication Engineering" + "\nBTech Mechanical Engineering(Production)")
        msg.body(bot)
        responded = True
    
    elif 'sikh' in user_msg:
        bot=("50% Seats are reserved for minority i.e Sikh Community out of total intake (out of 85% meant for Punjab as well as 15% meant for Other states). For admission under the Sikh minority quota, the candidates must qualify the Sikh Religion Examination (SRE). A candidate shall be eligible for admission by securing 36% marks in this examination. Admission will, however, be made on the basis of the JEE"
        + "\n\nThe Sikh Religion Examination is being conducted by Baba Banda Singh Bahadur Engineering College, Fatehgarh Sahib, on behalf of the Shiromani Gurdwara Parbandhak Committee (SGPC), Sri Amritsar." + "\n\n for More Information Regarding Sikh Quota kindly visit our Website:- gndec.ac.in")
        msg.body(bot)
        responded = True
   
    elif 'fee' in user_msg:
        bot=("Tuition Fee Waiver Scheme is available under B.Tech. courses (1st year & Lateral Entry both) for Punjab Residents only")
        msg.body(bot)
        responded = True
    
    elif 'scholarship' in user_msg:
        bot=("*There are more than 15 Scholarships which are currently being running under our college*"
        + "\n\n*GNDEC Alumni Scholarship (Sponsor: 1992'96 Mode of selection batch of GNDEC)* \n\n*UG scholarship (Sponsor: GNDEC/NSET)*"
        + "\n\n*Post Matric Scholarship for SC students* \n\n*Post Matric Scholarships Scheme for Minorities* \n\n*Merit Cum Means Scholarship for Professional and Technical Courses*"
        + "\n\n*Pragati scholarship scheme for girl students ( technical degree)* \n\n For more information Regarding Scholarships visit college Brochure link:- https://gndec.ac.in/?q=information%20brochure")
        msg.body(bot)
        responded = True

    
    elif 'mtech' in user_msg:
        bot=("These are The MTech courses currently we are offering into our college\n\n"+"\n*MTech Courses*\n" + "\nMTech Structural Engineering(FT)" + "\nMTech Geo Technical Engineering(FT)"
        + "\nMTech Environmental Science and Engg.(FT)" + "\nMTech Power Engineering(FT)" + "\nMTech Soil Mech. amd Foudation Engg.(PT)"
        + "\nMTech Electronics and Comm.(FT)" + "\nMTech Electronics and Comm.(PT)"
        + "\nMTech Production Engineering(PT)" + "\nMTech Mechanical Engineering(PT)"
        + "\nMTech Production Engg.(FT)" + "\nMTech Mechanical Engg.(FT)" + "\nMTech Computer Science and Engg.(FT)"
        + "\nMTech Computer Science and IT(FT)" + "\nMTech Electrical Engineering(PT)")
        msg.body(bot)
        responded = True
    
    elif 'phd' in user_msg:
        bot=("*Ph.D under QIP*" + "\n\nCivil Engineering \nMechanical Engineering \nElectrical Engineering"+ "\n\n*Ph.D is also offered in various departments under autonomous Status*")
        msg.body(bot)
        responded = True
    
    elif 'mba' in user_msg:
        bot=("*The Department offers Dual Specialization in below areas of Management. These are:*\n"
        + "\n*SPECIALIZATION OFFERED IN M.B.A as well as B.B.A:*\n\n"+"\nMBA and BBA In Marketing" + "\nMBA and BBA in Finance" + "\nMBA and BBA in Human Resourse Management")
        msg.body(bot)
        responded = True
    
    elif 'mca' in user_msg:
        bot=("*The Department offers 2 courses under Computer Applications*\n\n"+
        "\nBachelor Computer Application" + "\nMaster of Computer Application") 
        msg.body(bot)
        responded = True

    elif '1'  in user_msg:
        bot=("All the admission process is done under affiliated university  Punjab Technical university  centeralized counseling"
        + "\n\n for more Info visit university Website:- ptu.ac.in" + "\n\n then after which seats were left will be filled by Gndec itself (direct counseling)"
        + "\n\n for direct counseling Schedule visit our college website:- gndec.ac.in")
        msg.body(bot)
        responded = True

    elif '2' in user_msg:
        bot=("*Eligibility Criteria for BTech First Year*" + "\n\n JEE mains with 10+2 with Physics and Mathematics as compulsory along with chemistry/ Biotechnology/ Computer Science/ Biology"
        + "\n\n*Eligibility Criteria for BTech Second Year(LEET)*" + "\n\nAll those candidates who have passed Diploma examination from an AICTE approved Institution and have obtained at least 45% marks"
        + "\n\n*Eligibility Crteria for MTech*" + "\n\n GATE with BE/BTech in particular Branch with at least 50 % marks"
        + "\n\n*Eligibility Criteria for BCA*" + "\n\n The minimum eligibility criteria for BCA program is 10+2. in any discipline"
        + "\n\n *Elgibility Criteria for MCA*" + "\n\n All those candidates who have passed bachler degree of minimum 3 years duration in BCA or equivalent \n\n"
        + "\n\n*Eligibility Criteria for BBA*" + "\n\nAll those candidates who have passed the 10+2 or its equivalent examination in any stream conducted by a recognized Board / University."
        + "\n\n*Eligibility Criteria for MBA*" + "\n\nPreference given to the students having CMAT ranking (conducted by AICTE, New Delhi), other entrance examinations (CAT, MAT etc.)"
        + "\n\n*Eligibility Criteria for PHD. Program*" + "\n\nCandidates for admission to the PhD programme shall have a Masters degree in the relevant discipline wirth 55% marks")
        msg.body(bot)
        responded = True

    elif '3' in user_msg:
        bot=("Reservation of seats for candidates belonging to Gill  village or rural area. over all 70% seats shall be filled by students hailing from rural area in punjab under rural quota"
        + "\n\n for more information on rural quota visit our  college website:- gndec.ac.in")
        msg.body(bot)
        responded = True

    elif '4' in user_msg:
        bot=("These are The BTech courses currently we are offering into our college\n\n"+
        "\n *BTech* *Courses*\n\n" + "\nBTech Information Technology" + "\nBTech Computer Science Engineering"
        + "\nBTech Mechanical Engineering" + "\nBTech Civil Engineering" + "\nBTech Electrical Engineering"
        + "\nBTech Electronics and Communication Engineering" + "\nBTech Mechanical Engineering(Production)")
        msg.body(bot)
        responded = True

    elif '5' in user_msg:
        bot=("These are The MTech courses currently we are offering into our college\n\n"+"\n*MTech Courses*\n" + "\nMTech Structural Engineering(FT)" + "\nMTech Geo Technical Engineering(FT)"
        + "\nMTech Environmental Science and Engg.(FT)" + "\nMTech Power Engineering(FT)" + "\nMTech Soil Mech. amd Foudation Engg.(PT)"
        + "\nMTech Electronics and Comm.(FT)" + "\nMTech Electronics and Comm.(PT)"
        + "\nMTech Production Engineering(PT)" + "\nMTech Mechanical Engineering(PT)"
        +"\nMTech Production Engg.(FT)" + "\nMTech Mechanical Engg.(FT)" + "\nMTech Computer Science and Engg.(FT)"
        + "\nMTech Cmoputer Science and IT(FT)" + "\nMTech Electrical Engineering(PT)")
        msg.body(bot)
        responded = True

    elif '6' in user_msg:
        bot=("Tuition Fee Waiver Scheme is available under B.Tech. courses (1st year & Lateral Entry both) for Punjab Residents only")
        msg.body(bot)
        responded = True

    elif '7' in user_msg:
        bot=("50% Seats are reserved for minority i.e Sikh Community out of total intake (out of 85% meant for Punjab as well as 15% meant for Other states). For admission under the Sikh minority quota, the candidates must qualify the Sikh Religion Examination (SRE). A candidate shall be eligible for admission by securing 36% marks in this examination. Admission will, however, be made on the basis of the JEE"
        + "\n\nThe Sikh Religion Examination is being conducted by Baba Banda Singh Bahadur Engineering College, Fatehgarh Sahib, on behalf of the Shiromani Gurdwara Parbandhak Committee (SGPC), Sri Amritsar." + "\n\n for More Information Regarding Sikh Quota kindly visit our Website:- gndec.ac.in")
        msg.body(bot)
        responded = True

    elif '8' in user_msg:
        bot=("*There are more than 15 Scholarships which are currently being running under our college*"
        + "\n\n*GNDEC Alumni Scholarship (Sponsor: 1992'96 Mode of selection batch of GNDEC)* \n\n*UG scholarship (Sponsor: GNDEC/NSET)*"
        + "\n\n*Post Matric Scholarship for SC students* \n\n*Post Matric Scholarships Scheme for Minorities* \n\n*Merit Cum Means Scholarship for Professional and Technical Courses*"
        + "\n\n*Pragati scholarship scheme for girl students ( technical degree)* \n\n For more information Regarding Scholarships visit college Brochure link:- https://gndec.ac.in/?q=information%20brochure")
        msg.body(bot)
        responded = True

    elif '9' in user_msg:
        bot=("*The Department offers Dual Specialization in below areas of Management. These are:*\n"
        + "\n*SPECIALIZATION OFFERED IN M.B.A as well as B.B.A:*\n\n"+"\nMBA and BBA In Marketing" + "\nMBA and BBA in Finance" + "\nMBA and BBA in Human Resourse Management")
        msg.body(bot)
        responded = True

    elif '*' in user_msg:
        bot=("*The Department offers 2 courses under Computer Applications*\n\n"+
        "\nBachelor Computer Application" + "\nMaster of Computer Application") 
        msg.body(bot)
        responded = True

    elif '#' in user_msg:
        bot=("*Ph.D under QIP*" + "\n\nCivil Engineering \nMechanical Engineering \nElectrical Engineering"+ "\n\n*Ph.D is also offered in various departments under autonomous Status*")
        msg.body(bot)
        responded = True
    
    else:
        bot=("Press 1 for Admission \nPress 2 for Eligibility \nPress 3 for Rural Quota \nPress 4 for Btech \nPress 5 for Mtech \nPress 6 for Fee Waiver"
        + "\nPress 7 for Sikh Quota \nPress 8 for Scholarship \nPress 9 for MBA or BBA \nPress * for MCA or BCA \nPress # for Ph.D"
        )
        msg.body(bot)
        responded = True
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)