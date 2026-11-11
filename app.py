import os
from flask import Flask, render_template_string

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-fallback")

MODULES = [
    {
        "name": "RAB Rental",
        "tagline": "Rent bicycles by the hour. Automated billing, damage claims, full audit trail.",
        "url": "https://rab-daily-rental.onrender.com",
        "status": "Operational",
        "stack": "Flask · PostgreSQL · 2FA · CSRF",
    },
    {
        "name": "RAB Community",
        "tagline": "Onboard local shops as rental stations. Real-time chat and voice notes.",
        "url": "https://rab-community-app.onrender.com",
        "status": "Operational",
        "stack": "Flask · SQLite/Postgres · Rate limiting",
    },
    {
        "name": "Race App",
        "tagline": "Full event management — registration, finance, volunteers, vendors.",
        "url": "#",
        "status": "Deployed",
        "stack": "Flask · SQLite/Postgres · PDF reports",
    },
    {
        "name": "Loan App",
        "tagline": "Micro-loan management with daily interest engine and borrower portal.",
        "url": "#",
        "status": "Deployed",
        "stack": "Flask · SQLite · Twilio SMS",
    },
]

HOME_HTML = """
<!doctype html>
<html>
<head>
<title>RAB Ecosystem</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body { font-family: system-ui, sans-serif; margin: 0; background: #0d1f46; color: #fff; }
  .wrap { max-width: 960px; margin: 0 auto; padding: 60px 24px; }
  h1 { font-size: 2.4rem; margin: 0 0 8px; }
  .sub { color: #9fb3d1; margin-bottom: 20px; }
  .grid { display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-top: 30px; }
  
  /* Standard Module Cards */
  .card { background: #15294f; border-radius: 12px; padding: 24px; border: 1px solid #23407a; display: flex; flex-direction: column; }
  .card h2 { margin: 0 0 8px; font-size: 1.2rem; color: #ffe500; }
  .card p { color: #c5d3e8; margin: 0 0 16px; line-height: 1.4; flex-grow: 1; }
  .card .stack { font-size: 0.8rem; color: #7f93b3; margin-bottom: 12px; }
  .card a { display: inline-block; background: #ffe500; color: #0d1f46; padding: 10px 18px; border-radius: 8px; text-decoration: none; font-weight: 600; text-align: center; }
  .card a:hover { background: #ffef6a; }
  .status { display: inline-block; font-size: 0.75rem; padding: 3px 10px; border-radius: 999px; background: #1e7a3d; margin-bottom: 12px; align-self: flex-start; }
  
  /* Corporate Mission/Vision Cards */
  .corporate-card { background: #0a1731; border: 2px solid #23407a; }
  .corporate-card h2 { font-size: 1.4rem; border-bottom: 2px solid #ffe500; padding-bottom: 10px; margin-bottom: 15px; }
  .corporate-card ul { padding-left: 20px; margin: 0; color: #c5d3e8; line-height: 1.6; }
  .corporate-card li { margin-bottom: 8px; }
  .corporate-card li strong { color: #fff; }

  .vision-btn { display: inline-block; background: transparent; color: #ffe500; border: 2px solid #ffe500; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-bottom: 20px; transition: 0.3s; }
  .vision-btn:hover { background: #ffe500; color: #0d1f46; }
  footer { margin-top: 60px; color: #7f93b3; font-size: 0.85rem; text-align: center; }
</style>
</head>
<body>
<div class="wrap">
  <h1>RAB Ecosystem</h1>
  <p class="sub">Tools for the Namibian gig economy — built, deployed, and running by RAB BICYCLE SOLUTIONS.</p>
  
  <a href="/vision" class="vision-btn">✨ View the Future of RAB →</a>

  <div class="grid">
    {% for m in modules %}
    <div class="card">
      <span class="status">{{ m.status }}</span>
      <h2>{{ m.name }}</h2>
      <p>{{ m.tagline }}</p>
      <div class="stack">{{ m.stack }}</div>
      {% if m.url != '#' %}
      <a href="{{ m.url }}" target="_blank">Open live demo →</a>
      {% else %}
      <a href="#" style="opacity:.4;pointer-events:none;background:#7f93b3;">Coming online</a>
      {% endif %}
    </div>
    {% endfor %}
    
    <!-- NEW: Vision Card -->
    <div class="card corporate-card">
      <h2>Our Vision</h2>
      <p style="margin-bottom: 10px; font-weight: bold; color: #fff;">To be Namibia's leading bicycle rental service, empowering people and building healthier communities.</p>
      <ul>
        <li><strong>Job Creation:</strong> Creating sustainable income for youth.</li>
        <li><strong>Healthier Customers:</strong> Promoting active, healthy lifestyles.</li>
        <li><strong>Greener Future:</strong> Reducing carbon emissions in our cities.</li>
      </ul>
    </div>

    <!-- NEW: Mission Card -->
    <div class="card corporate-card">
      <h2>Our Mission</h2>
      <p style="margin-bottom: 10px; font-weight: bold; color: #fff;">To provide safe, affordable, and reliable bicycle rentals while driving socio-economic growth.</p>
      <ul>
        <li><strong>Production Increases:</strong> Getting workers to their jobs faster.</li>
        <li><strong>Community Impact:</strong> Partnering with local shops as rental stations.</li>
        <li><strong>Safe Transport:</strong> Providing helmets and maintained bicycles.</li>
      </ul>
    </div>

  </div>
  <footer>Built by Shitaku Hafeni · RAB BICYCLE SOLUTIONS</footer>
</div>
</body>
</html>
"""

