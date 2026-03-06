import streamlit as st
import sys
from pathlib import Path

# Make sure Python can find our src/ module
sys.path.append(str(Path(__file__).parent))

import requests

API_URL = "https://salary-api-production-fe98.up.railway.app"
# ─────────────────────────────────────────────
# PAGE CONFIG — must be the FIRST streamlit call
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Developer Salary Predictor",
    page_icon="💰",
    layout="centered"
)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.title("💰 Developer Salary Predictor")

st.markdown("""
Predict your salary based on **real data from 42,000+ developers**
from the Stack Overflow Annual Survey 2023.
""")

st.warning("""
⚠️ **Two important limitations to keep in mind:**

**1. Purchasing Power Parity (PPP):** Salaries are in USD, but $15k in Morocco
represents far better living standards than $15k in the USA.

**2. Employer location matters more than YOUR location:** A Moroccan developer
working remotely for a US company earns US-level salaries. A Moroccan developer
working for a local Moroccan company earns MAD-level salaries.
This model cannot distinguish between the two — it only knows your country!
""")

st.divider()

# ─────────────────────────────────────────────
# INPUT FORM
# ─────────────────────────────────────────────
st.subheader("📋 Tell Us About Yourself")

col1, col2 = st.columns(2)

with col1:
    country = st.selectbox(
        "🌍 Country",
        options=[
            'Australia',
            'Austria',
            'Belgium',
            'Brazil',
            'Canada',
            'Czech Republic',
            'Denmark',
            'Finland',
            'France',
            'Germany',
            'India',
            'Italy',
            'Netherlands',
            'New Zealand',
            'Norway',
            'Other',
            'Poland',
            'Portugal',
            'Spain',
            'Sweden',
            'Switzerland',
            'United Kingdom of Great Britain and Northern Ireland',
            'United States of America',
        ]
    )

    ed_level = st.selectbox(
        "🎓 Education Level",
        options=[
            'Bachelor',
            'Master',
            'PhD',
            'Associate',
            'No Degree',
            'Other',
        ]
    )

    years_experience = st.slider(
        "💼 Years of Professional Experience",
        min_value=0,
        max_value=50,
        value=3,
        step=1
    )

with col2:
    employment = st.selectbox(
        "👔 Employment Type",
        options=[
            'Employed, full-time',
            'Employed, part-time',
            'Independent contractor, freelancer, or self-employed',
            'Employed, full-time;Independent contractor, freelancer, or self-employed',
            'Employed, full-time;Employed, part-time',
            'Employed, full-time;Independent contractor, freelancer, or self-employed;Employed, part-time',
            'Employed, full-time;Independent contractor, freelancer, or self-employed;Retired',
            'Employed, full-time;Retired',
            'Employed, part-time;Retired',
            'Independent contractor, freelancer, or self-employed;Employed, part-time',
            'Independent contractor, freelancer, or self-employed;Retired',
            'Retired',
            'I prefer not to say',
            'Unknown',
        ]
    )

    dev_type = st.selectbox(
        "💻 Developer Type",
        options=[
            'Developer, full-stack',
            'Developer, back-end',
            'Developer, front-end',
            'Developer, mobile',
            'Developer, desktop or enterprise applications',
            'Developer, embedded applications or devices',
            'Developer, game or graphics',
            'Developer, QA or test',
            'Data scientist or machine learning specialist',
            'Engineer, data',
            'Engineer, site reliability',
            'DevOps specialist',
            'Cloud infrastructure engineer',
            'Security professional',
            'Data or business analyst',
            'Database administrator',
            'System administrator',
            'Academic researcher',
            'Engineering manager',
            'Product manager',
            'Project manager',
            'Senior Executive (C-Suite, VP, etc.)',
            'Student',
            'Educator',
            'Designer',
            'Blockchain',
            'Hardware Engineer',
            'Scientist',
            'Developer Advocate',
            'Developer Experience',
            'Research & Development role',
            'Marketing or sales professional',
            'Other (please specify):',
            'Unknown',
        ]
    )

    org_size = st.selectbox(
        "🏢 Organization Size",
        options=[
            '2 to 9 employees',
            '10 to 19 employees',
            '20 to 99 employees',
            '100 to 499 employees',
            '500 to 999 employees',
            '1,000 to 4,999 employees',
            '5,000 to 9,999 employees',
            '10,000 or more employees',
            'Just me - I am a freelancer, sole proprietor, etc.',
            "I don't know",
            'Unknown',
        ]
    )

st.divider()

# ─────────────────────────────────────────────
# PREDICTION BUTTON
# ─────────────────────────────────────────────
if st.button("🚀 Predict My Salary!", use_container_width=True, type="primary"):
    with st.spinner("Calling the API..."):
        try:
            response = requests.post(
                f"{API_URL}/predict",
                json={
                    "country": country,
                    "ed_level": ed_level,
                    "years_experience": years_experience,
                    "employment": employment,
                    "dev_type": dev_type,
                    "org_size": org_size
                },
                timeout=30  # wait max 30 seconds
            )

            if response.status_code == 200:
                data = response.json()
                salary = data['predicted_salary_usd']

                st.success("✅ Prediction complete!")

                st.metric(
                    label="💰 Predicted Annual Salary (USD)",
                    value=f"${salary:,.0f}"
                )

                st.info(f"""
**What this means:**
- Predicted salary: **${salary:,.0f}/year**
- Likely range: **${data['lower_bound_usd']:,.0f}** → **${data['upper_bound_usd']:,.0f}**
- Model average error: ~${data['model_mae_usd']:,.0f}
- Remember: remote work for international companies
  may result in significantly higher salaries!
                """)

            else:
                st.error(f"API returned error {response.status_code}: {response.text}")

        except requests.exceptions.Timeout:
            st.error("Request timed out — the API took too long to respond!")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the prediction API!")

st.divider()

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.85em;'>
    Built with ❤️ using Python, scikit-learn & Streamlit <br>
    Data: Stack Overflow Developer Survey 2023 (42,000+ responses) <br>
    <a href='https://github.com/abde-amarir/salary-predictor'>
    View source on GitHub</a>
</div>
""", unsafe_allow_html=True)