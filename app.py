import streamlit as st

# Set page config
st.set_page_config(page_title="Danamon FP", layout="wide")

# Initialize state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar Navigation
with st.sidebar:
    st.title("📂 Navigation")
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("📝 Planning"):
        st.session_state.page = "Planning"
    if st.button("💸 Expense"):
        st.session_state.page = "Expense"
    if st.button("📈 Result"):
        st.session_state.page = "Result"
    if st.button("📖 Glosarium"):
        st.session_state.page = "Glosarium"

# Back to home button
def back_home():
    st.markdown("---")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "Home"

# ---------------------- PAGE LOGIC ----------------------

if st.session_state.page == "Home":
    # Title
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

    # Description
    st.markdown("""
    <p style="font-size: 1.1em; color: #555;">
    Welcome to the <strong>Financial Planning Team Website</strong> of Bank Danamon. 
    This internal site is designed to help you understand our team structure and roles in supporting strategic financial decision-making across the bank.
    </p>
    <p style="font-size: 1.1em; color: #555;">
    The Financial Planning team oversees budgeting, expense management, and financial results monitoring — ensuring that every directorate aligns with Danamon's financial goals and accountability.
    </p>
    """, unsafe_allow_html=True)

    # Organization Chart
    st.header("🧭 Organization Chart")
    st.markdown("### 🟢 Erwinda Wijaya")
    st.caption("Financial Planning Head")

    st.subheader("Team Leads")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🔶 Maria Febiana Basuki")
        st.caption("Planning Lead")
        with st.expander("View Team Members"):
            st.markdown("- **Albert Davin** – Senior Planning Analyst")
            st.markdown("- **Melfin Tanzil** – Planning Analyst")
            st.markdown("- **Visakha Viriya** – Planning Analyst")

    with col2:
        st.markdown("#### 🔶 Harvey Rustandi")
        st.caption("Project & Expense Lead")
        with st.expander("View Team Members"):
            st.markdown("- **Novara Martina** – Senior Project & Expense Analyst")
            st.markdown("- **Yudi Hadisaputra** – Project & Expense Analyst")
            st.markdown("- **Zefanya Sharon Iswanto** – Project & Expense Analyst")

    with col3:
        st.markdown("#### 🔶 Yansen Taman")
        st.caption("Result Lead")
        with st.expander("View Team Members"):
            st.markdown("- **Cindy Uly Napitupulu** – Senior Result Analyst")
            st.markdown("- **Imam Sagita** – Result Analyst")
            st.markdown("- **Adinda Salsabila** – Result Analyst")

    # Section link
    st.markdown("### 📚 Explore Each Team")
    colA, colB = st.columns(2)
    with colA:
        if st.button("🔗 Go to Planning"):
            st.session_state.page = "Planning"
    with colB:
        if st.button("📬 Contact Us"):
            st.markdown("""
            - **Maria Febiana Basuki** – maria.basuki@danamon.co.id  
            - **Harvey Rustandi** – harvey.rustandi@danamon.co.id  
            - **Yansen Taman** – yansen.taman@danamon.co.id  
            """)

# ------------------- PLANNING PAGE -------------------
elif st.session_state.page == "Planning":
    st.title("📝 Planning Team")
    st.markdown("""
    The Planning team is responsible for preparing Danamon's business plans, managing RBB timelines, and supporting all units in submitting accurate and strategic financial projections.
    """)
    back_home()

# ------------------- EXPENSE PAGE -------------------
elif st.session_state.page == "Expense":
    st.title("💸 Expense Management Team")
    st.markdown("""
    The Expense team monitors operating and capital expenses, manages budget utilization, and ensures all spending aligns with financial targets and cost control policies.
    """)
    back_home()

# ------------------- RESULT PAGE -------------------
elif st.session_state.page == "Result":
    st.title("📈 Result Team")
    st.markdown("""
    The Result team consolidates and analyzes actual financial performance, compares it against the budget, and delivers key reports to management and regulators.
    """)
    back_home()

# ------------------- GLOSARIUM PAGE -------------------
elif st.session_state.page == "Glosarium":
    st.title("📖 Glosarium")
    st.markdown("""
    | **Istilah** | **Penjelasan** |
    |------------|----------------|
    | RBB | Rencana Bisnis Bank |
    | OPEX | Operational Expense |
    | CAPEX | Capital Expenditure |
    | Forecast | Proyeksi kinerja keuangan |
    | MIS | Management Information System |
    """, unsafe_allow_html=True)
    back_home()