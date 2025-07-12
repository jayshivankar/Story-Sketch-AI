import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.exceptions import OutputParserException
from Frontend.main import final_prompt


def story_generator(final_prompt):
    story_prompt = f"""
    You are a friendly and imaginative children's story writer.

    Please write a short and engaging story for kids aged 6 to 10 based on the idea: "{final_prompt}".

    Make the story:
    - Creative and magical 🌟
    - Easy to understand (use simple language)
    - Full of emotion and fun!
    - Contain a positive message or moral (like kindness, bravery, teamwork)

    Structure it like this:
    - Start with a strong opening line
    - Include a short adventure or journey
    - End with a happy or heartwarming conclusion 😊

    Use short paragraphs (2-4 lines) and include fun details kids will enjoy.
    ** Don't give any preamble. **
    """
    if final_prompt:
        pt = PromptTemplate.from_template(story_prompt)
        chain = pt | llm
        response = chain.invoke({'final_prompt': final_prompt})

    return response

if __name__=="__main__":
    story_generator(final_prompt)