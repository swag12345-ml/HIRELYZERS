import streamlit as st
import base64
from textwrap import dedent

st.set_page_config(page_title="KecxuBot — Cinematic Landing", page_icon="🚀", layout="wide")

# ---------------------- Helpful utilities ----------------------
def local_css(css: str):
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def img_to_base64(path: str) -> str:
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ---------------------- Cinematic CSS ----------------------
css = dedent("""
:root{
  --bg1: #050816;
  --bg2: #0e0b1a;
  --accent: linear-gradient(90deg,#ff6a88 0%,#5f2c82 50%,#2b5876 100%);
  --glass: rgba(255,255,255,0.04);
  --glass-strong: rgba(255,255,255,0.06);
  --card-shadow: 0 10px 30px rgba(2,6,23,0.6);
}
html, body, [class*="css"]{
  background: radial-gradient(1200px 600px at 10% 10%, rgba(79, 70, 229, 0.12), transparent),
              radial-gradient(1000px 600px at 90% 90%, rgba(59,130,246,0.06), transparent),
              linear-gradient(180deg,var(--bg1),var(--bg2));
  color: rgba(255,255,255,0.95);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
}
/* Hero + features + footer … */
.hero{display:flex;gap:24px;align-items:center;padding:48px 24px;border-radius:18px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));box-shadow:var(--card-shadow);}
.hero-left{flex:1;}
.hero-right{width:420px;min-width:320px}
.h-eyebrow{letter-spacing:2px;color:rgba(255,255,255,0.55);font-weight:600}
.h-title{font-size:48px;font-weight:800;line-height:1.02;margin:8px 0;}
.h-sub{color:rgba(255,255,255,0.7);font-size:18px;margin-bottom:18px}
.cta-row{display:flex;gap:12px}
.btn{background:var(--accent);padding:12px 20px;border-radius:12px;font-weight:700;border:none;cursor:pointer;box-shadow:0 8px 18px rgba(79,70,229,0.18);color:white;}
.btn.secondary{background:transparent;border:1px solid rgba(255,255,255,0.06);color:white;}
.features{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:24px}
.feature-card{padding:18px;border-radius:12px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border:1px solid rgba(255,255,255,0.03);}
.feature-title{font-weight:700;margin-top:8px}
.feature-desc{color:rgba(255,255,255,0.68);font-size:14px;margin-top:6px}
.footer{padding:28px 12px;margin-top:28px;color:rgba(255,255,255,0.6)}
@media (max-width: 900px){
  .hero{flex-direction:column}
  .features{grid-template-columns:repeat(1,1fr)}
  .h-title{font-size:32px}
}
/* Typewriter */
.typewriter{display:inline-block;overflow:hidden;white-space:nowrap;}
.typewriter-text{border-right:2px solid rgba(255,255,255,0.6);padding-right:6px}
""")
local_css(css)

# ---------------------- Page content ----------------------
st.markdown("""
<div style='display:flex;justify-content:space-between;align-items:center;padding:10px 6px;margin-bottom:8px;'>
  <div style='display:flex;align-items:center;gap:12px'>
    <div style='width:44px;height:44px;border-radius:10px;background:linear-gradient(135deg,#ff6a88,#5f2c82);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:18px'>KB</div>
    <div style='font-weight:700'>KecxuBot</div>
  </div>
  <div style='display:flex;gap:10px;align-items:center'>
    <a href='#features' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600'>Features</a>
    <a href='#pricing' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600'>Pricing</a>
    <a href='#contact' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600'>Contact</a>
    <!-- ✅ fixed button redirect -->
    <a href="https://hirelyzer-ijkfwqydjqz3wqyvjkhegw.streamlit.app/" target="_blank">
      <button class='btn'>Open App</button>
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- Hero Section ----------------------
hero_html = """
<div class='hero'>
  <div class='hero-left'>
    <div class='h-eyebrow'>AI-Powered Career Tools · Instant · Insightful</div>
    <div class='h-title'>Make Resumes that Pass — and People who Hire.</div>
    <div class='h-sub'><span class='typewriter'><span id='typewriter' class='typewriter-text'></span></span></div>
    <div class='cta-row'>
      <!-- ✅ fixed button redirect -->
      <a href="https://hirelyzer-ijkfwqydjqz3wqyvjkhegw.streamlit.app/" target="_blank">
        <button class='btn'>✨ Launch App</button>
      </a>
      <button class='btn secondary' onclick="window.location='#pricing'">View Plans</button>
    </div>
    <div class='features' style='margin-top:22px' id='features'>
      <div class='feature-card'>
        <div style='font-size:20px'>📄 Resume Analyzer</div>
        <div class='feature-title'>ATS-ready scoring & AI rewrite</div>
        <div class='feature-desc'>Upload resumes, get ATS score, grammar, bias detection & AI suggestions.</div>
      </div>
      <div class='feature-card'>
        <div style='font-size:20px'>📝 Builder & Cover Letter</div>
        <div class='feature-title'>Templates, AI preview & export</div>
        <div class='feature-desc'>Create resumes with templates, auto-generate cover letters, and export.</div>
      </div>
      <div class='feature-card'>
        <div style='font-size:20px'>🔍 Job Gateway</div>
        <div class='feature-title'>Search & market insights</div>
        <div class='feature-desc'>Direct search links plus premium market & salary insights.</div>
      </div>
    </div>
  </div>
  <div class='hero-right'>
    <div style='border-radius:14px;padding:18px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(0,0,0,0.2));box-shadow:0 20px 60px rgba(0,0,0,0.6);border:1px solid rgba(255,255,255,0.03)'>
      <div style='display:flex;justify-content:space-between;align-items:center'>
        <div style='font-weight:800'>Live ATS Preview</div>
        <div style='font-size:12px;color:rgba(255,255,255,0.6)'>Preview</div>
      </div>
      <div style='height:16px'></div>
      <div style='background:rgba(255,255,255,0.02);padding:12px;border-radius:10px'>
        <div style='font-size:12px;color:rgba(255,255,255,0.6)'>Resume: <b>John Doe — Backend Engineer</b></div>
        <div style='height:10px'></div>
        <div style='display:flex;gap:8px;flex-wrap:wrap'>
          <div style='padding:8px 10px;border-radius:999px;background:rgba(0,0,0,0.3);font-size:12px'>Python</div>
          <div style='padding:8px 10px;border-radius:999px;background:rgba(0,0,0,0.3);font-size:12px'>Django</div>
          <div style='padding:8px 10px;border-radius:999px;background:rgba(0,0,0,0.3);font-size:12px'>Postgres</div>
        </div>
        <div style='height:14px'></div>
        <div style='display:flex;justify-content:space-between;align-items:center'>
          <div style='font-size:12px;color:rgba(255,255,255,0.6)'>ATS Score</div>
          <div style='font-weight:800;font-size:18px'>78%</div>
        </div>
      </div>
    </div>
  </div>
</div>
<script>
const phrases = [
  'Upload your resume — get ATS-ready feedback in seconds.',
  'Rewrite bullets for impact. Fix grammar & bias automatically.',
  'Discover jobs, recommended courses, and salary insights.'
];
let idx=0;const el=document.getElementById('typewriter');
function show(){
  const txt = phrases[idx];
  let i=0;el.innerText='';
  const t = setInterval(()=>{
    el.innerText += txt[i++];
    if(i>txt.length-1){
      clearInterval(t);
      setTimeout(()=>{ idx=(idx+1)%phrases.length; show(); },2500);
    }
  },24);
}
if(el) show();
</script>
"""
st.markdown(hero_html, unsafe_allow_html=True)
