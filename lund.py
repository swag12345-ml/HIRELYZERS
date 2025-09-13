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
.hero{display:flex;gap:24px;align-items:center;padding:48px 24px;border-radius:18px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));box-shadow:var(--card-shadow);}
.hero-left{flex:1;}
.hero-right{width:420px;min-width:320px;cursor:pointer;}
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
.typewriter{display:inline-block;overflow:hidden;white-space:nowrap;}
.typewriter-text{border-right:2px solid rgba(255,255,255,0.6);padding-right:6px}

/* small hover affordance */
#ats-card:hover { transform: translateY(-3px); transition: transform 180ms ease; }
""")
local_css(css)

# ---------------------- Top Nav ----------------------
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
    <a href="https://hirelyzer-ijkfwqydjqz3wqyvjkhegw.streamlit.app/" target="_blank">
      <button class='btn'>Open App</button>
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- Hero Section with ATS Animation ----------------------
hero_html = """
<div class='hero'>
  <div class='hero-left'>
    <div class='h-eyebrow'>AI-Powered Career Tools · Instant · Insightful</div>
    <div class='h-title'>Make Resumes that Pass — and People who Hire.</div>
    <div class='h-sub'><span class='typewriter'><span id='typewriter' class='typewriter-text'></span></span></div>
    <div class='cta-row'>
      <a href="https://hirelyzer-ijkfwqydjqz3wqyvjkhegw.streamlit.app/" target="_blank">
        <button class='btn'>✨ Launch App</button>
      </a>
      <button class='btn secondary' onclick="window.location='#pricing'">View Plans</button>
    </div>
  </div>

  <!-- ATS card now has id="ats-card" and no inline onclick -->
  <div class='hero-right' id='ats-card'>
    <div style='border-radius:14px;padding:18px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(0,0,0,0.2));box-shadow:0 20px 60px rgba(0,0,0,0.6);border:1px solid rgba(255,255,255,0.03)'>
      <div style='display:flex;justify-content:space-between;align-items:center'>
        <div style='font-weight:800'>Live ATS Preview</div>
        <div style='font-size:12px;color:rgba(255,255,255,0.6)'>Click to Scan</div>
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

        <div style='font-size:12px;color:rgba(255,255,255,0.6);margin-bottom:6px'>ATS Score</div>
        <div id='progress-container' style='width:100%;height:14px;background:rgba(255,255,255,0.08);border-radius:8px;overflow:hidden;position:relative'>
          <div id='ats-bar' style='height:100%;width:0%;background:linear-gradient(90deg,#ff6a88,#5f2c82);border-radius:8px;'></div>
        </div>
        <div style='text-align:right;font-weight:800;font-size:18px;margin-top:6px' id='ats-score'>0%</div>
      </div>
    </div>
  </div>
</div>

<script>
// Typewriter (unchanged)
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

// Robust ATS animation function
function animateScore(target=78, duration=1400){
  const bar = document.getElementById('ats-bar');
  const scoreText = document.getElementById('ats-score');
  const container = document.getElementById('progress-container');

  if(!bar || !scoreText || !container) return;

  // Reset
  bar.style.transition = 'none';
  bar.style.width = '0%';
  scoreText.innerText = '0%';

  // force reflow so the browser applies the width=0 before we animate to target
  void bar.offsetWidth;

  // Apply transition and set to target width
  bar.style.transition = 'width ' + duration + 'ms cubic-bezier(.2,.9,.3,1)';
  // small timeout to ensure transition takes effect
  setTimeout(()=> { bar.style.width = target + '%'; }, 20);

  // Use requestAnimationFrame to smoothly update the number label across the same duration
  const startTime = performance.now();
  function update(now){
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const current = Math.round(progress * target);
    scoreText.innerText = current + '%';
    if(progress < 1){
      requestAnimationFrame(update);
    } else {
      // ensure final value exact
      scoreText.innerText = target + '%';
    }
  }
  requestAnimationFrame(update);
}

// Attach click listener to the card so it animates every click
const card = document.getElementById('ats-card');
if(card){
  card.addEventListener('click', function(){
    // can pass different targets/durations dynamically if desired
    animateScore(78, 1400);
  });
}

