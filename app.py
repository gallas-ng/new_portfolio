from datetime import datetime
import streamlit as st
import pandas as pd
import html

# Configure the Streamlit page settings
st.set_page_config(
    page_title="Falilou Niang - Portfolio",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the current year
today = datetime.today().strftime("%Y")

# Load external CSS and JS libraries
# Load external CSS libraries for styling (MaterializeCSS, Material Icons, and Font Awesome)
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">', unsafe_allow_html=True)
st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)

customStyle= """
<style>
.card.large {
    height: 550px;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
}
.card.large .card-content {
    overflow-y: auto;
    flex-grow: 1;
}
.card.large .card-image img {
    height: 200px;
    object-fit: cover;
}
.card.small {
    height: 340px;
    display: flex;
    flex-direction: column;
    # justify-content: space-between;
    margin-bottom: 14px;
}
.card.small .card-content {
    flex-grow: 1;
    overflow-y: auto;
}
.card.small .card-action {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}
button[data-baseweb="tab"] p {
    font-size: 20px !important;
}
div[data-testid="stAppViewBlockContainer"] {
    padding-top: 0px;
}
.row.flex-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    justify-content: space-between;
}
.col.s12.m4 {
    width: 33%;
}
.col.s12.m6 {
    width: 48%;
}
@media (max-width: 768px) {
    .col.s12.m2, .col.s12.m4, .col.s12.m6, .col.s12.m10, .col.s12.m12 {
        width: 100% !important;
        height: 100%;
    }
    img.responsive-img.circle {
        width: 100px !important;
        height: 100px !important;
        object-fit: cover;
    }
}
body {
    background: linear-gradient(to bottom, #f0f4f8, #ffffff);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1, h5, h6 {
    color: #2e3b4e;
}
.card-title {
    font-weight: bold;
}
.footer {
    text-align: center;
    padding: 1rem;
    font-size: 14px;
    color: #777;
    border-top: 1px solid #ddd;
    margin-top: 2rem;
}
</style>
"""

# Apply the custom styles
st.html(customStyle)


# Load Excel files
diplomas_df = pd.read_excel("sheets/diplomas.xlsx")
certifications_df = pd.read_excel("sheets/certifications.xlsx")
profile_df = pd.read_excel("sheets/profile.xlsx")
skills_df = pd.read_excel("sheets/skills.xlsx")
projects_df = pd.read_excel("sheets/projects.xlsx")
contacts_df = pd.read_excel("sheets/contacts.xlsx")

# Sidebar with diplomas and certifications
st.sidebar.header("🎓 Diplomas")
diplomas = diplomas_df.sort_values(by='Year', ascending=False)
for _, diploma in diplomas.iterrows():
    st.sidebar.markdown(f"**{diploma['Title']}** - \n{diploma['School']} ({diploma['Year']})")

st.sidebar.header("📜 Certifications")
certifications = certifications_df.sort_values(by='Year', ascending=False)
for _, cert in certifications.iterrows():
    st.sidebar.markdown(f"**{cert['Title']}** - \n{cert['Platform']} ({cert['Year']})")

# Profile
profile = profile_df.iloc[0]
name = profile['Name']
profileDescription = profile['Description']
profileTagline = profile['tagline']
linkedInLink = profile['linkedin']
xLink = profile['x']
githubLink = profile['github']
picture = profile['picture']

