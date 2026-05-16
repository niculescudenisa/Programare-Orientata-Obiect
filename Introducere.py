import streamlit as st
import plotly.graph_objects as go

# ──────────────────── CONFIG ────────────────────
st.set_page_config(
    page_title="Airbnb Seattle – Proiect PS",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────── CUSTOM CSS ────────────────────
st.markdown("""
<style>
/* ── Import Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }

/* ── Hide default Streamlit branding ── */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #FF5A5F 0%, #FF385C 40%, #BD1E59 100%);
    border-radius: 18px;
    padding: 3rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 12px 40px rgba(255, 90, 95, 0.25);
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-banner h1 {
    color: #fff;
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
    letter-spacing: -0.5px;
}
.hero-banner .subtitle {
    color: rgba(255,255,255,0.88);
    font-size: 1.15rem;
    font-weight: 300;
    margin-bottom: 0;
    line-height: 1.6;
}
.hero-banner .badge {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    color: #fff;
    padding: 0.3rem 1rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 500;
    margin-bottom: 1rem;
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255,255,255,0.15);
}

/* ── KPI Cards ── */
.kpi-card {
    background: linear-gradient(145deg, #1A1F2E, #222838);
    border-radius: 14px;
    padding: 1.5rem;
    text-align: center;
    border: 1px solid rgba(255, 90, 95, 0.15);
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
.kpi-card:hover {
    border-color: rgba(255, 90, 95, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
.kpi-value {
    font-size: 2.2rem;
    font-weight: 700;
    color: #FF5A5F;
    line-height: 1.1;
    margin-bottom: 0.3rem;
}
.kpi-label {
    font-size: 0.82rem;
    color: #8892A4;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

/* ── Glass Sections ── */
.glass-section {
    background: linear-gradient(145deg, rgba(26,31,46,0.8), rgba(34,40,56,0.6));
    border-radius: 14px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}
.glass-section h3 {
    color: #FF5A5F;
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.glass-section p, .glass-section li {
    color: #C8CDD8;
    font-size: 0.92rem;
    line-height: 1.75;
}

/* ── Accent Divider ── */
.accent-divider {
    height: 3px;
    background: linear-gradient(90deg, #FF5A5F, transparent);
    border-radius: 2px;
    margin: 1.5rem 0;
    border: none;
}

/* ── Tech Pills ── */
.tech-pill {
    display: inline-block;
    background: rgba(255, 90, 95, 0.12);
    color: #FF8A8E;
    padding: 0.35rem 1rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 500;
    margin: 0.2rem 0.3rem;
    border: 1px solid rgba(255, 90, 95, 0.2);
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #141824 0%, #0E1117 100%);
    border-right: 1px solid rgba(255,255,255,0.05);
}

/* ── Streamlit Metrics override ── */
[data-testid="stMetricValue"] {
    color: #FF5A5F !important;
}

/* ── Expander styling ── */
.streamlit-expanderHeader {
    font-weight: 600 !important;
    color: #FAFAFA !important;
}
</style>
""", unsafe_allow_html=True)

# ──────────────────── SIDEBAR ────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0 0.5rem;">
        <div style="font-size: 2.5rem;">🏠</div>
        <div style="font-size: 1.1rem; font-weight: 700; color: #FF5A5F; letter-spacing: -0.3px;">
            Airbnb Seattle
        </div>
        <div style="font-size: 0.75rem; color: #8892A4; margin-top: 0.2rem;">
            Proiect Pachete Software
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="padding: 0.5rem; font-size: 0.8rem; color: #8892A4; line-height: 1.7;">
        <b style="color:#C8CDD8;">📋 Navigare</b><br>
        <span style="color:#FF5A5F;">▸</span> <b>Introducere</b> — context și obiective<br>
        <span style="color:#8892A4;">▸</span> Analiza SAS — 11 exerciții<br>
        <span style="color:#8892A4;">▸</span> Analiza Python & Concluzii
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.72rem; color: #5A6377; text-align: center; padding-top: 0.5rem;">
        Academia de Studii Economice<br>Facultatea CSIE<br>
        Seria B · Grupa 1078<br>Cibernetică Economică
    </div>
    """, unsafe_allow_html=True)

# ──────────────────── HERO ────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="badge">📊 Proiect Pachete Software</div>
    <h1>Analiza Organizației Airbnb — Seattle</h1>
    <p class="subtitle">
        Studiu analitic al pieței de închirieri turistice din Seattle, realizat prin 
        integrarea tehnicilor de programare SAS și Python, de la curățarea datelor brute
        până la modelarea predictivă și segmentarea pieței.
    </p>
</div>
""", unsafe_allow_html=True)

