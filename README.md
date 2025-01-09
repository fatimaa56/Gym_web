Apex Fitness Web Application
Apex Fitness is a Flask-based web application for showcasing the services, mission, and membership options of a fitness center. It uses dynamic routing, HTML templates, and CSS for an engaging user experience.

Features
Home Page: A hero section with branding, navigation links, and a call-to-action.
About Us Page: Detailed information about the fitness center's team, mission, and values.
Membership Page: Different membership plans with descriptions and visually appealing images.

Project Structure
├── app.py                 # Main Flask application file
├── templates/             # Folder containing HTML templates
│   ├── index.html         # Home page template
│   ├── about.html         # About Us page template
│   └── membership.html    # Membership page template
├── static/                # Static files like CSS and images
│   ├── style.css          # Stylesheet for the home page
│   ├── about.css          # Stylesheet for the About Us page
│   ├── membership.css     # Stylesheet for the Membership page
│   └── images/            # Folder for static images (optional)
└── README.md              # Project documentation

Getting Started
Prerequisites
Python 3.8 or higher
Flask installed (pip install flask)

File Details
app.py
The main Flask application:

Defines routes for the home page, About Us page, and Membership page.
Uses Flask's render_template function to serve HTML templates.
Templates (/templates/)
index.html: Contains the layout and content for the home page.
about.html: Provides detailed information about Apex Fitness and its team.
membership.html: Displays membership plans and benefits.
Static Files (/static/)
style.css: Styles the home page (index.html).
about.css: Styles the About Us page (about.html).
membership.css: Styles the Membership page (membership.html).

Future Enhancements
Add user authentication for secure access to personalized features.
Integrate a database for user data and membership management.
Implement a contact form for inquiries.
Add a scheduling feature for classes and training sessions.
Enhance the application with JavaScript for better interactivity.

License
This project is open-source and available under the MIT License.
