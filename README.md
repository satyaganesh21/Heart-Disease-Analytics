🩺 Heart Disease Analytics Portal

An interactive, data-driven Business Intelligence web application that integrates highly visual Tableau Public dashboards with a responsive, lightweight Python Flask website. This platform transforms raw patient demographic, behavioral, and clinical data into actionable insights to support preventative healthcare and medical decision-making

👥 Project Team & Credits
This portal was developed, tested, and integrated by Healthcaregroup (Academic Year 2026–2027)
Kalyani Badugu – Frontend UI/UX Design & Styling 
G.V.V.Satya Ganesh – Data Engineering & Tableau Analytics

🛠️ Tech Stack & Architecture
The application is built on a decoupled, three-tier architecture to ensure fast load times, modularity, and easy maintenance

Backend: Python 3.x with the Flask micro-framework
Frontend:HTML5 (semantic elements), CSS3 (Flexbox/Grid), JavaScript (dynamic UI controls) 
Visualization Layer: Tableau Public embedded dynamically via the Tableau JavaScript API
tyling & Iconography: FontAwesome Core Libraries


📊 Operational Scenarios & Dashboard Mapping
Rather than displaying flat charts, this portal organizes its visualizations across three target real-world user paths

1. Dr. Sharma (Senior Cardiologist)
Objective:Diagnose chronic comorbidity thresholds and isolate vulnerable patient age groups.
Dashboards:Diabetes vs. Stroke Matrix,Diabetes & Average Age Tracking, and Clinical Age Trend Lines.

2. Ramesh (Public Health Policy Maker)
Objective: Map community wellness habits and demographic indicators to design targeted, state-funded preventative campaigns.
Dashboards: Race-Wise Caseload Distribution, Gender Proportions, and the Effect of Physical Activity on Heart Disease.

3. Anita (Preventive Care Consumer)
Objective: Monitor personal medical metrics against healthy population baselines.
Dashboards: Smoking & Alcohol Impact Grid, Personal Health Benchmarks, and Lifestyle Adaptation Index.

📂 Project Structure

Heart Disease Analysis/
│
├── app.py                     # Main Flask router & server initialization
├── templates/
│   └── index.html             # Master HTML single-page application template
├── static/
│   ├── css/
│   │   └── style.css          # Flexbox layout system & custom components
│   └── js/
│       └── main.js            # Scroll observers & Tableau resizing scripts
└── .gitignore                 # Excludes caches, virtual envs, and system files
