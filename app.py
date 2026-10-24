import streamlit as st
from src.agents.explainer import explain, follow_up
from src.rag.ingest import ingest_upload

st.set_page_config(page_title="KnowWhatYouKnow", page_icon="🧠")
st.title("🧠 KnowWhatYouKnow")
st.caption("Type any concept and get a quick, clear explanation.")

with st.sidebar:
    st.header("Knowledge base")
    upload = st.file_uploader("Add notes (PDF or TXT)", type=["pdf", "txt"])
    if upload and st.button("Add to knowledge base"):
        try:
            with st.spinner("Indexing..."):
                n = ingest_upload(upload)
            st.success(f"Added {n} chunks")
        except Exception as e:
            st.error(f"Could not index file: {e}")

concept = st.text_input("Enter a concept", placeholder="e.g. Scrum, Web Cache")
level = st.selectbox("Level", ["beginner", "intermediate", "advanced"])

if st.button("Explain"):
    if not concept.strip():
        st.warning("Please enter a concept first.")
    else:
        try:
            with st.spinner("Thinking..."):
                st.session_state.concept = concept.strip()
                st.session_state.explanation = explain(concept, level)
        except Exception as e:
            st.error(f"Something went wrong: {e}")

if "explanation" in st.session_state:
    st.subheader(st.session_state.concept)
    st.markdown(st.session_state.explanation)

    question = st.text_input("Ask a follow-up question")
    if st.button("Ask") and question.strip():
        try:
            with st.spinner("Thinking..."):
                st.markdown(
                    follow_up(
                        st.session_state.concept,
                        st.session_state.explanation,
                        question,
                    )
                )
        except Exception as e:
            st.error(f"Something went wrong: {e}")