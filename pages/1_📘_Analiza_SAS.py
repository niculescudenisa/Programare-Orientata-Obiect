# pyrefly: ignore [missing-import]
import streamlit as st
# pyrefly: ignore [missing-import]
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ──────────────────── CONFIG ────────────────────
st.set_page_config(page_title="Analiza SAS – Airbnb Seattle", page_icon="📘", layout="wide")

# ──────────────────── CSS ────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

.page-header {
    background: linear-gradient(135deg, #FF5A5F 0%, #BD1E59 100%);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 8px 30px rgba(255,90,95,0.2);
}
.page-header h1 {
    color: #fff; font-size: 1.8rem; font-weight: 700; margin: 0;
}
.page-header p {
    color: rgba(255,255,255,0.85); font-size: 0.95rem; margin-top: 0.4rem;
}

.exercise-card {
    background: linear-gradient(145deg, #1A1F2E, #222838);
    border-radius: 14px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1rem;
    border-left: 4px solid #FF5A5F;
    border-top: 1px solid rgba(255,255,255,0.04);
    border-right: 1px solid rgba(255,255,255,0.04);
    border-bottom: 1px solid rgba(255,255,255,0.04);
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
.exercise-card h4 {
    color: #FF5A5F; font-size: 1rem; font-weight: 600; margin-bottom: 0.6rem;
}
.exercise-card p, .exercise-card li {
    color: #C8CDD8; font-size: 0.88rem; line-height: 1.7;
}

.method-tag {
    display: inline-block;
    background: rgba(255,90,95,0.1);
    color: #FF8A8E;
    padding: 0.2rem 0.7rem;
    border-radius: 50px;
    font-size: 0.72rem;
    font-weight: 500;
    margin: 0.15rem 0.15rem;
    border: 1px solid rgba(255,90,95,0.18);
}

.interpretation-box {
    background: rgba(255,90,95,0.05);
    border-left: 3px solid #FF5A5F;
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.2rem;
    margin-top: 0.8rem;
}
.interpretation-box p {
    color: #B0B8C8 !important;
    font-size: 0.85rem !important;
    font-style: italic;
    margin: 0;
}

.section-title {
    color: #FAFAFA;
    font-size: 1.2rem;
    font-weight: 600;
    margin: 1.5rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.accent-divider {
    height: 3px;
    background: linear-gradient(90deg, #FF5A5F, transparent);
    border-radius: 2px;
    margin: 2rem 0 1.5rem;
    border: none;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #141824 0%, #0E1117 100%);
    border-right: 1px solid rgba(255,255,255,0.05);
}
</style>
""", unsafe_allow_html=True)

# ──────────────────── SIDEBAR ────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0 0.5rem;">
        <div style="font-size: 2.5rem;">🏠</div>
        <div style="font-size: 1.1rem; font-weight: 700; color: #FF5A5F;">Airbnb Seattle</div>
        <div style="font-size: 0.75rem; color: #8892A4; margin-top: 0.2rem;">Proiect Pachete Software</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="padding: 0.5rem; font-size: 0.8rem; color: #8892A4; line-height: 1.7;">
        <b style="color:#C8CDD8;">📋 Navigare</b><br>
        <span style="color:#8892A4;">▸</span> Introducere<br>
        <span style="color:#FF5A5F;">▸</span> <b>Analiza SAS — 11 exerciții</b><br>
        <span style="color:#8892A4;">▸</span> Analiza Python & Concluzii
    </div>
    """, unsafe_allow_html=True)

# ──────────────────── HEADER ────────────────────
st.markdown("""
<div class="page-header">
    <h1>📘 Partea I — Analiza în SAS</h1>
    <p>Curățarea datelor, formatarea rapoartelor, analiza textului recenziilor și generarea de grafice
       pentru fundamentarea deciziilor de business pe piața Airbnb din Seattle.</p>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# BLOC 1: Import, curățare, formate
# ════════════════════════════════════════════════
st.markdown('<div class="section-title">🔧 Import, curățare și formatare a datelor</div>', unsafe_allow_html=True)

with st.expander("**Exercițiul 1** — Importul datelor externe, curățarea și crearea de subseturi", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Importul și pregătirea datelor din fișierul calendar.csv</h4>
        <p>
            Coloana aferentă prețului conține simbolul „$" și virgule (ex: „$85.00"), de aceea
            a fost necesară curățarea și transformarea într-o variabilă numerică. S-a creat un
            subset de date care include exclusiv locuințele efectiv disponibile pentru închiriere.
        </p>
        <div>
            <span class="method-tag">INFILE + DSD</span>
            <span class="method-tag">COMPRESS()</span>
            <span class="method-tag">INPUT()</span>
            <span class="method-tag">IF available='t'</span>
        </div>
        <div class="interpretation-box">
            <p>
                Am obținut un set de date curățat ce conține doar oferta activă din piață. Includerea 
                datelor cu status indisponibil ar fi distorsionat statisticile referitoare la capacitatea 
                de cazare și la nivelul prețurilor cerute pe piața Airbnb din Seattle.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("**Exercițiul 2** — Formate definite de utilizator (variabile text)", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Traducerea codurilor tehnice în etichete descriptive</h4>
        <p>
            Statusul proprietăților era stocat ca 't' / 'f'. Prin PROC FORMAT, aceste coduri au
            fost transformate automat în „Disponibil" și „Ocupat / Indisponibil", fără a altera
            datele originale din tabelă.
        </p>
        <div>
            <span class="method-tag">PROC FORMAT</span>
            <span class="method-tag">VALUE $status_disp</span>
            <span class="method-tag">PROC PRINT</span>
        </div>
        <div class="interpretation-box">
            <p>
                Formatarea transformă un simplu tabel într-un instrument de monitorizare rapidă
                pentru management. Un analist poate identifica vizual perioadele cu cerere ridicată,
                iar deciziile legate de Revenue Management pot fi luate mult mai rapid.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("**Exercițiul 3** — Formate definite de utilizator (intervale numerice)", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Segmentarea ofertelor pe categorii de buget</h4>
        <p>
            Managerii Airbnb au nevoie de o segmentare a ofertelor: „Budget" (sub $100), 
            „Mid-Range" ($100–$200) și „Luxury" (peste $200). Algoritmul încadrează automat
            prețurile absolute în categoriile predefinite (ex: 85$ → Budget, 450$ → Luxury).
        </p>
        <div>
            <span class="method-tag">INPUT(COMPRESS(...))</span>
            <span class="method-tag">PROC FORMAT cu intervale</span>
            <span class="method-tag">LOW-99.99 / 100-200 / 200.01-HIGH</span>
        </div>
        <div class="interpretation-box">
            <p>
                Segmentarea permite luarea unor decizii rapide privind strategiile de marketing,
                evaluarea cotei de piață și înțelegerea comportamentului turiștilor în funcție de
                puterea lor de cumpărare — evidențiind o piață puternic diversificată.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="accent-divider"></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════
# BLOC 2: Analiza textului
# ════════════════════════════════════════════════
st.markdown('<div class="section-title">💬 Procesarea și analiza textului recenziilor</div>', unsafe_allow_html=True)

with st.expander("**Exercițiul 4** — Procesarea iterativă și condițională a datelor", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Clasificarea automată a recenziilor pe baza unui scor de satisfacție</h4>
        <p>
            Citirea manuală a recenziilor de către un manager este ineficientă. S-a creat un
            algoritm automat care parcurge textul, caută iterativ cuvinte-cheie pozitive
            („great", „clean", „perfect", „good", „nice") și clasifică fiecare comentariu
            într-o categorie de satisfacție (Foarte Pozitiv / Pozitiv / Neutru).
        </p>
        <div>
            <span class="method-tag">ARRAY _TEMPORARY_</span>
            <span class="method-tag">DO i = 1 TO 5</span>
            <span class="method-tag">FIND() + LOWCASE()</span>
            <span class="method-tag">IF-THEN-ELSE</span>
        </div>
        <div class="interpretation-box">
            <p>
                Algoritmul transformă feedback-ul calitativ al turiștilor în indicatori de
                performanță (KPI) măsurabili, eliminând necesitatea citirii manuale a miilor
                de comentarii. Managementul poate interveni rapid pentru soluționarea problemelor.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("**Exercițiul 5** — Crearea de subseturi pentru analiza calitativă", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Izolarea feedback-ului pentru o proprietate specifică</h4>
        <p>
            Un proprietar care deține mai multe locații (de ex. ID-ul 241032) poate primi un
            raport curat cu experiențele clienților săi. Prin IF listing_id = 241032 și KEEP,
            s-au păstrat doar coloanele necesare pentru citire, optimizând memoria SAS.
        </p>
        <div>
            <span class="method-tag">IF listing_id = ...</span>
            <span class="method-tag">KEEP</span>
            <span class="method-tag">PROC PRINT</span>
        </div>
        <div class="interpretation-box">
            <p>
                Segmentarea feedback-ului permite identificarea rapidă a punctelor forte și a
                problemelor specifice unei locații, facilitând decizii de îmbunătățire a serviciilor
                care conduc la creșterea satisfacției clienților și a veniturilor.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("**Exercițiul 6** — Utilizarea funcțiilor SAS", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Curățarea datelor și calculul vechimii recenziilor</h4>
        <p>
            Datele calendaristice stocate ca text au fost convertite în format numeric, s-a calculat
            automat vechimea fiecărei recenzii, iar numele clienților au fost standardizate cu UPCASE.
            Filtrarea cu IF data_reala ^= . elimină înregistrările incomplete.
        </p>
        <div>
            <span class="method-tag">INPUT(date, YYMMDD10.)</span>
            <span class="method-tag">YEAR()</span>
            <span class="method-tag">YRDIF()</span>
            <span class="method-tag">UPCASE()</span>
            <span class="method-tag">LENGTH()</span>
        </div>
        <div class="interpretation-box">
            <p>
                Calcularea vechimii recenziilor este critică pentru validarea actualității feedback-ului.
                Metrica lungimii comentariului servește ca indicator al „engagement-ului" clienților,
                ajutând la identificarea turiștilor cei mai implicați.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("**Exercițiul 8** — Utilizarea de masive (Arrays) pentru detecția problemelor", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Sistem automat de scanare pentru termeni critici</h4>
        <p>
            Echipa de Customer Support gestionează un volum masiv de recenzii. S-a creat un sistem
            automatizat de scanare care identifică termeni critici de nemulțumire:
            „noisy", „small", „dirty", „broken". Cazurile identificate sunt extrase într-un raport de alertă.
        </p>
        <div>
            <span class="method-tag">ARRAY termeni_critici</span>
            <span class="method-tag">DO i = 1 TO 6</span>
            <span class="method-tag">FIND() + LOWCASE()</span>
            <span class="method-tag">nr_probleme_gasite</span>
        </div>
        <div class="interpretation-box">
            <p>
                Sistemul de tip Early Warning transformă monitorizarea pasivă a feedback-ului
                într-o strategie proactivă de gestionare a reputației. Identificarea automată
                a nemulțumirilor (zgomot, spațiu limitat) permite remedierea deficiențelor
                înainte ca acestea să afecteze rating-ul și rata de rezervare.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="accent-divider"></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════
# BLOC 3: Combinare, rapoarte, grafice
# ════════════════════════════════════════════════
st.markdown('<div class="section-title">📊 Combinare, rapoarte statistice și vizualizări</div>', unsafe_allow_html=True)

with st.expander("**Exercițiul 7** — Combinarea seturilor de date (MERGE + SQL)", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Unirea datelor tarifare cu informațiile descriptive ale proprietăților</h4>
        <p>
            Setul calendar_disponibil (informații tarifare) a fost unit cu listings.csv (detalii
            descriptive), demonstrând două metode: interclasarea tradițională SAS (<b>MERGE</b>
            cu PROC SORT și RENAME=) și joncțiunea prin <b>PROC SQL</b> cu INNER JOIN.
        </p>
        <div>
            <span class="method-tag">PROC SORT</span>
            <span class="method-tag">MERGE + BY</span>
            <span class="method-tag">RENAME=</span>
            <span class="method-tag">IN=</span>
            <span class="method-tag">PROC SQL + INNER JOIN</span>
        </div>
        <div class="interpretation-box">
            <p>
                Datele financiare au fost reunite cu atributele descriptive. De exemplu, se poate
                vizualiza direct cum o proprietate „Cottage in the Heart of Ballard" își ajustează
                prețurile de la 69$ la 89$ în funcție de zi, în timp ce un „Stylish Queen Anne
                Apartment" are un preț constant de 85$.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("**Exercițiul 9** — Top 10 cele mai populare locații", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Clasificarea proprietăților după numărul de recenzii (Ranking)</h4>
        <p>
            Numărul de recenzii este cel mai bun indicator al popularității și al gradului de
            ocupare. S-a generat un raport cu primele 10 proprietăți din Seattle cu cel mai mare
            număr de recenzii.
        </p>
        <div>
            <span class="method-tag">PROC SORT DESCENDING</span>
            <span class="method-tag">PROC PRINT (OBS=10)</span>
            <span class="method-tag">LABEL</span>
        </div>
        <div class="interpretation-box">
            <p>
                Raportul de tip „Ranking" identifică liderii de performanță. Identificarea
                proprietăților de succes permite managementului să analizeze factorii de succes
                (preț, locație, facilități) și să folosească aceste unități ca modele de bune
                practici pentru restul portofoliului.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("**Exercițiul 10** — Analiza statistică pe segmente de buget", expanded=True):
    st.markdown("""
    <div class="exercise-card">
        <h4>Segmentarea pieței: Budget · Standard · Premium</h4>
        <p>
            Piața a fost segmentată prin IF-THEN-ELSE: <b>Budget</b> (sub 100$),
            <b>Standard</b> (100–250$), <b>Premium</b> (peste 250$). S-au aplicat
            PROC FREQ (cota de piață procentuală) și PROC MEANS (media de rating și volumul
            de recenzii pe fiecare segment).
        </p>
        <div>
            <span class="method-tag">IF-THEN-ELSE</span>
            <span class="method-tag">PROC FREQ</span>
            <span class="method-tag">PROC MEANS</span>
        </div>
        <div class="interpretation-box">
            <p>
                Dacă segmentul „Premium" are un rating semnificativ mai mare, strategia de preț este
                justificată de calitatea serviciilor. Dacă „Budget" are cele mai multe recenzii,
                acesta este motorul de rulaj al platformei — turiștii din Seattle prioritizează
                economia de cost, informație vitală pentru maximizarea gradului de ocupare.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ──── Grafic segmente ────
    col1, col2 = st.columns(2)

    segments_data = pd.DataFrame({
        "Segment": ["Budget\n(< $100)", "Standard\n($100–$250)", "Premium\n(> $250)"],
        "Procent": [44.5, 42.1, 13.4],
    })

    with col1:
        fig_pie = go.Figure(go.Pie(
            labels=["Budget (< $100)", "Standard ($100–$250)", "Premium (> $250)"],
            values=[44.5, 42.1, 13.4],
            hole=0.55,
            marker=dict(
                colors=["#FF5A5F", "#FF8A8E", "#FFB3B5"],
                line=dict(color="#0E1117", width=3)
            ),
            textfont=dict(size=13, color="#fff", family="Inter"),
            textinfo="label+percent",
            textposition="outside",
            pull=[0.03, 0, 0],
        ))
        fig_pie.update_layout(
            title=dict(text="Cota de piață pe segmente", font=dict(size=14, color="#C8CDD8")),
            margin=dict(t=50, l=20, r=20, b=20),
            height=340,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            font=dict(family="Inter", color="#C8CDD8"),
            annotations=[dict(text="Piața<br>Seattle", x=0.5, y=0.5, font_size=14,
                              font_color="#8892A4", showarrow=False)],
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        fig_bar_seg = go.Figure()
        fig_bar_seg.add_trace(go.Bar(
            x=["Budget", "Standard", "Premium"],
            y=[44.5, 42.1, 13.4],
            marker_color=["#FF5A5F", "#FF8A8E", "#FFB3B5"],
            text=["44.5%", "42.1%", "13.4%"],
            textposition="outside",
            textfont=dict(size=13, color="#C8CDD8"),
        ))
        fig_bar_seg.update_layout(
            title=dict(text="Volum proprietăți per segment", font=dict(size=14, color="#C8CDD8")),
            yaxis=dict(title="Procent (%)", showgrid=True, gridcolor="rgba(255,255,255,0.05)",
                       color="#8892A4"),
            xaxis=dict(color="#C8CDD8"),
            margin=dict(t=50, l=50, r=20, b=40),
            height=340,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter"),
        )
        st.plotly_chart(fig_bar_seg, use_container_width=True)


with st.expander("**Exercițiul 11** — Generarea de grafice (Pie Chart și Bar Chart)", expanded=False):
    st.markdown("""
    <div class="exercise-card">
        <h4>Vizualizarea segmentelor de piață prin grafice structurale</h4>
        <p>
            Datele statistice brute au fost transformate în reprezentări vizuale de impact, 
            utilizând două perspective complementare: cota de piață procentuală (PROC GCHART — 
            Pie Chart) și volumul absolut al proprietăților (PROC SGPLOT — Bar Chart).
        </p>
        <div>
            <span class="method-tag">PROC GCHART</span>
            <span class="method-tag">PIE + DISCRETE</span>
            <span class="method-tag">VALUE=INSIDE</span>
            <span class="method-tag">PROC SGPLOT</span>
            <span class="method-tag">VBAR + DATALABEL</span>
        </div>
        <div class="interpretation-box">
            <p>
                Segmentul „Standard" domină oferta și asigură stabilitatea veniturilor platformei.
                Segmentul „Premium" este sub-reprezentat — noi investiții ar putea genera marje
                de profit superioare. Graficele transformă cifrele într-un ghid strategic pentru
                optimizarea portofoliului.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ──────────────────── FOOTER ────────────────────
st.markdown("""
<div style="text-align:center; margin-top: 2rem; padding: 1rem;
     border-top: 1px solid rgba(255,255,255,0.06); color: #5A6377; font-size: 0.75rem;">
    Partea I din proiect · 11 exerciții SAS · Curățare, formatare, analiză text și vizualizări
</div>
""", unsafe_allow_html=True)
