import os

path = r'c:\Users\itxul\Desktop\ElevateWealthServices\index.html'

NAV = '''<!-- NAVIGATION -->
<nav class="nav" id="nav" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo" aria-label="Elevate Wealth Services — Home">
      <img src="images/ElevateWealthServicesLogo.png" alt="Elevate Wealth Services">
    </a>
    <ul class="nav-links" role="menubar">
      <li role="none"><a href="index.html" class="nav-active" role="menuitem">Home</a></li>
      <li role="none"><a href="about.html" role="menuitem">About</a></li>
      <li role="none"><a href="services.html" role="menuitem">Services</a></li>
      <li role="none"><a href="contact.html" class="nav-cta-btn" role="menuitem">Book a Consultation</a></li>
    </ul>
    <button class="nav-toggle" id="navToggle" aria-label="Open navigation menu" aria-expanded="false" aria-controls="navMobile">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- MOBILE NAVIGATION OVERLAY -->
<div class="nav-mobile" id="navMobile" role="dialog" aria-modal="true" aria-label="Mobile navigation">
  <button class="nav-mobile-close" id="navMobileClose" aria-label="Close navigation">&#x2715;</button>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="services.html">Services</a>
  <a href="contact.html" class="mobile-cta">Book a Consultation</a>
</div>'''

FOOTER = '''<footer class="footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="images/ElevateWealthServicesLogo.png" alt="Elevate Wealth Services">
        <p>Your trusted partner for Mutual Fund Advisory, Insurance Solutions, and Trading &amp; Investing Services across India.</p>
        <address>Cash Dhara Bazar, Near Bawa Lal Mandir,<br>Karmon Deori, Amritsar, Punjab</address>
        <div class="social-links" aria-label="Social media links">
          <a href="https://wa.me/919815519057" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.123.555 4.12 1.528 5.856L.057 23.882l6.187-1.622A11.944 11.944 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 01-5.006-1.368l-.36-.213-3.672.964.981-3.593-.234-.369A9.818 9.818 0 1112 21.818z"/></svg>
          </a>
          <a href="mailto:arvinder@elevatewealthservices.com" class="social-link" aria-label="Email us">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          </a>
        </div>
      </div>
      <nav class="footer-col" aria-label="Quick links">
        <h4>Quick Links</h4>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="contact.html">Book Consultation</a></li>
        </ul>
      </nav>
      <nav class="footer-col" aria-label="Our services">
        <h4>Services</h4>
        <ul class="footer-links">
          <li><a href="services.html#mutual-funds">Mutual Fund Advisory</a></li>
          <li><a href="services.html#insurance">Insurance Solutions</a></li>
          <li><a href="services.html#trading">Trading &amp; Investing</a></li>
          <li><a href="contact.html">Free Consultation</a></li>
        </ul>
      </nav>
      <div class="footer-col">
        <h4>Contact</h4>
        <div class="f-contact-item">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.63 3.34 2 2 0 0 1 3.6 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.6a16 16 0 0 0 6.29 6.29l.96-.96a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <a href="tel:+919815519057">+91 98155 19057</a>
        </div>
        <div class="f-contact-item">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          <a href="mailto:arvinder@elevatewealthservices.com">arvinder@elevatewealthservices.com</a>
        </div>
        <div class="f-contact-item">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <address>Cash Dhara Bazar, Near Bawa Lal Mandir, Karmon Deori, Amritsar</address>
        </div>
        <div class="f-contact-item">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <p>Mon&ndash;Fri: 9:30 AM &ndash; 6:30 PM<br>Sat: 10:00 AM &ndash; 4:00 PM</p>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="footer-copyright">&copy; 2026 Elevate Wealth Services. All rights reserved.</p>
      <div class="footer-badges" aria-label="Regulatory compliance badges">
        <span class="footer-badge">AMFI Registered</span>
        <span class="footer-badge">IRDAI Certified</span>
        <span class="footer-badge">SEBI Compliant</span>
      </div>
    </div>
    <p class="footer-disclaimer">
      Mutual Fund investments are subject to market risks. Please read all scheme-related documents carefully before investing. Insurance is the subject matter of solicitation. Past performance is not indicative of future results. Elevate Wealth Services is an AMFI Registered Mutual Fund Distributor and IRDAI Licensed Insurance Agent.
    </p>
  </div>
</footer>'''

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Elevate Wealth Services — Smart Financial Solutions</title>
  <meta name="description" content="Expert Mutual Fund Advisory, Insurance Solutions, and Trading &amp; Investing Services in Amritsar. AMFI Registered, IRDAI Certified, SEBI Compliant.">
  <meta property="og:title" content="Elevate Wealth Services — Smart Financial Solutions">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://elevatewealthservices.com/">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

