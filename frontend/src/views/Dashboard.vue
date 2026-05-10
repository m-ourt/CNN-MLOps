<template>
  <div class="page">
    <div class="bg-grid"></div>
    <div class="bg-glow"></div>

    <header class="navbar">
      <div class="logo">
        <span class="logo-icon">⬡</span>
        <span class="logo-text">CNN<span class="logo-accent">MLOps</span></span>
      </div>
      <nav class="nav-links">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/predict" class="nav-link">Predict</router-link>
        <router-link to="/dashboard" class="nav-link active">Dashboard</router-link>
      </nav>
    </header>

    <main class="content">
      <div class="page-header">
        <div class="badge">Model Metrics</div>
        <h1 class="page-title">Training <span class="gradient-text">Dashboard</span></h1>
        <p class="page-desc">CNN model performance metrics after training on the Cat vs Dog dataset.</p>
      </div>

      <div v-if="loading" class="loading-state">
        <div class="pulse-ring"></div>
        <p>Loading metrics from backend...</p>
      </div>

      <div v-else>
        <!-- Metric Cards -->
        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-icon">🎯</div>
            <div class="metric-info">
              <div class="metric-label">Accuracy</div>
              <div class="metric-value">{{ formatPct(metrics.accuracy) }}</div>
            </div>
            <div class="metric-bar-wrap">
              <div class="metric-bar" :style="{ width: pct(metrics.accuracy) }"></div>
            </div>
          </div>

          <div class="metric-card highlight">
            <div class="metric-icon">✅</div>
            <div class="metric-info">
              <div class="metric-label">Val Accuracy</div>
              <div class="metric-value accent">{{ formatPct(metrics.val_accuracy) }}</div>
            </div>
            <div class="metric-bar-wrap">
              <div class="metric-bar accent-bar" :style="{ width: pct(metrics.val_accuracy) }"></div>
            </div>
          </div>

          <div class="metric-card">
            <div class="metric-icon">📉</div>
            <div class="metric-info">
              <div class="metric-label">Loss</div>
              <div class="metric-value warn">{{ formatNum(metrics.loss) }}</div>
            </div>
            <div class="metric-bar-wrap">
              <div class="metric-bar warn-bar" :style="{ width: pct(metrics.loss, 2) }"></div>
            </div>
          </div>

          <div class="metric-card">
            <div class="metric-icon">📊</div>
            <div class="metric-info">
              <div class="metric-label">Val Loss</div>
              <div class="metric-value warn">{{ formatNum(metrics.val_loss) }}</div>
            </div>
            <div class="metric-bar-wrap">
              <div class="metric-bar warn-bar" :style="{ width: pct(metrics.val_loss, 2) }"></div>
            </div>
          </div>
        </div>

        <!-- Summary -->
        <div class="summary-card">
          <div class="summary-header">
            <h2 class="summary-title">Model Summary</h2>
            <span class="status-badge">✓ Trained</span>
          </div>
          <div class="summary-grid">
            <div class="summary-item">
              <span class="s-label">Architecture</span>
              <span class="s-val">Convolutional Neural Network</span>
            </div>
            <div class="summary-item">
              <span class="s-label">Framework</span>
              <span class="s-val">TensorFlow / Keras</span>
            </div>
            <div class="summary-item">
              <span class="s-label">Task</span>
              <span class="s-val">Binary Classification</span>
            </div>
            <div class="summary-item">
              <span class="s-label">Classes</span>
              <span class="s-val">Cat · Dog</span>
            </div>
            <div class="summary-item">
              <span class="s-label">Backend</span>
              <span class="s-val">FastAPI · Uvicorn</span>
            </div>
            <div class="summary-item">
              <span class="s-label">Deployment</span>
              <span class="s-val">REST API · localhost:8000</span>
            </div>
          </div>

          <router-link to="/predict" class="btn-goto">
            🔍 Run Prediction →
          </router-link>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import API from "../services/api";

