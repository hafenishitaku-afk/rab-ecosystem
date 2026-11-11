from flask import Flask, render_template_string

app = Flask(__name__)

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
        "url": "https://rab-community.onrender.com",
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

HTML = """
<!doctype html>
<html>
<head>
<title>RAB Ecosystem</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body { font-family: system-ui, sans-serif; margin: 0; background: #0d1f46; color: #fff; }
  .wrap { max-width: 960px; margin: 0 auto; padding: 60px 24px; }
  h1 { font-size: 2.4rem; margin: 0 0 8px; }
  .sub { color: #9fb3d1; margin-bottom: 40px; }
  .grid { display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
  .card { background: #15294f; border-radius: 12px; padding: 24px; border: 1px solid #23407a; }
  .card h2 { margin: 0 0 8px; font-size: 1.2rem; color: #ffe500; }
  .card p { color: #c5d3e8; margin: 0 0 16px; line-height: 1.4; }
  .card .stack { font-size: 0.8rem; color: #7f93b3; margin-bottom: 12px; }
  .card a { display: inline-block; background: #ffe500; color: #0d1f46; padding: 10px 18px; border-radius: 8px; text-decoration: none; font-weight: 600; }
  .card a:hover { background: #ffef6a; }
  .status { display: inline-block; font-size: 0.75rem; padding: 3px 10px; border-radius: 999px; background: #1e7a3d; margin-bottom: 12px; }
  footer { margin-top: 60px; color: #7f93b3; font-size: 0.85rem; text-align: center; }
</style>
</head>
<body>
<div class="wrap">
  <h1>RAB Ecosystem</h1>
  <p class="sub">Tools for the Namibian gig economy — built, deployed, and running.</p>
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
      <a href="#" style="opacity:.4;pointer-events:none;">Coming online</a>
      {% endif %}
    </div>
    {% endfor %}
  </div>
  <footer>
    Built by KaxHafeni · RAB Ecosystem
  </footer>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, modules=MODULES)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))