VISION_HTML = """
<!doctype html>
<html>
<head>
<title>Our Vision - RAB</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body { font-family: system-ui, sans-serif; margin: 0; background: #0d1f46; color: #fff; }
  .wrap { max-width: 1100px; margin: 0 auto; padding: 40px 24px; }
  h1 { font-size: 2.4rem; margin: 0 0 8px; color: #ffe500; text-align: center; }
  .sub { color: #9fb3d1; margin-bottom: 40px; text-align: center; font-size: 1.2rem; }
  .image-grid { display: grid; gap: 24px; grid-template-columns: 1fr; }
  .image-card { background: #15294f; border-radius: 12px; overflow: hidden; border: 1px solid #23407a; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
  .image-card img { width: 100%; height: auto; display: block; }
  .back-btn { display: inline-block; color: #9fb3d1; text-decoration: none; margin-bottom: 20px; font-weight: bold; }
  .back-btn:hover { color: #ffe500; }
  footer { margin-top: 60px; color: #7f93b3; font-size: 0.85rem; text-align: center; }
</style>
</head>
<body>
<div class="wrap">
  <a href="/" class="back-btn">← Back to Ecosystem</a>
  <h1>More Rides. More Dreams.</h1>
  <p class="sub">A look at the future headquarters and operations of RAB BICYCLE SOLUTIONS.</p>

  <div class="image-grid">
    <div class="image-card">
      <img src="/static/RAB Rent a Bike Executive Office.png" alt="RAB Future Office Workspace">
    </div>
    <div class="image-card">
      <img src="/static/Modern RAB Rent A Bike Office.png" alt="RAB Future Reception">
    </div>
    <div class="image-card">
      <img src="/static/future-meeting.png" alt="RAB Future Strategy Meeting">
    </div>

    
    <div class="image-card">
      <img src="/static/RAB Racer_ Ride More, Dream More.png" alt="The future RAB competitive cycling team">
    </div>
    <div class="image-card">
      <img src="/static/RAB Bikes_ More Rides, More Dreams.png" alt="RAB - Affordable Mobility. Healthier Living. A Greener Namibia">
    </div>
    <div class="image-card">
      <img src="/static/RAB Rent A Bike Office Concept Board.png" alt="RAB Collage - Ride Today Work Tomorrow">
    </div>    

    <div class="image-card">
      <img src="/static/RAB Future Headquarters Vision Poster-1.png">
    </div> 

    
  </div>


  <footer>Built by Shitaku Hafeni · RAB BICYCLE SOLUTIONS</footer>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML, modules=MODULES)

@app.route("/vision")
def vision():
    return render_template_string(VISION_HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))