# ──────────────────── KPIs ────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">3.810</div>
        <div class="kpi-label">Oferte active de cazare</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">50.000</div>
        <div class="kpi-label">Recenzii analizate</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">$128</div>
        <div class="kpi-label">Preț mediu / noapte</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">94.5</div>
        <div class="kpi-label">Scor mediu recenzii</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ──────────────────── CONTEXT ────────────────────
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("""
    <div class="glass-section">
        <h3>📌 Contextul proiectului</h3>
        <p>
            Apariția economiei colaborative (<em>sharing economy</em>) a transformat fundamental
            sectorul turismului și al ospitalității la nivel global. În centrul acestei schimbări
            se află Airbnb, o platformă care a eliminat intermediarii clasici, conectând direct
            proprietarii de locuințe cu turiștii în căutare de alternative la hotelurile tradiționale.
        </p>
        <p>
            Pe această piață, prețurile nu mai sunt dictate de mari lanțuri hoteliere, ci se
            reglează organic prin cerere și ofertă, fiind influențate de zeci de factori: de la
            dotările locuinței și locația exactă pe hartă, până la reputația gazdei și recenziile
            lăsate de clienții anteriori.
        </p>
        <p>
            Proiectul de față realizează o analiză detaliată a operațiunilor și ofertelor Airbnb,
            concentrându-se pe piața dintr-un oraș dinamic din SUA — <b>Seattle</b>. Scopul
            principal este extragerea de informații de business valoroase dintr-un volum masiv de
            date brute (oferte de cazare, calendare de disponibilitate și mii de recenzii ale clienților)
            pentru a fundamenta decizii economice optime.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class="glass-section">
        <h3>🎯 Obiective principale</h3>
        <p>
            <b>1.</b> Curățarea și standardizarea datelor brute provenite de pe platforma Kaggle
            (fișiere <em>listings.csv</em>, <em>calendar.csv</em>, <em>reviews.csv</em>).<br><br>
            <b>2.</b> Analiza descriptivă a pieței: segmentarea ofertelor pe categorii de buget,
            identificarea liderilor de performanță și monitorizarea feedback-ului clienților.<br><br>
            <b>3.</b> Analiza predictivă prin modele de Machine Learning: regresie multiplă,
            regresie logistică și clusterizare K-Means pentru segmentarea pieței.<br><br>
            <b>4.</b> Formularea de recomandări strategice pentru proprietari și investitori pe
            baza rezultatelor obținute.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ──────────────────── DIVIDER ────────────────────
st.markdown('<div class="accent-divider"></div>', unsafe_allow_html=True)

# ──────────────────── METHODOLOGY ────────────────────
st.markdown("""
<div class="glass-section">
    <h3>🔬 Metodologie și structură</h3>
    <p>
        Cercetarea a fost structurată în două etape tehnologice complementare, utilizând
        medii de programare distincte: <b>SAS</b> (11 exerciții) și <b>Python</b> (7 exerciții).
    </p>
</div>
""", unsafe_allow_html=True)

col_sas, col_py = st.columns(2)

with col_sas:
    st.markdown("""
    <div class="glass-section" style="border-left: 3px solid #FF5A5F;">
        <h3>📘 Partea I — SAS</h3>
        <p style="margin-bottom: 0.8rem;">
            Concentrată pe <b>curățarea datelor</b> și pe <b>analiza descriptivă</b> a pieței.
            Procesul a debutat cu standardizarea variabilelor financiare și filtrarea
            disponibilităților reale, asigurând că analizele reflectă doar oferta activă.
        </p>
        <p>
            Un accent deosebit a fost pus pe <b>analiza calitativă a feedback-ului</b> —
            prin algoritmi iterativi de scanare a textului, recenziile nestructurate
            au fost transformate în indicatori de performanță. S-au construit sisteme
            automate de detecție a satisfacției și a problemelor operaționale (curățenie, zgomot).
        </p>
        <div style="margin-top: 1rem;">
            <span class="tech-pill">PROC FORMAT</span>
            <span class="tech-pill">PROC SORT</span>
            <span class="tech-pill">PROC SQL</span>
            <span class="tech-pill">ARRAY</span>
            <span class="tech-pill">PROC GCHART</span>
            <span class="tech-pill">PROC SGPLOT</span>
            <span class="tech-pill">PROC MEANS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_py:
    st.markdown("""
    <div class="glass-section" style="border-left: 3px solid #767FFF;">
        <h3>📗 Partea II — Python</h3>
        <p style="margin-bottom: 0.8rem;">
            Ridică analiza la un <b>nivel strategic</b>, trecând de la explorarea datelor la
            <b>analitica predictivă</b>. S-a aprofundat dinamica prețurilor raportată la
            geografia orașului, identificând polii de maximă concurență (precum cartierul Belltown),
            dar și oportunitățile de extindere.
        </p>
        <p>
            Prin integrarea tehnicilor de <b>Machine Learning</b> — regresia multiplă,
            regresia logistică și clusterizarea K-Means — au fost izolați factorii
            matematici care dictează prețul unei nopți de cazare și s-a reușit segmentarea
            pieței în categorii clare de profitabilitate.
        </p>
        <div style="margin-top: 1rem;">
            <span class="tech-pill">pandas</span>
            <span class="tech-pill">matplotlib</span>
            <span class="tech-pill">statsmodels</span>
            <span class="tech-pill">scikit-learn</span>
            <span class="tech-pill">KMeans</span>
            <span class="tech-pill">OLS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ──────────────────── DATA OVERVIEW CHART ────────────────────
st.markdown('<div class="accent-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass-section">
    <h3>📂 Sursa datelor</h3>
    <p>
        Fișierele brute au fost extrase de pe platforma <b>Kaggle</b>. Seturile de dimensiuni
        mari (<em>calendar.csv</em> și <em>reviews.csv</em>) au fost reduse la 50.000 de rânduri
        fiecare, utilizând metoda <code>.iloc[:50000, :]</code> și salvate pe Google Drive
        sub denumirile <em>calendar_subset.csv</em> și <em>reviews_subset.csv</em>.
    </p>
</div>
""", unsafe_allow_html=True)

# Treemap of datasets
fig_data = go.Figure(go.Treemap(
    labels=[
        "Date Airbnb Seattle",
        "listings.csv", "calendar_subset.csv", "reviews_subset.csv",
        "3.810 proprietăți", "Preț · Disponibilitate · Date",
        "50.000 recenzii", "Feedback clienți",
        "50.000 înregistrări", "Calendare · Prețuri zilnice"
    ],
    parents=[
        "",
        "Date Airbnb Seattle", "Date Airbnb Seattle", "Date Airbnb Seattle",
        "listings.csv", "listings.csv",
        "reviews_subset.csv", "reviews_subset.csv",
        "calendar_subset.csv", "calendar_subset.csv"
    ],
    values=[0, 3810, 50000, 50000, 3810, 3810, 50000, 50000, 50000, 50000],
    textinfo="label",
    marker=dict(
        colors=[
            "#1A1F2E",
            "#FF5A5F", "#FF8A8E", "#FFB3B5",
            "#CC484C", "#E05458",
            "#CC8F91", "#D9A3A5",
            "#CC7072", "#D98486"
        ],
        line=dict(width=2, color="#0E1117")
    ),
    textfont=dict(size=14, color="#fff", family="Inter"),
    hovertemplate="<b>%{label}</b><br>Volum: %{value:,.0f}<extra></extra>",
))
fig_data.update_layout(
    margin=dict(t=30, l=10, r=10, b=10),
    height=320,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter"),
)
st.plotly_chart(fig_data, use_container_width=True)

# ──────────────────── FOOTER ────────────────────
st.markdown("""
<div style="text-align:center; margin-top: 2rem; padding: 1rem; 
     border-top: 1px solid rgba(255,255,255,0.06); color: #5A6377; font-size: 0.75rem;">
    Academia de Studii Economice București · Facultatea de Cibernetică, Statistică și Informatică Economică · 
    Proiect Pachete Software
</div>
""", unsafe_allow_html=True)
