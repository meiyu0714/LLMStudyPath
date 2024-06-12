from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
# Load .env files
from dotenv import load_dotenv
# Argparse python special function to import things from command line
import argparse
#Because we will need pandas in our LLM generated Code. 
import pandas as pd

#.env file should contain your own open-ai api key
load_dotenv()

# command line example:
# python main.py task "adds up 1 to 10" language "python"
parser = argparse.ArgumentParser()
parser.add_argument("--file_path", default="students.xlsx")
parser.add_argument("--sheet_name", default="Sheet1")
parser.add_argument("--gpa_threshold", type=float, default=3.5)
parser.add_argument("--language", default="python")
args = parser.parse_args()

# if you do not put your api inside the .env file
# do it like this: llm = OpenAI( openai_api_key = )
llm = OpenAI()

code_prompt = PromptTemplate(
    input_variables=["file_path", "sheet_name", "gpa_threshold", "language"],
    template=(
        "Write a {language} function that reads an Excel file from '{file_path}', "
        "and returns the names of students whose GPA is higher than {gpa_threshold}. "
        "The Excel sheet is named '{sheet_name}' and contains columns '姓名' and 'GPA'."
    )
)

# Here we used a chain to create our function
code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code"
)

result = code_chain({
    "file_path": args.file_path,
    "sheet_name": args.sheet_name,
    "gpa_threshold": args.gpa_threshold,
    "language": args.language
})

# The result would be the map
generated_code = result["code"]

# Print the code for better check in the future
print(">>>>>> GENERATED CODE:")
print(generated_code)

# run the code 
exec(generated_code)

