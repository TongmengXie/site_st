import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append('/mount/src/site_st/')
try: import base64
except: os.system("pip install base64")
finally: import base64

# set_page_config (This must be the first Streamlit command used on an app page, and must only be set once per page.)
# st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.set_page_config(layout="wide")

# CV
# centereing the cv
pdf_file = './cv_TongmengXie_DS_industrial.pdf'

# find if the file exists
if not os.path.exists(pdf_file):
    st.error("PDF file not found")

with open(pdf_file,"rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

st.markdown("<h1 style='text-align: center; color: grey;'>CV - Tongmeng Xie</h1>", unsafe_allow_html=True)
st.markdown("If PDF is not rendered, check on Google Drive: [CV - Tongmeng Xie](https://drive.google.com/file/d/19ajp4iERX5aoLSDvGJYWMJ3nhZxw5m29/view?usp=sharing)", unsafe_allow_html=True)

st.markdown(f"<h1 style='text-align: center; color: grey;'>{pdf_display}</h1>", unsafe_allow_html=True)




# Researches
st.title('Researches - Tongmeng Xie')
st.write('## Address Matching and Entity Extraction Across Data Sets')

with st.columns(3)[1]:
    st.image('./Overview_addrmatch.png', caption='Overview of Address Matching Workflow')
    st.image('./Conc_ensemble_lev.png', caption='Conclusions on various ensemble levels')
    st.image('./Comp_Ensemble.png', caption='Comparison of different Ensemble methods')
    st.image('./Prep_NER_train.png', caption='Preparing for NER training process')


other_researches =  \
'''
## **Has the expansion of Ultra Low Emission Zone in 2021 improved air quality in London? How to quantify the improvement?**

*The study found that the expansion of London's Ultra Low Emission Zone (ULEZ) in October 2021 led to a modest 3-9% reduction in PM10-associated pollutants, confirmed causality via Regression Discontinuity Design (RDD), and noted spatial spillover effects, but suggests further analysis on other pollutants and time scope adjustments.*

### **Research Questions:**

1.  Did the expansion of the Ultra Low Emission Zone (ULEZ) in October 2021 improve air quality in London?

2.  How can this improvement be quantified?

### **Key Findings:**

#### **Air Quality Improvement:**

The expansion of ULEZ on October 25, 2021, led to a noticeable but not significant improvement in air quality. Specifically, there was a 3-9% reduction in PM10-associated pollutants in Greater London.

#### **Sub-Questions:**

1.  **Categorization of Pollutants**: Pollutants were organized into groups based on their collinearity. The categories include:

    -   NOx (NO, NO2, NOXasNO2)

    -   PM10 & Associated (PM10, NV10, V10)

    -   PM2.5_Associated (NV2.5, V2.5, AT2.5, AP2.5)

    -   SO2 (SO2, AP10, CO)

    -   Uncategorised: PM2.5, O3

2.  **Causality**: The study confirmed a causal relationship between ULEZ expansion and air quality improvement through Regression Discontinuity Design (RDD).

3.  **Spatial Patterns**: Air quality improved not just within the expanded ULEZ area but also in areas outside it, potentially due to spatial spillover effects.

#### **Areas for Further Research:**

1.  **Other Pollutants**: Further investigation is needed to understand the impact on other pollutants.

2.  **Average Performance Metrics**: A more comprehensive measure of air quality improvement is yet to be developed.

3.  **Time Scope**: The timeframe for assessing the effects of ULEZ expansion may need adjustment and could necessitate iterative analysis.

## Why are KS4 performance in Liverpool and Manchester lower than the national average? Exploration and Quantification of Socio-economic Factors Influencing KS4 Performance in England

*The study reveals that while there is no significant difference in overall deprivation between Liverpool & Manchester and the rest of England, students in Liverpool & Manchester are more socio-demographically disadvantaged, and these disadvantages have a greater negative impact on their educational outcomes.*

### **Main Research Questions:**

1.  How does the attainment 8 score relate to deprivation indicators?

2.  Are socio-economic disadvantages more severe in Liverpool & Manchester?

3.  Do socio-economic disadvantages have a greater impact on educational outcomes in Liverpool & Manchester?

### **Key Findings:**

#### **Relationship between Attainment 8 and Deprivation**

-   After accounting for deprivation-related variables, the model's explanatory power (Adj. *R*2) increased from 57.5% to 77.3%.

-   An additional 1% of students with Special Education Needs (SEN) is associated with a 48.3-point decrease in a borough's attainment 8 score.

#### **Hypothesis Tests**

1.  **Severity of Socio-Economic Disadvantages in Liverpool & Manchester**: There is no significant difference in the level of deprivation in and outside of Liverpool & Manchester.

2.  **Impact of Socio-Economic Disadvantages in Liverpool & Manchester**: Socio-demographic disadvantages are more heavily weighted in Liverpool & Manchester, affecting educational outcomes more than they do in the rest of England.

#### **Model Limitations**

-   One variable related to socio-demographics in Liverpool & Manchester had a p-value greater than 0.05, indicating the model may not be a perfect fit.

-   The study may benefit from the inclusion of other socio-economic factors like disability, or the use of machine learning techniques for better fit.

### **Discussion**

Students in Liverpool & Manchester are more socio-demographically disadvantaged, and this has a heavier impact on their educational outcomes than for students outside these areas. Interventions such as cultural competency training for educators and safe spaces for marginalized students could improve educational equity and inclusion in Liverpool & Manchester.

By understanding these factors, policymakers can better tailor interventions to support students from disadvantaged backgrounds.
'''

st.write(other_researches)