export default {
  data() {
    return {
      metrics: {},
      loading: true,
    };
  },
  async mounted() {
  try {
    let res = await API.get("/metrics");
    const d = res.data;
    this.metrics = {
      accuracy: d.train_accuracy,
      val_accuracy: d.validation_accuracy,
      loss: d.train_loss,
      val_loss: d.validation_loss,
    };
  } catch (e) {
    this.metrics = { accuracy: 0, val_accuracy: 0, loss: 0, val_loss: 0 };
  } finally {
    this.loading = false;
  }
},
  methods: {
    formatPct(v) {
      if (v == null) return "—";
      return (v * 100).toFixed(1) + "%";
    },
    formatNum(v) {
      if (v == null) return "—";
      return parseFloat(v).toFixed(4);
    },
    pct(v, max = 1) {
      if (v == null) return "0%";
      return Math.min(100, (v / max) * 100).toFixed(1) + "%";
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

.page {
  min-height: 100vh;
  background: #020917;
  font-family: 'DM Sans', sans-serif;
  color: #e8f0fe;
  position: relative;
}

.bg-grid {
  position: fixed; inset: 0;
  background-image:
    linear-gradient(rgba(59,130,246,0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(59,130,246,0.05) 1px, transparent 1px);
  background-size: 60px 60px; pointer-events: none;
}

.bg-glow {
  position: fixed; top: -200px; left: 50%;
  transform: translateX(-50%);
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(37,99,235,0.15) 0%, transparent 70%);
  pointer-events: none;
}

.navbar {
  position: fixed; top: 0; left: 0; right: 0;
  display: flex; align-items: center; justify-content: space-between;
  padding: 1.2rem 3rem;
  background: rgba(2,9,23,0.85);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(59,130,246,0.15);
  z-index: 100;
}
.logo { display: flex; align-items: center; gap: 10px; font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.3rem; color: #fff; }
.logo-icon { font-size: 1.5rem; color: #3b82f6; }
.logo-accent { color: #3b82f6; }
.nav-links { display: flex; gap: 2rem; }
.nav-link { font-size: 0.9rem; color: rgba(232,240,254,0.6); text-decoration: none; transition: color 0.2s; }
.nav-link:hover, .nav-link.active { color: #60a5fa; }

.content {
  max-width: 900px; margin: 0 auto;
  padding: 9rem 2rem 4rem;
  position: relative; z-index: 1;
}

.page-header { text-align: center; margin-bottom: 3rem; }

.badge {
  display: inline-block; padding: 0.4rem 1.2rem;
  background: rgba(59,130,246,0.12);
  border: 1px solid rgba(59,130,246,0.3);
  border-radius: 100px; font-size: 0.78rem;
  letter-spacing: 0.08em; color: #93c5fd;
  margin-bottom: 1rem; text-transform: uppercase;
}

.page-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2rem, 4vw, 3.2rem);
  font-weight: 800; color: #fff;
  letter-spacing: -0.02em; margin-bottom: 0.8rem;
}

.gradient-text {
  background: linear-gradient(135deg, #3b82f6, #93c5fd);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page-desc { color: rgba(232,240,254,0.55); font-size: 1rem; }

.loading-state {
  display: flex; flex-direction: column;
  align-items: center; padding: 5rem;
  gap: 1rem; color: #93c5fd;
}
.pulse-ring {
  width: 60px; height: 60px; border-radius: 50%;
  border: 3px solid rgba(59,130,246,0.3);
  border-top-color: #3b82f6;
  animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* METRIC CARDS */
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.2rem;
  margin-bottom: 1.5rem;
}

@media (max-width: 600px) {
  .metrics-grid { grid-template-columns: 1fr; }
}

.metric-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(59,130,246,0.15);
  border-radius: 18px;
  padding: 1.5rem 1.8rem;
  transition: border-color 0.25s;
}
.metric-card:hover { border-color: rgba(59,130,246,0.3); }
.metric-card.highlight {
  border-color: rgba(59,130,246,0.35);
  background: rgba(59,130,246,0.06);
}

.metric-icon { font-size: 1.8rem; margin-bottom: 0.8rem; }
.metric-label {
  font-size: 0.78rem; text-transform: uppercase;
  letter-spacing: 0.1em; color: rgba(232,240,254,0.45);
  margin-bottom: 0.3rem;
}
.metric-value {
  font-family: 'Syne', sans-serif;
  font-size: 2.2rem; font-weight: 800;
  color: #e8f0fe; margin-bottom: 1rem;
}
.metric-value.accent { color: #60a5fa; }
.metric-value.warn { color: #fbbf24; font-size: 1.8rem; }

.metric-bar-wrap {
  height: 6px; background: rgba(255,255,255,0.06);
  border-radius: 100px; overflow: hidden;
}
.metric-bar {
  height: 100%; border-radius: 100px;
  background: linear-gradient(90deg, #1d4ed8, #60a5fa);
  transition: width 1s ease;
}
.metric-bar.accent-bar { background: linear-gradient(90deg, #2563eb, #93c5fd); }
.metric-bar.warn-bar { background: linear-gradient(90deg, #d97706, #fbbf24); }

/* SUMMARY */
.summary-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(59,130,246,0.15);
  border-radius: 20px; padding: 2rem;
}

.summary-header {
  display: flex; align-items: center;
  justify-content: space-between; margin-bottom: 1.5rem;
}
.summary-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.2rem; font-weight: 700; color: #fff;
}
.status-badge {
  padding: 0.35rem 1rem;
  background: rgba(74,222,128,0.1);
  border: 1px solid rgba(74,222,128,0.25);
  border-radius: 100px; font-size: 0.78rem;
  color: #4ade80;
}

.summary-grid {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 1rem; margin-bottom: 1.5rem;
}
@media (max-width: 600px) { .summary-grid { grid-template-columns: 1fr 1fr; } }

.summary-item {
  display: flex; flex-direction: column; gap: 0.3rem;
  padding: 0.9rem 1rem;
  background: rgba(59,130,246,0.05);
  border: 1px solid rgba(59,130,246,0.1);
  border-radius: 12px;
}
.s-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: rgba(232,240,254,0.4); }
.s-val { font-size: 0.88rem; color: #e8f0fe; font-weight: 500; }

.btn-goto {
  display: inline-flex; align-items: center; gap: 0.5rem;
  padding: 0.85rem 1.8rem;
  background: linear-gradient(135deg, #1d4ed8, #3b82f6);
  color: #fff; border-radius: 12px;
  text-decoration: none;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500; font-size: 0.95rem;
  box-shadow: 0 0 25px rgba(59,130,246,0.3);
  transition: all 0.25s;
}
.btn-goto:hover { transform: translateY(-2px); box-shadow: 0 0 40px rgba(59,130,246,0.5); }
</style>