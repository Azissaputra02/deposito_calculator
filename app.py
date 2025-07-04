import streamlit as st

st.set_page_config(page_title="Danamon Financial Planning Team", layout="wide")

# st.title("Financial Planning Team - Danamon")

# --- Title ---
st.markdown("""
<h1 style="
    font-size: 3em;
    font-weight: 900;
    background: linear-gradient(to right, #f39c12, #f1c40f, #e67e22);
    -webkit-background-clip: text;
    color: transparent;
    text-align: left;
    margin-top: -20px;
">
Financial Planning
</h1>
""", unsafe_allow_html=True)

st.markdown("Welcome to the **Financial Planning Team** page. Click on each leader to explore their team members.")

# Display Financial Planning Head
st.markdown("## Erwinda Wijaya")
st.caption("Financial Planning Head")

# Display Leads in Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Maria Febiana Basuki")
    st.caption("Planning Lead")
    with st.expander("View Team Members"):
        st.markdown("- **Albert Davin** – Senior Planning Analyst")
        st.markdown("- **Melfin Tanzil** – Planning Analyst")
        st.markdown("- **Visakha Viriya** – Planning Analyst")

with col2:
    st.markdown("### Harvey Rustandi")
    st.caption("Project & Expense Management Lead")
    with st.expander("View Team Members"):
        st.markdown("- **Novara Martina** – Senior Project & Expense Analyst")
        st.markdown("- **Yudi Hadisaputra** – Project & Expense Analyst")
        st.markdown("- **Zefanya Sharon Iswanto** – Project & Expense Analyst")

with col3:
    st.markdown("### Yansen Taman")
    st.caption("Result Lead")
    with st.expander("View Team Members"):
        st.markdown("- **Cindy Uly Napitupulu** – Senior Result Analyst")
        st.markdown("- **Imam Sagita** – Result Analyst")
        st.markdown("- **Adinda Salsabila** – Result Analyst")