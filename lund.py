#!/usr/bin/env python3
"""
HIRELYZER Landing Page Generator
Creates a beautiful, cinematic landing page with advanced CSS animations
"""

import os
from textwrap import dedent

def create_css():
    """Generate advanced cinematic CSS for HIRELYZER"""
    return dedent("""
    :root{
      --bg1: #050816;
      --bg2: #0e0b1a;
      --accent: linear-gradient(135deg,#ff6a88 0%,#ff8a50 25%,#5f2c82 50%,#2b5876 75%,#1e3c72 100%);
      --accent-hover: linear-gradient(135deg,#ff7a98 0%,#ff9a60 25%,#6f3c92 50%,#3b6886 75%,#2e4c82 100%);
      --glass: rgba(255,255,255,0.06);
      --glass-strong: rgba(255,255,255,0.08);
      --card-shadow: 0 20px 60px rgba(2,6,23,0.8), 0 8px 32px rgba(79,70,229,0.15);
      --glow: 0 0 40px rgba(79,70,229,0.3);
      --text-glow: 0 0 20px rgba(255,255,255,0.1);
    }

    @keyframes float {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      33% { transform: translateY(-10px) rotate(1deg); }
      66% { transform: translateY(5px) rotate(-1deg); }
    }

    @keyframes pulse-glow {
      0%, 100% { box-shadow: var(--card-shadow), var(--glow); }
      50% { box-shadow: var(--card-shadow), 0 0 60px rgba(79,70,229,0.4); }
    }

    @keyframes gradient-shift {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    @keyframes slide-up {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes scale-in {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
    }

    @keyframes shimmer {
      0% { left: -100%; }
      100% { left: 100%; }
    }

    @keyframes blink {
      0%, 50% { border-color: rgba(255,255,255,0.7); }
      51%, 100% { border-color: transparent; }
    }

    html, body {
      margin: 0;
      padding: 0;
      background: 
        radial-gradient(1400px 800px at 15% 15%, rgba(79, 70, 229, 0.15), transparent),
        radial-gradient(1200px 700px at 85% 85%, rgba(59,130,246,0.08), transparent),
        radial-gradient(800px 600px at 50% 0%, rgba(139, 92, 246, 0.05), transparent),
        linear-gradient(180deg,var(--bg1),var(--bg2));
      color: rgba(255,255,255,0.95);
      font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      overflow-x: hidden;
      min-height: 100vh;
    }

    .scroll-indicator {
      position: fixed;
      top: 0;
      left: 0;
      width: 0%;
      height: 3px;
      background: var(--accent);
      z-index: 1000;
      transition: width 0.1s ease;
    }

    .parallax-bg {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: -1;
    }

    .floating-element {
      position: absolute;
      opacity: 0.1;
      animation: float 10s ease-in-out infinite;
      font-size: 24px;
    }

    .floating-element:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
    .floating-element:nth-child(2) { top: 20%; right: 10%; animation-delay: 2s; }
    .floating-element:nth-child(3) { bottom: 30%; left: 20%; animation-delay: 4s; }
    .floating-element:nth-child(4) { bottom: 10%; right: 20%; animation-delay: 6s; }

    .nav-container {
      backdrop-filter: blur(20px);
      background: rgba(5,8,22,0.8);
      border-bottom: 1px solid rgba(255,255,255,0.05);
      position: sticky;
      top: 0;
      z-index: 100;
      animation: slide-up 0.6s ease-out;
    }

    .nav-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 24px;
      max-width: 1200px;
      margin: 0 auto;
    }

    .logo-container {
      display: flex;
      align-items: center;
      gap: 16px;
      transition: all 0.3s ease;
    }

    .logo-container:hover {
      transform: scale(1.05);
    }

    .logo {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: linear-gradient(135deg,#ff6a88,#5f2c82);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 20px;
      box-shadow: 0 8px 20px rgba(79,70,229,0.3);
      color: white;
    }

    .logo-text {
      font-weight: 800;
      font-size: 18px;
    }

    .nav-links {
      display: flex;
      gap: 32px;
      align-items: center;
    }

    .nav-link {
      text-decoration: none;
      color: rgba(255,255,255,0.75);
      font-weight: 600;
      font-size: 15px;
      transition: all 0.3s ease;
      position: relative;
    }

    .nav-link:hover {
      color: rgba(255,255,255,0.95);
      transform: translateY(-1px);
    }

    .nav-link::after {
      content: '';
      position: absolute;
      bottom: -4px;
      left: 0;
      width: 0;
      height: 2px;
      background: var(--accent);
      transition: width 0.3s ease;
    }

    .nav-link:hover::after {
      width: 100%;
    }

    .hero-container {
      max-width: 1200px;
      margin: 40px auto;
      padding: 0 20px;
    }

    .hero {
      display: flex;
      gap: 32px;
      align-items: center;
      padding: 60px 32px;
      border-radius: 24px;
      background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
      backdrop-filter: blur(20px);
      border: 1px solid rgba(255,255,255,0.05);
      box-shadow: var(--card-shadow);
      animation: slide-up 0.8s ease-out, pulse-glow 4s ease-in-out infinite;
      position: relative;
      overflow: hidden;
    }

    .hero::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.03), transparent);
      animation: shimmer 3s ease-in-out infinite;
    }

    .hero-left {
      flex: 1;
      z-index: 2;
    }

    .hero-right {
      width: 450px;
      min-width: 350px;
      z-index: 2;
      animation: float 6s ease-in-out infinite;
    }

    .h-eyebrow {
      letter-spacing: 3px;
      color: rgba(255,255,255,0.6);
      font-weight: 700;
      font-size: 13px;
      text-transform: uppercase;
      text-shadow: var(--text-glow);
      animation: slide-up 0.8s ease-out 0.2s both;
    }

    .h-title {
      font-size: 56px;
      font-weight: 900;
      line-height: 1.05;
      margin: 12px 0;
      background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 50%, #cbd5e1 100%);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 0 30px rgba(255,255,255,0.1);
      animation: slide-up 0.8s ease-out 0.4s both;
    }

    .h-sub {
      color: rgba(255,255,255,0.75);
      font-size: 20px;
      margin-bottom: 24px;
      line-height: 1.6;
      animation: slide-up 0.8s ease-out 0.6s both;
    }

    .typewriter-text {
      border-right: 3px solid rgba(255,255,255,0.7);
      padding-right: 8px;
      animation: blink 1s infinite;
    }

    .cta-row {
      display: flex;
      gap: 16px;
      animation: slide-up 0.8s ease-out 0.8s both;
    }

    .btn {
      background: var(--accent);
      background-size: 200% 200%;
      padding: 16px 28px;
      border-radius: 16px;
      font-weight: 800;
      border: none;
      cursor: pointer;
      box-shadow: 0 12px 24px rgba(79,70,229,0.25), 0 4px 12px rgba(0,0,0,0.1);
      color: white;
      font-size: 16px;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      overflow: hidden;
      text-decoration: none;
      display: inline-block;
      animation: gradient-shift 3s ease infinite;
    }

    .btn:hover {
      background: var(--accent-hover);
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 16px 32px rgba(79,70,229,0.35), 0 8px 16px rgba(0,0,0,0.2);
    }

    .btn:active {
      transform: translateY(0) scale(0.98);
    }

    .btn.secondary {
      background: transparent;
      border: 2px solid rgba(255,255,255,0.1);
      color: white;
      backdrop-filter: blur(10px);
    }

    .btn.secondary:hover {
      background: rgba(255,255,255,0.05);
      border-color: rgba(255,255,255,0.2);
      transform: translateY(-2px) scale(1.02);
    }

    .ats-preview {
      border-radius: 18px;
      padding: 24px;
      background: linear-gradient(135deg, rgba(255,255,255,0.04), rgba(0,0,0,0.3));
      backdrop-filter: blur(20px);
      box-shadow: 0 25px 80px rgba(0,0,0,0.7), 0 0 40px rgba(79,70,229,0.1);
      border: 1px solid rgba(255,255,255,0.06);
      transition: all 0.4s ease;
      animation: float 8s ease-in-out infinite;
    }

    .ats-preview:hover {
      transform: translateY(-5px) scale(1.02);
      box-shadow: 0 30px 100px rgba(0,0,0,0.8), 0 0 60px rgba(79,70,229,0.2);
    }

    .ats-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }

    .ats-title {
      font-weight: 800;
      font-size: 16px;
      color: rgba(255,255,255,0.95);
    }

    .live-indicator {
      font-size: 12px;
      color: rgba(255,255,255,0.6);
      background: rgba(0,255,0,0.1);
      padding: 4px 8px;
      border-radius: 12px;
      border: 1px solid rgba(0,255,0,0.2);
    }

    .ats-content {
      background: rgba(255,255,255,0.03);
      padding: 20px;
      border-radius: 14px;
      border: 1px solid rgba(255,255,255,0.05);
    }

    .resume-info {
      font-size: 13px;
      color: rgba(255,255,255,0.7);
      margin-bottom: 12px;
    }

    .resume-name {
      color: rgba(255,255,255,0.95);
      font-weight: bold;
    }

    .skills-container {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 16px;
    }

    .skill-tag {
      padding: 8px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      transition: all 0.3s ease;
    }

    .skill-tag:hover {
      transform: scale(1.05);
    }

    .skill-python {
      background: rgba(79,70,229,0.2);
      border: 1px solid rgba(79,70,229,0.3);
    }

    .skill-python:hover {
      background: rgba(79,70,229,0.3);
    }

    .skill-django {
      background: rgba(34,197,94,0.2);
      border: 1px solid rgba(34,197,94,0.3);
    }

    .skill-django:hover {
      background: rgba(34,197,94,0.3);
    }

    .skill-postgres {
      background: rgba(59,130,246,0.2);
      border: 1px solid rgba(59,130,246,0.3);
    }

    .skill-postgres:hover {
      background: rgba(59,130,246,0.3);
    }

    .score-section {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 0;
      border-top: 1px solid rgba(255,255,255,0.05);
    }

    .score-label {
      font-size: 13px;
      color: rgba(255,255,255,0.7);
    }

    .score-value {
      font-weight: 900;
      font-size: 24px;
      background: linear-gradient(135deg,#10b981,#3b82f6);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .progress-bar {
      width: 100%;
      height: 6px;
      background: rgba(255,255,255,0.1);
      border-radius: 3px;
      margin-top: 8px;
      overflow: hidden;
    }

    .progress-fill {
      width: 78%;
      height: 100%;
      background: linear-gradient(90deg,#10b981,#3b82f6);
      border-radius: 3px;
      animation: pulse 2s ease-in-out infinite;
    }

    .section {
      padding: 80px 20px;
      max-width: 1200px;
      margin: 0 auto;
    }

    .section-title {
      font-size: 48px;
      font-weight: 900;
      margin-bottom: 16px;
      text-align: center;
      background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: slide-up 0.8s ease-out;
    }

    .section-subtitle {
      text-align: center;
      color: rgba(255,255,255,0.7);
      font-size: 18px;
      margin-bottom: 48px;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
    }

    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 28px;
    }

    .feature-card {
      padding: 28px;
      border-radius: 20px;
      background: linear-gradient(135deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
      backdrop-filter: blur(20px);
      border: 1px solid rgba(255,255,255,0.06);
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      overflow: hidden;
      animation: scale-in 0.6s ease-out;
    }

    .feature-card:hover {
      transform: translateY(-8px) scale(1.02);
      box-shadow: 0 20px 60px rgba(0,0,0,0.4), 0 0 40px rgba(79,70,229,0.2);
      border-color: rgba(255,255,255,0.12);
    }

    .feature-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2px;
      background: var(--accent);
      transform: scaleX(0);
      transition: transform 0.4s ease;
    }

    .feature-card:hover::before {
      transform: scaleX(1);
    }

    .feature-icon {
      font-size: 32px;
      margin-bottom: 8px;
    }

    .feature-title {
      font-weight: 800;
      margin-top: 12px;
      font-size: 18px;
      color: rgba(255,255,255,0.95);
    }

    .feature-desc {
      color: rgba(255,255,255,0.7);
      font-size: 15px;
      margin-top: 8px;
      line-height: 1.6;
    }

    .feature-badge {
      margin-top: 16px;
      padding: 12px;
      border-radius: 8px;
      font-size: 12px;
      color: rgba(255,255,255,0.8);
      font-weight: 600;
    }

    .badge-ai {
      background: rgba(79,70,229,0.1);
      border-left: 3px solid #4f46e5;
    }

    .badge-templates {
      background: rgba(34,197,94,0.1);
      border-left: 3px solid #22c55e;
    }

    .badge-insights {
      background: rgba(59,130,246,0.1);
      border-left: 3px solid #3b82f6;
    }

    .pricing-section {
      padding: 80px 20px;
      background: linear-gradient(135deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));
      backdrop-filter: blur(20px);
      border-radius: 24px;
      margin: 40px 20px;
      border: 1px solid rgba(255,255,255,0.05);
      max-width: 1200px;
      margin-left: auto;
      margin-right: auto;
    }

    .pricing-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
      max-width: 1000px;
      margin: 0 auto;
    }

    .pricing-card {
      text-align: center;
      padding: 32px;
    }

    .pricing-card-featured {
      border: 2px solid rgba(79,70,229,0.3);
      transform: scale(1.05);
      position: relative;
      overflow: hidden;
    }

    .pricing-card-featured::before {
      content: 'MOST POPULAR';
      position: absolute;
      top: -10px;
      right: -30px;
      background: var(--accent);
      color: white;
      padding: 8px 40px;
      font-size: 12px;
      font-weight: 800;
      transform: rotate(45deg);
      letter-spacing: 1px;
    }

    .plan-name {
      font-size: 24px;
      font-weight: 800;
      margin-bottom: 8px;
    }

    .plan-desc {
      font-size: 15px;
      color: rgba(255,255,255,0.7);
      margin-bottom: 20px;
      line-height: 1.5;
    }

    .plan-price {
      font-size: 36px;
      font-weight: 900;
      margin: 20px 0;
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .price-free {
      background: linear-gradient(135deg,#10b981,#3b82f6);
    }

    .price-pro {
      background: linear-gradient(135deg,#ff6a88,#5f2c82);
    }

    .price-enterprise {
      background: linear-gradient(135deg,#f59e0b,#ef4444);
    }

    .plan-period {
      font-size: 14px;
      color: rgba(255,255,255,0.6);
      margin-bottom: 24px;
    }

    .plan-features {
      margin-top: 20px;
      text-align: left;
    }

    .plan-feature {
      font-size: 13px;
      color: rgba(255,255,255,0.7);
      margin: 8px 0;
    }

    .contact-section {
      padding: 80px 20px;
      margin-top: 40px;
      max-width: 1200px;
      margin-left: auto;
      margin-right: auto;
    }

    .contact-content {
      max-width: 700px;
      margin: 0 auto;
      text-align: center;
    }

    .contact-desc {
      color: rgba(255,255,255,0.7);
      font-size: 18px;
      margin-bottom: 40px;
      line-height: 1.6;
    }

    .contact-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 24px;
      margin-bottom: 40px;
    }

    .contact-card {
      text-align: center;
      padding: 24px;
    }

    .contact-icon {
      font-size: 32px;
      margin-bottom: 12px;
    }

    .contact-title {
      font-weight: 700;
      margin-bottom: 8px;
    }

    .contact-link {
      color: #8ab4f8;
      text-decoration: none;
      font-weight: 600;
    }

    .cta-final {
      padding: 32px;
      background: linear-gradient(135deg,rgba(79,70,229,0.1),rgba(59,130,246,0.05));
      border-radius: 16px;
      border: 1px solid rgba(79,70,229,0.2);
    }

    .cta-title {
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 12px;
      color: rgba(255,255,255,0.95);
    }

    .cta-desc {
      color: rgba(255,255,255,0.8);
      margin-bottom: 20px;
    }

    .footer {
      padding: 32px 16px;
      margin-top: 32px;
      color: rgba(255,255,255,0.6);
      text-align: center;
      border-top: 1px solid rgba(255,255,255,0.05);
    }

    .footer-content {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }

    .footer-links {
      display: flex;
      gap: 24px;
    }

    .footer-link {
      color: rgba(255,255,255,0.6);
      text-decoration: none;
      font-size: 14px;
    }

    @media (max-width: 900px) {
      .hero { flex-direction: column; padding: 40px 20px; }
      .hero-right { width: 100%; min-width: auto; }
      .h-title { font-size: 40px; }
      .cta-row { flex-direction: column; align-items: center; }
      .btn { width: 100%; text-align: center; }
      .nav-links { flex-direction: column; gap: 16px; }
    }

    @media (max-width: 600px) {
      .h-title { font-size: 32px; }
      .hero { padding: 30px 16px; }
      .feature-card { padding: 20px; }
      .section { padding: 60px 16px; }
      .section-title { font-size: 36px; }
    }
    """)

