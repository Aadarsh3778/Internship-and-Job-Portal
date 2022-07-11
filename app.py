import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    
    line = "-"*50 
    
    def internshala_func(role):
        try:
            internshala_url = f"https://internshala.com/internships/keywords-{role}/page-{0}"
            internshala_r = requests.get(internshala_url).content
        except Exception as e:
            st.header("Please! Check your Internet Connection....")
        internshala_soup = BeautifulSoup(internshala_r)

        internshala_coms = internshala_soup.find_all("div", class_="internship_meta")    
       
        for com in internshala_coms:

            try:
                internshala_company_name = com.find("div", class_="heading_6 company_name").text.replace("\n", "")
            except Exception as e:
                internshala_company_name = "None"
                #st.warning(e)
            try:
                internshala_role = com.find("div", class_="heading_4_5 profile").text.replace("\n","")
            except Exception as e:
                internshala_role = "None"
                #st.warning(e)
            try:
                internshala_location = com.find("a", class_="location_link view_detail_button").text
            except Exception as e:
                internshala_location = "None"
                #st.warning(e)
            try:
                internshala_stipend = com.find("span", class_ ="stipend").text.replace(" /month", "")
            except Exception as e:
                internshala_stipend = "None"
                #st.warning(e)
            try:
                internshala_info = com.find("a")["href"].replace(" ","")
            except Exception as e:
                internshala_info = "None"
                #st.warning(e)
                  
            
            f.write(f"Company Name : {internshala_company_name}\nRole : {internshala_role}\nLocation : {internshala_location}\nStipened : {internshala_stipend}\nMore Info : https://internshala.com/{internshala_info}\n{line}\n")
    
        f.close()
        
        
        
    def timejobs_func(role):
        
        try:
            url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={role}&txtLocation=#"
            r = requests.get(url).content
        except Exception as e:
            st.header("Please! Check your Internet Connection....")
        soup = BeautifulSoup(r)
    
        coms = soup.find_all("li", class_ ="clearfix job-bx wht-shd-bx")    
        for com in coms:
    
            try:
                timejobs_company_name = com.find("h3", class_ ="joblist-comp-name").text.replace("\n", "")
            except Exception as e:
                timejobs_company_name = "None"
                #st.warning(e)
            try:
                timejobs_role = com.find("h2").text.replace("\n", "")
            except Exception as e:
                timejobs_role = "None"
                #st.warning(e)
            try:
                timejobs_skills = com.find("span", class_ ="srp-skills").text.replace("\n", "")
            except Exception as e:
                timejobs_skills = "None"
                #st.warning(e)
            try:
                timejobs_info = com.find("a")["href"]
            except Exception as e:
                timejobs_info = "None"
                #st.warning(e)

            f.write(f"Company Name : {timejobs_company_name}\nRole : {timejobs_role}\nSkills : {timejobs_skills}\nMore Info : {timejobs_info}\n{line}\n")
    
        f.close()
        
        
        
        
    def indeed_func(role):

        try:
            url = f"https://in.indeed.com/jobs?q={role}&start={0}&vjk=54ae5b809131fd35"
            r = requests.get(url).content
        except Exception as e:
            st.header("Please! Check your Internet Connection....")
        soup = BeautifulSoup(r)

        coms = soup.find_all("div", class_="job_seen_beacon")     
        for com in coms:
            try:
                indeed_role = com.find("h2", class_="jobTitle").text
            except Exception as e:
                indeed_role = "None"
                #st.warning(e)
            try:
                indeed_info = com.find("a")["href"]
            except Exception as e:
                indeed_info = "None"
                #st.warning(e)
            try:
                indeed_company_name = com.find("span", class_="companyName").text
            except Exception as e:
                indeed_company_name = "None"
                #st.warning(e)
            try:
                indeed_location = com.find("div", class_="companyLocation").text
            except Exception as e:
                indeed_location = "None"
                #st.warning(e)
            try:
                indeed_stipend = com.find("div", class_="attribute_snippet").text.replace("₹", "")
            except Exception as e:
                indeed_stipend = "None"
                #st.warning(e)
                
            f.write(f"Company Name : {indeed_company_name}\nRole : {indeed_role}\nLocation : {indeed_location}\nStipened : {indeed_stipend}\nMore Info : https://in.indeed.com{indeed_info}\n{line}\n")
    
        f.close()

        
    
    
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Internship and Job Portal</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.info("Find jobs and internships from websites like indeed, internshala, jobtimes here in one")
    
    f = open("file.txt", "a")
      
    choice = st.selectbox("Choose: ",
    ['None', 'python', 'data science', 'web development', 'front end development', 'data analytics'])
    
    
    
    if choice == "python":
        internshala_func("python")
        f = open("file.txt", "r+")
        for i in f:
            st.write(i)
        f.truncate(0)

        indeed_func("python")
        f = open("file.txt", "r+")
        for i in f:
            st.write(i)
        f.truncate(0)
        
        timejobs_func("python")
        f = open("file.txt", "r+")
        for i in f:    
            st.write(i)
        f.truncate(0)
        

        
    elif choice == "data science":
        internshala_func("data science")
        f = open("file.txt", "r+")
        for i in f:
            st.write(i)
        f.truncate(0)

        indeed_func("data science")
        f = open("file.txt", "r+")
        for i in f:
            st.write(i)
        f.truncate(0)
        
        timejobs_func("data science")
        f = open("file.txt", "r+")
        for i in f:    
            st.write(i)
        f.truncate(0)
        

        
    elif choice == "web development":
        internshala_func("web development")
        f = open("file.txt", "r+")
        for i in f:
            st.write(i)
        f.truncate(0)

        indeed_func("web development")
        f = open("file.txt", "r+")
        for i in f:
            st.write(i)
        f.truncate(0)
        
        timejobs_func("web development")
        f = open("file.txt", "r+")
        for i in f:    
            st.write(i)
        f.truncate(0)
        

        
        
    elif choice == "front end development":
         internshala_func("front end development")
         f = open("file.txt", "r+")
         for i in f:
             st.write(i)
         f.truncate(0)

         indeed_func("front end development")
         f = open("file.txt", "r+")
         for i in f:
             st.write(i)
         f.truncate(0)
         
         timejobs_func("front end development")
         f = open("file.txt", "r+")
         for i in f:    
             st.write(i)
         f.truncate(0)
         

         
         
    elif choice == "data analytics":
         internshala_func("data analytics")
         f = open("file.txt", "r+")
         for i in f:
             st.write(i)
         f.truncate(0)

         indeed_func("data analytics")
         f = open("file.txt", "r+")
         for i in f:
             st.write(i)
         f.truncate(0)
         
         timejobs_func("data analytics")
         f = open("file.txt", "r+")
         for i in f:    
             st.write(i)
         f.truncate(0)
         

         
    elif choice == "None":
        st.header("Plesae Choose any Role.......")
    
        
        
     
    

if __name__ == "__main__":
    main()