{NAV}

<!-- ═══════════════════════════════════════
     HERO
═══════════════════════════════════════ -->
<section class="hero" aria-label="Homepage hero">
  <div class="hero-bg" aria-hidden="true">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
  </div>
  <div class="hero-grid" aria-hidden="true"></div>

  <!-- Decorative chart SVG -->
  <svg class="hero-chart" viewBox="0 0 560 340" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="presentation">
    <defs>
      <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#2FB5C4" stop-opacity="0.22"/>
        <stop offset="100%" stop-color="#2FB5C4" stop-opacity="0"/>
      </linearGradient>
    </defs>
    <path class="chart-area" d="M0 280 L60 240 L120 210 L180 190 L240 155 L300 130 L360 100 L420 75 L480 50 L540 30 L560 20 L560 340 L0 340 Z" fill="url(#chartGrad)"/>
    <path class="chart-line" d="M0 280 L60 240 L120 210 L180 190 L240 155 L300 130 L360 100 L420 75 L480 50 L540 30 L560 20" stroke="#2FB5C4" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    <circle class="chart-dot" cx="480" cy="50" r="6" fill="#44D4E0"/>
    <circle class="chart-dot" cx="300" cy="130" r="5" fill="#2FB5C4" fill-opacity="0.7"/>
    <circle class="chart-dot" cx="120" cy="210" r="4" fill="#2FB5C4" fill-opacity="0.5"/>
    <!-- Grid lines -->
    <line x1="0" y1="100" x2="560" y2="100" stroke="#2FB5C4" stroke-opacity="0.08" stroke-width="1"/>
    <line x1="0" y1="180" x2="560" y2="180" stroke="#2FB5C4" stroke-opacity="0.08" stroke-width="1"/>
    <line x1="0" y1="260" x2="560" y2="260" stroke="#2FB5C4" stroke-opacity="0.08" stroke-width="1"/>
  </svg>

  <div class="hero-content">
    <div class="hero-eyebrow" aria-label="Trust badges">
      <span>AMFI Registered</span>
      <span class="eyebrow-sep" aria-hidden="true"></span>
      <span>IRDAI Certified</span>
      <span class="eyebrow-sep" aria-hidden="true"></span>
      <span>SEBI Compliant</span>
    </div>
    <h1 class="hero-h1">
      Grow Your Wealth<br>with <em>Expert Guidance</em><br>You Can Trust
    </h1>
    <p class="hero-sub">
      Elevate Wealth Services — your fully regulated financial advisory in Amritsar. Mutual Funds, Insurance, and Trading tailored to your goals.
    </p>
    <div class="hero-actions">
      <a href="contact.html" class="btn btn-primary btn-lg">
        Book Free Consultation
        <svg class="btn-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
      </a>
      <a href="services.html" class="btn btn-ghost btn-lg">Explore Services</a>
    </div>
    <div class="hero-stats" role="list" aria-label="Key statistics">
      <div class="hero-stat" role="listitem">
        <span class="hero-stat-num gradient-text" data-count="500" data-suffix="+">500+</span>
        <span class="hero-stat-label">Happy Investors</span>
      </div>
      <div class="stat-sep" aria-hidden="true"></div>
      <div class="hero-stat" role="listitem">
        <span class="hero-stat-num gradient-text">20+</span>
        <span class="hero-stat-label">Partner Institutions</span>
      </div>
      <div class="stat-sep" aria-hidden="true"></div>
      <div class="hero-stat" role="listitem">
        <span class="hero-stat-num gradient-text">3</span>
        <span class="hero-stat-label">Expert Services</span>
      </div>
    </div>
  </div>

  <div class="hero-scroll" aria-hidden="true">
    <div class="scroll-mouse"><div class="scroll-dot"></div></div>
    <span>Scroll</span>
  </div>
