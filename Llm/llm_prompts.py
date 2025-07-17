from Llm.llm_helper import llm
from langchain_core.messages import HumanMessage

#  TEST INPUT
final_prompt = "A warrior dragon  "

def generate_story(prompt: str) -> str:
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
    response = llm.invoke([HumanMessage(content=story_prompt)])
    generated_story = response.content.strip()
    return generated_story


def extract_scenes(story_text: str) -> list[str]:
    scene_splitter_prompt = f"""
You are a helpful assistant that transforms a children's story into a list of vivid, visually descriptive, and fun-to-read sentences — one for each major scene.

Your job is to:
- Read the story carefully
- Identify key visual moments, actions, or emotional beats
- Write short, self-contained, descriptive sentences (1–2 per scene)
- Make them suitable for generating images or video clips (so they must be visual)
- Make sure they also sound delightful and imaginative when read aloud

🧸 IMPORTANT: In every scene you generate, include the main character’s name **and what they are**.  
For example: "Josh the panda", "Luna the fairy", or "Ember the dragon". This helps children visualize who they are.

🎉 Each sentence should:
- Be lively, playful, and spark the imagination
- Use child-friendly, expressive language
- Be clear, grounded in the story, and **avoid dialogue**
- Focus on what could be shown in a picture
- Have no preamble or explanation

📦 Output format:
Scene 1: ...
Scene 2: ...
Scene 3: ...

Here is the story:
\"\"\"{story_text}\"\"\"
"""

    response = llm.invoke([HumanMessage(content=scene_splitter_prompt)])
    raw_output = response.content.strip()
    scenes = [
        line.split(":", 1)[1].strip()
        for line in raw_output.splitlines()
        if line.lower().startswith("scene")
    ]
    return scenes



if __name__ == "__main__":

    story = generate_story(final_prompt)
    print("\n🎉 Generated Story:\n")
    print(story)

    scenes = extract_scenes(generated_story)
    print("\n🎉 Generated Scenes:\n")
    print(scenes)

