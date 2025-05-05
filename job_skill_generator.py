from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from secret_key import groq_api_key

import os
os.environ['GROQ_API_KEY'] = groq_api_key

# Initialize LLaMA 3
llm = ChatGroq(temperature=0.5, model_name="llama3-8b-8192")

def generate_skills_for_job(job_title):
    prompt_template = PromptTemplate(
        input_variables=['job_title'],
        template="List the most important technical and soft skills required for a {job_title} role. Provide them as a comma-separated list."
    )

    job_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="skills")

    response = job_chain({'job_title': job_title})
    return response
