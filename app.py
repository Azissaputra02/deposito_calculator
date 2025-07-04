import streamlit as st

st.set_page_config(page_title="Danamon Financial Planning Team", layout="wide")

st.title("Financial Planning Team - Danamon")

st.markdown("Welcome to the **Financial Planning Team** page. Click on each leader to explore their team members.")

# Display Financial Planning Head
st.caption("Financial Planning Head")
st.header("Erwinda Wijaya")

# Display Leads in Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.caption("Planning Lead")
    st.markdown("### Maria Febiana Basuki")
    with st.expander("View Team Members"):
        st.markdown("- **Albert Davin** – Senior Planning Analyst")
        st.markdown("- **Melfin Tanzil** – Planning Analyst")
        st.markdown("- **Visakha Viriya** – Planning Analyst")

with col2:
    st.caption("Project & Expense Management Lead")
    st.markdown("### Harvey Rustandi")
    with st.expander("View Team Members"):
        st.markdown("- **Novara Martina** – Senior Project & Expense Analyst")
        st.markdown("- **Yudi Hadisaputra** – Project & Expense Analyst")
        st.markdown("- **Zefanya Sharon Iswanto** – Project & Expense Analyst")

with col3:
    st.caption("Result Lead")
    st.markdown("### Yansen Taman")
    with st.expander("View Team Members"):
        st.markdown("- **Cindy Uly Napitupulu** – Senior Result Analyst")
        st.markdown("- **Imam Sagita** – Result Analyst")
        st.markdown("- **Adinda Salsabila** – Result Analyst")