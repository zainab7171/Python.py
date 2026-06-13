import streamlit as st
import requests

API = "http://localhost:8000"

st.title("📚 Quote Collection")

# ── Tabs ──────────────────────────────────────
tab1, tab2 = st.tabs(["View Quotes", "Add Quote"])

# ── Tab 1: Saari quotes dekho ─────────────────
with tab1:
    if st.button("Refresh Quotes"):
        st.rerun()

    res = requests.get(f"{API}/quotes")
    quotes = res.json()

    for q in quotes:
        with st.expander(f'"{q["quote_text"]}" — {q["author"]}'):
            st.write(f"**Source:** {q['source']}")
            st.write(f"**Category:** {q['category']}")
            st.write(f"**Added:** {q['added_at']}")

            # AI Explain button
            if st.button(f"AI se explain karo", key=f"exp_{q['id']}"):
                with st.spinner("AI soch raha hai..."):
                    r = requests.post(f"{API}/quotes/{q['id']}/explain")
                    st.info(r.json()["explanation"])

            # Delete button
            if st.button("Delete", key=f"del_{q['id']}"):
                requests.delete(f"{API}/quotes/{q['id']}")
                st.success("Quote delete ho gaya!")
                st.rerun()

# ── Tab 2: Naya quote add karo ────────────────
with tab2:
    with st.form("add_quote_form"):
        quote_text = st.text_area("Quote likho")
        author     = st.text_input("Author (e.g. Gandhi)")
        source     = st.text_input("Source (e.g. book ya movie)")
        category   = st.selectbox("Category",
                       ["motivation", "wisdom", "humor", "love", "other"])

        submitted = st.form_submit_button("Save Quote")
        if submitted and quote_text:
            requests.post(f"{API}/quotes", json={
                "quote_text": quote_text,
                "author": author,
                "source": source,
                "category": category
            })
            st.success("Quote save ho gaya!")
            st.rerun()
