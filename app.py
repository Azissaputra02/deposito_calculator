import streamlit as st

st.set_page_config(page_title="Danamon Financial Planning Team", layout="wide")

st.title("Financial Planning Team - Danamon")

st.markdown("Welcome to the **Financial Planning Team** page. Click on each leader to explore their team members.")

# Display Financial Planning Head
st.header("🟢 Erwinda Wijaya")
st.caption("Financial Planning Head")

# Display Leads in Columns
st.subheader("Team Leads")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔶 Maria Febiana Basuki")
    st.caption("Planning Lead")
    with st.expander("View Team Members"):
        st.markdown("- **Albert Davin** – Senior Planning Analyst")
        st.markdown("- **Melfin Tanzil** – Planning Analyst")
        st.markdown("- **Visakha Viriya** – Planning Analyst")

with col2:
    st.markdown("### 🔶 Harvey Rustandi")
    st.caption("Project & Expense Management Lead")
    with st.expander("View Team Members"):
        st.markdown("- **Novara Martina** – Senior Project & Expense Analyst")
        st.markdown("- **Yudi Hadisaputra** – Project & Expense Analyst")
        st.markdown("- **Zefanya Sharon Iswanto** – Project & Expense Analyst")

with col3:
    st.markdown("### 🔶 Yansen Taman")
    st.caption("Result Lead")
    with st.expander("View Team Members"):
        st.markdown("- **Cindy Uly Napitupulu** – Senior Result Analyst")
        st.markdown("- **Imam Sagita** – Result Analyst")
        st.markdown("- **Adinda Salsabila** – Result Analyst")