import streamlit as st
import re  

def main():
    st.set_page_config(page_title="📝 Text Analyzer by Syed Abdullah", page_icon="📄", layout="centered")

    # Custom Dark Theme CSS
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #1e1e1e !important;
            color: #f5f5f5 !important;
        }

        .main {
            background-color: #1e1e1e;
        }

        .stTextArea textarea, .stTextInput input {
            background-color: #2c2c2c !important;
            color: #f5f5f5 !important;
            border: 1px solid #444;
            border-radius: 10px;
            padding: 12px;
            font-size: 16px !important;
        }

        .stButton>button {
            background-color: #ff9800;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 10px 20px;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background-color: #f57c00;
            transform: scale(1.02);
        }

        .metric-style {
            background-color: #2c2c2c;
            border-left: 5px solid #00acc1;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }

        .highlight {
            color: #ffcc80;
            font-weight: 600;
        }

        .title-gradient {
            background: -webkit-linear-gradient(45deg, #ff9800, #ffe082);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 2.5rem;
        }

        .stCode, .stMarkdown code {
            background-color: #333 !important;
            color: #ffcc80 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<div class='title-gradient'>📝 Text Analyzer by Syed Abdullah 🚀</div>", unsafe_allow_html=True)
    st.markdown("✨ <i>Analyze and transform your text like a pro!</i>", unsafe_allow_html=True)

    paragraph = st.text_area("🖊 Enter Your Paragraph:", "", height=180)

    if paragraph.strip():
        st.markdown("---")
        st.subheader("📊 Text Analysis Results")

        words = paragraph.split()
        word_count = len(words)
        char_count = len(paragraph)

        col1, col2 = st.columns(2)
        col1.markdown(f"""<div class='metric-style'>🔤 <b>Total Words:</b> <span class='highlight'>{word_count}</span></div>""", unsafe_allow_html=True)
        col2.markdown(f"""<div class='metric-style'>🔠 <b>Total Characters:</b> <span class='highlight'>{char_count}</span></div>""", unsafe_allow_html=True)

        # Search & Replace
        st.markdown("### 🔍 Search & Replace")
        search_word = st.text_input("🔎 Enter a word to search")
        replace_word = st.text_input("✏️ Replace it with")

        if search_word and replace_word:
            modified_paragraph = re.sub(rf"\b{re.escape(search_word)}\b", replace_word, paragraph)
            st.success("✅ Modified Paragraph:")
            st.text_area("📝 Output:", modified_paragraph, height=130)
            st.code(modified_paragraph, language="text")

        # Case Conversion
        st.markdown("### 🔠 Case Conversion")
        col3, col4 = st.columns(2)
        col3.text_area("🔼 Uppercase", paragraph.upper(), height=100)
        col4.text_area("🔽 Lowercase", paragraph.lower(), height=100)

        # Check for keyword
        contains_python = "python" in paragraph.lower()
        st.info(f"🐍 Contains 'Python': **{'✅ Yes' if contains_python else '❌ No'}**")

        # Average word length
        avg_length = char_count / word_count if word_count else 0
        st.write(f"📏 **Average Word Length:** `{avg_length:.2f}` characters")

        # Tip
        st.markdown("---")
        st.success("💡 **Tip:** Use this tool to polish blogs, assignments, or any content like a true pro! 💫")

    else:
        st.warning("⚠ Please enter a paragraph to analyze.")

if __name__ == "__main__":
    main()
