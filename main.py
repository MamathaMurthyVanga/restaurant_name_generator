import streamlit as st
import name_menu_generator

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))


if cuisine:
    response = name_menu_generator.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items")
    for item in menu_items:
        st.write("-", item)



# import streamlit as st
# import job_skill_generator

# st.title("Job Skills Finder")

# job_title = st.text_input("Enter a Job Title", placeholder="e.g., Backend Developer")

# if job_title:
#     response = job_skill_generator.generate_skills_for_job(job_title)
#     st.header(f"Skills for {job_title}")
#     skills = response['skills'].strip().split(",")
#     for skill in skills:
#         st.write("-", skill.strip())
