import os
path = r'c:\Users\itxul\Desktop\ElevateWealthServices\js\script.js'
js = r"""/* ═══════════════════════════════════════════════════════
   ELEVATE WEALTH SERVICES — script.js v2.0
   Dark Luxury Fintech Theme
═══════════════════════════════════════════════════════ */

'use strict';

/* ─── NAV SCROLL ─── */
(function () {
  var nav = document.getElementById('nav');
  if (!nav) return;
  function onScroll() {
    if (window.scrollY > 60) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

/* ─── ACTIVE NAV LINK ─── */
(function () {
  var path = window.location.pathname.split('/').pop() || 'index.html';
  var links = document.querySelectorAll('.nav-links a, .nav-mobile a');
  links.forEach(function (a) {
    if (a.getAttribute('href') === path) a.classList.add('nav-active');
  });
})();

/* ─── MOBILE NAV ─── */
(function () {
  var toggle = document.getElementById('navToggle');
  var mobile = document.getElementById('navMobile');
  var close  = document.getElementById('navMobileClose');
  if (!toggle || !mobile) return;

  function openMenu() {
    mobile.classList.add('open');
    document.body.style.overflow = 'hidden';
    toggle.setAttribute('aria-expanded', 'true');
  }
  function closeMenu() {
    mobile.classList.remove('open');
    document.body.style.overflow = '';
    toggle.setAttribute('aria-expanded', 'false');
  }

  toggle.addEventListener('click', openMenu);
  if (close) close.addEventListener('click', closeMenu);
  mobile.addEventListener('click', function (e) {
    if (e.target === mobile) closeMenu();
  });
  mobile.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', closeMenu);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
  });
})();

/* ─── REVEAL OBSERVER ─── */
(function () {
  var els = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
  if (!els.length) return;
  if (!window.IntersectionObserver) {
    els.forEach(function (el) { el.classList.add('revealed'); });
    return;
  }
  var revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -48px 0px' });

  els.forEach(function (el) { revealObserver.observe(el); });
})();

/* ─── COUNTER ANIMATION ─── */
(function () {
  function easeOutQuart(t) { return 1 - Math.pow(1 - t, 4); }

  function animateCounter(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var prefix = el.getAttribute('data-prefix') || '';
    var decimals = (String(target).split('.')[1] || '').length;
    var duration = 1800;
    var start = null;

    function step(ts) {
      if (!start) start = ts;
      var elapsed = ts - start;
      var progress = Math.min(elapsed / duration, 1);
      var val = easeOutQuart(progress) * target;
      el.textContent = prefix + val.toFixed(decimals) + suffix;
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = prefix + target.toFixed(decimals) + suffix;
    }
    requestAnimationFrame(step);
  }

  var counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;
  if (!window.IntersectionObserver) {
    counters.forEach(animateCounter);
    return;
  }
  var counterObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(function (el) { counterObserver.observe(el); });
})();

/* ─── RIPPLE EFFECT ─── */
(function () {
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.btn-primary');
    if (!btn) return;
    var rect = btn.getBoundingClientRect();
    var size = Math.max(rect.width, rect.height);
    var x = e.clientX - rect.left - size / 2;
    var y = e.clientY - rect.top - size / 2;
    var ripple = document.createElement('span');
    ripple.className = 'ripple';
    ripple.style.cssText = 'width:' + size + 'px;height:' + size + 'px;left:' + x + 'px;top:' + y + 'px';
    btn.appendChild(ripple);
    ripple.addEventListener('animationend', function () { ripple.remove(); });
  });
})();

/* ─── CONTACT FORM ─── */
(function () {
  var form = document.getElementById('contactForm');
  if (!form) return;

  var fields = {
    name:    { el: document.getElementById('name'),    err: document.getElementById('nameError'),    msg: 'Please enter your full name.' },
    phone:   { el: document.getElementById('phone'),   err: document.getElementById('phoneError'),   msg: 'Please enter a valid 10-digit phone number.' },
    service: { el: document.getElementById('service'), err: document.getElementById('serviceError'), msg: 'Please select a service.' }
  };

  function setError(f, show) {
    if (!f.el || !f.err) return;
    if (show) {
      f.el.style.borderColor = '#ef5350';
      f.err.textContent = f.msg;
    } else {
      f.el.style.borderColor = '';
      f.err.textContent = '';
    }
  }

  function validate() {
    var ok = true;
    var f;

    f = fields.name;
    var nameVal = f.el ? f.el.value.trim() : '';
    if (!nameVal || nameVal.length < 2) { setError(f, true); ok = false; } else { setError(f, false); }

    f = fields.phone;
    var phoneVal = f.el ? f.el.value.trim().replace(/\s+/g, '') : '';
    if (!phoneVal || !/^[6-9]\d{9}$/.test(phoneVal)) { setError(f, true); ok = false; } else { setError(f, false); }

    f = fields.service;
    var svcVal = f.el ? f.el.value : '';
    if (!svcVal) { setError(f, true); ok = false; } else { setError(f, false); }

    return ok;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!validate()) return;

    var nameEl    = document.getElementById('name');
    var phoneEl   = document.getElementById('phone');
    var emailEl   = document.getElementById('email');
    var serviceEl = document.getElementById('service');
    var msgEl     = document.getElementById('message');

    var serviceLabels = {
      'mutual-funds': 'Mutual Fund Advisory',
      'insurance':    'Insurance Solutions',
      'trading':      'Trading & Investing',
      'all':          'All Services / General Consultation'
    };

    var name    = nameEl    ? nameEl.value.trim()    : '';
    var phone   = phoneEl   ? phoneEl.value.trim()   : '';
    var email   = emailEl   ? emailEl.value.trim()   : 'Not provided';
    var service = serviceEl ? (serviceLabels[serviceEl.value] || serviceEl.value) : '';
    var message = msgEl     ? msgEl.value.trim()     : 'No additional message';

    var text = [
      'Hello Elevate Wealth Services,',
      '',
      'I would like to book a free consultation. Details below:',
      '',
      'Name: '    + name,
      'Phone: '   + phone,
      'Email: '   + email,
      'Service: ' + service,
      'Message: ' + message,
      '',
      'Please contact me at your earliest convenience.',
      'Thank you.'
    ].join('\n');

    var url = 'https://wa.me/919815519057?text=' + encodeURIComponent(text);
    window.open(url, '_blank', 'noopener,noreferrer');
  });

  /* live validation on blur */
  Object.values(fields).forEach(function (f) {
    if (f.el) f.el.addEventListener('blur', function () { validate(); });
  });
})();

/* ─── BRAND PARTNERS SLIDER ─── */
(function () {
  function getVis() {
    return window.innerWidth >= 1024 ? 4 : window.innerWidth >= 640 ? 2 : 1;
  }

  function BPSlider(trackId, wrapId, prevId, nextId, dotsId) {
    var track  = document.getElementById(trackId);
    var wrap   = document.getElementById(wrapId);
    var prevBtn = document.getElementById(prevId);
    var nextBtn = document.getElementById(nextId);
    var dotsEl = document.getElementById(dotsId);
    if (!track || !wrap) return;

    var idx   = 0;
    var timer = null;
    var total = track.children.length;

    function maxIdx() { return Math.max(0, total - getVis()); }

    function buildDots() {
      if (!dotsEl) return;
      dotsEl.innerHTML = '';
      var count = maxIdx() + 1;
      for (var i = 0; i < count; i++) {
        var d = document.createElement('button');
        d.className = 'bp-dot' + (i === idx ? ' active' : '');
        d.setAttribute('aria-label', 'Slide ' + (i + 1));
        (function (n) {
          d.addEventListener('click', function () { go(n); resetTimer(); });
        })(i);
        dotsEl.appendChild(d);
      }
    }

    function update() {
      var vis  = getVis();
      var cardW = wrap.offsetWidth / vis;
      var offset = -(idx * cardW);
      track.style.transform = 'translateX(' + offset + 'px)';
      if (dotsEl) {
        dotsEl.querySelectorAll('.bp-dot').forEach(function (d, i) {
          d.classList.toggle('active', i === idx);
        });
      }
      if (prevBtn) prevBtn.disabled = idx === 0;
      if (nextBtn) nextBtn.disabled = idx >= maxIdx();
    }

    function go(n) {
      idx = Math.max(0, Math.min(n, maxIdx()));
      update();
    }

    function next() { go(idx < maxIdx() ? idx + 1 : 0); }
    function prev() { go(idx > 0 ? idx - 1 : maxIdx()); }

    function resetTimer() {
      clearInterval(timer);
      timer = setInterval(next, 4200);
    }

    if (nextBtn) nextBtn.addEventListener('click', function () { next(); resetTimer(); });
    if (prevBtn) prevBtn.addEventListener('click', function () { prev(); resetTimer(); });

    buildDots();
    update();
    resetTimer();

    window.addEventListener('resize', function () {
      buildDots();
      go(Math.min(idx, maxIdx()));
    }, { passive: true });
  }

  /* Mutual Funds slider */
  BPSlider('bpst-mf',  'bpsw-mf',  'bparr-mf-prev',  'bparr-mf-next',  'bpdots-mf');
  /* Insurance slider */
  BPSlider('bpst-ins', 'bpsw-ins', 'bparr-ins-prev', 'bparr-ins-next', 'bpdots-ins');
})();

/* ─── BRAND PARTNER TABS ─── */
(function () {
  var tabs   = document.querySelectorAll('.bp-tab');
  var panels = document.querySelectorAll('.bp-panel');
  if (!tabs.length) return;

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      var target = tab.getAttribute('data-tab');
      tabs.forEach(function (t) { t.classList.remove('active'); });
      panels.forEach(function (p) { p.classList.remove('active'); });
      tab.classList.add('active');
      var panel = document.getElementById('bpp-' + target);
      if (panel) panel.classList.add('active');
    });
  });
})();

/* ─── EXTERNAL LINK SAFETY ─── */
(function () {
  document.querySelectorAll('a[href^="https://wa.me"], a[href^="tel:"], a[href^="mailto:"]').forEach(function (a) {
    if (a.getAttribute('href').startsWith('https://')) {
      a.setAttribute('rel', 'noopener noreferrer');
      if (!a.getAttribute('target')) a.setAttribute('target', '_blank');
    }
  });
})();
"""
with open(path, 'w', encoding='utf-8') as f:
    f.write(js)
size = os.path.getsize(path)
print(f"JS written: {size} bytes")
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
checks = ['IntersectionObserver', 'revealObserver', 'BPSlider', 'wa.me', 'animateCounter', 'rippleAnim', 'navToggle']
for c in checks:
    print(f"  {c}: {'FOUND' if c in content else 'MISSING'}")
