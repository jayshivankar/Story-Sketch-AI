from llm_helper import llm
from langchain_core.messages import HumanMessage

# Just for testing
final_prompt = "A panda wants to go to the moon "

def story_generator(prompt):
    global generated_story
    story_prompt = f"""
You are a friendly and imaginative children's story writer.

Please write a short and engaging story for kids aged 6 to 10 based on the idea: "{prompt}".

Make the story:
- Creative and magical 🌟
- Easy to understand (use simple language)
- Full of emotion and fun!
- Contain a positive message or moral (like kindness, bravery, teamwork)

Structure it like this:
- Start with a strong opening line
- Include a short adventure or journey
- End with a happy or heartwarming conclusion 😊

Use short paragraphs (2–4 lines) and include fun details kids will enjoy.
** Don't give any preamble. **
"""

    response = llm.invoke([
        HumanMessage(content=story_prompt)
    ])
    generated_story = response.content.strip()
    return generated_story

def scene_splitter(story_text):
    scene_splitter_prompt = f"""
    You are a helpful assistant that transforms a children's story into a list of meaningful, visually descriptive sentences — one for each major scene.

    Your job is to:
    - Read the story carefully
    - Identify key visual moments, actions, or emotional beats
    - Write short, self-contained, descriptive sentences (1–2 per scene)
    - Make them suitable for generating images or video clips (so they must be visual)

    Each sentence should:
    - Be clear, vivid, and grounded in the story
    - Avoid dialogue, but capture the moment
    - No preamble
    - Focus on **what could be shown in a picture**

    Output format:
    Scene 1: ...
    Scene 2: ...
    Scene 3: ...

    Here is the story:
    \"\"\"{story_text}\"\"\"
    """
    response = llm.invoke([
        HumanMessage(content=scene_splitter_prompt)
    ])
    generated_scenes = response.content.strip()
    return generated_scenes


if __name__ == "__main__":
    story = story_generator(final_prompt)
    print("\n🎉 Generated Story:\n")
    print(story)

    scenes = scene_splitter(generated_story)
    print("\n🎉 Generated Scenes:\n")
    print(scenes)

