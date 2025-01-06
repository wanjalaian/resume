import streamlit as st
from PIL import Image, ImageOps

# Set page configuration
st.set_page_config(page_title="Ian Wanjala | Data Analyst Portfolio", layout="centered")

# Inject custom CSS for timeline and icons
st.markdown(
    """
    <style>
    * {
        box-sizing: border-box;
    }

    .contact-links {
        display: flex;
        gap: 10px;
        align-items: center;
        margin-top: 10px;
    }
    .contact-links a {
        text-decoration: none;
        color: #2E86C1;
        display: flex;
        align-items: center;
    }
    .icon {
        width: 16px;
        height: 16px;
        vertical-align: middle;
        margin-right: 4px;
    }
    .profile-column {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
    }
    .hire-me-button {
        background-color: #f5f6fa;
        color: #2f3640; /* Default text color */
        padding: 10px 20px;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-size: 16px;
        margin-top: 10px;
        tex
        
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .hire-me-button:hover {
        background-color: #44bd32;
        color: white; /* Text color on hover */
        text-decoration: none;
    }
    .hire-me-button span {
        text-decoration: none; /* Ensure no underline */
        color: #2f3640; /* Explicitly set text color */
        transition: color 0.3s ease; /* Smooth color transition */
    }
    .hire-me-button:hover span {
        color: white; /* Change text color to white on hover */
    }
    .hire-me-button:hover .upwork-icon {
        fill: white; /* SVG color on hover */
    }
    .upwork-icon {
        width: 20px;
        height: 20px;
        fill: #2f3640; /* Default SVG color */
        transition: fill 0.3s ease;
    }
    .location {
        font-size: 0.9em; /* Smaller font size */
        color: #666; /* Gray text color */
        margin-top: -10px; /* Move closer to the name */
        margin-bottom: 10px; /* Space before the job title */
    }
    .skill-pill {
        display: inline-block;
        padding: 0.5em 1em;
        margin: 0.25em;
        border-radius: 20px;
        background-color: #192a56;
        color: white;
        font-size: 0.9em;
    }
    a:link { 
      text-decoration: none; 
    } 
    a:visited { 
      text-decoration: none; 
    } 
    a:hover { 
      text-decoration: none; 
    } 
    a:active { 
      text-decoration: none; 
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Profile picture and name
col1, col2 = st.columns([1, 2])

with col1:
    # Load the profile image
    profile_pic = Image.open("profile.png")  # Replace with the path to your profile picture

    # Convert the image to a base64 string for embedding in HTML
    import base64
    from io import BytesIO

    buffered = BytesIO()
    profile_pic.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Wrap the profile picture and button in a flex container
    st.markdown(
        f"""
        <div class="profile-column">
            <img src="data:image/png;base64,{img_str}" alt="Profile Picture" width="150" style="border-radius: 50%;">
            <a href="https://www.upwork.com/freelancers/~01266f15a2764c93fb?mp_source=share" target="_blank" class="hire-me-button">
            <svg class="upwork-icon" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
                <path d="M24.75 17.542c-1.469 0-2.849-0.62-4.099-1.635l0.302-1.432 0.010-0.057c0.276-1.521 1.13-4.078 3.786-4.078 1.99 0 3.604 1.615 3.604 3.604 0 1.984-1.615 3.599-3.604 3.599zM24.75 6.693c-3.385 0-6.016 2.198-7.083 5.818-1.625-2.443-2.865-5.38-3.583-7.854h-3.646v9.484c-0.005 1.875-1.521 3.391-3.396 3.396-1.875-0.005-3.391-1.526-3.396-3.396v-9.484h-3.646v9.484c0 3.885 3.161 7.068 7.042 7.068 3.885 0 7.042-3.182 7.042-7.068v-1.589c0.708 1.474 1.578 2.974 2.635 4.297l-2.234 10.495h3.729l1.62-7.615c1.417 0.906 3.047 1.479 4.917 1.479 4 0 7.25-3.271 7.25-7.266 0-4-3.25-7.25-7.25-7.25z"/>
            </svg>
            <span>Hire Me</span>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.title("Ian Wanjala")
    st.markdown(
        """
        <div class="location">📍 Nairobi, Kenya</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("##### Data Analyst | Business Analytics | Transforming Data into Actionable Strategies")

    # Contact links in pills separated by |
    st.markdown(
        """
        <div class="contact-links">
            <a href="mailto:wanjalaian@gmail.com">📧 Email</a> |
            <a href="tel:+254700182482">📞 Phone</a> |
            <a href="https://linkedin.com/in/ian-wanjala-ke" target="_blank">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" style="width: 23px; height: 23px;">
                    <path fill="#0078d4" d="M42,37c0,2.762-2.238,5-5,5H11c-2.761,0-5-2.238-5-5V11c0-2.762,2.239-5,5-5h26c2.762,0,5,2.238,5,5V37z"></path>
                    <path fill="#fff" d="M12,19h5v17h-5V19z M14.485,17h-0.028C12.965,17,12,15.888,12,14.499C12,13.08,12.995,12,14.514,12c1.521,0,2.458,1.08,2.486,2.499C17,15.887,16.035,17,14.485,17z M36,36h-5v-9.099c0-2.198-1.225-3.698-3.192-3.698c-1.501,0-2.313,1.012-2.707,1.99C24.957,25.543,25,26.511,25,27v9h-5V19h5v2.616C25.721,20.5,26.85,19,29.738,19c3.578,0,6.261,2.25,6.261,7.274L36,36L36,36z"></path>
                </svg>
                LinkedIn
            </a> |
            <a href="https://github.com/wanjalaian" target="_blank">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" style="width: 23px; height: 23px;">
                    <path fill="#2100c4" d="M24,4C12.954,4,4,12.954,4,24c0,8.887,5.801,16.411,13.82,19.016h12.36C38.199,40.411,44,32.887,44,24C44,12.954,35.046,4,24,4z"></path>
                    <path fill="#ddbaff" d="M37,23.5c0-2.897-0.875-4.966-2.355-6.424C35.591,15.394,34.339,12,34.339,12c-2.5,0.5-4.367,1.5-5.609,2.376C27.262,14.115,25.671,14,24,14c-1.71,0-3.339,0.118-4.834,0.393c-1.242-0.879-3.115-1.889-5.632-2.393c0,0-1.284,3.492-0.255,5.146C11.843,18.6,11,20.651,11,23.5c0,6.122,3.879,8.578,9.209,9.274C19.466,33.647,19,34.764,19,36l0,0.305c-0.163,0.045-0.332,0.084-0.514,0.108c-1.107,0.143-2.271,0-2.833-0.333c-0.562-0.333-1.229-1.083-1.729-1.813c-0.422-0.616-1.263-2.032-3.416-1.979c-0.376-0.01-0.548,0.343-0.5,0.563c0.043,0.194,0.213,0.5,0.896,0.75c0.685,0.251,1.063,0.854,1.438,1.458c0.418,0.674,0.417,2.468,2.562,3.416c1.53,0.677,2.988,0.594,4.097,0.327l0.001,3.199c0,0.639-0.585,1.125-1.191,1.013C19.755,43.668,21.833,44,24,44c2.166,0,4.243-0.332,6.19-0.984C29.584,43.127,29,42.641,29,42.002L29,36c0-1.236-0.466-2.353-1.209-3.226C33.121,32.078,37,29.622,37,23.5z"></path>
                </svg>
                GitHub
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Line separator
st.divider()

# About Me
st.markdown("###### About Me")
st.write(
    "Dynamic Data Analyst with a proven track record in leveraging data to deliver actionable insights, "
    "build dashboards, and drive strategic decisions. Experienced in Python, SQL, Tableau, and Power BI, "
    "with a strong focus on collaboration and cross-functional alignment to achieve organizational goals."
)

# Line separator
st.divider()

# Career Highlights
st.markdown("###### Career Highlights")

# Highlight 1: Product Analysis & Reporting
with st.expander("📊 Product Analysis & Reporting"):
    st.write(
        "Delivered actionable insights by analyzing large datasets. "
        "Developed custom reports and dashboards to track key performance indicators (KPIs). "
        "Collaborated with stakeholders to identify trends and provide data-driven recommendations."
    )

# Highlight 2: Data Visualization
with st.expander("📈 Data Visualization"):
    st.write(
        "Utilized tools like Tableau and Power BI to create interactive dashboards. "
        "Designed visualizations to simplify complex data for non-technical audiences. "
        "Improved decision-making processes by providing real-time data insights."
    )

# Highlight 3: Client Portal Development & Adoption
with st.expander("🚀 Client Portal Development & Adoption"):
    st.write(
        "Designed, built, and maintain a client-facing portal that enables direct interaction with our system, eliminating manual processes and streamlining operations. "
        "The portal now has over 💯 daily active users and has become a critical component of daily workflows. "
        "Developed custom reporting dashboards to provide real-time insights and trained users to achieve 100% adoption, ensuring seamless integration into their routines."
    )

# Highlight 4: KYC/Verification API Integration
with st.expander("🔐 API Integration"):
    st.write(
        "Integrated KYC (Know Your Customer) and verification APIs into our system, introducing a new service offering that significantly enhanced our product portfolio. "
        "This integration not only improved operational efficiency but also drove measurable revenue growth by expanding our service capabilities and attracting new clients."
    )

# Highlight 5: Workflow Automation & Efficiency Gains
with st.expander("🤖 Workflow Automation & Efficiency Gains"):
    st.write(
        "Developed and implemented workflow automations within our business applications, enabling real-time status updates and reducing delays across key processes. "
        "These automations have dramatically improved operational efficiency, minimized manual intervention, and accelerated decision-making, contributing to overall business agility."
    )

# Line separator
st.divider()

# Skills
st.markdown("###### Skills")
skills = [
    ("📊", "Data Analysis"),
    ("📈", "Product Metrics"),
    ("🧹", "Data Cleaning"),
    ("🐍", "Python"),
    ("🗃️", "SQL"),
    ("🐼", "Pandas"),
    ("🚀", "Streamlit"),
    ("📊", "Data Visualization (Excel, Power BI, Zoho Analytics)"),
    ("📉", "Statistical Analysis"),
    ("⚙️", "Zapier"),
    ("🔗", "REST APIs"),
    ("📑", "Reporting & Dashboards"),
    ("🤝", "Cross-Functional Collaboration"),
    ("🧩", "Problem-solving"),
    ("🧠", "Critical Thinking"),
    ("🗣️", "Communication")
]

# Display skills as pills with emojis
skill_pills = " ".join([f'<span class="skill-pill">{emoji} {skill}</span>' for emoji, skill in skills])
st.markdown(skill_pills, unsafe_allow_html=True)

# Line separator
st.divider()

# Work Experience Section
st.markdown("###### Work Experience")

# Work Experience
work_experience = [
    {
        "title": "Data Analyst",
        "company": "Reporthub Limited (Remote)",
        "duration": "Sep 2023 – Present",
        "skills": ["Data Analysis", "REST APIs", "Power BI", "Workflow Automation", "Zoho Suite"],
        "description": [
            "Built and maintained interactive dashboards using Tableau and Power BI.",
            "Developed and optimized SQL queries for actionable insights.",
            "Led ad-hoc analysis projects, identifying trends for business growth.",
            "Collaborated with cross-functional teams to define data requirements.",
        ],
    },
    {
        "title": "Web Developer",
        "company": "Freelance (Remote)",
        "duration": "May 2023 – Jul 2023",
        "skills": ["Web Development", "S.E.O", "Data Mining & Cleaning", "Data Entry", "WordPress"],
        "description": [
            "Led the development of a custom data integration system using APIs.",
            "Managed and processed large datasets using SQL and analysis techniques.",
            "Developed custom reporting solutions to track key metrics.",
        ],
    },
    {
        "title": "Intern",
        "company": "Judicial Service Commission (Nairobi, Kenya)",
        "duration": "Jun 2019 – Aug 2019",
        "skills": ["Database Management", "SQL", "Exploratory Data Analysis", "Reporting", "Data Cleaning"],
        "description": [
            "Assisted in managing and querying SQL databases.",
            "Conducted data analysis to support decision-making.",
            "Automated routine reports to improve efficiency.",
        ],
    },
]

# Display work experience as expanders
for job in work_experience:
    with st.expander(f"{job['title']} | {job['duration']}"):
        # Display top 5 skills as pills
        skill_pills = " ".join([f'<span class="skill-pill">{skill}</span>' for skill in job['skills'][:5]])
        st.markdown(skill_pills, unsafe_allow_html=True)
        # Display description as bullet points
        for item in job['description']:
            st.markdown(f"- {item}")

# Line separator
st.divider()

# Education
st.markdown("###### Education")
st.write("🎓 BSc in Computer Science | Egerton University | 2022")

#Projects
st.markdown("######  Projects")

# Project 1: Solo Project - Taxi Hailing App
with st.expander("🚕 Taxi Hailing App (Solo Project)"):
    st.write("Developed a taxi hailing app that connects drivers and passengers, allowing for real-time booking and tracking of rides.")
    skill_pills = " ".join([f'<span class="skill-pill">{skill}</span>' for skill in ["Python", "Mobile App Development", "Real-time Data Processing", "User Interface Design"]])
    st.markdown(skill_pills, unsafe_allow_html=True)

# Project 2: Group Project - Milk Shop Management Web App
with st.expander("🥛 Milk Shop Management Web App (Group Project)"):
    st.write("Created a web application to help manage a milk shop within the university, including inventory management, sales tracking, and customer orders.")
    skill_pills = " ".join([f'<span class="skill-pill">{skill}</span>' for skill in ["Web Development", "Database Management", "Inventory Management", "User Experience Design"]])
    st.markdown(skill_pills, unsafe_allow_html=True)

# Project 3: Solo Project - Data Analysis Dashboard
with st.expander("📊 Data Analysis Dashboard (Solo Project)"):
    st.write("Built an interactive data analysis dashboard to visualize and analyze various datasets, providing insights and trends.")
    skill_pills = " ".join([f'<span class="skill-pill">{skill}</span>' for skill in ["Data Visualization", "Python", "SQL", "Data Analysis", "Dashboard Development"]])
    st.markdown(skill_pills, unsafe_allow_html=True)

# Line separator
st.divider()


# Section header
st.markdown("###### Things I Do on the Side")

# Define the tools and their descriptions
tools = {
    "Graphic Design": [
        {
            "name": "Adobe Creative Suite",
            "svg": """<svg viewBox="0 0 240 234" xmlns="http://www.w3.org/2000/svg" width="50" height="50"><path d="M42.5 0h155C221 0 240 19 240 42.5v149c0 23.5-19 42.5-42.5 42.5h-155C19 234 0 215 0 191.5v-149C0 19 19 0 42.5 0z" fill="#001e36"/><g fill="#31a8ff"><path d="M54 164.1V61.2c0-.7.3-1.1 1-1.1 1.7 0 3.3 0 5.6-.1 2.4-.1 4.9-.1 7.6-.2s5.6-.1 8.7-.2 6.1-.1 9.1-.1c8.2 0 15 1 20.6 3.1 5 1.7 9.6 4.5 13.4 8.2 3.2 3.2 5.7 7.1 7.3 11.4 1.5 4.2 2.3 8.5 2.3 13 0 8.6-2 15.7-6 21.3s-9.6 9.8-16.1 12.2c-6.8 2.5-14.3 3.4-22.5 3.4-2.4 0-4 0-5-.1s-2.4-.1-4.3-.1V164c.1.7-.4 1.3-1.1 1.4H55.2c-.8 0-1.2-.4-1.2-1.3zm21.8-84.7V113c1.4.1 2.7.2 3.9.2H85c3.9 0 7.8-.6 11.5-1.8 3.2-.9 6-2.8 8.2-5.3 2.1-2.5 3.1-5.9 3.1-10.3.1-3.1-.7-6.2-2.3-8.9-1.7-2.6-4.1-4.6-7-5.7-3.7-1.5-7.7-2.1-11.8-2-2.6 0-4.9 0-6.8.1-2-.1-3.4 0-4.1.1zM192 106.9c-3-1.6-6.2-2.7-9.6-3.4-3.7-.8-7.4-1.3-11.2-1.3-2-.1-4.1.2-6 .7-1.3.3-2.4 1-3.1 2-.5.8-.8 1.8-.8 2.7s.4 1.8 1 2.6c.9 1.1 2.1 2 3.4 2.7 2.3 1.2 4.7 2.3 7.1 3.3 5.4 1.8 10.6 4.3 15.4 7.3 3.3 2.1 6 4.9 7.9 8.3 1.6 3.2 2.4 6.7 2.3 10.3.1 4.7-1.3 9.4-3.9 13.3-2.8 4-6.7 7.1-11.2 8.9-4.9 2.1-10.9 3.2-18.1 3.2-4.6 0-9.1-.4-13.6-1.3-3.5-.6-7-1.7-10.2-3.2-.7-.4-1.2-1.1-1.1-1.9v-17.4c0-.3.1-.7.4-.9s.6-.1.9.1c3.9 2.3 8 3.9 12.4 4.9 3.8 1 7.8 1.5 11.8 1.5 3.8 0 6.5-.5 8.3-1.4 1.6-.7 2.7-2.4 2.7-4.2 0-1.4-.8-2.7-2.4-4s-4.9-2.8-9.8-4.7c-5.1-1.8-9.8-4.2-14.2-7.2-3.1-2.2-5.7-5.1-7.6-8.5-1.6-3.2-2.4-6.7-2.3-10.2 0-4.3 1.2-8.4 3.4-12.1 2.5-4 6.2-7.2 10.5-9.2 4.7-2.4 10.6-3.5 17.7-3.5 4.1 0 8.3.3 12.4.9 3 .4 5.9 1.2 8.6 2.3.4.1.8.5 1 .9.1.4.2.8.2 1.2v16.3c0 .4-.2.8-.5 1-.9.2-1.4.2-1.8 0z"/></g></svg>""",
            "description": "Designing logos, posters, social media graphics, and T-Shirt Designs.",
        },
        {
            "name": "Canva",
            "svg": """<svg height="50" width="80" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="-0.010000000000005116 -0.03 305.43 97.95"><linearGradient id="b" gradientUnits="userSpaceOnUse" x1="302.104" x2="47.994" y1="99.623" y2="39.143"><stop offset="0" stop-color="#7d2ae7"/><stop offset=".77" stop-color="#7d2ae7"/><stop offset="1" stop-color="#7d2ae7" stop-opacity="0"/></linearGradient><linearGradient id="a"><stop offset="0" stop-color="#6420ff"/><stop offset="1" stop-color="#6420ff" stop-opacity="0"/></linearGradient><radialGradient id="c" cx="-845.572" cy="27.009" gradientTransform="matrix(420 -432 287.1025 279.12743 347542.61 -372723.723)" gradientUnits="userSpaceOnUse" r=".15" xlink:href="#a"/><radialGradient id="d" cx="-843.93" cy="26.012" gradientTransform="matrix(1168 104 -82.89013 930.91997 987875.733 63622.988)" gradientUnits="userSpaceOnUse" r=".15"><stop offset=".25" stop-color="#00c4cc"/><stop offset="1" stop-color="#00c4cc" stop-opacity="0"/></radialGradient><radialGradient id="e" cx="-845.227" cy="26.889" gradientTransform="matrix(588.50003 -473.99996 324.1088 402.40096 488825.82 -411362.899)" gradientUnits="userSpaceOnUse" r=".15" xlink:href="#a"/><radialGradient id="f" cx="-844.454" cy="27.094" gradientTransform="matrix(727.99996 -496.00006 339.14786 497.78145 605588.091 -432219.404)" gradientUnits="userSpaceOnUse" r=".15" xlink:href="#a"/><radialGradient id="g" cx="-844.248" cy="25.519" gradientTransform="matrix(1699.99998 376.00007 -461.14867 2084.98028 1447017.579 264243.99)" gradientUnits="userSpaceOnUse" r=".15"><stop offset="0" stop-color="#00c4cc" stop-opacity=".73"/><stop offset="0" stop-color="#00c4cc"/><stop offset="1" stop-color="#00c4cc" stop-opacity="0"/></radialGradient><path d="M303.3 66.97a1.34 1.34 0 0 0-1.24 1c-3.13 8.93-7.36 14.25-10.84 14.25-2 0-2.81-2.23-2.81-5.73 0-8.75 5.24-27.3 7.88-35.76.292-.88.46-1.795.5-2.72 0-2.46-1.34-3.67-4.67-3.67-3.59 0-7.45 1.4-11.21 8-1.3-5.8-5.22-8.34-10.71-8.34-6.34 0-12.46 4.08-17.5 10.69s-11 8.78-15.42 7.71c3.21-7.85 4.4-13.71 4.4-18.07 0-6.83-3.37-10.95-8.83-10.95-8.29 0-13.07 7.91-13.07 16.23 0 6.43 2.92 13 9.33 16.25-5.38 12.16-13.22 23.15-16.2 23.15-3.85 0-5-18.83-4.76-32.3.14-7.73.78-8.12.78-10.46 0-1.34-.87-2.26-4.37-2.26-8.15 0-10.67 6.9-11.06 14.83a39.07 39.07 0 0 1-1.4 8.9c-3.41 12.16-10.43 21.38-15 21.38-2.12 0-2.7-2.12-2.7-4.9 0-8.75 4.9-19.68 4.9-29 0-6.86-3-11.19-8.67-11.19-6.67 0-15.5 7.94-23.85 22.82 2.75-11.39 3.88-22.42-4.26-22.42a11 11 0 0 0-5.05 1.31 2.87 2.87 0 0 0-1.65 2.78c.78 12.13-9.77 43.19-19.78 43.19-1.82 0-2.7-2-2.7-5.15 0-8.77 5.22-27.27 7.85-35.75a10.05 10.05 0 0 0 .52-2.87c0-2.32-1.44-3.51-4.69-3.51-3.57 0-7.45 1.36-11.19 7.94-1.31-5.8-5.24-8.34-10.72-8.34-9 0-19 9.51-23.46 21.91-5.91 16.55-17.82 32.54-33.86 32.54-14.55 0-22.23-12.11-22.23-31.24 0-27.63 20.28-50.2 35.32-50.2 7.19 0 10.63 4.58 10.63 11.61 0 8.51-4.75 12.46-4.75 15.7 0 1 .82 2 2.46 2 6.54 0 14.23-7.68 14.23-18.16S64.92-.03 49.87-.03c-24.86 0-49.88 25-49.88 57.07 0 25.5 12.58 40.88 34.34 40.88 14.84 0 27.81-11.54 34.8-25 .79 11.16 5.86 17 13.59 17 6.87 0 12.43-4.09 16.68-11.29 1.63 7.53 6 11.21 11.61 11.21 6.46 0 11.87-4.09 17-11.7-.08 6 1.28 11.59 6.46 11.59 2.44 0 5.36-.57 5.88-2.7 5.45-22.54 18.92-40.94 23-40.94 1.22 0 1.56 1.18 1.56 2.57 0 6.12-4.32 18.68-4.32 26.69 0 8.66 3.68 14.39 11.29 14.39 8.43 0 17-10.32 22.71-25.41 1.79 14.1 5.65 25.47 11.7 25.47 7.42 0 20.6-15.62 28.59-32.16a17.24 17.24 0 0 0 12.35-2.9 42.62 42.62 0 0 0-3.05 15.53c0 15.35 7.33 19.65 13.64 19.65 6.86 0 12.42-4.09 16.68-11.29 1.4 6.49 5 11.19 11.59 11.19 10.32 0 19.29-10.55 19.29-19.21.04-2.28-.94-3.64-2.08-3.64zM89.03 81.42c-4.17 0-5.8-4.2-5.8-10.46 0-10.87 7.44-29 15.3-29 3.44 0 4.73 4 4.73 9 0 11.01-7.07 30.46-14.23 30.46zm142.8-32.45a16.55 16.55 0 0 1-3.39-10.58c0-4.43 1.62-8.17 3.56-8.17s2.54 1.91 2.54 4.57c-.01 4.44-1.6 10.93-2.71 14.18zm32.33 32.45c-4.17 0-5.8-4.83-5.8-10.46 0-10.49 7.44-29 15.36-29 3.44 0 4.66 4 4.66 9 0 11.01-6.95 30.46-14.22 30.46z" fill="url(#b)"/><path d="M303.3 66.97a1.34 1.34 0 0 0-1.24 1c-3.13 8.93-7.36 14.25-10.84 14.25-2 0-2.81-2.23-2.81-5.73 0-8.75 5.24-27.3 7.88-35.76.292-.88.46-1.795.5-2.72 0-2.46-1.34-3.67-4.67-3.67-3.59 0-7.45 1.4-11.21 8-1.3-5.8-5.22-8.34-10.71-8.34-6.34 0-12.46 4.08-17.5 10.69s-11 8.78-15.42 7.71c3.21-7.85 4.4-13.71 4.4-18.07 0-6.83-3.37-10.95-8.83-10.95-8.29 0-13.07 7.91-13.07 16.23 0 6.43 2.92 13 9.33 16.25-5.38 12.16-13.22 23.15-16.2 23.15-3.85 0-5-18.83-4.76-32.3.14-7.73.78-8.12.78-10.46 0-1.34-.87-2.26-4.37-2.26-8.15 0-10.67 6.9-11.06 14.83a39.07 39.07 0 0 1-1.4 8.9c-3.41 12.16-10.43 21.38-15 21.38-2.12 0-2.7-2.12-2.7-4.9 0-8.75 4.9-19.68 4.9-29 0-6.86-3-11.19-8.67-11.19-6.67 0-15.5 7.94-23.85 22.82 2.75-11.39 3.88-22.42-4.26-22.42a11 11 0 0 0-5.05 1.31 2.87 2.87 0 0 0-1.65 2.78c.78 12.13-9.77 43.19-19.78 43.19-1.82 0-2.7-2-2.7-5.15 0-8.77 5.22-27.27 7.85-35.75a10.05 10.05 0 0 0 .52-2.87c0-2.32-1.44-3.51-4.69-3.51-3.57 0-7.45 1.36-11.19 7.94-1.31-5.8-5.24-8.34-10.72-8.34-9 0-19 9.51-23.46 21.91-5.91 16.55-17.82 32.54-33.86 32.54-14.55 0-22.23-12.11-22.23-31.24 0-27.63 20.28-50.2 35.32-50.2 7.19 0 10.63 4.58 10.63 11.61 0 8.51-4.75 12.46-4.75 15.7 0 1 .82 2 2.46 2 6.54 0 14.23-7.68 14.23-18.16S64.92-.03 49.87-.03c-24.86 0-49.88 25-49.88 57.07 0 25.5 12.58 40.88 34.34 40.88 14.84 0 27.81-11.54 34.8-25 .79 11.16 5.86 17 13.59 17 6.87 0 12.43-4.09 16.68-11.29 1.63 7.53 6 11.21 11.61 11.21 6.46 0 11.87-4.09 17-11.7-.08 6 1.28 11.59 6.46 11.59 2.44 0 5.36-.57 5.88-2.7 5.45-22.54 18.92-40.94 23-40.94 1.22 0 1.56 1.18 1.56 2.57 0 6.12-4.32 18.68-4.32 26.69 0 8.66 3.68 14.39 11.29 14.39 8.43 0 17-10.32 22.71-25.41 1.79 14.1 5.65 25.47 11.7 25.47 7.42 0 20.6-15.62 28.59-32.16a17.24 17.24 0 0 0 12.35-2.9 42.62 42.62 0 0 0-3.05 15.53c0 15.35 7.33 19.65 13.64 19.65 6.86 0 12.42-4.09 16.68-11.29 1.4 6.49 5 11.19 11.59 11.19 10.32 0 19.29-10.55 19.29-19.21.04-2.28-.94-3.64-2.08-3.64zM89.03 81.42c-4.17 0-5.8-4.2-5.8-10.46 0-10.87 7.44-29 15.3-29 3.44 0 4.73 4 4.73 9 0 11.01-7.07 30.46-14.23 30.46zm142.8-32.45a16.55 16.55 0 0 1-3.39-10.58c0-4.43 1.62-8.17 3.56-8.17s2.54 1.91 2.54 4.57c-.01 4.44-1.6 10.93-2.71 14.18zm32.33 32.45c-4.17 0-5.8-4.83-5.8-10.46 0-10.49 7.44-29 15.36-29 3.44 0 4.66 4 4.66 9 0 11.01-6.95 30.46-14.22 30.46z" fill="url(#c)"/><path d="M303.3 66.97a1.34 1.34 0 0 0-1.24 1c-3.13 8.93-7.36 14.25-10.84 14.25-2 0-2.81-2.23-2.81-5.73 0-8.75 5.24-27.3 7.88-35.76.292-.88.46-1.795.5-2.72 0-2.46-1.34-3.67-4.67-3.67-3.59 0-7.45 1.4-11.21 8-1.3-5.8-5.22-8.34-10.71-8.34-6.34 0-12.46 4.08-17.5 10.69s-11 8.78-15.42 7.71c3.21-7.85 4.4-13.71 4.4-18.07 0-6.83-3.37-10.95-8.83-10.95-8.29 0-13.07 7.91-13.07 16.23 0 6.43 2.92 13 9.33 16.25-5.38 12.16-13.22 23.15-16.2 23.15-3.85 0-5-18.83-4.76-32.3.14-7.73.78-8.12.78-10.46 0-1.34-.87-2.26-4.37-2.26-8.15 0-10.67 6.9-11.06 14.83a39.07 39.07 0 0 1-1.4 8.9c-3.41 12.16-10.43 21.38-15 21.38-2.12 0-2.7-2.12-2.7-4.9 0-8.75 4.9-19.68 4.9-29 0-6.86-3-11.19-8.67-11.19-6.67 0-15.5 7.94-23.85 22.82 2.75-11.39 3.88-22.42-4.26-22.42a11 11 0 0 0-5.05 1.31 2.87 2.87 0 0 0-1.65 2.78c.78 12.13-9.77 43.19-19.78 43.19-1.82 0-2.7-2-2.7-5.15 0-8.77 5.22-27.27 7.85-35.75a10.05 10.05 0 0 0 .52-2.87c0-2.32-1.44-3.51-4.69-3.51-3.57 0-7.45 1.36-11.19 7.94-1.31-5.8-5.24-8.34-10.72-8.34-9 0-19 9.51-23.46 21.91-5.91 16.55-17.82 32.54-33.86 32.54-14.55 0-22.23-12.11-22.23-31.24 0-27.63 20.28-50.2 35.32-50.2 7.19 0 10.63 4.58 10.63 11.61 0 8.51-4.75 12.46-4.75 15.7 0 1 .82 2 2.46 2 6.54 0 14.23-7.68 14.23-18.16S64.92-.03 49.87-.03c-24.86 0-49.88 25-49.88 57.07 0 25.5 12.58 40.88 34.34 40.88 14.84 0 27.81-11.54 34.8-25 .79 11.16 5.86 17 13.59 17 6.87 0 12.43-4.09 16.68-11.29 1.63 7.53 6 11.21 11.61 11.21 6.46 0 11.87-4.09 17-11.7-.08 6 1.28 11.59 6.46 11.59 2.44 0 5.36-.57 5.88-2.7 5.45-22.54 18.92-40.94 23-40.94 1.22 0 1.56 1.18 1.56 2.57 0 6.12-4.32 18.68-4.32 26.69 0 8.66 3.68 14.39 11.29 14.39 8.43 0 17-10.32 22.71-25.41 1.79 14.1 5.65 25.47 11.7 25.47 7.42 0 20.6-15.62 28.59-32.16a17.24 17.24 0 0 0 12.35-2.9 42.62 42.62 0 0 0-3.05 15.53c0 15.35 7.33 19.65 13.64 19.65 6.86 0 12.42-4.09 16.68-11.29 1.4 6.49 5 11.19 11.59 11.19 10.32 0 19.29-10.55 19.29-19.21.04-2.28-.94-3.64-2.08-3.64zM89.03 81.42c-4.17 0-5.8-4.2-5.8-10.46 0-10.87 7.44-29 15.3-29 3.44 0 4.73 4 4.73 9 0 11.01-7.07 30.46-14.23 30.46zm142.8-32.45a16.55 16.55 0 0 1-3.39-10.58c0-4.43 1.62-8.17 3.56-8.17s2.54 1.91 2.54 4.57c-.01 4.44-1.6 10.93-2.71 14.18zm32.33 32.45c-4.17 0-5.8-4.83-5.8-10.46 0-10.49 7.44-29 15.36-29 3.44 0 4.66 4 4.66 9 0 11.01-6.95 30.46-14.22 30.46z" fill="url(#d)"/><path d="M303.3 66.97a1.34 1.34 0 0 0-1.24 1c-3.13 8.93-7.36 14.25-10.84 14.25-2 0-2.81-2.23-2.81-5.73 0-8.75 5.24-27.3 7.88-35.76.292-.88.46-1.795.5-2.72 0-2.46-1.34-3.67-4.67-3.67-3.59 0-7.45 1.4-11.21 8-1.3-5.8-5.22-8.34-10.71-8.34-6.34 0-12.46 4.08-17.5 10.69s-11 8.78-15.42 7.71c3.21-7.85 4.4-13.71 4.4-18.07 0-6.83-3.37-10.95-8.83-10.95-8.29 0-13.07 7.91-13.07 16.23 0 6.43 2.92 13 9.33 16.25-5.38 12.16-13.22 23.15-16.2 23.15-3.85 0-5-18.83-4.76-32.3.14-7.73.78-8.12.78-10.46 0-1.34-.87-2.26-4.37-2.26-8.15 0-10.67 6.9-11.06 14.83a39.07 39.07 0 0 1-1.4 8.9c-3.41 12.16-10.43 21.38-15 21.38-2.12 0-2.7-2.12-2.7-4.9 0-8.75 4.9-19.68 4.9-29 0-6.86-3-11.19-8.67-11.19-6.67 0-15.5 7.94-23.85 22.82 2.75-11.39 3.88-22.42-4.26-22.42a11 11 0 0 0-5.05 1.31 2.87 2.87 0 0 0-1.65 2.78c.78 12.13-9.77 43.19-19.78 43.19-1.82 0-2.7-2-2.7-5.15 0-8.77 5.22-27.27 7.85-35.75a10.05 10.05 0 0 0 .52-2.87c0-2.32-1.44-3.51-4.69-3.51-3.57 0-7.45 1.36-11.19 7.94-1.31-5.8-5.24-8.34-10.72-8.34-9 0-19 9.51-23.46 21.91-5.91 16.55-17.82 32.54-33.86 32.54-14.55 0-22.23-12.11-22.23-31.24 0-27.63 20.28-50.2 35.32-50.2 7.19 0 10.63 4.58 10.63 11.61 0 8.51-4.75 12.46-4.75 15.7 0 1 .82 2 2.46 2 6.54 0 14.23-7.68 14.23-18.16S64.92-.03 49.87-.03c-24.86 0-49.88 25-49.88 57.07 0 25.5 12.58 40.88 34.34 40.88 14.84 0 27.81-11.54 34.8-25 .79 11.16 5.86 17 13.59 17 6.87 0 12.43-4.09 16.68-11.29 1.63 7.53 6 11.21 11.61 11.21 6.46 0 11.87-4.09 17-11.7-.08 6 1.28 11.59 6.46 11.59 2.44 0 5.36-.57 5.88-2.7 5.45-22.54 18.92-40.94 23-40.94 1.22 0 1.56 1.18 1.56 2.57 0 6.12-4.32 18.68-4.32 26.69 0 8.66 3.68 14.39 11.29 14.39 8.43 0 17-10.32 22.71-25.41 1.79 14.1 5.65 25.47 11.7 25.47 7.42 0 20.6-15.62 28.59-32.16a17.24 17.24 0 0 0 12.35-2.9 42.62 42.62 0 0 0-3.05 15.53c0 15.35 7.33 19.65 13.64 19.65 6.86 0 12.42-4.09 16.68-11.29 1.4 6.49 5 11.19 11.59 11.19 10.32 0 19.29-10.55 19.29-19.21.04-2.28-.94-3.64-2.08-3.64zM89.03 81.42c-4.17 0-5.8-4.2-5.8-10.46 0-10.87 7.44-29 15.3-29 3.44 0 4.73 4 4.73 9 0 11.01-7.07 30.46-14.23 30.46zm142.8-32.45a16.55 16.55 0 0 1-3.39-10.58c0-4.43 1.62-8.17 3.56-8.17s2.54 1.91 2.54 4.57c-.01 4.44-1.6 10.93-2.71 14.18zm32.33 32.45c-4.17 0-5.8-4.83-5.8-10.46 0-10.49 7.44-29 15.36-29 3.44 0 4.66 4 4.66 9 0 11.01-6.95 30.46-14.22 30.46z" fill="url(#e)"/><path d="M303.3 66.97a1.34 1.34 0 0 0-1.24 1c-3.13 8.93-7.36 14.25-10.84 14.25-2 0-2.81-2.23-2.81-5.73 0-8.75 5.24-27.3 7.88-35.76.292-.88.46-1.795.5-2.72 0-2.46-1.34-3.67-4.67-3.67-3.59 0-7.45 1.4-11.21 8-1.3-5.8-5.22-8.34-10.71-8.34-6.34 0-12.46 4.08-17.5 10.69s-11 8.78-15.42 7.71c3.21-7.85 4.4-13.71 4.4-18.07 0-6.83-3.37-10.95-8.83-10.95-8.29 0-13.07 7.91-13.07 16.23 0 6.43 2.92 13 9.33 16.25-5.38 12.16-13.22 23.15-16.2 23.15-3.85 0-5-18.83-4.76-32.3.14-7.73.78-8.12.78-10.46 0-1.34-.87-2.26-4.37-2.26-8.15 0-10.67 6.9-11.06 14.83a39.07 39.07 0 0 1-1.4 8.9c-3.41 12.16-10.43 21.38-15 21.38-2.12 0-2.7-2.12-2.7-4.9 0-8.75 4.9-19.68 4.9-29 0-6.86-3-11.19-8.67-11.19-6.67 0-15.5 7.94-23.85 22.82 2.75-11.39 3.88-22.42-4.26-22.42a11 11 0 0 0-5.05 1.31 2.87 2.87 0 0 0-1.65 2.78c.78 12.13-9.77 43.19-19.78 43.19-1.82 0-2.7-2-2.7-5.15 0-8.77 5.22-27.27 7.85-35.75a10.05 10.05 0 0 0 .52-2.87c0-2.32-1.44-3.51-4.69-3.51-3.57 0-7.45 1.36-11.19 7.94-1.31-5.8-5.24-8.34-10.72-8.34-9 0-19 9.51-23.46 21.91-5.91 16.55-17.82 32.54-33.86 32.54-14.55 0-22.23-12.11-22.23-31.24 0-27.63 20.28-50.2 35.32-50.2 7.19 0 10.63 4.58 10.63 11.61 0 8.51-4.75 12.46-4.75 15.7 0 1 .82 2 2.46 2 6.54 0 14.23-7.68 14.23-18.16S64.92-.03 49.87-.03c-24.86 0-49.88 25-49.88 57.07 0 25.5 12.58 40.88 34.34 40.88 14.84 0 27.81-11.54 34.8-25 .79 11.16 5.86 17 13.59 17 6.87 0 12.43-4.09 16.68-11.29 1.63 7.53 6 11.21 11.61 11.21 6.46 0 11.87-4.09 17-11.7-.08 6 1.28 11.59 6.46 11.59 2.44 0 5.36-.57 5.88-2.7 5.45-22.54 18.92-40.94 23-40.94 1.22 0 1.56 1.18 1.56 2.57 0 6.12-4.32 18.68-4.32 26.69 0 8.66 3.68 14.39 11.29 14.39 8.43 0 17-10.32 22.71-25.41 1.79 14.1 5.65 25.47 11.7 25.47 7.42 0 20.6-15.62 28.59-32.16a17.24 17.24 0 0 0 12.35-2.9 42.62 42.62 0 0 0-3.05 15.53c0 15.35 7.33 19.65 13.64 19.65 6.86 0 12.42-4.09 16.68-11.29 1.4 6.49 5 11.19 11.59 11.19 10.32 0 19.29-10.55 19.29-19.21.04-2.28-.94-3.64-2.08-3.64zM89.03 81.42c-4.17 0-5.8-4.2-5.8-10.46 0-10.87 7.44-29 15.3-29 3.44 0 4.73 4 4.73 9 0 11.01-7.07 30.46-14.23 30.46zm142.8-32.45a16.55 16.55 0 0 1-3.39-10.58c0-4.43 1.62-8.17 3.56-8.17s2.54 1.91 2.54 4.57c-.01 4.44-1.6 10.93-2.71 14.18zm32.33 32.45c-4.17 0-5.8-4.83-5.8-10.46 0-10.49 7.44-29 15.36-29 3.44 0 4.66 4 4.66 9 0 11.01-6.95 30.46-14.22 30.46z" fill="url(#f)"/><path d="M303.3 66.97a1.34 1.34 0 0 0-1.24 1c-3.13 8.93-7.36 14.25-10.84 14.25-2 0-2.81-2.23-2.81-5.73 0-8.75 5.24-27.3 7.88-35.76.292-.88.46-1.795.5-2.72 0-2.46-1.34-3.67-4.67-3.67-3.59 0-7.45 1.4-11.21 8-1.3-5.8-5.22-8.34-10.71-8.34-6.34 0-12.46 4.08-17.5 10.69s-11 8.78-15.42 7.71c3.21-7.85 4.4-13.71 4.4-18.07 0-6.83-3.37-10.95-8.83-10.95-8.29 0-13.07 7.91-13.07 16.23 0 6.43 2.92 13 9.33 16.25-5.38 12.16-13.22 23.15-16.2 23.15-3.85 0-5-18.83-4.76-32.3.14-7.73.78-8.12.78-10.46 0-1.34-.87-2.26-4.37-2.26-8.15 0-10.67 6.9-11.06 14.83a39.07 39.07 0 0 1-1.4 8.9c-3.41 12.16-10.43 21.38-15 21.38-2.12 0-2.7-2.12-2.7-4.9 0-8.75 4.9-19.68 4.9-29 0-6.86-3-11.19-8.67-11.19-6.67 0-15.5 7.94-23.85 22.82 2.75-11.39 3.88-22.42-4.26-22.42a11 11 0 0 0-5.05 1.31 2.87 2.87 0 0 0-1.65 2.78c.78 12.13-9.77 43.19-19.78 43.19-1.82 0-2.7-2-2.7-5.15 0-8.77 5.22-27.27 7.85-35.75a10.05 10.05 0 0 0 .52-2.87c0-2.32-1.44-3.51-4.69-3.51-3.57 0-7.45 1.36-11.19 7.94-1.31-5.8-5.24-8.34-10.72-8.34-9 0-19 9.51-23.46 21.91-5.91 16.55-17.82 32.54-33.86 32.54-14.55 0-22.23-12.11-22.23-31.24 0-27.63 20.28-50.2 35.32-50.2 7.19 0 10.63 4.58 10.63 11.61 0 8.51-4.75 12.46-4.75 15.7 0 1 .82 2 2.46 2 6.54 0 14.23-7.68 14.23-18.16S64.92-.03 49.87-.03c-24.86 0-49.88 25-49.88 57.07 0 25.5 12.58 40.88 34.34 40.88 14.84 0 27.81-11.54 34.8-25 .79 11.16 5.86 17 13.59 17 6.87 0 12.43-4.09 16.68-11.29 1.63 7.53 6 11.21 11.61 11.21 6.46 0 11.87-4.09 17-11.7-.08 6 1.28 11.59 6.46 11.59 2.44 0 5.36-.57 5.88-2.7 5.45-22.54 18.92-40.94 23-40.94 1.22 0 1.56 1.18 1.56 2.57 0 6.12-4.32 18.68-4.32 26.69 0 8.66 3.68 14.39 11.29 14.39 8.43 0 17-10.32 22.71-25.41 1.79 14.1 5.65 25.47 11.7 25.47 7.42 0 20.6-15.62 28.59-32.16a17.24 17.24 0 0 0 12.35-2.9 42.62 42.62 0 0 0-3.05 15.53c0 15.35 7.33 19.65 13.64 19.65 6.86 0 12.42-4.09 16.68-11.29 1.4 6.49 5 11.19 11.59 11.19 10.32 0 19.29-10.55 19.29-19.21.04-2.28-.94-3.64-2.08-3.64zM89.03 81.42c-4.17 0-5.8-4.2-5.8-10.46 0-10.87 7.44-29 15.3-29 3.44 0 4.73 4 4.73 9 0 11.01-7.07 30.46-14.23 30.46zm142.8-32.45a16.55 16.55 0 0 1-3.39-10.58c0-4.43 1.62-8.17 3.56-8.17s2.54 1.91 2.54 4.57c-.01 4.44-1.6 10.93-2.71 14.18zm32.33 32.45c-4.17 0-5.8-4.83-5.8-10.46 0-10.49 7.44-29 15.36-29 3.44 0 4.66 4 4.66 9 0 11.01-6.95 30.46-14.22 30.46z" fill="url(#g)"/></svg>""",
            "description": "Designing quick posters and social media posts for brands.",
        },
        {
            "name": "Affinity Suite",
            "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 675.7 614.9" width="50" fill="#0097e6" height="50"><path d="M263.7 0h106.4l8.9 15.5h30.5l266.1 461-57.3 97.7H385.4l23.6 40.7h-10.3l-23.6-40.7H86l-14.8-26H52.9L0 456.6h.1L67.9 339l62.8-36.2 103.9-179.9-20.9-36.2 50-86.7zm62.7 159.1L142.6 476.6h175.9l-20.3-35.1 191.7.2-163.5-282.6z"/></svg>""",
            "description": "Designing quick posters and social media posts for brands.",
        },
    ],
    "Web Development": [
        {
            "name": "WordPress",
            "svg": """<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="8.399 8.4 51.2 51.2"><path fill="#0097e6" d="M34 59.6C19.813 59.6 8.293 48.293 8.4 34 8.507 19.707 19.28 8.4 34 8.4c14.721 0 25.6 11.52 25.6 25.6S48.187 59.6 34 59.6zm7.573-3.947l-7.253-19.52-6.827 19.947c5.014 1.174 8.427 1.493 14.08-.427zm-17.706-1.066l-10.88-29.76c-1.494 3.2-1.813 5.867-2.027 9.173.107 8.746 5.013 16.746 12.907 20.587zM56.934 34c.106-5.653-2.453-10.133-2.667-10.773.214 4.374-.427 6.613-1.173 9.067l-7.467 21.44C55.014 48.08 56.826 39.653 57.04 34h-.106zm-23.68-.96l-3.627-9.92-2.667-.213c-1.066-.747-.427-1.92.32-1.92 4.8.32 7.466.32 12.267 0 1.174 0 1.493 1.707.106 1.92l-2.56.213 8.319 24.533 3.946-13.44c.214-5.866-1.387-6.506-3.52-10.773-1.707-3.307.107-6.507 3.414-6.613-2.668-2.56-8.107-5.76-15.254-5.867s-14.72 3.52-19.2 10.347l7.894-.213c.96.427.533 1.813 0 1.92l-2.773.213 8.32 24.96 5.015-15.147z"/></svg>""",
            "description": "Building and managing websites for blogs and businesses.",
        },
        {
            "name": "Wix",
            "svg": """<svg height="50" width="50" xmlns="http://www.w3.org/2000/svg" viewBox="0 -2.4 311 125.2" width="50" height="50"><path d="M178 2.3c-6 3-8.6 8.6-8.6 23.8 0 0 3-3 7.8-4.8 3.5-1.3 6-3 7.8-4.3 5.2-3.9 6-8.6 6-16.8-.1 0-8.3-.5-13 2.1z" fill="#fbbd71"/><path d="M141.3 5.8c-5.2 4.3-6.5 11.7-6.5 11.7L118 81.9l-13.8-52.7c-1.3-5.6-3.9-12.5-7.8-17.3-4.8-6.1-14.8-6.5-16-6.5-.9 0-10.8.4-16 6.5-3.9 4.8-6.5 11.7-7.8 17.3l-13 52.7-16.8-64.4s-1.3-6.9-6.5-11.7C12.1-1.6 0 .2 0 .2l32 120.5s10.4.9 15.6-1.7c6.9-3.5 10.4-6 14.3-22.5C65.8 81.8 76.2 39 77 36c.4-1.3 1.3-5.2 3.9-5.2s3.5 3.5 3.9 5.2c.9 3 11.2 45.8 15.1 60.5 4.3 16.4 7.3 19 14.3 22.5 5.2 2.6 15.6 1.7 15.6 1.7L161.6.2s-12.1-1.7-20.3 5.6zM190.9 19.6s-2.2 3-6.5 5.6c-3 1.7-5.6 2.6-8.6 4.3-5.2 2.6-6.5 5.2-6.5 9.1V120.3s8.2.9 13.4-1.7c6.9-3.5 8.2-6.9 8.2-21.6V24.4zM270.4 60.7L311 .6s-16.8-3-25.5 4.8c-5.6 4.8-11.2 13.8-11.2 13.8l-14.7 21.6c-.9 1.3-1.7 2.2-3 2.2s-2.6-1.3-3-2.2l-14.7-21.6s-6-8.6-11.2-13.8C219.1-2.4 202.2.6 202.2.6l39.3 60-40.2 60s17.7 2.2 26.4-5.6c5.6-4.8 10.8-13 10.8-13l14.7-21.6c.9-1.3 1.7-2.2 3-2.2s2.6 1.3 3 2.2l14.7 21.6s5.6 8.2 10.8 13c8.6 7.8 25.9 5.6 25.9 5.6z" fill="white"/></svg>""",
            "description": "Creating visually appealing websites with drag-and-drop functionality.",
        },
        {
            "name": "WooCommerce",
            "svg": """<svg width="50" height="50" viewBox="0 0 256 153" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid"><path d="M23.759 0h208.378C245.325 0 256 10.675 256 23.863v79.541c0 13.188-10.675 23.863-23.863 23.863H157.41l10.257 25.118-45.109-25.118H23.863c-13.187 0-23.862-10.675-23.862-23.863V23.863C-.104 10.78 10.57 0 23.759 0z" fill="#9B5C8F"/><path d="M14.578 21.75c1.457-1.978 3.642-3.018 6.556-3.226 5.308-.417 8.326 2.08 9.054 7.492 3.226 21.75 6.764 40.17 10.51 55.259l22.79-43.395c2.082-3.955 4.684-6.036 7.806-6.244 4.579-.312 7.388 2.601 8.533 8.741 2.602 13.84 5.932 25.6 9.886 35.59 2.706-26.432 7.285-45.476 13.737-57.235 1.56-2.914 3.85-4.371 6.868-4.58 2.394-.207 4.579.521 6.556 2.082 1.977 1.561 3.018 3.538 3.226 5.932.104 1.873-.208 3.434-1.04 4.995-4.059 7.493-7.39 20.085-10.095 37.567-2.601 16.963-3.538 30.18-2.914 39.65.209 2.6-.208 4.89-1.248 6.868-1.25 2.289-3.122 3.538-5.516 3.746-2.706.208-5.515-1.04-8.221-3.85-9.678-9.887-17.379-24.664-22.998-44.332-6.765 13.32-11.76 23.31-14.986 29.97-6.14 11.76-11.343 17.796-15.714 18.108-2.81.208-5.203-2.186-7.284-7.18-5.307-13.633-11.031-39.962-17.17-78.986-.417-2.706.207-5.1 1.664-6.972zm223.636 16.338c-3.746-6.556-9.262-10.51-16.65-12.072-1.978-.416-3.85-.624-5.62-.624-9.99 0-18.107 5.203-24.455 15.61-5.412 8.845-8.117 18.627-8.117 29.346 0 8.013 1.665 14.881 4.995 20.605 3.746 6.556 9.262 10.51 16.65 12.071 1.977.417 3.85.625 5.62.625 10.094 0 18.211-5.203 24.455-15.61 5.411-8.95 8.117-18.732 8.117-29.45.104-8.117-1.665-14.882-4.995-20.501zm-13.112 28.826c-1.457 6.868-4.059 11.967-7.91 15.401-3.017 2.706-5.827 3.85-8.428 3.33-2.498-.52-4.58-2.705-6.14-6.764-1.25-3.226-1.873-6.452-1.873-9.47 0-2.601.208-5.203.728-7.596.937-4.267 2.706-8.43 5.515-12.384 3.435-5.1 7.077-7.18 10.823-6.452 2.498.52 4.58 2.706 6.14 6.764 1.249 3.226 1.873 6.452 1.873 9.47 0 2.706-.208 5.307-.728 7.7zm-52.033-28.826c-3.746-6.556-9.366-10.51-16.65-12.072-1.977-.416-3.85-.624-5.62-.624-9.99 0-18.107 5.203-24.455 15.61-5.411 8.845-8.117 18.627-8.117 29.346 0 8.013 1.665 14.881 4.995 20.605 3.746 6.556 9.262 10.51 16.65 12.071 1.978.417 3.85.625 5.62.625 10.094 0 18.211-5.203 24.455-15.61 5.412-8.95 8.117-18.732 8.117-29.45 0-8.117-1.665-14.882-4.995-20.501zm-13.216 28.826c-1.457 6.868-4.059 11.967-7.909 15.401-3.018 2.706-5.828 3.85-8.43 3.33-2.497-.52-4.578-2.705-6.14-6.764-1.248-3.226-1.872-6.452-1.872-9.47 0-2.601.208-5.203.728-7.596.937-4.267 2.706-8.43 5.516-12.384 3.434-5.1 7.076-7.18 10.822-6.452 2.498.52 4.58 2.706 6.14 6.764 1.25 3.226 1.873 6.452 1.873 9.47.105 2.706-.208 5.307-.728 7.7z" fill="#FFF"/></svg>""",
            "description": "Setting up and managing e-commerce stores for clients.",
        },
        {
            "name": "Shopify",
            "svg": """<svg width="50" height="50" viewBox="0 0 256 292" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid"><path d="M223.774 57.34c-.201-1.46-1.48-2.268-2.537-2.357-1.055-.088-23.383-1.743-23.383-1.743s-15.507-15.395-17.209-17.099c-1.703-1.703-5.029-1.185-6.32-.805-.19.056-3.388 1.043-8.678 2.68-5.18-14.906-14.322-28.604-30.405-28.604-.444 0-.901.018-1.358.044C129.31 3.407 123.644.779 118.75.779c-37.465 0-55.364 46.835-60.976 70.635-14.558 4.511-24.9 7.718-26.221 8.133-8.126 2.549-8.383 2.805-9.45 10.462C21.3 95.806.038 260.235.038 260.235l165.678 31.042 89.77-19.42S223.973 58.8 223.775 57.34zM156.49 40.848l-14.019 4.339c.005-.988.01-1.96.01-3.023 0-9.264-1.286-16.723-3.349-22.636 8.287 1.04 13.806 10.469 17.358 21.32zm-27.638-19.483c2.304 5.773 3.802 14.058 3.802 25.238 0 .572-.005 1.095-.01 1.624-9.117 2.824-19.024 5.89-28.953 8.966 5.575-21.516 16.025-31.908 25.161-35.828zm-11.131-10.537c1.617 0 3.246.549 4.805 1.622-12.007 5.65-24.877 19.88-30.312 48.297l-22.886 7.088C75.694 46.16 90.81 10.828 117.72 10.828z" fill="#95BF46"/><path d="M221.237 54.983c-1.055-.088-23.383-1.743-23.383-1.743s-15.507-15.395-17.209-17.099c-.637-.634-1.496-.959-2.394-1.099l-12.527 256.233 89.762-19.418S223.972 58.8 223.774 57.34c-.201-1.46-1.48-2.268-2.537-2.357" fill="#5E8E3E"/><path d="M135.242 104.585l-11.069 32.926s-9.698-5.176-21.586-5.176c-17.428 0-18.305 10.937-18.305 13.693 0 15.038 39.2 20.8 39.2 56.024 0 27.713-17.577 45.558-41.277 45.558-28.44 0-42.984-17.7-42.984-17.7l7.615-25.160s14.95 12.835 27.565 12.835c8.243 0 11.596-6.49 11.596-11.232 0-19.616-32.16-20.491-32.16-52.724 0-27.129 19.472-53.382 58.778-53.382 15.145 0 22.627 4.338 22.627 4.338" fill="#FFF"/></svg>""",
            "description": "Building and Running Shopify stores.",
        },
    ],
}


# Function to display tools in columns
def display_tools(category, tools_list):
    st.markdown(f"**{category}**")
    cols = st.columns(len(tools_list))  # Create columns for each tool
    for i, tool in enumerate(tools_list):
        with cols[i]:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    {tool["svg"]}
                    <div style="margin-top: 10px;">
                        <strong>{tool["name"]}</strong>
                        <p style="font-size: 0.9em; color: #718093;">{tool["description"]}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Display Graphic Design tools
display_tools("Graphic Design", tools["Graphic Design"])

# Add some vertical space
st.write("")  # Spacer

# Display Web Development tools
display_tools("Web Development", tools["Web Development"])