profileHTML = f"""
<div class="row">
<h1>{name} <span class="blue-text text-darken-3">Portfolio</span> </h1>
<h5>{profileTagline}</h5>
</div>
<div class="row">
    <div class="col s12 m12">
        <div class="card">
            <div class="card-content">
                <div class="row">                    
                    <div class="col s12 m2">
                        <img class="circle responsive-img" src="{picture}">
                    </div>
                        <div class="col s12 m10 ">
                            <span class="card-title">About me</span>
                            <p>{profileDescription}</p>
                            <div class="card-action">
                                <a href="{linkedInLink}" class="tooltipped blue-text text-darken-3" data-tooltip="LinkedIn"><i class="fa-brands fa-linkedin fa-2xl"></i></a>
                                <a href="{githubLink}" class="tooltipped black-text text-darken-3" data-tooltip="GitHub"><i class="fa-brands fa-github fa-2xl"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""
st.html(profileHTML)
# Tabs
with st.container():
    tabSkills, tabPortfolio, tabContact = st.tabs(['💡 My skills', '🚀 My projects', '📬 Contact'])

    with tabSkills:
        tabSkills_content = ""
        for _, skill in skills_df.sort_values(by='Level', ascending=False).iterrows():
            skillName = skill['Name']
            skillDescription = skill['Notes']
            skillLevel = skill['Level']
            skillStars = "".join(['<i class="material-icons">star</i>' if i <= skillLevel else '<i class="material-icons">star_border</i>' for i in range(1, 6)])
            skillYears = skill['startYear']
            skillExperience = int(today) - int(skillYears)

            skillHTML = f"""
                <div class="col s12 m4">
                    <div class="card small">
                        <div class="card-content">
                            <span class="card-title">{skillName}</span>
                            <p>{html.escape(skillDescription)}</p>
                        </div>
                        <div class="card-action">
                            <div>
                                <p>Level:<br/> {skillStars}</p>
                            </div>
                            <div>
                                <p>Since:<br/> {skillYears} - More than {skillExperience} years</p>
                            </div>
                        </div>
                    </div>
                </div>
            """
            tabSkills_content += skillHTML
        st.html(f"<div class='row'>{tabSkills_content}</div>")

    with tabPortfolio:
        tabPortfolio_content = ""
        for _, project in projects_df.iterrows():
            projectName = project['Name']
            projectDescription = project['Description']
            projectSkills = project['skills'].split(",")  # Assuming skills are comma-separated
            projectKnowledge = project['Knowledge'].split(",")  # Assuming knowledge is comma-separated
            projectLink = project['link']
            projectImageUrl = project['image']

            skillsHTML = "".join([f'<div class="chip green lighten-4">{p}</div>' for p in projectSkills])
            knowledgeHTML = "".join([f'<div class="chip blue lighten-4">{p}</div>' for p in projectKnowledge])

            projectHTML = f"""
                <div class="col s12 m6">
                    <div class="card large">
                        <div class="card-image">
                            <a href="{projectLink}" target="_blank" rel="noopener noreferrer"><img src="{projectImageUrl}"></a>
                        </div>
                        <div class="card-content">
                            <span class="card-title">{projectName}</span>
                            <p>{projectDescription}</p>
                            <div class="row">
                                <div class="col s12 m6">
                                    <h6>Knowledge:</h6>
                                    {knowledgeHTML}
                                </div>
                                <div class="col s12 m6">
                                    <h6>Skills:</h6>
                                    {skillsHTML}
                                </div>
                            </div>
                        </div>
                        <div class="card-action right-align">
                            <a href="{projectLink}" target="_blank" rel="noopener noreferrer" class="waves-effect waves-light btn-large white-text blue darken-3"><i class="material-icons left">open_in_new</i>View</a>
                        </div>
                    </div>
                </div>
            """
            tabPortfolio_content += projectHTML
        st.html(f"<div class='row'>{tabPortfolio_content}</div>")

    with tabContact:
        st.info("Send me a message if you'd like to collaborate or have any inquiries.")
        parName = st.text_input("Your name")
        parEmail = st.text_input("Your email")
        parPhone = st.text_input("Your phone number")
        parNotes = st.text_area("Your message")
        if st.button("Send"):
            new_contact = pd.DataFrame([{
                "Name": parName,
                "email": parEmail,
                "phone": parPhone,
                "Notes": parNotes
            }])
            contacts_df = pd.concat([contacts_df, new_contact], ignore_index=True)
            contacts_df.to_excel("sheets\contacts.xlsx", index=False)  # Save the updated contacts
            st.toast("Message sent!")

# Footer
st.html("""<div class='footer'>
&copy; 2024 Falilou Niang • Made with ;) and Streamlit
</div>""")