</section>

<!-- ═══════════════════════════════════════
     LOGO SHOWCASE
═══════════════════════════════════════ -->
<section class="logo-showcase" aria-label="Brand identity">
  <div class="logo-showcase-bg" aria-hidden="true">
    <div class="logo-glow"></div>
    <svg class="logo-bar-chart" viewBox="0 0 340 80" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <rect class="bar-rise" x="10" y="40" width="24" height="40" rx="3" fill="#2FB5C4" fill-opacity="0.6"/>
      <rect class="bar-rise" x="50" y="20" width="24" height="60" rx="3" fill="#2FB5C4" fill-opacity="0.5" style="animation-delay:0.15s"/>
      <rect class="bar-rise" x="90" y="30" width="24" height="50" rx="3" fill="#2FB5C4" fill-opacity="0.4" style="animation-delay:0.25s"/>
      <rect class="bar-rise" x="130" y="10" width="24" height="70" rx="3" fill="#2FB5C4" fill-opacity="0.6" style="animation-delay:0.1s"/>
      <rect class="bar-rise" x="170" y="25" width="24" height="55" rx="3" fill="#2FB5C4" fill-opacity="0.5" style="animation-delay:0.2s"/>
      <rect class="bar-rise" x="210" y="5"  width="24" height="75" rx="3" fill="#44D4E0" fill-opacity="0.65" style="animation-delay:0.05s"/>
      <rect class="bar-rise" x="250" y="15" width="24" height="65" rx="3" fill="#2FB5C4" fill-opacity="0.55" style="animation-delay:0.3s"/>
      <rect class="bar-rise" x="290" y="35" width="24" height="45" rx="3" fill="#2FB5C4" fill-opacity="0.4" style="animation-delay:0.35s"/>
    </svg>
  </div>
  <div class="logo-showcase-inner reveal">
    <img src="images/ElevateWealthServicesLogo.png" alt="Elevate Wealth Services" width="200">
    <p class="logo-tagline">"Elevating every investment journey with expertise and integrity."</p>
  </div>
</section>

<!-- ═══════════════════════════════════════
     SERVICES
═══════════════════════════════════════ -->
<section class="services-section section-pad" aria-labelledby="svc-heading">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-label">What We Offer</span>
      <h2 id="svc-heading">Comprehensive Financial Services</h2>
      <p>Three pillars of financial excellence — each designed to build, protect, and grow your wealth with regulated expertise.</p>
      <div class="teal-rule"></div>
    </div>
    <div class="services-grid">

      <!-- Mutual Funds -->
      <article class="service-card reveal d-1" aria-label="Mutual Fund Advisory">
        <div class="svc-icon" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <h3>Mutual Fund Advisory</h3>
        <p>AMFI Registered expert guidance on mutual fund selection, portfolio construction, and SIP planning aligned to your risk profile.</p>
        <ul class="svc-features" aria-label="Features">
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Goal-based SIP planning</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Risk profiling &amp; fund selection</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Equity, debt &amp; hybrid funds</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>ELSS tax-saving strategies</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Regular portfolio reviews</span></li>
        </ul>
        <a href="services.html#mutual-funds" class="svc-link">
          Learn More
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
      </article>

      <!-- Insurance -->
      <article class="service-card reveal d-2" aria-label="Insurance Solutions">
        <div class="svc-icon" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h3>Insurance Solutions</h3>
        <p>IRDAI certified advisory on life and health insurance — protecting what matters most while optimising your coverage and premiums.</p>
        <ul class="svc-features" aria-label="Features">
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Term &amp; whole life insurance</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Health &amp; critical illness cover</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>ULIPs &amp; endowment plans</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Retirement &amp; pension plans</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Claims assistance support</span></li>
        </ul>
        <a href="services.html#insurance" class="svc-link">
          Learn More
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
      </article>

      <!-- Trading -->
      <article class="service-card reveal d-3" aria-label="Trading and Investing">
        <div class="svc-icon" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h3>Trading &amp; Investing</h3>
        <p>SEBI compliant stock market guidance — equities, derivatives, and long-term wealth creation strategies for disciplined investors.</p>
        <ul class="svc-features" aria-label="Features">
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Equity &amp; derivative advisory</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Fundamental &amp; technical analysis</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Portfolio diversification</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>IPO &amp; NFO guidance</span></li>
          <li class="svc-feature"><span class="svc-check" aria-hidden="true">&#x2714;</span><span>Risk management strategies</span></li>
        </ul>
        <a href="services.html#trading" class="svc-link">
          Learn More
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
      </article>

    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     WHY ELEVATE
