// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      })
    }
  })
})

// Header scroll effect
window.addEventListener("scroll", () => {
  const header = document.querySelector(".header")
  if (window.scrollY > 100) {
    header.style.background = "rgba(255, 255, 255, 0.98)"
    header.style.boxShadow = "0 4px 6px -1px rgb(0 0 0 / 0.1)"
  } else {
    header.style.background = "rgba(255, 255, 255, 0.95)"
    header.style.boxShadow = "none"
  }
})

// Mobile menu toggle
const mobileMenuBtn = document.querySelector(".mobile-menu-btn")
const navMenu = document.querySelector(".nav-menu")

mobileMenuBtn.addEventListener("click", () => {
  navMenu.classList.toggle("active")
  const icon = mobileMenuBtn.querySelector("i")
  if (navMenu.classList.contains("active")) {
    icon.className = "fas fa-times"
    navMenu.style.display = "flex"
    navMenu.style.position = "absolute"
    navMenu.style.top = "100%"
    navMenu.style.left = "0"
    navMenu.style.right = "0"
    navMenu.style.background = "white"
    navMenu.style.flexDirection = "column"
    navMenu.style.padding = "1rem"
    navMenu.style.boxShadow = "0 4px 6px -1px rgb(0 0 0 / 0.1)"
    navMenu.style.borderTop = "1px solid var(--border)"
  } else {
    icon.className = "fas fa-bars"
    navMenu.style.display = "none"
  }
})

// Scroll animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("animated")
    }
  })
}, observerOptions)

// Add animation classes to elements
document.addEventListener("DOMContentLoaded", () => {
  const animateElements = document.querySelectorAll(".project-card, .testimonial-card, .experience-card, .skill-badge")
  animateElements.forEach((el) => {
    el.classList.add("animate-on-scroll")
    observer.observe(el)
  })
})

// Skill badges hover effect
document.querySelectorAll(".skill-badge").forEach((badge) => {
  badge.addEventListener("mouseenter", () => {
    badge.style.transform = "translateY(-2px) scale(1.05)"
  })

  badge.addEventListener("mouseleave", () => {
    badge.style.transform = "translateY(0) scale(1)"
  })
})

// Project cards tilt effect
document.querySelectorAll(".project-card").forEach((card) => {
  card.addEventListener("mouseenter", (e) => {
    const rect = card.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top

    const centerX = rect.width / 2
    const centerY = rect.height / 2

    const rotateX = (y - centerY) / 20
    const rotateY = (centerX - x) / 20

    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`
  })

  card.addEventListener("mouseleave", () => {
    card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)"
  })
})
  const cards = document.querySelectorAll('.testimonial-card');

  cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.classList.add('bouncing');
      card.addEventListener('animationend', () => {
        card.classList.remove('bouncing');
      }, { once: true });
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
  const images = document.querySelectorAll('.profile-image');
  let current = 0;

  setInterval(() => {
    images[current].classList.remove('active');
    current = (current + 1) % images.length;
    images[current].classList.add('active');
  }, 3000);
});

// Typing effect for hero code snippet
const codeSnippet = document.querySelector(".code-snippet span")
const originalText = codeSnippet.textContent
let i = 0

function typeWriter() {
  if (i < originalText.length) {
    codeSnippet.textContent = originalText.substring(0, i + 1) + "|"
    i++
    setTimeout(typeWriter, 100)
  } else {
    codeSnippet.textContent = originalText
    setTimeout(() => {
      i = 0
      codeSnippet.textContent = ""
      typeWriter()
    }, 3000)
  }
}

// Start typing effect after page load
window.addEventListener("load", () => {
  setTimeout(typeWriter, 1000)
})

// Active navigation link highlighting
window.addEventListener("scroll", () => {
  const sections = document.querySelectorAll("section[id]")
  const navLinks = document.querySelectorAll(".nav-link")

  let current = ""
  sections.forEach((section) => {
    const sectionTop = section.offsetTop
    const sectionHeight = section.clientHeight
    if (scrollY >= sectionTop - 200) {
      current = section.getAttribute("id")
    }
  })

  navLinks.forEach((link) => {
    link.classList.remove("active")
    if (link.getAttribute("href") === `#${current}`) {
      link.classList.add("active")
    }
  })
})

// Add active class styles
const style = document.createElement("style")
style.textContent = `
    .nav-link.active {
        color: var(--primary) !important;
    }
    .nav-link.active::after {
        width: 100% !important;
    }
`
document.head.appendChild(style)

// Button click effects
document.querySelectorAll(".btn").forEach((btn) => {
  btn.addEventListener("click", function (e) {
    const ripple = document.createElement("span")
    const rect = this.getBoundingClientRect()
    const size = Math.max(rect.width, rect.height)
    const x = e.clientX - rect.left - size / 2
    const y = e.clientY - rect.top - size / 2

    ripple.style.width = ripple.style.height = size + "px"
    ripple.style.left = x + "px"
    ripple.style.top = y + "px"
    ripple.classList.add("ripple")

    this.appendChild(ripple)

    setTimeout(() => {
      ripple.remove()
    }, 600)
  })
})

// Add ripple effect styles
const rippleStyle = document.createElement("style")
rippleStyle.textContent = `
    .btn {
        position: relative;
        overflow: hidden;
    }
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`
document.head.appendChild(rippleStyle)

// Parallax effect for hero section
window.addEventListener("scroll", () => {
  const scrolled = window.pageYOffset
  const heroImage = document.querySelector(".hero-image")
  if (heroImage) {
    heroImage.style.transform = `translateY(${scrolled * 0.1}px)`
  }
})

// Console easter egg
console.log(`
    ██████╗ ███████╗██╗   ██╗██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ ██╗     ██╗ ██████╗ 
    ██╔══██╗██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗██║     ██║██╔═══██╗
    ██║  ██║█████╗  ██║   ██║██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██║   ██║██║     ██║██║   ██║
    ██║  ██║██╔══╝  ╚██╗ ██╔╝██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██║   ██║██║     ██║██║   ██║
    ██████╔╝███████╗ ╚████╔╝ ██║     ╚██████╔╝██║  ██║   ██║   ██║     ╚██████╔╝███████╗██║╚██████╔╝
    ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚═╝ ╚═════╝ 
    
    🚀 Olá! Vejo que você é curioso sobre código!
    💻 Este portfólio foi desenvolvido com HTML, CSS e JavaScript vanilla
    ⚡ Quer conversar sobre desenvolvimento? Entre em contato!
    
    Dica: Digite 'portfolio.info()' no console para mais informações!
`)

// Console commands
window.portfolio = {
    info: () => {
        console.log(`
        📊 Informações do Portfólio:
        ━━━━━━━━━━━━━━━
        `);
    }
}
