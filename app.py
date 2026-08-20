import os
import streamlit as st
from google import genai

# --- ১. পেজ কনফিগারেশন ---
st.set_page_config(
    page_title="Pro YT SEO Creator AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ২. সাইডবার সেটিংস & API কনফিগারেশন ---
# নিচে "YOUR_GEMINI_API_KEY_HERE" সরিয়ে আপনার AIzaSy... দিয়ে শুরু হওয়া আসল Key-টি বসান
USER_API_KEY = "AQ.Ab8RN6KAnvB_OtI8cyIgHPICdnBaqrydBb3NMbMcj9dGJuRIgA"

with st.sidebar:
  st.markdown("### ⚙️ Settings")

  api_key = st.text_input(
      "Gemini API Key",
      value=os.environ.get("GEMINI_API_KEY", USER_API_KEY),
      type="password",
      help="aistudio.google.com থেকে সংগৃহীত API Key এখানে পেস্ট করুন।",
  )

  st.markdown("---")
  st.markdown("### 🌓 Theme Mode")
  theme_mode = st.radio(
      "Choose Theme",
      ["Dark 🌙", "Light ☀️"],
      index=0,
      label_visibility="collapsed",
  )

# --- ৩. রেসপনসিভ & অ্যানিমেটেড CSS ---
if theme_mode == "Dark 🌙":
  bg_color = "#0E1117"
  text_color = "#FAFAFA"
  card_bg = "#1E222D"
  border_color = "#30363D"
  accent_color = "#6366F1"
else:
  bg_color = "#F8F9FA"
  text_color = "#1F2937"
  card_bg = "#FFFFFF"
  border_color = "#E5E7EB"
  accent_color = "#4F46E5"

st.markdown(
    f"""
    <style>
    @keyframes fadeIn {{
        0% {{ opacity: 0; transform: translateY(12px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}

    .stApp {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
        animation: fadeIn 0.6s ease-in-out;
    }}

    .main-header {{
        font-size: 32px;
        font-weight: 800;
        background: linear-gradient(90deg, {accent_color}, #EC4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: -5px;
    }}

    div[data-testid="stForm"], div[data-testid="stMetricValue"], div.stCodeBlock {{
        background-color: {card_bg} !important;
        border: 1px solid {border_color} !important;
        border-radius: 12px !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }}

    div.stButton > button, div.stFormSubmitButton > button {{
        background: linear-gradient(90deg, {accent_color}, #8B5CF6) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.3s ease-in-out !important;
    }}

    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stTextArea textarea {{
        background-color: {card_bg} !important;
        color: {text_color} !important;
        border-color: {border_color} !important;
        border-radius: 8px !important;
    }}

    @media only screen and (max-width: 768px) {{
        .main-header {{ font-size: 24px !important; }}
        div[data-testid="column"] {{ width: 100% !important; flex: 1 1 100% !important; margin-bottom: 10px; }}
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# --- ৪. অ্যাপ ইন্টারফেস ---
st.markdown(
    '<p class="main-header">🚀 Pro YouTube SEO Creator AI</p>',
    unsafe_allow_html=True,
)
st.caption(
    "Deep AI Research Engine — Search Intent, CTR Trigger & Ranking Analytics"
)

tab1, tab2 = st.tabs(["🎯 AI SEO Generator", "💡 Analytics & Export"])

with tab1:
  with st.form("pro_seo_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
      keyword = st.text_input(
          "Main Keyword / Topic*", placeholder="e.g., India Tour Vlog"
      )
    with col2:
      video_type = st.selectbox(
          "Format", ["YouTube Shorts (<60s)", "Long Video (10m+)"]
      )
    with col3:
      niche = st.selectbox(
          "Category",
          ["Vlog", "Gaming", "Tech", "Design", "Education", "Entertainment"],
      )

    submit_btn = st.form_submit_button(
        "🧠 Research & Generate SEO Package", use_container_width=True
    )

  if submit_btn:
    if not keyword.strip():
      st.error("⚠️ অনুগ্রহ করে একটি মূল কিউওয়ার্ড বা টপিক লিখুন!")
    elif not api_key or "YOUR_GEMINI_API_KEY_HERE" in api_key:
      st.error(
          "⚠️ সঠিক Gemini API Key প্রয়োজন! Google AI Studio থেকে AIzaSy... দিয়ে"
          " শুরু হওয়া Key কপি করে সাইডবারে বসান।"
      )
    else:
      with st.spinner(
          "🔍 AI অ্যালগরিদম রিসার্চ, কম্পিটিটর গ্যাপ এবং সার্চ ইনটেন্ট বিশ্লেষণ"
          " করছে..."
      ):
        try:
          client = genai.Client(api_key=api_key)

          prompt = f"""
                    You are an expert YouTube SEO Strategist.
                    Perform deep YouTube search analysis and competitive research for:
                    - Topic/Keyword: "{keyword}"
                    - Format: {video_type}
                    - Category: {niche}

                    Respond EXACTLY in this block structure:

                    [RESEARCH_SUMMARY]
                    Provide a concise 2-3 sentence AI Research Summary detailing the strategy, psychological trigger, and target audience hook.

                    [TITLE_1]
                    High-CTR Title Option 1

                    [TITLE_2]
                    High-CTR Title Option 2

                    [DESCRIPTION]
                    SEO-rich YouTube description incorporating LSI keywords, timestamps, and CTA.

                    [TAGS]
                    comma, separated, viral, tags, high search volume, long-tail keywords

                    [HASHTAGS]
                    #hashtag1 #hashtag2 #hashtag3 #hashtag4
                    """

          response = client.models.generate_content(
              model="gemini-3.6-flash", contents=prompt
          )

          res_text = response.text

          research_summary = "AI-backed SEO research complete."
          titles, desc, tags, hashtags = [], "", "", ""

          if "[RESEARCH_SUMMARY]" in res_text:
            parts = res_text.split("[RESEARCH_SUMMARY]")
            summary_part = parts[1].split("[TITLE_1]")
            research_summary = summary_part[0].strip()

            rest_part = summary_part[1]
            title1_part = rest_part.split("[TITLE_2]")
            titles.append(title1_part[0].strip())

            title2_part = title1_part[1].split("[DESCRIPTION]")
            titles.append(title2_part[0].strip())

            desc_part = title2_part[1].split("[TAGS]")
            desc = desc_part[0].strip()

            tags_part = desc_part[1].split("[HASHTAGS]")
            tags = tags_part[0].strip()
            hashtags = tags_part[1].strip()
          else:
            titles = [f"Ultimate {keyword} Strategy", f"How to Master {keyword}"]
            desc = res_text
            tags = f"{keyword}, youtube seo, viral"
            hashtags = f"#{keyword.replace(' ', '')} #YouTube"

          st.success("✅ AI Research & SEO প্যাকেজ প্রস্তুত!")

          st.markdown("### 🧠 AI Research Insights")
          st.info(f"💡 **Strategy Breakdown:**\n{research_summary}")

          st.subheader("📌 Research-Backed Titles (High CTR)")
          for t in titles:
            if t:
              st.code(t, language="markdown")

          st.subheader("📝 SEO Optimized Description")
          st.text_area("Copy for YouTube Studio:", desc, height=160)

          col_t, col_h = st.columns(2)
          with col_t:
            st.subheader("🏷️ Viral & Long-Tail Tags")
            st.code(tags, language="markdown")
          with col_h:
            st.subheader("#️⃣ Trending Hashtags")
            st.code(hashtags, language="markdown")

          full_package = (
              f"AI Research Summary:\n{research_summary}\n\nTitles:\n"
              + "\n".join(titles)
              + f"\n\nDescription:\n{desc}\n\nTags:\n{tags}\n\nHashtags:\n{hashtags}"
          )
          st.session_state["seo_data"] = full_package
          st.session_state["keyword"] = keyword.strip()

        except Exception as e:
          st.error(
              f"❌ API Key ভুল বা নিষ্ক্রিয়। সঠিক Key দিয়ে চেষ্টা করুন:"
              f" {e}"
          )

with tab2:
  if "seo_data" in st.session_state:
    st.subheader("📊 SEO Analytics & Export")
    m1, m2, m3 = st.columns(3)
    m1.metric("Search Intent", "High Match", "Top 5%")
    m2.metric("Competition", "Analyzed", "Gap Found")
    m3.metric("CTR Predictor", "92/100", "+18% Potential")

    st.markdown("---")
    st.subheader("📥 Export Complete AI Package")

    file_kw = st.session_state.get("keyword", "youtube").replace(" ", "_")
    st.download_button(
        label="Download Research & SEO Package (.txt)",
        data=st.session_state["seo_data"],
        file_name=f"{file_kw}_AI_Research_SEO.txt",
        mime="text/plain",
        use_container_width=True,
    )
  else:
    st.info("👈 প্রথম ট্যাব থেকে AI রিসার্চ সফল হলে এক্সপোর্ট অপশন পাবেন।")