═══════════════════════════════════════ -->
<section class="why-section section-pad" aria-labelledby="why-heading">
  <div class="container">
    <div class="why-grid">

      <div class="why-left">
        <span class="section-label reveal">Why Choose Us</span>
        <h2 id="why-heading" class="reveal">Your Financial Success is Our Measure of Excellence</h2>
        <p class="reveal">At Elevate Wealth Services, we combine regulatory expertise with a deeply personal approach. Every client gets a dedicated advisor who understands their unique financial situation and goals.</p>
        <div class="why-features" role="list">
          <div class="why-feat reveal d-1" role="listitem">
            <div class="why-feat-icon" aria-hidden="true">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <div><h4>Fully Regulated</h4><p>AMFI, IRDAI &amp; SEBI registered — your investments are always protected.</p></div>
          </div>
          <div class="why-feat reveal d-2" role="listitem">
            <div class="why-feat-icon" aria-hidden="true">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
            <div><h4>Transparent Advice</h4><p>No hidden agendas — only clear, honest guidance aligned to your goals.</p></div>
          </div>
          <div class="why-feat reveal d-3" role="listitem">
            <div class="why-feat-icon" aria-hidden="true">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </div>
            <div><h4>Personal Advisor</h4><p>One dedicated advisor who knows you and your financial journey.</p></div>
          </div>
          <div class="why-feat reveal d-4" role="listitem">
            <div class="why-feat-icon" aria-hidden="true">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </div>
            <div><h4>Proven Results</h4><p>500+ satisfied investors with consistent, long-term wealth growth.</p></div>
          </div>
          <div class="why-feat reveal d-5" role="listitem">
            <div class="why-feat-icon" aria-hidden="true">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            </div>
            <div><h4>Holistic Planning</h4><p>Investment, insurance &amp; trading under one roof for complete financial health.</p></div>
          </div>
          <div class="why-feat reveal d-6" role="listitem">
            <div class="why-feat-icon" aria-hidden="true">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            </div>
            <div><h4>Always Accessible</h4><p>Reach us on WhatsApp, phone, or in-person — whenever you need guidance.</p></div>
          </div>
        </div>
      </div>

      <div class="why-right">
        <div class="why-stats" role="list">
          <div class="why-stat-row reveal d-1" role="listitem">
            <span class="why-stat-num gradient-text" data-count="500" data-suffix="+">500+</span>
            <span class="why-stat-label">Investors trust Elevate Wealth Services with their financial futures</span>
          </div>
          <div class="why-stat-row reveal d-2" role="listitem">
            <span class="why-stat-num gradient-text">20+</span>
            <span class="why-stat-label">Partner AMCs, Insurance &amp; Brokerage institutions across India</span>
          </div>
          <div class="why-stat-row reveal d-3" role="listitem">
            <span class="why-stat-num gradient-text">3</span>
            <span class="why-stat-label">Core service verticals — Mutual Funds, Insurance, and Trading</span>
          </div>
          <div class="why-stat-row reveal d-4" role="listitem">
            <span class="why-stat-num gradient-text">100%</span>
            <span class="why-stat-label">AMFI, IRDAI &amp; SEBI regulated — full regulatory compliance</span>
          </div>
        </div>
        <a href="about.html" class="btn btn-ghost" style="margin-top:1.5rem;">
          Meet Our Team
          <svg class="btn-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
      </div>

    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     PROCESS TIMELINE
