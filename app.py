import streamlit as st

# --- Inisialisasi Session State ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Tampilan Header Global ---
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
Financial planning
</h1>
""", unsafe_allow_html=True)

st.markdown("""
Welcome to the Financial Planning Knowledge Center — this is where strategic and financial planning insights are built and shared across the bank. Tap on each leader to see their team members.
""")

st.divider()

# --- Home Page ---
if st.session_state.page == "Home":
    st.header("👤 Erwinda Wijaya")
    st.caption("Financial Planning Head")

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

    st.divider()
    st.markdown("### 🔎 Quick Access to Sections")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("📘 Glossary"):
        st.session_state.page = "Glossary"
        st.experimental_rerun()

    if col2.button("🗂️ Planning"):
        st.session_state.page = "Planning"
        st.experimental_rerun()

    if col3.button("💸 Expense"):
        st.session_state.page = "Expense"
        st.experimental_rerun()

    if col4.button("📊 Result"):
        st.session_state.page = "Result"
        st.experimental_rerun()

# --- Glossary Page ---
elif st.session_state.page == "Glossary":
    if st.button("🔙 Back to Home"):
        st.session_state.page = "Home"
        st.experimental_rerun()
    st.header("📘 Glossary")
    st.info("Glossary content goes here.")

# --- Planning Page ---
elif st.session_state.page == "Planning":
    if st.button("🔙 Back to Home"):
        st.session_state.page = "Home"
        st.experimental_rerun()
    st.header("🗂️ Planning")
    st.info("Planning content goes here.")

# --- Expense Page ---
elif st.session_state.page == "Expense":
    if st.button("🔙 Back to Home"):
        st.session_state.page = "Home"
        st.experimental_rerun()
    st.header("💸 Expense")
    st.info("Expense content goes here.")

# --- Result Page ---
elif st.session_state.page == "Result":
    if st.button("🔙 Back to Home"):
        st.session_state.page = "Home"
        st.experimental_rerun()
    st.header("📊 Result")
    st.info("Result content goes here.")