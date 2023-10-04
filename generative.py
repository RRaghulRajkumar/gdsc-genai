"""
for mac:
pip install virtualenv
python -m venv myenv
source venv/bin/activate

for windows:
pip install virtualenv
python -m venv myenv
myenv\Scripts\activate
"""

import streamlit as st
import openai

#Set your openai API Key 
openai.api_key=st.secrets["openai_api"]
st.title("Generative AI")

#Input Text Box
prompt=st.text_area("Enter A Prompt:")
def generate_text(prompt):
    response=openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1200
    )
    return response.choices[0].text
#Button to generate text

if st.button("Generate"):
    if prompt:
        generate_text=generate_text(prompt)
        st.write("Generated Text")
        st.write(generate_text)
    else:
        st.warning("Please Enter a prompt")    