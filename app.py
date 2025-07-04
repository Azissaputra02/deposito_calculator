import streamlit as st

# Inisialisasi session_state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk berpindah halaman
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- Sidebar navigasi ---
with st.sidebar:
    st.markdown("##  List of content")
    page = st.radio(
        "Go to:",
        ("Home", "Planning", "Expense", "Result", "Glossary"),
        index=("Home", "Planning", "Expense", "Result", "Glossary").index(st.session_state.page)
    )
    st.session_state.page = page

# --- Halaman Home ---
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
    ">
    Financial Planning
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    Welcome to the Financial Planning Knowledge Center — here’s where strategic and financial planning insights across the bank are made. Tap on each leader to see their team members.
    """)

    st.divider()

    # Tampilan struktur organisasi
    st.header(" Erwinda Wijaya")
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
    # Tampilan tombol navigasi sejajar
    st.markdown("### Explore")
    with st.expander("🗂️ Planning"):
        st.markdown("""
        Initiated, coordinate and consolidate Bank-wide Financial Planning & Strategy in collaboration with CSO team.
        """)
        if st.button("Read more →", key="go_planning"):
            go_to("Planning")

    with st.expander("💸 Expense"):
        st.markdown("""
        Initiated, coordinate and consolidate Bank-wide OPEX and CAPEX Planning & Budgeting. 
        """)
        if st.button("Read more →", key="go_expense"):
            go_to("Expense")

    with st.expander("📊 Result"):
        st.markdown("""
        Provide Bank-wide Performance Result Report to BODM, BOC, and DQUM on monthly and quarterly basis including analysis and feedback action needed.
        """)
        if st.button("Read more →", key="go_result"):
            go_to("Result")

    with st.expander("📘 Glossary"):
        st.markdown("""
        All the key financial terms, acronyms, and concepts used within Financial Planning  
        — in one place for your quick reference.
        """)
        if st.button("Read more →", key="go_glossary"):
            go_to("Glossary")

# --- Halaman Planning ---
elif st.session_state.page == "Planning":
    if st.button("🔙 "):
        go_to("Home")
    st.header("🗂️ Planning")
    st.markdown("Content for Planning goes here...")

# --- Halaman Expense ---
elif st.session_state.page == "Expense":
    if st.button("🔙 "):
        go_to("Home")
    st.header("💸 Expense")
    st.markdown("Content for Expense goes here...")

# --- Halaman Result ---
elif st.session_state.page == "Result":
    if st.button("🔙 "):
        go_to("Home")
    st.header("📊 Result")
    st.markdown("Content for Result goes here...")

# --- Halaman Glossary ---
elif st.session_state.page == "Glossary":
    if st.button("🔙 "):
        go_to("Home")
    st.header("📘 Glossary")
    st.markdown("Content for Glossary goes here...")