def create_javascript():
    """Generate JavaScript for typewriter effect and interactions"""
    return dedent("""
    // Typewriter effect
    const phrases = [
        '🚀 Upload your resume — get ATS-ready feedback in seconds.',
        '✍️ Rewrite bullets for impact. Fix grammar & bias automatically.',
        '🔍 Discover jobs, recommended courses, and salary insights.'
    ];
    
    let currentPhraseIndex = 0;
    const typewriterElement = document.getElementById('typewriter');
    
    function typewriterEffect() {
        const currentPhrase = phrases[currentPhraseIndex];
        let charIndex = 0;
        typewriterElement.textContent = '';
        
        const typeInterval = setInterval(() => {
            typewriterElement.textContent += currentPhrase[charIndex];
            charIndex++;
            
            if (charIndex >= currentPhrase.length) {
                clearInterval(typeInterval);
                setTimeout(() => {
                    currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
                    typewriterEffect();
                }, 3000);
            }
        }, 30);
    }
    
    // Start typewriter effect
    if (typewriterElement) {
        typewriterEffect();
    }
    
    // Scroll progress indicator
    window.addEventListener('scroll', () => {
        const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
        const indicator = document.getElementById('scrollIndicator');
        if (indicator) {
            indicator.style.width = scrolled + '%';
        }
    });
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
    
    // Add hover effects to buttons
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.02)';
        });
        
        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    """)

