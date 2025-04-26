# Pranav_Pandey_CSE2_SmartStationary
Your login, register, and dashboard pages are not styled because the CSS file was not correctly linked. Flask requires using url_for('static', filename='css/style.css') inside the HTML head tag. Also, ensure your CSS is stored under a static/css/ folder. Restart the server after fixing.