═══════════════════════════════════════ -->
<section class="process-section section-pad" aria-labelledby="process-heading">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-label">How It Works</span>
      <h2 id="process-heading">Your Journey to Financial Clarity</h2>
      <p>Four simple steps from your first conversation to a fully optimised, growing portfolio.</p>
      <div class="teal-rule"></div>
    </div>
    <div class="process-timeline" role="list">
      <div class="process-step reveal d-1" role="listitem">
        <div class="step-num" aria-hidden="true">01</div>
        <h3>Free Consultation</h3>
        <p>A no-obligation 30-minute call to understand your financial goals, current situation, and risk appetite.</p>
      </div>
      <div class="process-step reveal d-2" role="listitem">
        <div class="step-num" aria-hidden="true">02</div>
        <h3>Financial Analysis</h3>
        <p>Deep-dive assessment of your income, liabilities, existing investments, and insurance coverage.</p>
      </div>
      <div class="process-step reveal d-3" role="listitem">
        <div class="step-num" aria-hidden="true">03</div>
        <h3>Custom Strategy</h3>
        <p>A personalised financial plan covering mutual funds, insurance, and investment recommendations.</p>
      </div>
      <div class="process-step reveal d-4" role="listitem">
        <div class="step-num" aria-hidden="true">04</div>
        <h3>Ongoing Support</h3>
        <p>Regular portfolio reviews, market updates, and continuous advisory as your goals evolve.</p>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     BENEFITS
═══════════════════════════════════════ -->
<section class="benefits-section section-pad" aria-labelledby="benefits-heading">
  <div class="container">
    <div class="section-header reveal">
      <span class="section-label">The Elevate Advantage</span>
      <h2 id="benefits-heading">Why Thousands of Investors Choose Us</h2>
      <p>Every feature is designed to give you confidence, clarity, and control over your financial future.</p>
      <div class="teal-rule"></div>
    </div>
    <div class="benefits-grid" role="list">
      <div class="benefit-card reveal d-1" role="listitem">
        <div class="benefit-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <div>
          <h4>Regulatory Safety</h4>
          <p>Triple-registered with AMFI, IRDAI, and SEBI — your money is always in compliant hands.</p>
        </div>
      </div>
      <div class="benefit-card reveal d-2" role="listitem">
        <div class="benefit-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        </div>
        <div>
          <h4>Client-First Approach</h4>
          <p>Your goals come first — we never push products that don&apos;t serve your best interests.</p>
        </div>
      </div>
      <div class="benefit-card reveal d-3" role="listitem">
        <div class="benefit-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        </div>
        <div>
          <h4>Timely Reviews</h4>
          <p>Scheduled portfolio reviews to rebalance, optimise, and adapt to market changes.</p>
        </div>
      </div>
      <div class="benefit-card reveal d-4" role="listitem">
        <div class="benefit-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
        </div>
        <div>
          <h4>Data-Driven Decisions</h4>
          <p>Every recommendation backed by market research, fund analysis, and financial modelling.</p>
        </div>
      </div>
      <div class="benefit-card reveal d-5" role="listitem">
        <div class="benefit-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        </div>
        <div>
          <h4>WhatsApp Support</h4>
          <p>Direct WhatsApp access to your advisor — quick answers whenever markets move.</p>
        </div>
      </div>
      <div class="benefit-card reveal d-6" role="listitem">
        <div class="benefit-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 12h-4l-2-4-2 8-2-4H4"/></svg>
        </div>
        <div>
          <h4>Paperless Onboarding</h4>
          <p>Fast, digital onboarding — start your investment journey in minutes, not days.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     CREDENTIALS
