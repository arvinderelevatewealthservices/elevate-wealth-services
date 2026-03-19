import os

path = r'c:\Users\itxul\Desktop\ElevateWealthServices\services.html'

NAV = '''<!-- NAVIGATION -->
<nav class="nav" id="nav" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo" aria-label="Elevate Wealth Services — Home">
      <img src="images/ElevateWealthServicesLogo.png" alt="Elevate Wealth Services">
    </a>
    <ul class="nav-links" role="menubar">
      <li role="none"><a href="index.html" role="menuitem">Home</a></li>
      <li role="none"><a href="about.html" role="menuitem">About</a></li>
      <li role="none"><a href="services.html" class="nav-active" role="menuitem">Services</a></li>
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
  <title>Services &mdash; Elevate Wealth Services</title>
  <meta name="description" content="Explore Elevate Wealth Services — AMFI Registered Mutual Fund Advisory, IRDAI Certified Insurance Solutions, and SEBI Compliant Trading &amp; Investing in Amritsar.">
  <meta property="og:title" content="Services — Elevate Wealth Services">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

{NAV}

<!-- ═══════════════════════════════════════
     PAGE HERO
═══════════════════════════════════════ -->
<section class="page-hero" aria-labelledby="page-hero-heading">
  <div class="page-hero-bg" aria-hidden="true">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
  </div>
  <div class="page-hero-inner reveal">
    <span class="section-label">Our Services</span>
    <h1 id="page-hero-heading">Expert Solutions for Every <span class="gradient-text">Financial Goal</span></h1>
    <p>Whether you&apos;re growing wealth through mutual funds, protecting your family with insurance, or building a trading portfolio — we have the expertise, licences, and partnerships to guide you.</p>
    <div class="page-hero-links" role="list" aria-label="Jump to service sections">
      <a href="#mutual-funds" class="chip" role="listitem">Mutual Funds</a>
      <a href="#insurance" class="chip" role="listitem">Insurance</a>
      <a href="#trading" class="chip" role="listitem">Trading &amp; Investing</a>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     MUTUAL FUNDS
═══════════════════════════════════════ -->
<section id="mutual-funds" class="service-deep section-pad" aria-labelledby="mf-heading">
  <div class="container">
    <div class="service-deep-grid">

      <div class="service-deep-text">
        <span class="service-deep-label reveal">AMFI Registered</span>
        <h2 id="mf-heading" class="reveal">Mutual Fund Advisory</h2>
        <p class="reveal">We help you build a goal-based, diversified mutual fund portfolio aligned with your risk tolerance, time horizon, and return expectations. As AMFI Registered distributors, every recommendation is transparent, compliant, and in your best interest.</p>
        <p class="reveal">Whether you&apos;re investing for retirement, your child&apos;s education, a home purchase, or tax savings under Section 80C — our advisors create personalised SIP plans that work consistently toward your objectives.</p>
        <div class="service-deep-feats reveal">
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </div>
            <span>SIP &amp; Lump Sum Planning</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
            <span>Risk Profiling</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            </div>
            <span>Equity &amp; Hybrid Funds</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/></svg>
            </div>
            <span>ELSS Tax Saving</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
            </div>
            <span>Dedicated Advisor</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            </div>
            <span>Regular Portfolio Reviews</span>
          </div>
        </div>
        <a href="contact.html" class="btn btn-primary" style="margin-top:1.5rem;">
          Start Investing Today
          <svg class="btn-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
      </div>

      <div class="service-deep-visual">
        <div class="sdv-card reveal">
          <span class="sdv-label">Partner AMCs</span>
          <h3>20+ Leading Mutual Fund Houses</h3>
          <p>We partner with India&apos;s top Asset Management Companies to give you access to a broad universe of funds across all categories and risk levels.</p>
          <div class="sdv-stats" role="list">
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">500+</span>
              <span class="sdv-stat-lbl">Happy Investors</span>
            </div>
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">20+</span>
              <span class="sdv-stat-lbl">Partner AMCs</span>
            </div>
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">SIP</span>
              <span class="sdv-stat-lbl">From &#8377;500/mo</span>
            </div>
          </div>
          <div class="sdv-partners" aria-label="Mutual fund partner logos">
            <span class="sdv-partner-chip">SBI MF</span>
            <span class="sdv-partner-chip">HDFC MF</span>
            <span class="sdv-partner-chip">ICICI Pru</span>
            <span class="sdv-partner-chip">Nippon</span>
            <span class="sdv-partner-chip">Axis MF</span>
            <span class="sdv-partner-chip">Kotak MF</span>
            <span class="sdv-partner-chip">DSP MF</span>
            <span class="sdv-partner-chip">Mirae</span>
          </div>
          <a href="contact.html" class="btn btn-ghost" style="width:100%;justify-content:center;margin-top:1rem;">Book a Free MF Consultation</a>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     INSURANCE
═══════════════════════════════════════ -->
<section id="insurance" class="service-deep-alt section-pad" aria-labelledby="ins-heading">
  <div class="container">
    <div class="service-deep-grid flip">

      <div class="service-deep-visual">
        <div class="sdv-card reveal">
          <span class="sdv-label">IRDAI Certified</span>
          <h3>Protect What Matters Most</h3>
          <p>From term plans to ULIPs and health insurance — we analyse your coverage gaps and recommend plans from India&apos;s most trusted insurers.</p>
          <div class="sdv-stats" role="list">
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">6+</span>
              <span class="sdv-stat-lbl">Insurance Partners</span>
            </div>
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">100%</span>
              <span class="sdv-stat-lbl">Claims Support</span>
            </div>
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">Life</span>
              <span class="sdv-stat-lbl">&amp; Health Cover</span>
            </div>
          </div>
          <div class="sdv-partners" aria-label="Insurance partner logos">
            <span class="sdv-partner-chip">LIC</span>
            <span class="sdv-partner-chip">SBI Life</span>
            <span class="sdv-partner-chip">HDFC Life</span>
            <span class="sdv-partner-chip">ICICI Pru</span>
            <span class="sdv-partner-chip">Max Life</span>
            <span class="sdv-partner-chip">Bajaj Allianz</span>
          </div>
          <a href="contact.html" class="btn btn-ghost" style="width:100%;justify-content:center;margin-top:1rem;">Get Insurance Quote</a>
        </div>
      </div>

      <div class="service-deep-text">
        <span class="service-deep-label reveal">IRDAI Certified Agent</span>
        <h2 id="ins-heading" class="reveal">Insurance Solutions</h2>
        <p class="reveal">Life is unpredictable. The right insurance plan ensures your family and financial goals are protected no matter what. As an IRDAI licensed agent, we provide unbiased advice across all leading insurers to find the best fit for your situation.</p>
        <p class="reveal">We guide you through every step — from selecting the ideal coverage amount and policy term, to claims assistance when you need it most. Our goal is to ensure no insurance gap in your financial plan.</p>
        <div class="service-deep-feats reveal">
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <span>Term Life Insurance</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </div>
            <span>Health &amp; Critical Illness</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            </div>
            <span>ULIPs &amp; Endowment Plans</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            </div>
            <span>Pension &amp; Retirement Plans</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            </div>
            <span>Claims Assistance</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
            <span>Unbiased Multi-Insurer Advice</span>
          </div>
        </div>
        <a href="contact.html" class="btn btn-primary" style="margin-top:1.5rem;">
          Review My Coverage
          <svg class="btn-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
      </div>

    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════
     TRADING & INVESTING
═══════════════════════════════════════ -->
<section id="trading" class="service-deep section-pad" aria-labelledby="trade-heading">
  <div class="container">
    <div class="service-deep-grid">

      <div class="service-deep-text">
        <span class="service-deep-label reveal">SEBI Compliant</span>
        <h2 id="trade-heading" class="reveal">Trading &amp; Investing</h2>
        <p class="reveal">Equity markets offer significant wealth creation potential for those who approach them with discipline, knowledge, and a clear strategy. We provide SEBI compliant advisory on equities, derivatives, IPOs, and long-term investment portfolios.</p>
        <p class="reveal">Our advisors combine fundamental and technical analysis to identify opportunities while managing risk through diversification, position sizing, and stop-loss discipline — helping you navigate markets with confidence.</p>
        <div class="service-deep-feats reveal">
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </div>
            <span>Equity Advisory</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            </div>
            <span>Technical &amp; Fundamental Analysis</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/></svg>
            </div>
            <span>Portfolio Diversification</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
            <span>IPO &amp; NFO Application</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <span>Risk Management</span>
          </div>
          <div class="service-feat-card">
            <div class="sfc-icon" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            </div>
            <span>Market Reports &amp; Updates</span>
          </div>
        </div>
        <a href="contact.html" class="btn btn-primary" style="margin-top:1.5rem;">
          Start Your Trading Journey
          <svg class="btn-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
      </div>

      <div class="service-deep-visual">
        <div class="sdv-card sdv-card-alt reveal">
          <div class="sdv-shield" aria-hidden="true">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <span class="sdv-label">SEBI Compliant</span>
          <h3>NSE &amp; BSE Regulated Trading</h3>
          <p>Our trading advisory covers NSE and BSE listed equities, F&amp;O segments, and CDSL depository services — all within a fully SEBI regulated framework.</p>
          <div class="sdv-stats" role="list">
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">NSE</span>
              <span class="sdv-stat-lbl">National Stock Exch.</span>
            </div>
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">BSE</span>
              <span class="sdv-stat-lbl">Bombay Stock Exch.</span>
            </div>
            <div class="sdv-stat" role="listitem">
              <span class="sdv-stat-num gradient-text">CDSL</span>
              <span class="sdv-stat-lbl">Depository Services</span>
            </div>
          </div>
          <div class="sdv-disclaimer" aria-label="Risk disclosure">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <p>Equity investments are subject to market risks. Please invest responsibly.</p>
          </div>
          <a href="contact.html" class="btn btn-ghost" style="width:100%;justify-content:center;margin-top:1rem;">Get Trading Advisory</a>
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
checks = ['service-deep', 'sdv-card', 'service-feat-card', 'sdv-partner-chip', 'navToggle', 'nav-mobile', 'flip', 'sdv-card-alt', 'service-deep-alt', 'mutual-funds', 'insurance', 'trading']
ok = all(c in content for c in checks)
old_markers = ['mobile-menu-toggle', 'nav-menu', 'background-color: #ffffff', 'hero-blob']
old_found = [m for m in old_markers if m in content]
print(f"services.html written: {size} bytes")
print(f"All new markers: {'PASS' if ok else 'FAIL'}")
if old_found:
    print(f"OLD MARKERS FOUND: {old_found}")
else:
    print("No old markers: CLEAN")
