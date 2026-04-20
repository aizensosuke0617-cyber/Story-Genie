import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import time

# --- Page Configuration ---
st.set_page_config(page_title="StoryGenie AI", page_icon="✨", layout="wide")

# --- Initialize Session State ---
# This acts as the "memory" for our app so the story doesn't vanish when we click other buttons
if "story_content" not in st.session_state:
    st.session_state.story_content = ""
if "generation_time" not in st.session_state:
    st.session_state.generation_time = 0
if "used_prompt" not in st.session_state:
    st.session_state.used_prompt = ""

# --- UI Header ---
st.title("✨ StoryGenie: Personalized AI Storyteller")
st.markdown("Welcome to StoryGenie! Fill in the details on the left, and our local AI will craft a unique story just for you.")
st.divider()

# --- Sidebar / Input Section ---
with st.sidebar:
    st.header("📖 Story Elements")
    protagonist = st.text_input("Protagonist's Name", value="Alex")
    
    age_group = st.selectbox(
        "Target Age Group",
        ["Toddler (2-5 years)", "Children (6-12 years)", "Teenager (13-17 years)", "Adult (18+)"]
    )
    
    genre = st.selectbox(
        "Story Genre",
        ["Fantasy", "Sci-Fi", "Mystery", "Adventure", "Fairy Tale", "Horror"]
    )
    
    moral = st.text_area("Moral or Theme of the Story", value="The importance of friendship and bravery.")
    
    generate_btn = st.button("Generate My Story 🚀", type="primary", use_container_width=True)

# --- AI Logic Setup ---
@st.cache_resource
def load_llm():
    return Ollama(model="llama3")

llm = load_llm()

template = """
You are an expert, creative storyteller. Write a compelling {genre} story tailored for a {age_group} audience. 

Key Requirements:
- The main character's name must be {protagonist}.
- The story must clearly convey the following theme or moral: {moral}.
- The tone, vocabulary, and complexity MUST be strictly appropriate for the {age_group} age group.
- Keep the story engaging, well-structured, and approximately 3 to 5 paragraphs long.

Story:
"""
prompt = PromptTemplate(input_variables=["genre", "age_group", "protagonist", "moral"], template=template)

# --- Main Page Layout ---
col1, col2 = st.columns([7, 3])

# --- 1. Generation Logic ---
if generate_btn:
    if protagonist and moral:
        with st.spinner(f"Conjuring a {genre} story for {protagonist}..."):
            try:
                start_time = time.time()
                formatted_prompt = prompt.format(genre=genre, age_group=age_group, protagonist=protagonist, moral=moral)
                
                # Fetch response from AI and save it to "memory" (Session State)
                response = llm.invoke(formatted_prompt)
                
                st.session_state.story_content = response
                st.session_state.generation_time = round(time.time() - start_time, 2)
                st.session_state.used_prompt = formatted_prompt
                
            except Exception as e:
                st.error(f"An error occurred. Is Ollama running? Details: {e}")
    else:
        st.warning("Please ensure all fields are filled out before generating.")

# --- 2. Display, Edit, Download, and Feedback Logic ---
# We only show this section IF a story exists in our memory
if st.session_state.story_content:
    
    with col1:
        st.subheader(f"📖 A {genre} Tale for {protagonist}")
        
        # Text area allows the user to manually edit the generated story
        edited_story = st.text_area(
            "Review and manually edit your story below:", 
            value=st.session_state.story_content, 
            height=300
        )
        
        # Create a small row for the Commit and Download buttons
        button_col1, button_col2 = st.columns([1, 1])
        
        with button_col1:
            if st.button("Commit Changes ✅"):
                st.session_state.story_content = edited_story
                st.success("Changes saved! You can now download the updated version.")
                
        with button_col2:
            # Native Streamlit Download Button
            st.download_button(
                label="Download Story as .txt 💾",
                data=st.session_state.story_content,
                file_name=f"{protagonist}_{genre}_story.txt",
                mime="text/plain",
                type="primary"
            )
            
        st.divider()
        
        # Feedback Slider (0 to 10)
        st.subheader("📊 Rate this Story")
        feedback_score = st.slider(
            "How would you rate this generation? (0 = Terrible, 10 = Masterpiece)", 
            min_value=0, 
            max_value=10, 
            value=5
        )
        if st.button("Submit Feedback"):
            st.toast(f"Thank you! You rated this story a {feedback_score}/10. This data could be saved to a database for future model tuning!")

    with col2:
        # Display our saved stats
        st.subheader("⚙️ Generation Stats")
        st.info(f"**Model Used:** Llama 3 (Local)")
        st.info(f"**Time Taken:** {st.session_state.generation_time} seconds")
        
        with st.expander("See AI Prompt (For Grading)"):
            st.code(st.session_state.used_prompt, language="markdown")