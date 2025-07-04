import streamlit as st

# Fungsi navigasi sederhana
def go_to(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()

# Inisialisasi halaman default
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Sidebar ---
st.sidebar.markdown("## List of content")
page = st.sidebar.radio("Select:", ["Home", "Glossary", "Planning", "Expense", "Result"])

# Update state jika navigasi dari sidebar
if page != st.session_state.page:
    st.session_state.page = page
    st.experimental_rerun()

# --- HOME ---
if st.session_state.page == "Home":
    st.markdown("""
    <h1 style="
        font-size: 3em;
        font-weight: 900;
        background: linear-gradient(to right, #f39c12, #f1c40f, #e67e22);
        -webkit-background-clip: text;
        color: transparent;
        text-align: left;
        margin-top: -20px;
    ">Financial planning</h1>
    """, unsafe_allow_html=True)

    st.markdown("Welcome to the Financial Planning Knowledge Center — this is where strategic and financial planning insights are built and shared across the bank. Tap on each leader to see their team members.")

    st.divider()

    # Financial Planning Head
    st.header("Erwinda Wijaya")
    st.caption("Financial Planning Head")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Maria Febiana B")
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

    with col1:
        if st.button("📘 Glossary"):
            go_to("Glossary")
    with col2:
        if st.button("🗂️ Planning"):
            go_to("Planning")
    with col3:
        if st.button("💸 Expense"):
            go_to("Expense")
    with col4:
        if st.button("📊 Result"):
            go_to("Result")

# --- GLOSSARY PAGE ---
elif st.session_state.page == "Glossary":
    if st.button("🔙 Back to Home"):
        go_to("Home")
    st.header("📘 Glossary")

# --- PLANNING PAGE ---
elif st.session_state.page == "Planning":
    if st.button("🔙 Back to Home"):
        go_to("Home")
    st.header("🗂️ Planning")

# --- EXPENSE PAGE ---
elif st.session_state.page == "Expense":
    if st.button("🔙 Back to Home"):
        go_to("Home")
    st.header("💸 Expense")

# --- RESULT PAGE ---
elif st.session_state.page == "Result":
    if st.button("🔙 Back to Home"):
        go_to("Home")
    st.header("📊 Result")