def generate_html():
    """Generate the complete HTML landing page"""
    css = create_css()
    js = create_javascript()
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HIRELYZER — AI-Powered Resume Analyzer</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>">
    <style>{css}</style>
</head>
<body>
    <!-- Scroll Progress Indicator -->
    <div class="scroll-indicator" id="scrollIndicator"></div>
    
    <!-- Floating Background Elements -->
    <div class="parallax-bg">
        <div class="floating-element">🚀</div>
        <div class="floating-element">⭐</div>
        <div class="floating-element">💼</div>
        <div class="floating-element">📊</div>
    </div>

    <!-- Navigation -->
    <div class="nav-container">
        <div class="nav-content">
            <div class="logo-container">
                <div class="logo">HR</div>
                <div class="logo-text">HIRELYZER</div>
            </div>
            <div class="nav-links">
                <a href="#features" class="nav-link">Features</a>
                <a href="#pricing" class="nav-link">Pricing</a>
                <a href="#contact" class="nav-link">Contact</a>
                <a href="https://hirelyzer-app.streamlit.app/" target="_blank" class="btn">
                    🚀 Open App
                </a>
            </div>
        </div>
    </div>

    <!-- Hero Section -->
    <div class="hero-container">
        <div class="hero">
            <div class="hero-left">
                <div class="h-eyebrow">🤖 AI-Powered Career Tools · ⚡ Instant · 🎯 Insightful</div>
                <div class="h-title">Resumes that Pass ATS — and Impress Recruiters.</div>
                <div class="h-sub">
                    <span class="typewriter-text" id="typewriter"></span>
                </div>
                <div class="cta-row">
                    <a href="https://hirelyzer-app.streamlit.app/" target="_blank" class="btn">
                        ✨ Launch HIRELYZER
                    </a>
                    <a href="#pricing" class="btn secondary">
                        💎 View Plans
                    </a>
                </div>
            </div>
            <div class="hero-right">
                <div class="ats-preview">
                    <div class="ats-header">
                        <div class="ats-title">🎯 Live ATS Preview</div>
                        <div class="live-indicator">● LIVE</div>
                    </div>
                    <div class="ats-content">
                        <div class="resume-info">
                            📄 Resume: <span class="resume-name">Sarah Chen — Data Scientist</span>
                        </div>
                        <div class="skills-container">
                            <div class="skill-tag skill-python">Python</div>
                            <div class="skill-tag skill-django">Machine Learning</div>
                            <div class="skill-tag skill-postgres">TensorFlow</div>
                        </div>
                        <div class="score-section">
                            <div class="score-label">🎯 ATS Score</div>
                            <div class="score-value">85%</div>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Features Section -->
    <div id="features" class="section">
        <h2 class="section-title">🚀 Powerful Features</h2>
        <p class="section-subtitle">Everything you need to create winning resumes and land your dream job</p>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">📄</div>
                <div class="feature-title">AI Resume Analyzer</div>
                <div class="feature-desc">Upload your resume and instantly receive comprehensive ATS scoring with AI-powered feedback for keywords, grammar, formatting, and bias detection to maximize your chances.</div>
                <div class="feature-badge badge-ai">
                    ✨ AI-Powered Analysis
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📝</div>
                <div class="feature-title">Smart Resume Builder</div>
                <div class="feature-desc">Create professional resumes and cover letters using modern, ATS-friendly templates. Generate tailored content with AI assistance and export in multiple formats (PDF, DOCX).</div>
                <div class="feature-badge badge-templates">
                    🎨 Professional Templates
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔍</div>
                <div class="feature-title">Career Intelligence Hub</div>
                <div class="feature-desc">Explore curated job opportunities, access real-time salary benchmarks, and discover personalized course recommendations perfectly aligned with your career goals and aspirations.</div>
                <div class="feature-badge badge-insights">
                    📊 Market Insights
                </div>
            </div>
        </div>
    </div>

    <!-- Pricing Section -->
    <div id="pricing" class="pricing-section">
        <h2 class="section-title">💎 Choose Your Plan</h2>
        <p class="section-subtitle">Start free, upgrade when you're ready to accelerate your career</p>
        <div class="pricing-grid">
            <div class="feature-card pricing-card">
                <div class="plan-name">🆓 Free</div>
                <div class="plan-desc">Perfect for getting started with basic ATS scoring and resume analysis</div>
                <div class="plan-price price-free">$0</div>
                <div class="plan-period">Forever free</div>
                <button class="btn secondary" style="width: 100%;">🚀 Get Started</button>
                <div class="plan-features">
                    <div class="plan-feature">✅ Basic ATS scoring</div>
                    <div class="plan-feature">✅ Grammar check</div>
                    <div class="plan-feature">✅ 3 resume uploads/month</div>
                </div>
            </div>
            <div class="feature-card pricing-card pricing-card-featured">
                <div class="plan-name">⭐ Pro</div>
                <div class="plan-desc">Complete resume builder with AI rewrites, advanced analytics, and job insights</div>
                <div class="plan-price price-pro">$9</div>
                <div class="plan-period">per month</div>
                <button class="btn" style="width: 100%;">🎯 Choose Pro</button>
                <div class="plan-features">
                    <div class="plan-feature">✅ Everything in Free</div>
                    <div class="plan-feature">✅ AI-powered rewrites</div>
                    <div class="plan-feature">✅ Premium templates</div>
                    <div class="plan-feature">✅ Job market insights</div>
                    <div class="plan-feature">✅ Unlimited uploads</div>
                </div>
            </div>
            <div class="feature-card pricing-card">
                <div class="plan-name">🏢 Enterprise</div>
                <div class="plan-desc">Advanced tools for recruiters and teams with bulk hiring and analytics</div>
                <div class="plan-price price-enterprise">Custom</div>
                <div class="plan-period">Contact for pricing</div>
                <button class="btn secondary" style="width: 100%;">📞 Contact Sales</button>
                <div class="plan-features">
                    <div class="plan-feature">✅ Everything in Pro</div>
                    <div class="plan-feature">✅ Team management</div>
                    <div class="plan-feature">✅ Bulk processing</div>
                    <div class="plan-feature">✅ Custom integrations</div>
                    <div class="plan-feature">✅ Priority support</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Contact Section -->
    <div id="contact" class="contact-section">
        <h2 class="section-title">💬 Get In Touch</h2>
        <div class="contact-content">
            <p class="contact-desc">Have questions or need support? Our team is here to help you succeed in your career journey.</p>
            <div class="contact-grid">
                <div class="feature-card contact-card">
                    <div class="contact-icon">📧</div>
                    <div class="contact-title">Email Support</div>
                    <a href="mailto:support@hirelyzer.com" class="contact-link">support@hirelyzer.com</a>
                </div>
                <div class="feature-card contact-card">
                    <div class="contact-icon">🌐</div>
                    <div class="contact-title">Visit Website</div>
                    <a href="https://hirelyzer.com" target="_blank" class="contact-link">www.hirelyzer.com</a>
                </div>
            </div>
            <div class="cta-final">
                <div class="cta-title">🚀 Ready to Transform Your Career?</div>
                <p class="cta-desc">Join thousands of professionals who have already upgraded their resumes with HIRELYZER</p>
                <a href="https://hirelyzer-app.streamlit.app/" target="_blank" class="btn">
                    ✨ Start Your Journey Now
                </a>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <div class="footer">
        <div class="footer-content">
            <div>© 2025 HIRELYZER. All rights reserved.</div>
            <div class="footer-links">
                <a href="#" class="footer-link">Privacy Policy</a>
                <a href="#" class="footer-link">Terms of Service</a>
                <a href="#" class="footer-link">Cookie Policy</a>
            </div>
        </div>
    </div>

    <script>{js}</script>
</body>
</html>"""
    
    return html

def main():
    """Main function to generate the landing page"""
    print("🚀 Generating HIRELYZER Landing Page...")
    
    # Generate HTML content
    html_content = generate_html()
    
    # Write to file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Landing page generated successfully!")
    print("📄 File created: index.html")
    print("🌐 Open index.html in your browser to view the landing page")
    
    # Also create a simple server script
    server_script = dedent("""
    #!/usr/bin/env python3
    import http.server
    import socketserver
    import webbrowser
    import os
    
    PORT = 8000
    
    class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
    
    def main():
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🚀 HIRELYZER Landing Page Server")
            print(f"📡 Serving at http://localhost:{PORT}")
            print(f"🌐 Opening browser...")
            
            # Open browser
            webbrowser.open(f'http://localhost:{PORT}')
            
            print(f"🛑 Press Ctrl+C to stop the server")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\\n🛑 Server stopped")
    
    if __name__ == "__main__":
        main()
    """)
    
    with open('serve.py', 'w', encoding='utf-8') as f:
        f.write(server_script)
    
    print("🖥️  Server script created: serve.py")
    print("💡 Run 'python serve.py' to start a local server")

if __name__ == "__main__":
    main()