// Optionally: animate once on load (comment out if you don't want auto-run)
// animateScore(78, 1400);
</script>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ---------------------- Features Section ----------------------
features_html = """
<div id='features' style='padding:60px 20px'>
  <h2 style='font-size:36px;font-weight:800;margin-bottom:24px;text-align:center'>Features</h2>
  <div style='display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px'>
    <div class='feature-card'>
      <div style='font-size:22px'>📄 Resume Analyzer</div>
      <div class='feature-title'>ATS Optimization</div>
      <div class='feature-desc'>Upload your resume and instantly see your ATS score with AI-powered feedback for keywords, grammar, and bias detection.</div>
    </div>
    <div class='feature-card'>
      <div style='font-size:22px'>📝 Smart Builder</div>
      <div class='feature-title'>Resume + Cover Letter</div>
      <div class='feature-desc'>Use modern templates, generate tailored cover letters with AI, and export in PDF or DOCX formats.</div>
    </div>
    <div class='feature-card'>
      <div style='font-size:22px'>🔍 Job Gateway</div>
      <div class='feature-title'>Market Insights</div>
      <div class='feature-desc'>Explore job opportunities, salary benchmarks, and course recommendations aligned with your career goals.</div>
    </div>
  </div>
</div>
"""
st.markdown(features_html, unsafe_allow_html=True)

# ---------------------- Pricing Section ----------------------
pricing_html = """
<div id='pricing' style='padding:60px 20px;background:rgba(255,255,255,0.02);border-radius:14px;margin-top:40px'>
  <h2 style='font-size:36px;font-weight:800;margin-bottom:24px;text-align:center'>Pricing</h2>
  <div style='display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;max-width:900px;margin:0 auto'>
    <div class='feature-card' style='text-align:center'>
      <div style='font-size:22px;font-weight:700'>Free</div>
      <div style='font-size:14px;color:rgba(255,255,255,0.7);margin:10px 0'>Basic ATS scoring & resume analysis</div>
      <div style='font-size:26px;font-weight:800;margin:10px 0'>$0</div>
      <button class='btn secondary'>Get Started</button>
    </div>
    <div class='feature-card' style='text-align:center;border:2px solid rgba(255,255,255,0.15)'>
      <div style='font-size:22px;font-weight:700'>Pro</div>
      <div style='font-size:14px;color:rgba(255,255,255,0.7);margin:10px 0'>Full resume builder, AI rewrites, job insights</div>
      <div style='font-size:26px;font-weight:800;margin:10px 0'>$9 / mo</div>
      <button class='btn'>Choose Pro</button>
    </div>
    <div class='feature-card' style='text-align:center'>
      <div style='font-size:22px;font-weight:700'>Enterprise</div>
      <div style='font-size:14px;color:rgba(255,255,255,0.7);margin:10px 0'>For recruiters & teams with bulk hiring tools</div>
      <div style='font-size:26px;font-weight:800;margin:10px 0'>Custom</div>
      <button class='btn secondary'>Contact Sales</button>
    </div>
  </div>
</div>
"""
st.markdown(pricing_html, unsafe_allow_html=True)

# ---------------------- Contact Section ----------------------
contact_html = """
<div id='contact' style='padding:60px 20px;margin-top:40px'>
  <h2 style='font-size:36px;font-weight:800;margin-bottom:24px;text-align:center'>Contact Us</h2>
  <div style='max-width:600px;margin:0 auto;text-align:center;color:rgba(255,255,255,0.7)'>
    <p>Have questions or need support? We'd love to hear from you.</p>
    <p>📧 Email: <a href='mailto:support@kecxubot.com' style='color:#8ab4f8'>support@kecxubot.com</a></p>
    <p>🌐 Website: <a href='https://kecxubot.com' target='_blank' style='color:#8ab4f8'>www.kecxubot.com</a></p>
  </div>
</div>
<div class='footer'>© 2025 KecxuBot. All rights reserved.</div>
"""
st.markdown(contact_html, unsafe_allow_html=True)
