<template>
  <div class="home">
    <div class="bg-grid"></div>
    <div class="bg-glow"></div>

    <header class="navbar">
      <div class="logo">
        <span class="logo-icon">⬡</span>
        <span class="logo-text">CNN<span class="logo-accent">MLOps</span></span>
      </div>
      <nav class="nav-links">
        <router-link to="/" class="nav-link active">Home</router-link>
        <router-link to="/predict" class="nav-link">Predict</router-link>
        <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
      </nav>
    </header>

    <main class="hero">
      <div class="badge">Academic Research Project · 2026</div>

      <h1 class="hero-title">
        Deep Learning<br/>
        <span class="gradient-text">Cat vs Dog</span><br/>
        Classification
      </h1>

      <p class="hero-desc">
        A Convolutional Neural Network (CNN) trained and deployed using modern MLOps practices.
        Upload an image and get real-time predictions with confidence scores powered by TensorFlow
        and served via a FastAPI backend.
      </p>

      <div class="tech-pills">
        <span class="pill">TensorFlow</span>
        <span class="pill">FastAPI</span>
        <span class="pill">Vue.js</span>
        <span class="pill">CNN</span>
        <span class="pill">MLOps</span>
      </div>

      <div class="cta-group">
        <router-link to="/predict" class="btn-primary">
          <span class="btn-icon">🔍</span>
          Try Prediction
          <span class="btn-arrow">→</span>
        </router-link>
        <router-link to="/dashboard" class="btn-secondary">
          <span class="btn-icon">📊</span>
          View Dashboard
        </router-link>
      </div>

      <div class="stats-row">
        <div class="stat-card">
          <div class="stat-number">CNN</div>
          <div class="stat-label">Architecture</div>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-card">
          <div class="stat-number">2</div>
          <div class="stat-label">Classes</div>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-card">
          <div class="stat-number">RT</div>
          <div class="stat-label">Inference</div>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-card">
          <div class="stat-number">REST</div>
          <div class="stat-label">API</div>
        </div>
      </div>
    </main>

    <div class="floating-card card-left">
      <div class="fc-icon">🐱</div>
      <div class="fc-text">Cat detected</div>
      <div class="fc-conf">98.2% confidence</div>
    </div>

    <div class="floating-card card-right">
      <div class="fc-icon">🐶</div>
      <div class="fc-text">Dog detected</div>
      <div class="fc-conf">94.7% confidence</div>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

.home {
  min-height: 100vh;
  background: #020917;
  font-family: 'DM Sans', sans-serif;
  color: #e8f0fe;
  overflow: hidden;
  position: relative;
}

.bg-grid {
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(59,130,246,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(59,130,246,0.06) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
}

.bg-glow {
  position: fixed;
  top: -200px;
  left: 50%;
  transform: translateX(-50%);
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, rgba(37,99,235,0.18) 0%, transparent 70%);
  pointer-events: none;
}

/* NAVBAR */
.navbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.2rem 3rem;
  background: rgba(2,9,23,0.8);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(59,130,246,0.15);
  z-index: 100;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 1.3rem;
  color: #fff;
}

.logo-icon {
  font-size: 1.5rem;
  color: #3b82f6;
}

.logo-accent { color: #3b82f6; }

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9rem;
  color: rgba(232,240,254,0.6);
  text-decoration: none;
  letter-spacing: 0.05em;
  transition: color 0.2s;
}

.nav-link:hover, .nav-link.active {
  color: #60a5fa;
}

/* HERO */
.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 10rem 2rem 5rem;
  position: relative;
  z-index: 1;
}

.badge {
  display: inline-block;
  padding: 0.4rem 1.2rem;
  background: rgba(59,130,246,0.12);
  border: 1px solid rgba(59,130,246,0.3);
  border-radius: 100px;
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: #93c5fd;
  margin-bottom: 2rem;
  text-transform: uppercase;
}

