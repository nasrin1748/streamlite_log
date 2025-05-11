import streamlit as st

# Set the page title
st.set_page_config(page_title="Single-Link Streamlit App", layout="centered")

# Dictionary to store user credentials (for demo purposes)
USER_CREDENTIALS = {
    "admin": "password123",
    "user1": "pass1",
    "user2": "pass2"
}

# Function to handle login
def login():
    # Title for the login page
    st.title("Login Page")

    # Username and password inputs
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        # Check if the entered credentials are valid
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.success(f"Welcome, {username}!")
            # Save the login state (session state)
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
        else:
            st.error("Invalid username or password. Please try again.")

# Function to handle logout
def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.success("You have been logged out.")

# Function to render content dynamically
def render_content(page):
    # Define the content for each page
    pages = {
        "home": ("Home Page", "Welcome to the home page!"),
        "about": ("About Us", "This is the about page. Learn more about us here."),
        "contact": ("Contact Us", "This is the contact page. Get in touch with us!"),
    }

    # Get content for the selected page
    title, content = pages.get(page, ("404 Not Found", "The page you requested does not exist."))
    st.title(title)
    st.write(content)

# Main application
def main():
    # If the user is not logged in, show the login page
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        login()
    else:
        # If the user is logged in, show the main app interface
        st.sidebar.title(f"Welcome, {st.session_state['username']}!")
        st.sidebar.button("Logout", on_click=logout)

        # Sidebar navigation
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", options=["home", "about", "contact"])

        # Render the selected page
        render_content(page)

# Run the main application
if __name__ == "__main__":
    main()
