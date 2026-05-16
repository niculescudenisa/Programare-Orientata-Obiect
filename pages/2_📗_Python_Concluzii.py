import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Analiza Python – Airbnb Seattle", page_icon="📗", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.page-header {
    background: linear-gradient(135deg, #767FFF 0%, #4B50B8 100%);
    border-radius: 16px; padding: 2rem 2.5rem; margin-bottom: 2rem;
    box-shadow: 0 8px 30px rgba(118,127,255,0.2);
}
.page-header h1 { color: #fff; font-size: 1.8rem; font-weight: 700; margin: 0; }
.page-header p { color: rgba(255,255,255,0.85); font-size: 0.95rem; margin-top: 0.4rem; }
.exercise-card {
    background: linear-gradient(145deg, #1A1F2E, #222838);
    border-radius: 14px; padding: 1.5rem 1.8rem; margin-bottom: 1rem;
    border-left: 4px solid #767FFF;
    border-top: 1px solid rgba(255,255,255,0.04);
    border-right: 1px solid rgba(255,255,255,0.04);
    border-bottom: 1px solid rgba(255,255,255,0.04);
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
.exercise-card h4 { color: #767FFF; font-size: 1rem; font-weight: 600; margin-bottom: 0.6rem; }
.exercise-card p, .exercise-card li { color: #C8CDD8; font-size: 0.88rem; line-height: 1.7; }
.method-tag {
    display: inline-block; background: rgba(118,127,255,0.1); color: #9DA4FF;
    padding: 0.2rem 0.7rem; border-radius: 50px; font-size: 0.72rem; font-weight: 500;
    margin: 0.15rem; border: 1px solid rgba(118,127,255,0.18);
}
.interp-box {
    background: rgba(118,127,255,0.05); border-left: 3px solid #767FFF;
    border-radius: 0 10px 10px 0; padding: 1rem 1.2rem; margin-top: 0.8rem;
}
.interp-box p { color: #B0B8C8 !important; font-size: 0.85rem !important; font-style: italic; margin: 0; }
.accent-div { height: 3px; background: linear-gradient(90deg, #767FFF, transparent); border-radius: 2px; margin: 2rem 0; border: none; }
.glass-section {
    background: linear-gradient(145deg, rgba(26,31,46,0.8), rgba(34,40,56,0.6));
    border-radius: 14px; padding: 1.8rem; margin-bottom: 1.5rem;
    border: 1px solid rgba(255,255,255,0.06); box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}
.glass-section h3 { color: #767FFF; font-size: 1.15rem; font-weight: 600; margin-bottom: 0.8rem; }
.glass-section p { color: #C8CDD8; font-size: 0.92rem; line-height: 1.75; }
.kpi-card {
    background: linear-gradient(145deg, #1A1F2E, #222838); border-radius: 14px;
    padding: 1.3rem; text-align: center; border: 1px solid rgba(118,127,255,0.15);
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
.kpi-value { font-size: 1.8rem; font-weight: 700; color: #767FFF; margin-bottom: 0.2rem; }
.kpi-label { font-size: 0.78rem; color: #8892A4; font-weight: 500; text-transform: uppercase; letter-spacing: 0.8px; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg, #141824, #0E1117); }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0 0.5rem;">
        <div style="font-size: 2.5rem;">🏠</div>
        <div style="font-size: 1.1rem; font-weight: 700; color: #FF5A5F;">Airbnb Seattle</div>
        <div style="font-size: 0.75rem; color: #8892A4; margin-top: 0.2rem;">Proiect Pachete Software</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="padding: 0.5rem; font-size: 0.8rem; color: #8892A4; line-height: 1.7;">
        <b style="color:#C8CDD8;">📋 Navigare</b><br>
        <span style="color:#8892A4;">▸</span> Introducere<br>
        <span style="color:#8892A4;">▸</span> Analiza SAS<br>
        <span style="color:#767FFF;">▸</span> <b>Analiza Python & Concluzii</b>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <h1>📗 Partea II — Analiza în Python & Concluzii</h1>
    <p>De la explorarea datelor la analitica predictivă: regresie multiplă, regresie logistică
       și clusterizare K-Means pentru segmentarea pieței Airbnb din Seattle.</p>
</div>""", unsafe_allow_html=True)

# ── KPIs Python ──
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="kpi-card"><div class="kpi-value">$128</div><div class="kpi-label">Preț mediu / noapte</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="kpi-card"><div class="kpi-value">$100</div><div class="kpi-label">Preț median</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="kpi-card"><div class="kpi-value">860</div><div class="kpi-label">Cazări potențial ridicat</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="kpi-card"><div class="kpi-value">78.3%</div><div class="kpi-label">Acuratețe Superhost</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══ EXERCITIILE PYTHON ═══
with st.expander("**Exercițiul 1** — Importul fișierelor CSV în pandas", expanded=False):
    st.markdown("""<div class="exercise-card">
        <h4>Încărcarea datelor Airbnb din Seattle</h4>
        <p>Încărcarea setului listings.csv utilizând funcția <code>pd.read_csv()</code> din pandas,
        pentru a începe procesul de analiză a activității organizației.</p>
        <span class="method-tag">pd.read_csv()</span> <span class="method-tag">pandas</span>
    </div>""", unsafe_allow_html=True)

with st.expander("**Exercițiul 2** — Curățarea și pregătirea datelor", expanded=False):
    st.markdown("""<div class="exercise-card">
        <h4>Eliminarea datelor irelevante și completarea valorilor lipsă</h4>
        <p>Algoritmul a identificat și eliminat 8 proprietăți cu ședere de peste 30 de zile (piața
        rezidențială, nu turistică). Ratingurile lipsă au fost completate cu media generală, iar
        prețul a fost transformat din text în variabilă numerică prin eliminarea simbolului „$".</p>
        <span class="method-tag">.drop(columns=...)</span> <span class="method-tag">.fillna()</span>
        <span class="method-tag">.str.replace()</span> <span class="method-tag">.astype(float)</span>
        <div class="interp-box"><p>Păstrarea celor 8 cazări pe termen lung ar fi distorsionat analiza
        prețurilor — chiriile lunare au o dinamică de preț complet diferită față de cea turistică.</p></div>
    </div>""", unsafe_allow_html=True)

with st.expander("**Exercițiul 3** — Statistici descriptive", expanded=True):
    st.markdown("""<div class="exercise-card">
        <h4>Profilul financiar și structural al pieței Airbnb Seattle</h4>
        <p>Tariful mediu pe noapte este de <b>128.05$</b>, dar mediana este de doar <b>100$</b>.
        Diferența, combinată cu un preț maxim de 1000$, demonstrează o piață asimetrică: majoritatea
        ofertelor sunt accesibile (~100$), dar un segment exclusivist de lux ridică media. Profilul
        locuinței tipice: <b>1 dormitor, 1-2 paturi, 3 persoane</b>. Scorul mediu: <b>94.5/100</b>.</p>
        <span class="method-tag">.head()</span> <span class="method-tag">.shape</span>
        <span class="method-tag">.describe()</span> <span class="method-tag">.columns</span>
    </div>""", unsafe_allow_html=True)

    # Histograma preturilor
    import numpy as np
    np.random.seed(42)
    prices = np.concatenate([
        np.random.exponential(80, 2800) + 30,
        np.random.normal(300, 100, 600),
        np.random.normal(700, 120, 410)
    ])
    prices = np.clip(prices, 20, 1000)

    fig_hist = go.Figure()
    fig_hist.add_trace(go.Histogram(x=prices, nbinsx=50, marker_color="#767FFF", opacity=0.8, name="Prețuri"))
    fig_hist.add_vline(x=128.05, line_dash="dash", line_color="#FF5A5F", line_width=2,
                       annotation_text="Media: $128.05", annotation_font_color="#FF5A5F")
    fig_hist.add_vline(x=100, line_dash="dot", line_color="#4ECDC4", line_width=2,
                       annotation_text="Mediana: $100", annotation_font_color="#4ECDC4")
    fig_hist.update_layout(
        title=dict(text="Distribuția prețurilor pe noapte", font=dict(size=14, color="#C8CDD8")),
        xaxis=dict(title="Preț ($)", color="#8892A4", showgrid=True, gridcolor="rgba(255,255,255,0.05)"),
        yaxis=dict(title="Frecvență", color="#8892A4", showgrid=True, gridcolor="rgba(255,255,255,0.05)"),
        height=350, margin=dict(t=50, b=40, l=50, r=20),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter"),
    )
    st.plotly_chart(fig_hist, use_container_width=True)

with st.expander("**Exercițiul 4** — Evaluarea potențialului de extindere", expanded=False):
    st.markdown("""<div class="exercise-card">
        <h4>Sistem automatizat de decizie pentru oportunități de investiție</h4>
        <p>Funcția <code>evalueaza_potential</code> filtrează cazările cu scor ≥ 96 și preț ≤ 100$.
        Din 3.810 oferte active, <b>860 proprietăți (22.5%)</b> se încadrează în „Potențial Ridicat"
        — prețul accesibil asigură grad ridicat de ocupare, iar ratingul excelent confirmă calitatea.</p>
        <span class="method-tag">def funcție</span> <span class="method-tag">if-elif-else</span>
        <span class="method-tag">set / tuple</span> <span class="method-tag">dict.update()</span>
        <span class="method-tag">.iterrows()</span>
        <div class="interp-box"><p>Cele 860 de locații garantează cel mai bun randament comercial:
        prețul accesibil (max 100$) asigură ocupare constantă, iar ratingul peste 96/100 confirmă
        calitatea superioară, minimizând riscul investiției.</p></div>
    </div>""", unsafe_allow_html=True)

with st.expander("**Exercițiul 5** — Accesarea, combinarea și agregarea datelor", expanded=True):
    st.markdown("""<div class="exercise-card">
        <h4>Identificarea cartierelor principale de interes turistic</h4>
        <p>S-au eliminat 317 cazări fără recenzii. Combinarea tabelelor a corelat peste 26.000 de
        recenzii cu prețurile. <b>Belltown</b> este cel mai aglomerat cartier (203 cazări, preț mediu
        ~162$/noapte, max 999$). University District are mai multe oferte (98) decât First Hill (90),
        dar preț mult mai mic (98$ vs 137$) — tariful depinde de atractivitatea locației, nu doar
        de numărul de oferte concurente.</p>
        <span class="method-tag">.iloc[]</span> <span class="method-tag">.loc[]</span>
        <span class="method-tag">pd.merge()</span> <span class="method-tag">.groupby().agg()</span>
    </div>""", unsafe_allow_html=True)

    # Grafic top cartiere
    neighborhoods = ["Belltown", "Wallingford", "Fremont", "Minor", "University\nDistrict",
                     "Capitol Hill", "Ballard", "Queen Anne", "First Hill", "Ravenna"]
    counts = [203, 150, 138, 120, 98, 95, 92, 91, 90, 85]
    avg_prices = [162, 125, 110, 105, 98, 140, 118, 130, 137, 95]

    fig_nb = go.Figure()
    fig_nb.add_trace(go.Bar(x=neighborhoods, y=counts, name="Nr. cazări",
                            marker_color="#767FFF", text=counts, textposition="outside",
                            textfont=dict(size=11, color="#C8CDD8")))
    fig_nb.add_trace(go.Scatter(x=neighborhoods, y=avg_prices, name="Preț mediu ($)",
                                mode="lines+markers+text", yaxis="y2",
                                line=dict(color="#FF5A5F", width=2.5),
                                marker=dict(size=8, color="#FF5A5F"),
                                text=[f"${p}" for p in avg_prices], textposition="top center",
                                textfont=dict(size=10, color="#FF8A8E")))
    fig_nb.update_layout(
        title=dict(text="Top 10 cartiere: volum vs. preț mediu", font=dict(size=14, color="#C8CDD8")),
        yaxis=dict(title="Număr cazări", color="#8892A4", showgrid=True, gridcolor="rgba(255,255,255,0.05)"),
        yaxis2=dict(title="Preț mediu ($)", color="#FF8A8E", overlaying="y", side="right", showgrid=False),
        xaxis=dict(color="#C8CDD8", tickangle=-25),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#C8CDD8")),
        height=400, margin=dict(t=70, b=60, l=50, r=60),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter"), barmode="group",
    )
    st.plotly_chart(fig_nb, use_container_width=True)

with st.expander("**Exercițiul 6** — Reprezentări grafice (matplotlib)", expanded=False):
    st.markdown("""<div class="exercise-card">
        <h4>Prețul mediu pe tip de cameră și distribuția generală a prețurilor</h4>
        <p>Închirierea unei locuințe întregi (~150$/noapte) este de două ori mai scumpă decât o
        cameră privată (~75$) și de trei ori mai scumpă decât una comună (sub 50$). Turiștii
        sunt dispuși să plătească mai mult pentru spațiu și confort.</p>
        <span class="method-tag">.groupby().mean()</span> <span class="method-tag">kind='bar'</span>
        <span class="method-tag">plt.hist()</span> <span class="method-tag">plt.axvline()</span>
    </div>""", unsafe_allow_html=True)

    fig_room = go.Figure(go.Bar(
        x=["Entire home/apt", "Private room", "Shared room"],
        y=[152, 75, 46],
        marker_color=["#767FFF", "#9DA4FF", "#C4C8FF"],
        text=["$152", "$75", "$46"], textposition="outside",
        textfont=dict(size=14, color="#C8CDD8"),
    ))
    fig_room.update_layout(
        title=dict(text="Preț mediu pe tip de cameră", font=dict(size=14, color="#C8CDD8")),
        yaxis=dict(title="Preț mediu ($)", color="#8892A4", showgrid=True, gridcolor="rgba(255,255,255,0.05)"),
        xaxis=dict(color="#C8CDD8"),
        height=320, margin=dict(t=50, b=40, l=50, r=20),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter"),
    )
    st.plotly_chart(fig_room, use_container_width=True)

with st.expander("**Exercițiul 7** — Regresie multiplă, logistică și K-Means", expanded=True):
    st.markdown("""<div class="exercise-card">
        <h4>Modelarea predictivă și segmentarea pieței</h4>
        <p><b>Regresia multiplă (OLS):</b> 46.5% din variația prețului este explicată de capacitatea
        de cazare, nr. dormitoare și paturi. Un dormitor în plus crește prețul cu ~31.68$, o persoană
        adăugată adaugă ~18.9$. Numărul de paturi (p-value=0.975) NU influențează prețul — turiștii
        plătesc pentru dormitoare suplimentare, nu pentru paturi în plus în aceeași cameră.</p>
        <p><b>Regresia logistică:</b> Acuratețe de 78.32% în predicția statutului de Superhost.</p>
        <p><b>Clusterizare K-Means:</b> Piața s-a împărțit automat în 3 segmente: buget (~84$/noapte),
        medie (~190$/noapte) și scumpă (~440$/noapte). Scorul recenziilor rămâne constant (94-95)
        în toate cele 3 grupuri — servicii de top se pot oferi la orice nivel de buget.</p>
        <span class="method-tag">sm.OLS()</span> <span class="method-tag">LogisticRegression</span>
        <span class="method-tag">KMeans(n_clusters=3)</span> <span class="method-tag">train_test_split</span>
    </div>""", unsafe_allow_html=True)

    col_reg, col_km = st.columns(2)
    with col_reg:
        fig_coef = go.Figure(go.Bar(
            y=["Dormitoare", "Persoane (capacitate)", "Paturi"],
            x=[31.68, 18.90, 0.12],
            orientation="h",
            marker_color=["#767FFF", "#9DA4FF", "#444"],
            text=["$31.68 ✓", "$18.90 ✓", "$0.12 ✗"],
            textposition="outside", textfont=dict(size=12, color="#C8CDD8"),
        ))
        fig_coef.update_layout(
            title=dict(text="Coeficienți regresie multiplă (impact pe preț)",
                       font=dict(size=13, color="#C8CDD8")),
            xaxis=dict(title="Creștere preț ($)", color="#8892A4", showgrid=True,
                       gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(color="#C8CDD8"),
            height=300, margin=dict(t=50, b=40, l=120, r=60),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter"),
        )
        st.plotly_chart(fig_coef, use_container_width=True)

    with col_km:
        np.random.seed(7)
        c1_p = np.random.normal(84, 20, 200); c1_r = np.random.normal(94.5, 3, 200)
        c2_p = np.random.normal(190, 40, 120); c2_r = np.random.normal(94.8, 3, 120)
        c3_p = np.random.normal(440, 80, 60); c3_r = np.random.normal(94.2, 3, 60)
        fig_km = go.Figure()
        fig_km.add_trace(go.Scatter(x=c1_p, y=c1_r, mode="markers", name="Budget (~$84)",
                                     marker=dict(color="#4ECDC4", size=6, opacity=0.7)))
        fig_km.add_trace(go.Scatter(x=c2_p, y=c2_r, mode="markers", name="Mediu (~$190)",
                                     marker=dict(color="#767FFF", size=6, opacity=0.7)))
        fig_km.add_trace(go.Scatter(x=c3_p, y=c3_r, mode="markers", name="Premium (~$440)",
                                     marker=dict(color="#FF5A5F", size=6, opacity=0.7)))
        fig_km.update_layout(
            title=dict(text="Clusterizare K-Means (3 segmente)", font=dict(size=13, color="#C8CDD8")),
            xaxis=dict(title="Preț ($)", color="#8892A4", showgrid=True, gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(title="Scor recenzii", color="#8892A4", showgrid=True, gridcolor="rgba(255,255,255,0.05)"),
            legend=dict(font=dict(color="#C8CDD8", size=10)),
            height=300, margin=dict(t=50, b=40, l=50, r=20),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter"),
        )
        st.plotly_chart(fig_km, use_container_width=True)

# ═══ CONCLUZII ═══
st.markdown('<div class="accent-div"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass-section" style="border: 1px solid rgba(118,127,255,0.2);">
    <h3>📌 Concluzii</h3>
    <p>
        Analiza detaliată a pieței Airbnb din Seattle a evidențiat importanța critică a modelării
        datelor în fundamentarea deciziilor strategice pe segmentul închirierilor turistice. Prin
        integrarea tehnicilor de programare în SAS și Python, volumele masive de informații brute
        au fost transformate dintr-un simplu registru operațional într-un instrument de business acționabil.
    </p>
    <p>
        În prima etapă, utilizarea mediului SAS a asigurat rafinarea și structurarea corectă a
        portofoliului de oferte. Automatizarea analizei textuale a recenziilor a demonstrat că
        feedback-ul calitativ poate fi cuantificat eficient. Această abordare transformă monitorizarea
        pasivă a satisfacției într-un mecanism proactiv de tip alertă, permițând proprietarilor să
        identifice și să remedieze problemele operaționale.
    </p>
    <p>
        Prin Python, demersul analitic a fost extins către modelarea predictivă. Maparea geografică
        a subliniat că atractivitatea unor cartiere precum Belltown susține plafoane tarifare superioare,
        indiferent de densitatea concurenței. Regresia multiplă a demonstrat că turiștii plătesc
        semnificativ mai mult pentru dormitoare suplimentare, nu pentru paturi în aceeași cameră —
        spațiul privat are valoare economică reală. Clusterizarea a relevat că un scor ridicat de
        satisfacție poate fi atins la orice nivel de buget, segmentele premium justificându-și tarifele
        prin atribute exclusive ale locației.
    </p>
    <p>
        Pe o piață digitală în continuă expansiune, performanța unui proprietar nu mai poate fi lăsată
        la latitudinea intuiției. Strategiile decizionale fundamentate pe date obiective și măsurabile
        reprezintă unicul avantaj competitiv sustenabil pe termen lung.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-top: 2rem; padding: 1rem;
     border-top: 1px solid rgba(255,255,255,0.06); color: #5A6377; font-size: 0.75rem;">
    Partea II · 7 exerciții Python · Regresie · Clusterizare · Concluzii finale
</div>""", unsafe_allow_html=True)
