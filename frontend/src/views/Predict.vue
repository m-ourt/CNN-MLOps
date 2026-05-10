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
        <router-link to="/predict" class="nav-link active">Predict</router-link>
        <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
      </nav>
    </header>

    <main class="content">
      <div class="page-header">
        <div class="badge">Image Classification</div>
        <h1 class="page-title">CNN <span class="gradient-text">Prediction</span></h1>
        <p class="page-desc">Upload a cat or dog image and the model will classify it in real time.</p>
      </div>

      <div class="predict-layout">

        <!-- Upload Zone -->
        <div class="card upload-card"
             :class="{ 'drag-over': isDragging }"
             @dragover.prevent="isDragging = true"
             @dragleave="isDragging = false"
             @drop.prevent="onDrop">

          <div v-if="!preview" class="upload-zone" @click="$refs.fileInput.click()">
            <div class="upload-icon">📁</div>
            <p class="upload-title">Drop your image here</p>
            <p class="upload-sub">or click to browse · JPG, PNG, WEBP</p>
            <button class="btn-upload">Choose File</button>
          </div>

          <div v-else class="preview-zone">
            <img :src="preview" class="preview-img" alt="Preview" />
            <div class="preview-overlay" @click="$refs.fileInput.click()">
              <span>Change image</span>
            </div>
          </div>

          <input ref="fileInput" type="file" accept="image/*" @change="onFileChange" style="display:none" />

          <div v-if="file" class="file-info">
            <span class="file-name">{{ file.name }}</span>
            <span class="file-size">{{ (file.size / 1024).toFixed(1) }} KB</span>
          </div>

          <button
            class="btn-predict"
            :class="{ loading: isLoading }"
            :disabled="!file || isLoading"
            @click="predict">
            <span v-if="!isLoading">🔍 Run Prediction</span>
            <span v-else class="spinner-text">⟳ Analyzing...</span>
          </button>
        </div>

        <!-- Result Zone -->
        <div class="card result-card">
          <div v-if="!result && !isLoading" class="result-empty">
            <div class="empty-icon">🤖</div>
            <p class="empty-title">Awaiting image</p>
            <p class="empty-sub">Upload an image and click "Run Prediction" to see the CNN model output.</p>
          </div>

          <div v-if="isLoading" class="result-loading">
            <div class="pulse-ring"></div>
            <p class="loading-text">Model is processing...</p>
            <div class="loading-bars">
              <div class="bar"></div>
              <div class="bar"></div>
              <div class="bar"></div>
              <div class="bar"></div>
            </div>
          </div>

          <div v-if="result && !isLoading" class="result-content">
            <div class="result-icon">{{ result.class === 'cat' ? '🐱' : '🐶' }}</div>
            <div class="result-label">Predicted Class</div>
            <div class="result-class">{{ result.class }}</div>

            <div class="confidence-section">
              <div class="conf-label">
                <span>Confidence</span>
                <span class="conf-value">{{ (result.confidence * 100).toFixed(1) }}%</span>
              </div>
              <div class="conf-bar-bg">
                <div class="conf-bar-fill" :style="{ width: (result.confidence * 100) + '%' }"></div>
              </div>
            </div>

            <div class="result-meta">
              <div class="meta-item">
                <span class="meta-label">Model</span>
                <span class="meta-val">CNN TensorFlow</span>
              </div>
              <div class="meta-item">
                <span class="meta-label">Status</span>
                <span class="meta-val success">✓ Complete</span>
              </div>
            </div>

            <button class="btn-reset" @click="reset">↺ New Prediction</button>
          </div>
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
      file: null,
      preview: null,
      result: null,
      isLoading: false,
      isDragging: false,
    };
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
      this.result = null;
      if (this.file) {
        this.preview = URL.createObjectURL(this.file);
      }
    },
    onDrop(e) {
      this.isDragging = false;
      this.file = e.dataTransfer.files[0];
      this.result = null;
      if (this.file) {
        this.preview = URL.createObjectURL(this.file);
      }
    },
    async predict() {
  if (!this.file) return;
  this.isLoading = true;
  try {
    let formData = new FormData();
    formData.append("file", this.file);
    let res = await API.post("/predict", formData);
    this.result = res.data.prediction; // ← ajoute .prediction ici
  } catch (e) {
    alert("Error connecting to backend.");
  } finally {
    this.isLoading = false;
  }
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
  background-size: 60px 60px;
  pointer-events: none;
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
  max-width: 1100px;
  margin: 0 auto;
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

/* LAYOUT */
.predict-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

@media (max-width: 768px) {
  .predict-layout { grid-template-columns: 1fr; }
}

.card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(59,130,246,0.15);
  border-radius: 20px;
  padding: 2rem;
}

/* UPLOAD */
.upload-zone {
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  border: 2px dashed rgba(59,130,246,0.3);
  border-radius: 14px; padding: 3rem 1rem;
  cursor: pointer; transition: all 0.25s;
  margin-bottom: 1.2rem;
}