═══════════════════════════════════════ -->
<section class="credentials-section" aria-labelledby="cred-heading">
  <div class="container">
    <div class="section-header reveal" style="margin-bottom:2rem;">
      <span class="section-label">Our Credentials</span>
      <h2 id="cred-heading" style="font-family:var(--ff-display);color:var(--c-gold-lt);">Fully Licensed &amp; Regulated</h2>
    </div>
    <div class="credentials-row" role="list">
      <div class="cred-badge reveal d-1" role="listitem">
        <div class="cred-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <div>
          <span class="cred-title">AMFI Registered</span>
          <span class="cred-sub">Mutual Fund Distributor</span>
        </div>
      </div>
      <div class="cred-badge reveal d-2" role="listitem">
        <div class="cred-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <div>
          <span class="cred-title">IRDAI Certified</span>
          <span class="cred-sub">Licensed Insurance Agent</span>
        </div>
      </div>
      <div class="cred-badge reveal d-3" role="listitem">
        <div class="cred-icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
        </div>
        <div>
          <span class="cred-title">SEBI Compliant</span>
          <span class="cred-sub">Securities &amp; Exchange Board of India</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     BRAND PARTNERS
═══════════════════════════════════════ -->
<section id="bpsec" aria-labelledby="bp-heading">
  <div class="bp-glow bp-glow-a" aria-hidden="true"></div>
  <div class="bp-glow bp-glow-b" aria-hidden="true"></div>
  <div class="bpsec-inner container">
    <div class="bphdr reveal">
      <span class="bplabel">Our Network</span>
      <h2 class="bptitle" id="bp-heading">Trusted Partner Institutions</h2>
      <p class="bpdesc">We work exclusively with India&apos;s most reputable AMCs, insurers, and platforms — giving you access to the best products in each category.</p>
      <div class="bprule"></div>
    </div>

    <!-- Tabs -->
    <div class="bp-tabs" role="tablist" aria-label="Partner categories">
      <button class="bp-tab active" data-tab="mf" role="tab" aria-selected="true" aria-controls="bpp-mf">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        Mutual Funds
      </button>
      <button class="bp-tab" data-tab="ins" role="tab" aria-selected="false" aria-controls="bpp-ins">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        Insurance
      </button>
      <button class="bp-tab" data-tab="trade" role="tab" aria-selected="false" aria-controls="bpp-trade">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        Trading
      </button>
    </div>

    <!-- Mutual Funds Panel -->
    <div class="bp-panel active" id="bpp-mf" role="tabpanel" aria-label="Mutual fund partners">
      <div class="bp-slider-outer">
        <button class="bparr bparr-prev" id="bparr-mf-prev" aria-label="Previous mutual fund partners">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>
        </button>
        <div class="bpswrap" id="bpsw-mf">
          <div class="bpstrack" id="bpst-mf">
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#1F7A8C;">SBI</div></div><p class="bpc-name">SBI Mutual Fund</p><p class="bpc-type">AMC Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#0E2A3A;">HDFC</div></div><p class="bpc-name">HDFC Mutual Fund</p><p class="bpc-type">AMC Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#1A3548;font-size:0.75rem;">ICICI</div></div><p class="bpc-name">ICICI Prudential MF</p><p class="bpc-type">AMC Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#2FB5C4;color:#071520;">NI</div></div><p class="bpc-name">Nippon India MF</p><p class="bpc-type">AMC Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#C9A84C;color:#071520;">AXIS</div></div><p class="bpc-name">Axis Mutual Fund</p><p class="bpc-type">AMC Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#0E2A3A;">KMF</div></div><p class="bpc-name">Kotak Mutual Fund</p><p class="bpc-type">AMC Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#1F7A8C;">DSP</div></div><p class="bpc-name">DSP Mutual Fund</p><p class="bpc-type">AMC Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#1A3548;font-size:0.7rem;">Mirae</div></div><p class="bpc-name">Mirae Asset MF</p><p class="bpc-type">AMC Partner</p></div></div>
          </div>
        </div>
        <button class="bparr bparr-next" id="bparr-mf-next" aria-label="Next mutual fund partners">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>
        </button>
      </div>
      <div class="bp-dots" id="bpdots-mf" role="tablist" aria-label="Slide navigation"></div>
    </div>

    <!-- Insurance Panel -->
    <div class="bp-panel" id="bpp-ins" role="tabpanel" aria-label="Insurance partners">
      <div class="bp-slider-outer">
        <button class="bparr bparr-prev" id="bparr-ins-prev" aria-label="Previous insurance partners">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>
        </button>
        <div class="bpswrap" id="bpsw-ins">
          <div class="bpstrack" id="bpst-ins">
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#1F7A8C;">LIC</div></div><p class="bpc-name">LIC of India</p><p class="bpc-type">Insurance Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#0E2A3A;font-size:0.7rem;">SBI Life</div></div><p class="bpc-name">SBI Life Insurance</p><p class="bpc-type">Insurance Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#1A3548;font-size:0.65rem;">HDFC Life</div></div><p class="bpc-name">HDFC Life Insurance</p><p class="bpc-type">Insurance Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#2FB5C4;color:#071520;font-size:0.7rem;">ICICI</div></div><p class="bpc-name">ICICI Pru Life</p><p class="bpc-type">Insurance Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#C9A84C;color:#071520;font-size:0.7rem;">Max</div></div><p class="bpc-name">Max Life Insurance</p><p class="bpc-type">Insurance Partner</p></div></div>
            <div class="bpc"><div class="bpc-body"><div class="bpc-logo"><div class="bpc-fb" style="display:flex;background:#0E2A3A;font-size:0.65rem;">Bajaj</div></div><p class="bpc-name">Bajaj Allianz Life</p><p class="bpc-type">Insurance Partner</p></div></div>
          </div>
        </div>
        <button class="bparr bparr-next" id="bparr-ins-next" aria-label="Next insurance partners">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>
        </button>
      </div>
      <div class="bp-dots" id="bpdots-ins" role="tablist" aria-label="Slide navigation"></div>
    </div>

    <!-- Trading Panel -->
    <div class="bp-panel" id="bpp-trade" role="tabpanel" aria-label="Trading partners">
      <div class="bp-trade-wrap">
        <div class="bpc bpc-solo">
          <div class="bpc-body">
            <div class="bpc-logo bpc-logo-lg"><div class="bpc-fb" style="display:flex;background:linear-gradient(135deg,#1F7A8C,#2FB5C4);font-size:0.8rem;">NSE<br>BSE</div></div>
            <p class="bpc-name">NSE &amp; BSE</p>
            <p class="bpc-type">Recognised Stock Exchanges</p>
            <span class="bpc-badge">SEBI Regulated</span>
          </div>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ═══════════════════════════════════════
     CTA BANNER
