import streamlit as st
import os
import sys
import base64

# Add paths for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append('/mount/src/site_st/')

# Page configuration
st.set_page_config(page_title="Tongmeng Xie - Portfolio", page_icon="📘", layout="wide")

# Check if CV PDF exists and display it
pdf_file = './cv_TongmengXie_DS_industrial.pdf'
if not os.path.exists(pdf_file):
    st.error("PDF file not found")
else:
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf">'
    st.markdown("<h1 style='text-align: center; color: black;'>CV - Tongmeng Xie</h1>", unsafe_allow_html=True)
    st.markdown(pdf_display, unsafe_allow_html=True)
    st.markdown("If PDF is not rendered, check on [Google Drive](https://drive.google.com/file/d/19ajp4iERX5aoLSDvGJYWMJ3nhZxw5m29/view?usp=sharing)", unsafe_allow_html=True)

# Research section
st.title('Research Projects - Tongmeng Xie')

# Research details
research_details = [
    {
        "title": "09/2023-01/2024: Research Assistant, Marshallian Theories In A Historical Context",
        "description": "Matching Across Censuses and Patent Data",
        "images": [
            ('./Overview_addrmatch.png', 'Overview of Address Matching Workflow'),
            ('./Conc_ensemble_lev.png', 'Conclusions on various ensemble levels'),
            ('./Comp_Ensemble.png', 'Comparison of different Ensemble methods'),
            ('./Prep_NER_train.png', 'Preparing for NER training process'),
        ]
    },
    # Additional research projects can be added here in similar dictionary format
]

# Display research projects
for project in research_details:
    st.subheader(project["title"])
    st.caption(project["description"])
    cols = st.columns(len(project["images"]))
    for col, img in zip(cols, project["images"]):
        col.image(img[0], caption=img[1])

# ULEZ Research
ulez_research = '''
## Has the expansion of Ultra Low Emission Zone in 2021 improved air quality in London?

**Study Findings:**
- The expansion led to a 3-9% reduction in PM10-associated pollutants.
- Confirmed causality via Regression Discontinuity Design (RDD).
- Noted spatial spillover effects.
- Suggests further analysis on other pollutants and time scope adjustments.

**Research Questions:**
1. Did the ULEZ expansion improve air quality in London?
2. How can this improvement be quantified?
'''

st.markdown(ulez_research)

# Socio-economic factors in education
education_research = '''
## Socio-economic Factors Influencing KS4 Performance in Liverpool and Manchester

**Study Overview:**
- Explored socio-economic impacts on educational outcomes.
- Used statistical analysis and machine learning techniques for deeper insights.

**Key Findings:**
- No significant difference in overall deprivation levels, but higher socio-demographic disadvantages in Liverpool & Manchester.
- These disadvantages impact educational outcomes more heavily.

**Further Analysis:**
- Importance of addressing cultural competency and safe spaces in education.

**Visualizations:**
- Multivariate linear regression results
- Hypothesis testing results
'''

st.markdown(education_research)
cols = st.columns(2)
with cols[0]:
    st.image('./imgs/multivariate_linear_regression.png', caption='Multivariate linear regression result')
with cols[1]:
    st.image('./imgs/hypothesis_1.png', caption='Hypothesis testing results')
