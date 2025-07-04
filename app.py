import streamlit as st

# Inisialisasi session_state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk berpindah halaman
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# Sidebar navigasi
with st.sidebar:
    st.markdown("## List of content")
    page = st.radio(
        "Select:",
        ("Home", "Glossary", "Planning", "Expense", "Result"),
        index=("Home", "Glossary", "Planning", "Expense", "Result").index(st.session_state.page)
    )
    st.session_state.page = page

# Tampilan halaman Home
if st.session_state.page == "Home":
    st.markdown("""
    <h1 style="
        font-size: 3em;
        font-weight: 900;
        background: linear-gradient(to right, #ED5626, #F69322, #FEC025);
        -webkit-background-clip: text;
        color: transparent;
        text-align: left;
        margin-top: -20px;
    ">
    Financial planning
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("Welcome to the Financial Planning Knowledge Center — this is where strategic and financial planning insights are built and shared across the bank. Tap on each leader to see their team members.")

    # Display Financial Planning Head
    st.header("Erwinda Wijaya")
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