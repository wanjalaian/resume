import streamlit as st
from PIL import Image

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
        text-decoration: none;
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
st.subheader("About Me")
st.write(
    "Dynamic Data Analyst with a proven track record in leveraging data to deliver actionable insights, "
    "build dashboards, and drive strategic decisions. Experienced in Python, SQL, Tableau, and Power BI, "
    "with a strong focus on collaboration and cross-functional alignment to achieve organizational goals."
)

# Line separator
st.divider()

# Career Highlights
st.subheader("Career Highlights")

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

# Highlight 3: End-to-End Experimentation
with st.expander("🧪 End-to-End Experimentation"):
    st.write(
        "Led A/B testing and experimentation efforts to optimize product features. "
        "Designed experiments, analyzed results, and presented findings to stakeholders. "
        "Implemented data-driven changes that improved user engagement and conversion rates."
    )

# Highlight 4: Python & SQL Expertise
with st.expander("🐍 Python & SQL Expertise"):
    st.write(
        "Used Python for scripting, automation, and data analysis. "
        "Developed ETL pipelines to process and transform large datasets. "
        "Wrote complex SQL queries to extract and analyze data from relational databases."
    )

# Highlight 5: Collaboration with Cross-Functional Teams
with st.expander("🤝 Collaboration with Cross-Functional Teams"):
    st.write(
        "Worked closely with product and engineering teams to define data requirements. "
        "Collaborated on projects to ensure alignment between data analysis and business goals. "
        "Facilitated communication between technical and non-technical stakeholders."
    )

# Line separator
st.divider()

# Skills
st.subheader("Skills")
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
st.subheader("Work Experience")

# Work Experience
work_experience = [
    {
        "title": "Data Analyst",
        "company": "Reporthub Limited (Remote)",
        "duration": "Sep 2023 – Present",
        "skills": ["Data Analysis", "SQL", "Tableau", "Power BI", "Python"],
        "description": [
            "Built and maintained interactive dashboards using Tableau and Power BI.",
            "Developed and optimized SQL queries for actionable insights.",
            "Led ad-hoc analysis projects, identifying trends for business growth.",
            "Collaborated with cross-functional teams to define data requirements.",
        ],
    },
    {
        "title": "Web Developer",
        "company": "Byte Pulse Agency (Remote)",
        "duration": "May 2023 – Jul 2023",
        "skills": ["Web Development", "API Integration", "SQL", "Data Analysis", "Python"],
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
        "skills": ["Database Management", "SQL", "Data Analysis", "Reporting", "Automation"],
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
st.subheader("Education")
st.write("🎓 BSc in Computer Science | Egerton University | 2022")

#Projects
st.markdown("##### Projects")

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