.upload-zone:hover { border-color: rgba(59,130,246,0.6); background: rgba(59,130,246,0.04); }
.drag-over .upload-zone { border-color: #3b82f6; background: rgba(59,130,246,0.08); }

.upload-icon { font-size: 2.5rem; margin-bottom: 0.8rem; }
.upload-title { font-family: 'Syne', sans-serif; font-weight: 600; font-size: 1.1rem; color: #e8f0fe; margin-bottom: 0.4rem; }
.upload-sub { font-size: 0.82rem; color: rgba(232,240,254,0.45); margin-bottom: 1.2rem; }

.btn-upload {
  padding: 0.5rem 1.4rem;
  background: rgba(59,130,246,0.12);
  border: 1px solid rgba(59,130,246,0.35);
  border-radius: 8px; color: #93c5fd;
  font-size: 0.85rem; cursor: pointer;
  transition: all 0.2s;
}
.btn-upload:hover { background: rgba(59,130,246,0.2); }

.preview-zone {
  position: relative; border-radius: 14px;
  overflow: hidden; margin-bottom: 1.2rem;
  max-height: 260px;
}

.preview-img { width: 100%; height: 260px; object-fit: cover; display: block; }

.preview-overlay {
  position: absolute; inset: 0;
  background: rgba(2,9,23,0.6);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; transition: opacity 0.25s; cursor: pointer;
  color: #fff; font-size: 0.9rem;
}
.preview-zone:hover .preview-overlay { opacity: 1; }

.file-info {
  display: flex; justify-content: space-between;
  padding: 0.6rem 0.8rem;
  background: rgba(59,130,246,0.06);
  border-radius: 8px; margin-bottom: 1.2rem;
  font-size: 0.8rem;
}
.file-name { color: #93c5fd; }
.file-size { color: rgba(232,240,254,0.4); }

.btn-predict {
  width: 100%; padding: 1rem;
  background: linear-gradient(135deg, #1d4ed8, #3b82f6);
  border: none; border-radius: 12px;
  color: #fff; font-family: 'DM Sans', sans-serif;
  font-size: 1rem; font-weight: 500;
  cursor: pointer; transition: all 0.25s;
  box-shadow: 0 0 25px rgba(59,130,246,0.3);
}
.btn-predict:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 0 40px rgba(59,130,246,0.5); }
.btn-predict:disabled { opacity: 0.45; cursor: not-allowed; }
.btn-predict.loading { background: linear-gradient(135deg, #1e3a6e, #2563eb); }

/* RESULT */
.result-empty, .result-loading {
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  min-height: 400px; text-align: center;
}
.empty-icon { font-size: 3rem; margin-bottom: 1rem; opacity: 0.5; }
.empty-title { font-family: 'Syne', sans-serif; font-size: 1.2rem; color: rgba(232,240,254,0.5); margin-bottom: 0.5rem; }
.empty-sub { font-size: 0.85rem; color: rgba(232,240,254,0.3); max-width: 220px; line-height: 1.6; }

.pulse-ring {
  width: 80px; height: 80px; border-radius: 50%;
  border: 3px solid rgba(59,130,246,0.3);
  border-top-color: #3b82f6;
  animation: spin 1s linear infinite;
  margin-bottom: 1.5rem;
}
@keyframes spin { to { transform: rotate(360deg); } }

.loading-text { color: #93c5fd; margin-bottom: 1.5rem; }

.loading-bars { display: flex; gap: 6px; align-items: flex-end; }
.bar {
  width: 6px; height: 24px;
  background: #3b82f6; border-radius: 3px;
  animation: pulse-bar 1s ease-in-out infinite;
}
.bar:nth-child(2) { animation-delay: 0.15s; }
.bar:nth-child(3) { animation-delay: 0.3s; }
.bar:nth-child(4) { animation-delay: 0.45s; }
@keyframes pulse-bar { 0%,100%{opacity:0.3;transform:scaleY(0.6)} 50%{opacity:1;transform:scaleY(1)} }

.result-content {
  display: flex; flex-direction: column;
  align-items: center; padding: 1rem 0;
}

.result-icon { font-size: 4rem; margin-bottom: 1rem; animation: pop 0.4s ease; }
@keyframes pop { 0%{transform:scale(0.5);opacity:0} 100%{transform:scale(1);opacity:1} }

.result-label { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(232,240,254,0.45); margin-bottom: 0.4rem; }
.result-class {
  font-family: 'Syne', sans-serif; font-size: 2.5rem; font-weight: 800;
  text-transform: capitalize; color: #fff; margin-bottom: 2rem;
  background: linear-gradient(135deg, #3b82f6, #93c5fd);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

.confidence-section { width: 100%; margin-bottom: 1.5rem; }
.conf-label { display: flex; justify-content: space-between; font-size: 0.85rem; color: rgba(232,240,254,0.6); margin-bottom: 0.5rem; }
.conf-value { color: #60a5fa; font-weight: 500; }
.conf-bar-bg { height: 8px; background: rgba(59,130,246,0.15); border-radius: 100px; overflow: hidden; }
.conf-bar-fill { height: 100%; background: linear-gradient(90deg, #1d4ed8, #60a5fa); border-radius: 100px; transition: width 0.8s ease; }

.result-meta { display: flex; gap: 1rem; width: 100%; margin-bottom: 1.5rem; }
.meta-item {
  flex: 1; display: flex; flex-direction: column;
  background: rgba(59,130,246,0.06);
  border: 1px solid rgba(59,130,246,0.12);
  border-radius: 10px; padding: 0.8rem 1rem;
}
.meta-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: rgba(232,240,254,0.4); margin-bottom: 0.3rem; }
.meta-val { font-size: 0.9rem; color: #e8f0fe; }
.meta-val.success { color: #4ade80; }

.btn-reset {
  padding: 0.7rem 2rem;
  background: transparent;
  border: 1px solid rgba(59,130,246,0.3);
  border-radius: 10px; color: #93c5fd;
  font-size: 0.9rem; cursor: pointer;
  transition: all 0.2s;
}
.btn-reset:hover { background: rgba(59,130,246,0.1); }
</style>