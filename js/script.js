// Mobile Menu Toggle
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuBtn) {
  mobileMenuBtn.addEventListener('click', () => {
    const isActive = navLinks.classList.toggle('active');
    mobileMenuBtn.textContent = isActive ? '✕' : '☰';
    mobileMenuBtn.setAttribute('aria-expanded', isActive ? 'true' : 'false');
  });
}

// Navbar Scroll Effect
const navbar = document.querySelector('nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 20) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Form Handling
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;

    // Simulate form submission
    setTimeout(() => {
      const formData = new FormData(contactForm);
      const data = Object.fromEntries(formData);
      
      console.log('Form submitted:', data);
      
      // Show success message
      const successMessage = document.getElementById('successMessage');
      if (successMessage) {
        successMessage.style.display = 'block';
        contactForm.style.display = 'none';
        
        // Reset after 3 seconds
        setTimeout(() => {
          contactForm.style.display = 'block';
          successMessage.style.display = 'none';
          contactForm.reset();
          submitBtn.textContent = originalText;
          submitBtn.disabled = false;
        }, 3000);
      } else {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
        alert('Thank you! We will get back to you within 24 hours.');
        contactForm.reset();
      }
    }, 1000);
  });
}

// Intersection Observer for fade-in animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.animate-on-scroll').forEach(element => {
  element.style.opacity = '0';
  element.style.transform = 'translateY(20px)';
  element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(element);
});

// Close mobile menu when link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('active');
    if (mobileMenuBtn) {
      mobileMenuBtn.textContent = '☰';
      mobileMenuBtn.setAttribute('aria-expanded', 'false');
    }
  });
});

// WhatsApp button
const whatsappBtn = document.querySelector('[href^="https://wa.me/"]');
if (whatsappBtn) {
  whatsappBtn.target = '_blank';
  whatsappBtn.rel = 'noopener noreferrer';
}

// Phone and email click handlers
document.querySelectorAll('a[href^="tel:"]').forEach(link => {
  link.addEventListener('click', function(e) {
    // Allow default behavior for phone links
  });
});

document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
  link.addEventListener('click', function(e) {
    // Allow default behavior for email links
  });
});