.hero-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2.8rem, 6vw, 5rem);
  font-weight: 800;
  line-height: 1.1;
  color: #fff;
  margin-bottom: 1.8rem;
  letter-spacing: -0.02em;
}

.gradient-text {
  background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 50%, #93c5fd 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-desc {
  max-width: 600px;
  font-size: 1.05rem;
  line-height: 1.75;
  color: rgba(232,240,254,0.65);
  margin-bottom: 2rem;
  font-weight: 300;
}

.tech-pills {
  display: flex;
  gap: 0.6rem;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 2.8rem;
}

.pill {
  padding: 0.35rem 1rem;
  background: rgba(59,130,246,0.08);
  border: 1px solid rgba(59,130,246,0.2);
  border-radius: 100px;
  font-size: 0.8rem;
  color: #93c5fd;
  letter-spacing: 0.04em;
}

/* BUTTONS */
.cta-group {
  display: flex;
  gap: 1rem;
  margin-bottom: 4rem;
  flex-wrap: wrap;
  justify-content: center;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.9rem 2rem;
  background: linear-gradient(135deg, #1d4ed8, #3b82f6);
  color: #fff;
  border-radius: 12px;
  text-decoration: none;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 1rem;
  box-shadow: 0 0 30px rgba(59,130,246,0.35);
  transition: all 0.25s;
  position: relative;
  overflow: hidden;
}

.btn-primary::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #2563eb, #60a5fa);
  opacity: 0;
  transition: opacity 0.25s;
}

.btn-primary:hover::before { opacity: 1; }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 0 45px rgba(59,130,246,0.5); }

.btn-primary span { position: relative; z-index: 1; }
.btn-arrow { font-size: 1.1rem; transition: transform 0.2s; }
.btn-primary:hover .btn-arrow { transform: translateX(4px); }

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.9rem 2rem;
  background: rgba(59,130,246,0.08);
  border: 1px solid rgba(59,130,246,0.3);
  color: #93c5fd;
  border-radius: 12px;
  text-decoration: none;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 1rem;
  transition: all 0.25s;
}

.btn-secondary:hover {
  background: rgba(59,130,246,0.15);
  border-color: rgba(59,130,246,0.5);
  transform: translateY(-2px);
}

/* STATS */
.stats-row {
  display: flex;
  align-items: center;
  gap: 0;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(59,130,246,0.12);
  border-radius: 16px;
  padding: 1.5rem 2.5rem;
}

.stat-card {
  text-align: center;
  padding: 0 2rem;
}

.stat-number {
  font-family: 'Syne', sans-serif;
  font-size: 1.6rem;
  font-weight: 800;
  color: #60a5fa;
  letter-spacing: -0.02em;
}

.stat-label {
  font-size: 0.75rem;
  color: rgba(232,240,254,0.45);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-top: 0.2rem;
}

.stat-divider {
  width: 1px;
  height: 40px;
  background: rgba(59,130,246,0.15);
}

/* FLOATING CARDS */
.floating-card {
  position: fixed;
  background: rgba(10,25,50,0.85);
  border: 1px solid rgba(59,130,246,0.2);
  border-radius: 14px;
  padding: 1rem 1.3rem;
  backdrop-filter: blur(12px);
  animation: float 4s ease-in-out infinite;
}

.card-left {
  left: 3%;
  top: 40%;
  animation-delay: 0s;
}

.card-right {
  right: 3%;
  top: 55%;
  animation-delay: 2s;
}

.fc-icon { font-size: 1.8rem; margin-bottom: 0.3rem; }
.fc-text { font-size: 0.85rem; font-weight: 500; color: #e8f0fe; }
.fc-conf { font-size: 0.75rem; color: #60a5fa; margin-top: 0.2rem; }

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12px); }
}

@media (max-width: 768px) {
  .navbar { padding: 1rem 1.5rem; }
  .floating-card { display: none; }
  .stats-row { flex-wrap: wrap; justify-content: center; }
}
</style>