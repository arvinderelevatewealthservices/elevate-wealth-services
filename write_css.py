import os
path = r'c:\Users\itxul\Desktop\ElevateWealthServices\css\styles.css'
css = r"""/* ═══════════════════════════════════════════════════════
   ELEVATE WEALTH SERVICES — CSS Design System v2.0
   Dark Luxury Fintech Theme
═══════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ─── DESIGN TOKENS ─── */
:root {
  --c-navy-deep: #071520;
  --c-navy: #0E2A3A;
  --c-navy-card: #0F2535;
  --c-navy-light: #1A3548;
  --c-teal: #1F7A8C;
  --c-teal-2: #2FB5C4;
  --c-teal-3: #44D4E0;
  --c-gold: #C9A84C;
  --c-gold-lt: #E8C97A;
  --t-primary: #E8F4F8;
  --t-secondary: #A8CDD8;
  --t-muted: #5E8A9A;
  --t-dim: #3A6070;
  --s-card: rgba(15,37,53,0.92);
  --b-subtle: rgba(47,181,196,0.13);
  --b-hover: rgba(47,181,196,0.42);
  --ff-display: 'Playfair Display', Georgia, 'Times New Roman', serif;
  --ff-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --nav-h: 72px;
  --r-sm: 6px;
  --r-md: 12px;
  --r-lg: 18px;
  --r-xl: 24px;
  --r-full: 9999px;
  --t-fast: 0.18s;
  --t-base: 0.32s;
  --t-slow: 0.6s;
  --t-reveal: 0.72s;
}

/* ─── RESET ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
body {
  font-family: var(--ff-body);
  background: var(--c-navy-deep);
  color: var(--t-primary);
  padding-top: var(--nav-h);
  overflow-x: hidden;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
img { max-width: 100%; display: block; height: auto; }
a { color: inherit; text-decoration: none; }
ul { list-style: none; }
button { cursor: pointer; background: none; border: none; font-family: var(--ff-body); }
address { font-style: normal; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--c-navy-deep); }
::-webkit-scrollbar-thumb { background: var(--c-teal); border-radius: 3px; }

/* ─── UTILITIES ─── */
.container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
.section-pad { padding: 96px 0; }
.gradient-text {
  background: linear-gradient(135deg, var(--c-teal-2), var(--c-teal-3));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.section-label {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--c-teal-2);
  margin-bottom: 1rem;
}
.teal-rule {
  width: 48px;
  height: 3px;
  background: linear-gradient(90deg, var(--c-teal-2), var(--c-teal-3));
  border-radius: 2px;
  margin-top: 1.2rem;
}
.section-header {
  text-align: center;
  max-width: 640px;
  margin: 0 auto 3.5rem;
}
.section-header h2 {
  font-family: var(--ff-display);
  font-size: clamp(1.75rem, 3vw, 2.4rem);
  font-weight: 600;
  color: var(--t-primary);
  margin-bottom: 0.75rem;
  line-height: 1.2;
}
.section-header p {
  color: var(--t-secondary);
  font-size: 1.05rem;
  line-height: 1.65;
}
.section-header .teal-rule { margin: 1rem auto 0; }

/* ─── REVEAL ANIMATIONS ─── */
.reveal, .reveal-left, .reveal-right, .reveal-scale {
  opacity: 0;
  transition: opacity var(--t-reveal) ease, transform var(--t-reveal) cubic-bezier(0.16,1,0.3,1);
}
.reveal { transform: translateY(32px); }
.reveal-left { transform: translateX(-40px); }
.reveal-right { transform: translateX(40px); }
.reveal-scale { transform: scale(0.9); }
.revealed { opacity: 1 !important; transform: none !important; }
.d-1 { transition-delay: 0.05s; }
.d-2 { transition-delay: 0.12s; }
.d-3 { transition-delay: 0.19s; }
.d-4 { transition-delay: 0.26s; }
.d-5 { transition-delay: 0.33s; }
.d-6 { transition-delay: 0.40s; }

/* ─── KEYFRAMES ─── */
@keyframes orbFloat {
  0%, 100% { transform: translate(0,0) scale(1); }
  33% { transform: translate(24px,-40px) scale(1.08); }
  66% { transform: translate(-18px,28px) scale(0.94); }
}
@keyframes fadeUp {
  from { opacity:0; transform: translateY(24px); }
  to   { opacity:1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity:0; }
  to   { opacity:1; }
}
@keyframes lineGrow {
  from { stroke-dashoffset: 1200; }
  to   { stroke-dashoffset: 0; }
}
@keyframes barRise {
  from { transform: scaleY(0); transform-origin: bottom; }
  to   { transform: scaleY(1); transform-origin: bottom; }
}
@keyframes scrollDot {
  0%,100% { transform: translateY(0); opacity:1; }
  50% { transform: translateY(9px); opacity:0.4; }
}
@keyframes rippleAnim {
  to { transform: scale(3); opacity: 0; }
}
@keyframes lineGrowH {
  from { width: 0; }
  to   { width: 100%; }
}

/* ─── NAVIGATION ─── */
.nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  height: var(--nav-h);
  z-index: 900;
  background: rgba(7,21,32,0.78);
  backdrop-filter: blur(18px) saturate(1.6);
  -webkit-backdrop-filter: blur(18px) saturate(1.6);
  border-bottom: 1px solid rgba(47,181,196,0.1);
  transition: background var(--t-base) ease, box-shadow var(--t-base) ease;
}
.nav.scrolled {
  background: rgba(7,21,32,0.97);
  box-shadow: 0 2px 32px rgba(0,0,0,0.5);
}
.nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
}
.nav-logo img { height: 40px; width: auto; }
.nav-links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}
.nav-links a {
  padding: 0.45rem 0.9rem;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--t-secondary);
  border-radius: var(--r-full);
  transition: color var(--t-fast) ease, background var(--t-fast) ease;
}
.nav-links a:hover, .nav-links a.nav-active {
  color: var(--t-primary);
  background: var(--b-subtle);
}
.nav-cta-btn {
  background: linear-gradient(135deg, var(--c-teal), var(--c-teal-2)) !important;
  color: #fff !important;
  padding: 0.5rem 1.25rem !important;
  border-radius: var(--r-full) !important;
  font-weight: 600 !important;
  font-size: 0.85rem !important;
  transition: opacity var(--t-fast) ease, transform var(--t-fast) ease !important;
}
.nav-cta-btn:hover { opacity: 0.9; transform: translateY(-1px); }
.nav-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  padding: 6px;
  cursor: pointer;
}
.nav-toggle span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--t-primary);
  border-radius: 2px;
  transition: all 0.3s ease;
}
.nav-mobile {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(7,21,32,0.97);
  backdrop-filter: blur(24px);
  z-index: 910;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
}
.nav-mobile.open { display: flex; animation: fadeIn 0.3s ease; }
.nav-mobile a {
  font-size: 1.4rem;
  font-weight: 600;
  color: var(--t-secondary);
  transition: color var(--t-fast) ease;
}
.nav-mobile a:hover { color: var(--c-teal-3); }
.nav-mobile .mobile-cta {
  margin-top: 0.5rem;
  padding: 0.7rem 2rem;
  background: linear-gradient(135deg, var(--c-teal), var(--c-teal-2));
  color: #fff;
  border-radius: var(--r-full);
  font-size: 1rem;
}
.nav-mobile-close {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  font-size: 1.5rem;
  color: var(--t-muted);
  padding: 0.5rem;
  transition: color var(--t-fast) ease;
  background: none;
  border: none;
  cursor: pointer;
}
.nav-mobile-close:hover { color: var(--t-primary); }

/* ─── BUTTONS ─── */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 1.5rem;
  font-size: 0.925rem;
  font-weight: 600;
  font-family: var(--ff-body);
  border-radius: var(--r-full);
  transition: all var(--t-base) cubic-bezier(0.34,1.56,0.64,1);
  cursor: pointer;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  border: none;
  text-decoration: none;
}
.btn-primary {
  background: linear-gradient(135deg, var(--c-teal) 0%, var(--c-teal-2) 100%);
  color: #fff;
  box-shadow: 0 4px 24px rgba(31,122,140,0.35);
}
.btn-primary:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 32px rgba(47,181,196,0.5);
}
.btn-ghost {
  background: transparent;
  color: var(--t-primary);
  border: 1.5px solid rgba(47,181,196,0.4);
}
.btn-ghost:hover {
  background: var(--b-subtle);
  border-color: var(--c-teal-2);
  transform: translateY(-2px);
}
.btn-lg { padding: 0.85rem 2rem; font-size: 1rem; }
.btn-arrow { transition: transform var(--t-fast) ease; }
.btn:hover .btn-arrow { transform: translateX(4px); }
.ripple {
  position: absolute;
  border-radius: 50%;
  background: rgba(255,255,255,0.22);
  transform: scale(0);
  animation: rippleAnim 0.6s linear;
  pointer-events: none;
}

/* ─── HERO ─── */
.hero {
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  overflow: hidden;
  background: var(--c-navy-deep);
}
.hero-bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  animation: orbFloat 12s ease-in-out infinite;
}
.orb-1 {
  width: 520px; height: 520px;
  background: radial-gradient(circle, rgba(31,122,140,0.28) 0%, transparent 70%);
  top: -100px; left: -160px;
  animation-duration: 14s;
}
.orb-2 {
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(47,181,196,0.18) 0%, transparent 70%);
  top: 30%; right: -120px;
  animation-duration: 18s;
  animation-delay: -4s;
}
.orb-3 {
  width: 300px; height: 300px;
  background: radial-gradient(circle, rgba(201,168,76,0.1) 0%, transparent 70%);
  bottom: -80px; left: 40%;
  animation-duration: 20s;
  animation-delay: -8s;
}
.hero-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(47,181,196,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(47,181,196,0.04) 1px, transparent 1px);
  background-size: 64px 64px;
  mask-image: radial-gradient(ellipse at center, black 0%, transparent 70%);
}
.hero-chart {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 55%;
  max-width: 700px;
  opacity: 0.55;
  pointer-events: none;
}
.chart-line {
  stroke-dasharray: 1200;
  stroke-dashoffset: 1200;
  animation: lineGrow 2.2s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;
}
.chart-area { animation: fadeIn 1s ease 0.8s both; }
.chart-dot { animation: fadeIn 0.5s ease 2.4s both; }
.hero-content {
  position: relative;
  z-index: 2;
  max-width: 640px;
  animation: fadeUp 0.8s cubic-bezier(0.16,1,0.3,1) 0.2s both;
  padding: 6rem 0 5rem;
  margin: 0 auto;
  width: 100%;
  padding-left: max(24px, calc((100vw - 1200px) / 2 + 24px));
  padding-right: 24px;
}
.hero-eyebrow {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
}
.hero-eyebrow span {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--c-gold);
}
.eyebrow-sep {
  display: inline-block;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--c-teal-2);
  opacity: 0.6;
}
.hero-h1 {
  font-family: var(--ff-display);
  font-size: clamp(2.4rem, 5.5vw, 3.8rem);
  font-weight: 600;
  line-height: 1.12;
  color: var(--t-primary);
  margin-bottom: 1.25rem;
}
.hero-h1 em {
  font-style: italic;
  color: var(--c-teal-3);
}
.hero-sub {
  font-size: clamp(1rem, 1.4vw, 1.15rem);
  color: var(--t-secondary);
  line-height: 1.72;
  margin-bottom: 2rem;
  max-width: 500px;
}
.hero-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
}
.hero-stats {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}
.hero-stat {
  display: flex;
  flex-direction: column;
  padding: 0 1.5rem;
}
.hero-stat:first-child { padding-left: 0; }
.hero-stat-num {
  font-family: var(--ff-display);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--c-teal-3);
  line-height: 1;
}
.hero-stat-label {
  font-size: 0.7rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  color: var(--t-muted);
  margin-top: 4px;
  text-transform: uppercase;
}
.stat-sep {
  width: 1px;
  height: 32px;
  background: rgba(47,181,196,0.22);
}
.hero-scroll {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: var(--t-muted);
  font-size: 0.65rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  animation: fadeIn 1s ease 2s both;
}
.scroll-mouse {
  width: 22px; height: 36px;
  border: 2px solid rgba(47,181,196,0.35);
  border-radius: 12px;
  display: flex;
  justify-content: center;
  padding-top: 6px;
}
.scroll-dot {
  width: 4px; height: 4px;
  background: var(--c-teal-2);
  border-radius: 50%;
  animation: scrollDot 2s ease-in-out infinite;
}

/* ─── LOGO SHOWCASE ─── */
.logo-showcase {
  position: relative;
  padding: 64px 0;
  background: var(--c-navy);
  overflow: hidden;
  text-align: center;
  border-top: 1px solid rgba(47,181,196,0.1);
  border-bottom: 1px solid rgba(47,181,196,0.1);
}
.logo-showcase-bg { position: absolute; inset: 0; pointer-events: none; }
.logo-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 400px; height: 200px;
  background: radial-gradient(ellipse, rgba(47,181,196,0.12) 0%, transparent 70%);
}
.logo-bar-chart {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 340px;
  opacity: 0.28;
  pointer-events: none;
}
.bar-rise {
  transform-origin: bottom;
  animation: barRise 1.2s cubic-bezier(0.16,1,0.3,1) 0.4s both;
}
.logo-showcase-inner {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}
.logo-showcase-inner img { height: 60px; width: auto; }
.logo-tagline {
  font-family: var(--ff-display);
  font-style: italic;
  font-size: 1.05rem;
  color: var(--t-muted);
}

/* ─── SERVICES (Homepage) ─── */
.services-section { background: var(--c-navy-deep); }
.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}
.service-card {
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-lg);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: border-color var(--t-base) ease, box-shadow var(--t-base) ease, transform var(--t-base) ease;
}
.service-card:hover {
  border-color: var(--b-hover);
  box-shadow: 0 8px 40px rgba(31,122,140,0.25);
  transform: translateY(-4px);
}
.svc-icon {
  width: 48px; height: 48px;
  border-radius: var(--r-md);
  background: linear-gradient(135deg, rgba(31,122,140,0.3), rgba(47,181,196,0.15));
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-teal-3);
  flex-shrink: 0;
}
.service-card h3 {
  font-family: var(--ff-display);
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--t-primary);
}
.service-card > p {
  color: var(--t-secondary);
  font-size: 0.92rem;
  line-height: 1.65;
}
.svc-features { display: flex; flex-direction: column; gap: 0.42rem; margin: 0.25rem 0; flex: 1; }
.svc-feature {
  display: flex;
  align-items: flex-start;
  gap: 0.55rem;
  font-size: 0.875rem;
  color: var(--t-secondary);
}
.svc-check {
  color: var(--c-teal-2);
  font-size: 0.8rem;
  margin-top: 2px;
  flex-shrink: 0;
  font-weight: 700;
}
.svc-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--c-teal-2);
  transition: gap var(--t-fast) ease, color var(--t-fast) ease;
  margin-top: auto;
}
.svc-link:hover { gap: 0.55rem; color: var(--c-teal-3); }

/* ─── WHY SECTION ─── */
.why-section { background: var(--c-navy); }
.why-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: start;
}
.why-left h2 {
  font-family: var(--ff-display);
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  font-weight: 600;
  color: var(--t-primary);
  margin: 0.5rem 0 1.25rem;
  line-height: 1.15;
}
.why-left > p {
  color: var(--t-secondary);
  font-size: 1rem;
  line-height: 1.72;
  margin-bottom: 2rem;
}
.why-features {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
}
.why-feat {
  display: flex;
  gap: 0.85rem;
  align-items: flex-start;
}
.why-feat-icon {
  width: 36px; height: 36px;
  border-radius: var(--r-md);
  background: linear-gradient(135deg, rgba(31,122,140,0.3), rgba(47,181,196,0.12));
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-teal-2);
  flex-shrink: 0;
  margin-top: 2px;
}
.why-feat h4 { font-size: 0.9rem; font-weight: 600; color: var(--t-primary); margin-bottom: 0.25rem; }
.why-feat p { font-size: 0.82rem; color: var(--t-muted); line-height: 1.55; }
.why-right { display: flex; flex-direction: column; gap: 1.5rem; }
.why-stats { display: flex; flex-direction: column; gap: 1.25rem; }
.why-stat-row {
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
  padding: 1.25rem 1.5rem;
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-md);
}
.why-stat-num {
  font-family: var(--ff-display);
  font-size: 2.2rem;
  font-weight: 700;
  line-height: 1;
}
.why-stat-label { font-size: 0.9rem; color: var(--t-secondary); }

/* ─── PROCESS TIMELINE ─── */
.process-section { background: var(--c-navy-deep); }
.process-timeline {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  position: relative;
}
.process-timeline::before {
  content: '';
  position: absolute;
  top: 28px;
  left: calc(12.5% + 28px);
  right: calc(12.5% + 28px);
  height: 2px;
  background: linear-gradient(90deg, var(--c-teal), var(--c-teal-3));
  opacity: 0.35;
}
.process-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 1rem;
}
.step-num {
  width: 56px; height: 56px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--c-teal), var(--c-teal-2));
  color: #fff;
  font-family: var(--ff-display);
  font-size: 1.25rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 20px rgba(31,122,140,0.4);
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}
.process-step h3 { font-size: 1rem; font-weight: 700; color: var(--t-primary); }
.process-step p { font-size: 0.875rem; color: var(--t-secondary); line-height: 1.6; }

/* ─── BENEFITS ─── */
.benefits-section { background: var(--c-navy); }
.benefits-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}
.benefit-card {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
  padding: 1.5rem;
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-md);
  transition: border-color var(--t-base) ease;
}
.benefit-card:hover { border-color: var(--b-hover); }
.benefit-icon {
  width: 40px; height: 40px;
  border-radius: var(--r-sm);
  background: linear-gradient(135deg, rgba(31,122,140,0.3), rgba(47,181,196,0.12));
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-teal-2);
  flex-shrink: 0;
}
.benefit-card h4 { font-size: 0.95rem; font-weight: 600; color: var(--t-primary); margin-bottom: 0.3rem; }
.benefit-card p { font-size: 0.85rem; color: var(--t-secondary); line-height: 1.6; }

/* ─── CREDENTIALS ─── */
.credentials-section {
  background: linear-gradient(135deg, rgba(14,42,58,0.9), rgba(31,122,140,0.15));
  border-top: 1px solid rgba(201,168,76,0.2);
  border-bottom: 1px solid rgba(201,168,76,0.2);
  padding: 48px 0;
}
.credentials-row {
  display: flex;
  justify-content: center;
  gap: 3rem;
  flex-wrap: wrap;
}
.cred-badge {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem 2rem;
  background: rgba(201,168,76,0.06);
  border: 1px solid rgba(201,168,76,0.22);
  border-radius: var(--r-lg);
  min-width: 220px;
}
.cred-icon {
  width: 42px; height: 42px;
  border-radius: 50%;
  background: rgba(201,168,76,0.12);
  border: 1px solid rgba(201,168,76,0.28);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-gold);
  flex-shrink: 0;
}
.cred-title { display: block; font-size: 0.95rem; font-weight: 700; color: var(--c-gold-lt); }
.cred-sub { display: block; font-size: 0.78rem; color: var(--t-muted); margin-top: 2px; }

/* ─── CTA BANNER ─── */
.cta-banner {
  background: linear-gradient(135deg, var(--c-teal) 0%, #0a3f4e 50%, var(--c-navy) 100%);
  position: relative;
  overflow: hidden;
}
.cta-banner::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
}
.cta-banner-inner {
  max-width: 700px;
  margin: 0 auto;
  padding: 96px 24px;
  text-align: center;
  position: relative;
  z-index: 1;
}
.cta-banner h2 {
  font-family: var(--ff-display);
  font-size: clamp(1.8rem, 3.5vw, 2.6rem);
  font-weight: 700;
  color: #fff;
  margin: 0.5rem 0 1rem;
  line-height: 1.2;
}
.cta-banner p {
  color: rgba(232,244,248,0.82);
  font-size: 1.05rem;
  line-height: 1.68;
  margin-bottom: 2rem;
}
.cta-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* ─── BRAND PARTNERS ─── */
#bpsec {
  background: var(--c-navy);
  padding: 80px 0;
  position: relative;
  overflow: hidden;
  border-top: 1px solid var(--b-subtle);
  border-bottom: 1px solid var(--b-subtle);
}
.bp-glow {
  position: absolute;
  border-radius: 50%;
  filter: blur(90px);
  pointer-events: none;
}
.bp-glow-a {
  width: 500px; height: 300px;
  background: radial-gradient(ellipse, rgba(31,122,140,0.12), transparent);
  top: -60px; left: -120px;
}
.bp-glow-b {
  width: 400px; height: 300px;
  background: radial-gradient(ellipse, rgba(47,181,196,0.08), transparent);
  bottom: -40px; right: -100px;
}
.bpsec-inner { position: relative; z-index: 1; }
.bphdr { text-align: center; margin-bottom: 2.5rem; }
.bplabel { display: inline-block; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: var(--c-teal-2); margin-bottom: 0.6rem; }
.bptitle { font-family: var(--ff-display); font-size: clamp(1.5rem, 2.5vw, 2rem); font-weight: 600; color: var(--t-primary); margin-bottom: 0.6rem; }
.bpdesc { color: var(--t-secondary); font-size: 0.95rem; max-width: 480px; margin: 0 auto; }
.bprule { width: 40px; height: 3px; background: linear-gradient(90deg, var(--c-teal-2), var(--c-teal-3)); border-radius: 2px; margin: 0.8rem auto 0; }
.bp-tabs {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}
.bp-tab {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.2rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--t-muted);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-full);
  background: transparent;
  font-family: var(--ff-body);
  transition: all var(--t-fast) ease;
  cursor: pointer;
}
.bp-tab:hover { color: var(--t-primary); border-color: var(--b-hover); }
.bp-tab.active {
  color: #fff;
  background: linear-gradient(135deg, var(--c-teal), var(--c-teal-2));
  border-color: transparent;
  box-shadow: 0 4px 16px rgba(31,122,140,0.35);
}
.bp-panel { display: none; }
.bp-panel.active { display: block; }
.bp-slider-outer {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.bpswrap {
  flex: 1;
  overflow: hidden;
  border-radius: var(--r-lg);
}
.bpstrack {
  display: flex;
  gap: 1rem;
  transition: transform 0.5s cubic-bezier(0.16,1,0.3,1);
}
.bpc {
  flex: 0 0 calc(25% - 0.75rem);
  min-width: 0;
}
.bpc-body {
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-md);
  padding: 1.5rem;
  text-align: center;
  transition: border-color var(--t-base) ease, transform var(--t-base) ease;
  height: 100%;
}
.bpc-body:hover { border-color: var(--b-hover); transform: translateY(-3px); }
.bpc-logo {
  width: 56px; height: 56px;
  border-radius: var(--r-md);
  overflow: hidden;
  margin: 0 auto 0.85rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,0.06);
}
.bpc-logo-lg { width: 72px; height: 72px; }
.bpc-img { width: 100%; height: 100%; object-fit: contain; }
.bpc-fb {
  display: none;
  width: 100%; height: 100%;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: 0.05em;
}
.bpc-name { font-size: 0.875rem; font-weight: 600; color: var(--t-primary); margin-bottom: 4px; }
.bpc-type { font-size: 0.775rem; color: var(--t-muted); }
.bpc-badge {
  display: inline-block;
  margin-top: 0.5rem;
  padding: 0.2rem 0.65rem;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--c-gold);
  background: rgba(201,168,76,0.1);
  border: 1px solid rgba(201,168,76,0.25);
  border-radius: var(--r-full);
}
.bparr {
  width: 38px; height: 38px;
  border-radius: 50%;
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--t-secondary);
  transition: all var(--t-fast) ease;
  flex-shrink: 0;
  cursor: pointer;
  font-family: var(--ff-body);
}
.bparr:hover { border-color: var(--b-hover); color: var(--t-primary); background: var(--b-subtle); }
.bp-dots {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 1.25rem;
}
.bp-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: var(--b-subtle);
  border: 1px solid var(--b-subtle);
  transition: all var(--t-fast) ease;
  cursor: pointer;
}
.bp-dot.active { background: var(--c-teal-2); width: 22px; border-radius: 4px; }
.bp-trade-wrap { display: flex; justify-content: center; }
.bpc-solo { min-width: 240px; max-width: 300px; }

/* ─── CONTACT ─── */
.contact-section { background: var(--c-navy-deep); }
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 400px;
  gap: 3rem;
  align-items: start;
}
.contact-form-wrap h2 {
  font-family: var(--ff-display);
  font-size: clamp(1.6rem, 2.5vw, 2.2rem);
  font-weight: 600;
  color: var(--t-primary);
  margin-bottom: 0.5rem;
}
.contact-form-sub { color: var(--t-muted); font-size: 0.9rem; margin-bottom: 2rem; }
.contact-form { display: flex; flex-direction: column; gap: 1.25rem; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; }
.form-group { display: flex; flex-direction: column; gap: 0.4rem; }
.form-label { font-size: 0.85rem; font-weight: 600; color: var(--t-secondary); }
.form-label span { color: var(--c-teal-2); }
.form-input, .form-textarea, .form-select {
  padding: 0.75rem 1rem;
  background: rgba(15,37,53,0.8);
  border: 1px solid rgba(47,181,196,0.2);
  border-radius: var(--r-md);
  color: var(--t-primary);
  font-family: var(--ff-body);
  font-size: 0.9rem;
  transition: border-color var(--t-fast) ease, box-shadow var(--t-fast) ease;
  outline: none;
  width: 100%;
}
.form-input::placeholder, .form-textarea::placeholder { color: var(--t-dim); }
.form-input:focus, .form-textarea:focus, .form-select:focus {
  border-color: var(--c-teal-2);
  box-shadow: 0 0 0 3px rgba(47,181,196,0.15);
}
.form-select {
  -webkit-appearance: none;
  appearance: none;
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-color: rgba(15,37,53,0.8);
  cursor: pointer;
  padding-right: 36px;
}
.form-select option { background: #0F2535; color: var(--t-primary); }
.form-textarea { resize: vertical; min-height: 100px; }
.form-error { font-size: 0.78rem; color: #ef5350; }
.wa-btn-full { width: 100%; justify-content: center; }
.contact-info-wrap { position: sticky; top: calc(var(--nav-h) + 2rem); }
.contact-card {
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-lg);
  padding: 2rem;
}
.contact-card h3 {
  font-family: var(--ff-display);
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--t-primary);
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--b-subtle);
}
.contact-info-item {
  display: flex;
  gap: 0.9rem;
  align-items: flex-start;
  padding: 0.85rem 0;
  border-bottom: 1px solid rgba(47,181,196,0.07);
}
.contact-info-item:last-of-type { border-bottom: none; }
.ci-icon {
  width: 34px; height: 34px;
  border-radius: var(--r-sm);
  background: linear-gradient(135deg, rgba(31,122,140,0.25), rgba(47,181,196,0.1));
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-teal-2);
  flex-shrink: 0;
  margin-top: 1px;
}
.ci-label { display: block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--t-muted); margin-bottom: 3px; }
.ci-value { display: block; font-size: 0.88rem; color: var(--t-secondary); line-height: 1.55; }
.ci-value a { color: var(--c-teal-2); transition: color var(--t-fast) ease; }
.ci-value a:hover { color: var(--c-teal-3); }
.wa-direct-btn { margin-top: 1.5rem; width: 100%; justify-content: center; }
.contact-creds {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-top: 1.25rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--b-subtle);
}
.cc-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.35rem 0.75rem;
  background: rgba(201,168,76,0.07);
  border: 1px solid rgba(201,168,76,0.2);
  border-radius: var(--r-full);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: var(--c-gold);
}

/* ─── PAGE HERO ─── */
.page-hero {
  min-height: 44vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: var(--c-navy);
}
.page-hero-bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}
.page-hero-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(47,181,196,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(47,181,196,0.04) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: radial-gradient(ellipse at center, black 0%, transparent 70%);
}
.page-hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 6rem 24px 4rem;
  max-width: 680px;
  animation: fadeUp 0.7s cubic-bezier(0.16,1,0.3,1) 0.15s both;
}
.page-hero-content h1 {
  font-family: var(--ff-display);
  font-size: clamp(2rem, 5vw, 3.2rem);
  font-weight: 600;
  color: var(--t-primary);
  margin: 0.5rem 0 1rem;
  line-height: 1.15;
}
.page-hero-content p {
  color: var(--t-secondary);
  font-size: 1.05rem;
  line-height: 1.68;
  max-width: 520px;
  margin: 0 auto;
}

/* ─── ABOUT ─── */
.about-intro { background: var(--c-navy-deep); }
.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}
.about-left h2 {
  font-family: var(--ff-display);
  font-size: clamp(1.75rem, 3vw, 2.4rem);
  font-weight: 600;
  color: var(--t-primary);
  margin: 0.5rem 0 1.25rem;
  line-height: 1.15;
}
.about-left > p, .about-right > p {
  color: var(--t-secondary);
  font-size: 0.97rem;
  line-height: 1.75;
  margin-bottom: 1rem;
}
.about-facts {
  display: flex;
  gap: 2rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--b-subtle);
  flex-wrap: wrap;
}
.about-fact { display: flex; flex-direction: column; }
.about-fact-num { font-family: var(--ff-display); font-size: 1.8rem; font-weight: 700; line-height: 1; }
.about-fact-label { font-size: 0.78rem; color: var(--t-muted); margin-top: 4px; letter-spacing: 0.05em; text-transform: uppercase; }
.vm-card {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  position: sticky;
  top: calc(var(--nav-h) + 2rem);
}
.vm-block {
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-lg);
  padding: 2rem;
  transition: border-color var(--t-base) ease;
}
.vm-block:hover { border-color: var(--b-hover); }
.vm-block-alt {
  background: linear-gradient(135deg, rgba(15,37,53,0.9), rgba(31,122,140,0.12));
  border-color: rgba(31,122,140,0.25);
}
.vm-icon {
  width: 40px; height: 40px;
  border-radius: var(--r-md);
  background: linear-gradient(135deg, rgba(31,122,140,0.3), rgba(47,181,196,0.12));
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-teal-2);
  margin-bottom: 1rem;
}
.vm-block h3 {
  font-family: var(--ff-display);
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--t-primary);
  margin-bottom: 0.6rem;
}
.vm-block p { font-size: 0.9rem; color: var(--t-secondary); line-height: 1.7; }

/* ─── VALUES ─── */
.values-section { background: var(--c-navy); }
.values-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}
.value-card {
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-md);
  padding: 1.75rem;
  transition: border-color var(--t-base) ease, transform var(--t-base) ease;
}
.value-card:hover { border-color: var(--b-hover); transform: translateY(-3px); }
.value-icon {
  width: 42px; height: 42px;
  border-radius: var(--r-md);
  background: linear-gradient(135deg, rgba(31,122,140,0.3), rgba(47,181,196,0.12));
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-teal-2);
  margin-bottom: 1rem;
}
.value-card h4 { font-size: 0.95rem; font-weight: 700; color: var(--t-primary); margin-bottom: 0.4rem; }
.value-card p { font-size: 0.85rem; color: var(--t-secondary); line-height: 1.62; }

/* ─── SERVICE DEEP SECTIONS ─── */
.service-deep { background: var(--c-navy-deep); }
.service-deep-alt { background: var(--c-navy); }
.service-deep-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: start;
}
.service-deep-grid.flip { direction: rtl; }
.service-deep-grid.flip > * { direction: ltr; }
.service-deep-label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--c-teal-2);
  margin-bottom: 0.75rem;
}
.sdl-icon {
  width: 24px; height: 24px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(31,122,140,0.4), rgba(47,181,196,0.2));
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-teal-2);
}
.service-deep-text h2 {
  font-family: var(--ff-display);
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  font-weight: 600;
  color: var(--t-primary);
  margin-bottom: 1.25rem;
  line-height: 1.15;
}
.service-deep-text > p {
  color: var(--t-secondary);
  font-size: 0.97rem;
  line-height: 1.75;
  margin-bottom: 1rem;
}
.service-deep-feats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1.5rem 0 2rem;
}
.service-feat-card {
  display: flex;
  gap: 0.75rem;
  align-items: flex-start;
  padding: 1rem;
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-md);
  transition: border-color var(--t-base) ease;
}
.service-feat-card:hover { border-color: var(--b-hover); }
.sfeat-icon {
  width: 30px; height: 30px;
  border-radius: var(--r-sm);
  background: linear-gradient(135deg, rgba(31,122,140,0.3), rgba(47,181,196,0.12));
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-teal-2);
  flex-shrink: 0;
}
.service-feat-card h5 { font-size: 0.85rem; font-weight: 700; color: var(--t-primary); margin-bottom: 0.2rem; }
.service-feat-card p { font-size: 0.78rem; color: var(--t-secondary); line-height: 1.5; }
.service-deep-visual { position: sticky; top: calc(var(--nav-h) + 2rem); }
.sdv-card {
  background: var(--s-card);
  border: 1px solid var(--b-subtle);
  border-radius: var(--r-lg);
  padding: 2rem;
  transition: border-color var(--t-base) ease;
}
.sdv-card-alt { background: linear-gradient(135deg, rgba(15,37,53,0.9), rgba(31,122,140,0.12)); }
.sdv-label { display: block; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--t-muted); margin-bottom: 1rem; }
.sdv-stats {
  display: flex;
  gap: 0;
  margin-top: 1.5rem;
  border-top: 1px solid var(--b-subtle);
  padding-top: 1.25rem;
}
.sdv-stat { flex: 1; text-align: center; }
.sdv-stat + .sdv-stat { border-left: 1px solid var(--b-subtle); }
.sdv-val { display: block; font-family: var(--ff-display); font-size: 1.1rem; font-weight: 700; line-height: 1; margin-bottom: 4px; }
.sdv-lbl { display: block; font-size: 0.7rem; color: var(--t-muted); letter-spacing: 0.08em; text-transform: uppercase; }
.sdv-shield { margin: 1.5rem 0; text-align: center; }
.sdv-card h3 {
  font-family: var(--ff-display);
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--t-primary);
  margin-bottom: 1rem;
}
.sdv-card p {
  font-size: 0.9rem;
  color: var(--t-secondary);
  line-height: 1.68;
}

/* ─── FOOTER ─── */
.footer {
  background: var(--c-navy-deep);
  border-top: 1px solid var(--b-subtle);
  padding: 64px 0 0;
}
.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 3rem;
  padding-bottom: 3rem;
  border-bottom: 1px solid rgba(47,181,196,0.08);
}
.footer-brand img { height: 36px; width: auto; margin-bottom: 1.25rem; }
.footer-brand p { font-size: 0.88rem; color: var(--t-muted); line-height: 1.68; max-width: 260px; margin-bottom: 0.75rem; }
.footer-brand address { font-size: 0.82rem; color: var(--t-dim); line-height: 1.6; margin-bottom: 1rem; }
.social-links { display: flex; gap: 0.6rem; margin-top: 0.5rem; }
.social-link {
  width: 34px; height: 34px;
  border-radius: 50%;
  background: var(--b-subtle);
  border: 1px solid var(--b-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--t-muted);
  transition: all var(--t-fast) ease;
}
.social-link:hover { border-color: var(--b-hover); color: var(--t-primary); background: var(--b-hover); }
.footer-col h4 { font-size: 0.85rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--t-secondary); margin-bottom: 1.25rem; }
.footer-links { display: flex; flex-direction: column; gap: 0.65rem; }
.footer-links a { font-size: 0.875rem; color: var(--t-muted); transition: color var(--t-fast) ease; }
.footer-links a:hover { color: var(--c-teal-2); }
.f-contact-item {
  display: flex;
  gap: 0.65rem;
  align-items: flex-start;
  font-size: 0.82rem;
  color: var(--t-muted);
  margin-bottom: 0.7rem;
  line-height: 1.55;
}
.f-contact-item svg { color: var(--c-teal-2); margin-top: 1px; flex-shrink: 0; }
.f-contact-item a { color: var(--t-muted); transition: color var(--t-fast) ease; }
.f-contact-item a:hover { color: var(--c-teal-2); }
.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  padding: 1.5rem 0;
}
.footer-copyright { font-size: 0.82rem; color: var(--t-dim); }
.footer-badges { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.footer-badge {
  padding: 0.2rem 0.65rem;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--c-gold);
  background: rgba(201,168,76,0.08);
  border: 1px solid rgba(201,168,76,0.2);
  border-radius: var(--r-full);
}
.footer-disclaimer {
  font-size: 0.72rem;
  color: var(--t-dim);
  line-height: 1.7;
  padding: 1rem 0 1.5rem;
  border-top: 1px solid rgba(47,181,196,0.06);
}

/* ─── RESPONSIVE ─── */
@media (max-width: 1100px) {
  .hero-content { padding-left: 24px; max-width: 560px; }
  .hero-chart { width: 48%; opacity: 0.4; }
  .services-grid, .benefits-grid { grid-template-columns: 1fr 1fr; }
  .process-timeline { grid-template-columns: repeat(2, 1fr); gap: 2rem; }
  .process-timeline::before { display: none; }
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 2rem; }
  .contact-grid { grid-template-columns: 1fr 360px; }
}

@media (max-width: 768px) {
  .nav-links { display: none; }
  .nav-toggle { display: flex; }
  .hero-chart { display: none; }
  .hero-content { padding: 5rem 24px 4rem; max-width: 100%; }
  .hero-h1 { font-size: 2.2rem; }
  .hero-stat { padding: 0 0.75rem; }
  .hero-stat:first-child { padding-left: 0; }
  .services-grid { grid-template-columns: 1fr; }
  .benefits-grid { grid-template-columns: 1fr 1fr; }
  .values-grid { grid-template-columns: 1fr 1fr; }
  .why-grid { grid-template-columns: 1fr; gap: 2.5rem; }
  .why-features { grid-template-columns: 1fr; }
  .about-grid { grid-template-columns: 1fr; gap: 2rem; }
  .vm-card { position: static; }
  .contact-grid { grid-template-columns: 1fr; }
  .contact-info-wrap { position: static; }
  .service-deep-grid { grid-template-columns: 1fr; gap: 2.5rem; }
  .service-deep-grid.flip { direction: ltr; }
  .service-deep-visual { position: static; }
  .service-deep-feats { grid-template-columns: 1fr 1fr; }
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 2rem; }
  .bpc { flex: 0 0 calc(50% - 0.5rem); }
  .credentials-row { gap: 1rem; }
  .cred-badge { min-width: 160px; flex: 1; }
  .cta-banner-inner { padding: 64px 24px; }
  .process-timeline { grid-template-columns: 1fr; max-width: 360px; margin: 0 auto; }
  .section-pad { padding: 64px 0; }
}

@media (max-width: 480px) {
  .hero-h1 { font-size: 1.9rem; }
  .hero-actions { flex-direction: column; }
  .hero-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; }
  .stat-sep { display: none; }
  .hero-stat { padding: 0; }
  .form-row { grid-template-columns: 1fr; }
  .cta-actions { flex-direction: column; align-items: center; }
  .footer-bottom { flex-direction: column; align-items: flex-start; }
  .footer-grid { grid-template-columns: 1fr; }
  .about-facts { flex-wrap: wrap; gap: 1rem; }
  .benefits-grid { grid-template-columns: 1fr; }
  .values-grid { grid-template-columns: 1fr; }
  .service-deep-feats { grid-template-columns: 1fr; }
  .credentials-row { flex-direction: column; align-items: stretch; }
  .cred-badge { min-width: unset; }
}
"""
with open(path, 'w', encoding='utf-8') as f:
    f.write(css)
size = os.path.getsize(path)
print(f"CSS written: {size} bytes")
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
checks = ['Playfair', '--c-navy', '#071520', '--c-teal', 'c-navy-deep', 'orbFloat']
for c in checks:
    print(f"  {c}: {'FOUND' if c in content else 'MISSING'}")