═══════════════════════════════════════ -->
<section class="cta-banner" aria-labelledby="cta-heading">
  <div class="cta-banner-inner">
    <span class="section-label" style="color:rgba(232,244,248,0.7);">Take the First Step</span>
    <h2 id="cta-heading">Ready to Elevate Your Financial Future?</h2>
    <p>Book a free 30-minute consultation with our registered financial advisors. No obligation, no jargon — just clear, expert guidance tailored to your goals.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary btn-lg">
        Book Free Consultation
        <svg class="btn-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
      </a>
      <a href="https://wa.me/919815519057" class="btn btn-ghost btn-lg" target="_blank" rel="noopener noreferrer">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.123.555 4.12 1.528 5.856L.057 23.882l6.187-1.622A11.944 11.944 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 01-5.006-1.368l-.36-.213-3.672.964.981-3.593-.234-.369A9.818 9.818 0 1112 21.818z"/></svg>
        Chat on WhatsApp
      </a>
    </div>
  </div>
</section>

{FOOTER}

<script src="js/script.js"></script>
</body>
</html>'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize(path)
content = open(path, encoding='utf-8').read()
checks = ['hero-eyebrow', 'logo-showcase', 'bpsec', 'process-timeline', 'why-section', 'navToggle', 'nav-mobile', 'btn-primary', 'credentials-section', 'benefits-grid']
ok = all(c in content for c in checks)
old_markers = ['mobile-menu-toggle', 'nav-menu', 'background-color: #ffffff', 'hero-blob']
old_found = [m for m in old_markers if m in content]
print(f"index.html written: {size} bytes")
print(f"All new markers: {'PASS' if ok else 'FAIL'}")
if old_found:
    print(f"OLD MARKERS FOUND: {old_found}")
else:
    print("No old markers: CLEAN")
