import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Notes Dashboard", layout="wide")

st.title("Notes Dashboard")
st.markdown(
    "Use this Streamlit frontend to connect to the FastAPI notes API. "
    "Make sure the backend is running at `http://127.0.0.1:8000`."
)


def api_request(method, path, **kwargs):
    try:
        response = requests.request(method, f"{API_BASE_URL}{path}", timeout=5, **kwargs)
        return response
    except requests.exceptions.RequestException as exc:
        st.error(f"API request failed: {exc}")
        return None


def parse_tags(text: str) -> list[str]:
    return [tag.strip() for tag in text.split(",") if tag.strip()]


def load_notes(filters=None):
    params = filters or {}
    response = api_request("GET", "/notes", params=params)
    if response is None:
        return []
    if response.status_code != 200:
        st.warning(f"Failed to load notes: {response.status_code}")
        return []
    return response.json()


def show_note_row(note):
    st.write(f"**ID**: {note['id']}  ")
    st.write(f"**Title**: {note['title']}")
    st.write(f"**Category**: {note['category']}")
    st.write(f"**Tags**: {', '.join(note['tags'])}")
    st.write(f"**Created**: {note['created_at']}")
    st.write(note['content'])
    st.markdown("---")


st.header("Notes CRUD")
with st.expander("Create a new note", expanded=True):
    title = st.text_input("Title", key="create_title")
    content = st.text_area("Content", key="create_content")
    category = st.text_input("Category", key="create_category")
    tag_text = st.text_input("Tags (comma-separated)", key="create_tags")
    if st.button("Create note"):
        payload = {
            "title": title,
            "content": content,
            "category": category,
            "tags": parse_tags(tag_text),
        }
        response = api_request("POST", "/notes", json=payload)
        if response is not None:
            if response.status_code == 201:
                st.success("Note created successfully")
            else:
                st.error(f"Failed to create note: {response.status_code} - {response.text}")

st.subheader("Search and filter notes")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    search = st.text_input("Search", key="search")
with col2:
    category_filter = st.text_input("Category", key="filter_category")
with col3:
    tag_filter = st.text_input("Tag", key="filter_tag")
with col4:
    created_after = st.text_input("Created after (ISO)", key="filter_after")
with col5:
    created_before = st.text_input("Created before (ISO)", key="filter_before")

filters = {}
if category_filter:
    filters["category"] = category_filter
if search:
    filters["search"] = search
if tag_filter:
    filters["tag"] = tag_filter
if created_after:
    filters["created_after"] = created_after
if created_before:
    filters["created_before"] = created_before

notes = load_notes(filters)
total_notes = len(notes)
notes = notes[:10]
if total_notes > len(notes):
    st.info(f"Showing 10 of {total_notes} notes. Refine filters to narrow results.")
else:
    st.write(f"Found {total_notes} notes")

for note in notes:
    show_note_row(note)
    if st.button("Delete this note", key=f"delete_note_{note['id']}"):
        response = api_request("DELETE", f"/notes/{note['id']}")
        if response is not None:
            if response.status_code == 204:
                st.success("Note deleted successfully")
            else:
                st.error(f"Failed to delete note: {response.status_code} - {response.text}")

st.subheader("Update or delete a note")
note_ids = [note["id"] for note in notes]
selected_note_id = st.selectbox("Select note ID", options=[None] + note_ids, index=0)
if selected_note_id:
    selected_note = next((note for note in notes if note["id"] == selected_note_id), None)
    if selected_note:
        st.write("### Selected note")
        show_note_row(selected_note)
        with st.form("update_note_form"):
            title = st.text_input("Title", value=selected_note["title"])
            content = st.text_area("Content", value=selected_note["content"])
            category = st.text_input("Category", value=selected_note["category"])
            tags = st.text_input("Tags (comma-separated)", value=", ".join(selected_note["tags"]))
            submitted = st.form_submit_button("Update note")
            if submitted:
                payload = {
                    "title": title,
                    "content": content,
                    "category": category,
                    "tags": parse_tags(tags),
                }
                response = api_request("PUT", f"/notes/{selected_note_id}", json=payload)
                if response is not None:
                    if response.status_code == 200:
                        st.success("Note updated successfully")
                    else:
                        st.error(f"Failed to update note: {response.status_code} - {response.text}")
        if st.button("Delete selected note"):
            response = api_request("DELETE", f"/notes/{selected_note_id}")
            if response is not None:
                if response.status_code == 204:
                    st.success("Note deleted successfully")
                else:
                    st.error(f"Failed to delete note: {response.status_code} - {response.text}")

st.sidebar.markdown("---")
st.sidebar.markdown("**Backend URL:**")
st.sidebar.write(API_BASE_URL)   
