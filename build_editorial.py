#!/usr/bin/env python3
"""
Builds an editorial, ultra-luxury portfolio for Nithillen Jayaseelan
modeled precisely after the aesthetic and interactive architecture of
https://www.joegarnerdesign.com/

Features:
- Warm paper palette (#f0f0ee background, #1f1d1e charcoal text, dashed dividers)
- Iconic 8-pointed geometric SVG star accents and spinning emblems
- Fullscreen counting loader (0% -> 100% even numbers) with circular tracker and curtain reveal
- Signature Joe Garner layout with framing dots [ •   • ] around quotes and overlines
- Interactive mathematical generative canvas in the hero showcase
- Magazine-style 2-column project cards with top year/tag, visual mockups, and bottom titles
- Editorial dashed timeline table for Education, Experience, Patents & Schooling (CBSE 89.6% & 87.4%)
- Interactive FAQ accordion with dashed borders and numbered indices (01, 02, 03...)
- Fullscreen editorial navigation menu drawer with smooth toggle
- Complete interactive Résumé modal and Project detail modals with GitHub links
"""

import os

STAR_SVG = '''<svg viewBox="0 0 44 49" fill="none" xmlns="http://www.w3.org/2000/svg" class="svg-star">
<path d="M19.139 48.5C21.1121 35.7531 21.3094 30.7739 21.3094 25.5954C16.574 28.3838 10.2601 32.1681 2.76233 38.7407L0 33.9606C9.66816 30.5747 16.1794 26.9896 20.9148 24.4004C16.1794 21.8112 9.66816 18.027 0 14.8403L2.76233 10.0602C10.2601 16.6328 16.574 20.2178 21.3094 23.2054C21.3094 18.027 21.1121 13.0477 19.139 0.5H24.6637C22.8879 13.0477 22.6906 18.027 22.4933 23.4046C27.0314 20.417 33.3453 16.6328 41.0404 10.0602L44 14.8403C34.5292 18.2261 28.0179 22.0104 23.0852 24.4004C28.0179 26.9896 34.5292 30.5747 44 33.9606L41.0404 38.7407C33.3453 32.1681 27.0314 28.1846 22.4933 25.3963C22.6906 30.7739 22.8879 35.7531 24.6637 48.5H19.139Z" fill="currentColor"/>
</svg>'''

HTML_CONTENT = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Nithillen Jayaseelan — Data Science & Machine Learning</title>
<meta name="description" content="Portfolio of Nithillen Jayaseelan. M.Sc. Data Science & Machine Learning Candidate at the National University of Singapore (NUS). Machine Learning Engineer & Quantitative Systems Architect."/>

<!-- Google Fonts: Plus Jakarta Sans (display), Inter (body), JetBrains Mono (technical code/data) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">

<style>
/* CSS RESET & VARIABLES (PROFESSIONAL TECH SECTOR STACK) */
*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

:root {{
  --bg-primary: #f8fafc;
  --bg-card: #ffffff;
  --bg-dark: #0f172a;
  --text-primary: #0f172a;
  --text-muted: #475569;
  --text-light: #f8fafc;
  --line-color: rgba(15, 23, 42, 0.09);
  --line-dashed: rgba(15, 23, 42, 0.16);
  --font-display: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', 'Space Mono', monospace;
  --gutter: clamp(16px, 4vw, 48px);
  --max-w: 1360px;
}}

html {{
  background: var(--bg-primary);
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.5;
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}}

body {{
  background-color: var(--bg-primary);
  overflow-x: hidden;
  position: relative;
}}

a {{
  color: inherit;
  text-decoration: none;
}}

button {{
  background: none;
  border: none;
  font: inherit;
  cursor: pointer;
  color: inherit;
}}

/* CONTAINER & LAYOUT UTILITIES */
.container {{
  width: 100%;
  max-width: var(--max-w);
  margin: 0 auto;
  padding-left: var(--gutter);
  padding-right: var(--gutter);
}}

.line {{
  width: 100%;
  height: 1px;
  background-color: var(--line-color);
}}

.line-dashed {{
  width: 100%;
  border-top: 1px dashed var(--line-dashed);
}}

.dots-frame {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 4px 0;
}}

.dot {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--text-primary);
}}

.dot.is-light {{
  background-color: var(--text-light);
}}

.svg-star {{
  width: 22px;
  height: 24px;
  display: inline-block;
  vertical-align: middle;
  animation: starRotate 24s linear infinite;
}}

@keyframes starRotate {{
  from {{ transform: rotate(0deg); }}
  to {{ transform: rotate(360deg); }}
}}

/* ====================================================================
   1. LOADER OVERLAY (JOE GARNER ICONIC COUNTER & CURTAIN)
   ==================================================================== */
#loader {{
  position: fixed;
  inset: 0;
  z-index: 1000;
  background-color: var(--bg-dark);
  color: var(--text-light);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: clamp(24px, 4vw, 56px);
  transition: transform 0.85s cubic-bezier(0.77, 0, 0.175, 1);
}}

#loader.loaded {{
  transform: translateY(-100%);
  pointer-events: none;
}}

.loader-top {{
  display: flex;
  justify-content: space-between;
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.1em;
  opacity: 0.8;
}}

.loader-center {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  position: relative;
}}

.loader-circle-wrapper {{
  position: relative;
  width: 140px;
  height: 140px;
  margin-bottom: 28px;
  display: grid;
  place-items: center;
}}

.loader-svg {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}}

.loader-circle-bg {{
  stroke: rgba(240, 240, 238, 0.15);
  stroke-width: 2;
  fill: none;
}}

.loader-circle-progress {{
  stroke: var(--text-light);
  stroke-width: 2.5;
  stroke-linecap: round;
  fill: none;
  stroke-dasharray: 408;
  stroke-dashoffset: 408;
  transition: stroke-dashoffset 0.05s linear;
}}

.loader-number {{
  font-family: var(--font-display);
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -0.02em;
}}

.loader-title {{
  font-family: var(--font-display);
  font-size: clamp(28px, 5vw, 64px);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1;
  text-transform: uppercase;
}}

.loader-subtitle {{
  font-family: var(--font-mono);
  font-size: 14px;
  letter-spacing: 0.25em;
  opacity: 0.6;
  margin-top: 10px;
}}

.loader-bottom {{
  display: flex;
  justify-content: space-between;
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.08em;
  opacity: 0.7;
}}

/* ====================================================================
   2. NAVBAR
   ==================================================================== */
.navbar {{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 900;
  background-color: rgba(240, 240, 238, 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line-color);
  transition: transform 0.3s ease;
}}

.nav-layout {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 64px;
}}

.nav-left {{
  display: flex;
  align-items: center;
  gap: 12px;
}}

.nav-logo {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 17px;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 8px;
}}

.nav-desc {{
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  text-transform: uppercase;
  display: none;
}}

@media (min-width: 860px) {{
  .nav-desc {{
    display: inline-block;
    padding-left: 12px;
    border-left: 1px solid var(--line-color);
  }}
}}

.nav-menu-btn {{
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid var(--line-color);
  background: rgba(255, 255, 255, 0.6);
  transition: all 0.25s ease;
}}

.nav-menu-btn:hover {{
  background: var(--text-primary);
  color: var(--text-light);
  border-color: var(--text-primary);
}}

.nav-right {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.nav-contact-link {{
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: opacity 0.2s;
}}

.nav-contact-link:hover {{
  opacity: 0.6;
}}

/* ====================================================================
   3. FULLSCREEN MENU DRAWER
   ==================================================================== */
#menuDrawer {{
  position: fixed;
  inset: 0;
  z-index: 950;
  background-color: var(--bg-dark);
  color: var(--text-light);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: clamp(24px, 4vw, 56px);
  transform: translateY(-100%);
  transition: transform 0.6s cubic-bezier(0.77, 0, 0.175, 1);
}}

#menuDrawer.open {{
  transform: translateY(0);
}}

.menu-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.menu-brand {{
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 18px;
  display: flex;
  align-items: center;
  gap: 10px;
}}

.menu-close-btn {{
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 8px 18px;
  border: 1px solid rgba(240, 240, 238, 0.3);
  border-radius: 999px;
  transition: all 0.25s;
}}

.menu-close-btn:hover {{
  background: var(--text-light);
  color: var(--bg-dark);
}}

.menu-body {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 40px 0;
}}

.menu-stars-badge {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
  opacity: 0.8;
}}

.menu-links {{
  display: flex;
  flex-direction: column;
  gap: clamp(12px, 2.5vw, 24px);
}}

.menu-link {{
  font-family: var(--font-display);
  font-size: clamp(28px, 5vw, 64px);
  font-weight: 700;
  letter-spacing: -0.025em;
  line-height: 1.15;
  color: rgba(248, 250, 252, 0.6);
  transition: color 0.25s, transform 0.25s;
}}

.menu-link:hover {{
  color: var(--text-light);
  transform: scale(1.03);
}}

.menu-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.08em;
  opacity: 0.7;
  border-top: 1px solid rgba(240, 240, 238, 0.15);
  padding-top: 20px;
}}

.menu-social-links {{
  display: flex;
  gap: 20px;
}}

.menu-social-links a:hover {{
  color: #fff;
  text-decoration: underline;
}}

/* ====================================================================
   4. HERO SECTION
   ==================================================================== */
.hero-section {{
  padding-top: 120px;
  padding-bottom: 60px;
}}

.hero-video-wrapper {{
  position: relative;
  width: 100%;
  height: clamp(340px, 58vh, 680px);
  background: #181717;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.12);
  margin-bottom: 48px;
}}

#heroCanvas {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}}

.hero-video-overlay {{
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(circle at 50% 50%, rgba(24, 23, 23, 0) 30%, rgba(24, 23, 23, 0.5) 100%);
}}

.hero-video-badge {{
  position: absolute;
  bottom: 24px;
  left: 24px;
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.1em;
  color: #fff;
  background: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(8px);
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  display: flex;
  align-items: center;
  gap: 8px;
}}

.hero-video-badge .dot {{
  background: #22c55e;
  box-shadow: 0 0 10px #22c55e;
}}

.hero-heading-stack {{
  display: flex;
  flex-direction: column;
}}

.hero-paragraph {{
  font-family: var(--font-body);
  font-size: clamp(16px, 1.8vw, 22px);
  font-weight: 500;
  color: var(--text-muted);
  max-width: 820px;
  line-height: 1.55;
  margin: 22px 0 14px;
}}

.hero-title {{
  font-family: var(--font-display);
  font-size: clamp(42px, 8.2vw, 108px);
  font-weight: 800;
  line-height: 1.0;
  letter-spacing: -0.035em;
  color: var(--text-primary);
  margin-top: 6px;
}}

/* ====================================================================
   5. ABOUT SECTION (WITH SIGNATURE JOE GARNER DOT FRAMES)
   ==================================================================== */
.about-section {{
  padding: 80px 0;
}}

.about-card {{
  border-top: 1px solid var(--line-color);
  border-bottom: 1px solid var(--line-color);
  padding: 60px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}}

.overline {{
  font-family: var(--font-mono);
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 28px;
}}

.about-lead {{
  font-family: var(--font-display);
  font-size: clamp(22px, 2.7vw, 38px);
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: -0.02em;
  max-width: 980px;
  color: var(--text-primary);
  margin-bottom: 24px;
}}

.about-lead em {{
  font-style: normal;
  font-weight: 700;
  color: #2563eb;
}}

.about-body {{
  font-family: var(--font-body);
  font-size: clamp(15px, 1.2vw, 17px);
  line-height: 1.75;
  color: var(--text-muted);
  max-width: 780px;
  margin-bottom: 36px;
}}

.btn-rule-wrap {{
  display: flex;
  align-items: center;
  gap: 20px;
  width: 100%;
  max-width: 520px;
}}

.btn-rule-wrap .line {{
  flex: 1;
}}

.btn-editorial {{
  font-family: var(--font-mono);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 12px 28px;
  border: 1px solid var(--text-primary);
  border-radius: 999px;
  background: var(--bg-primary);
  color: var(--text-primary);
  transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
  white-space: nowrap;
}}

.btn-editorial:hover {{
  background: var(--text-primary);
  color: var(--text-light);
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(31, 29, 30, 0.15);
}}

/* ====================================================================
   6. WORKS SECTION (2-COLUMN EDITORIAL MAGAZINE GRID)
   ==================================================================== */
.works-section {{
  padding: 90px 0;
}}

.works-header {{
  display: flex;
  flex-direction: column;
  margin-bottom: 60px;
}}

.works-subhead-row {{
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 12px;
}}

.works-subhead-title {{
  font-family: var(--font-display);
  font-size: clamp(20px, 2.5vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}}

.works-desc-row {{
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 1px solid var(--line-color);
  padding-bottom: 20px;
}}

.works-desc-text {{
  font-family: var(--font-body);
  font-size: 15.5px;
  line-height: 1.6;
  color: var(--text-muted);
  max-width: 560px;
}}

.works-title-huge {{
  font-family: var(--font-display);
  font-size: clamp(36px, 5.5vw, 76px);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.05;
  margin-top: 18px;
}}

.projects-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 40px;
}}

@media (min-width: 768px) {{
  .projects-grid {{
    grid-template-columns: repeat(2, 1fr);
    gap: 48px 32px;
  }}
}}

.project-card {{
  position: relative;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  group: project;
}}

.project-meta-top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 12px;
}}

.project-media-box {{
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 10;
  border-radius: 10px;
  overflow: hidden;
  background: #1a1a1c;
  box-shadow: 0 14px 34px rgba(0, 0, 0, 0.08);
  margin-bottom: 16px;
  transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}}

.project-card:hover .project-media-box {{
  transform: translateY(-4px) scale(1.015);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.14);
}}

.project-canvas-preview {{
  width: 100%;
  height: 100%;
  display: block;
}}

.project-media-badge {{
  position: absolute;
  top: 14px;
  right: 14px;
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  padding: 4px 10px;
  background: rgba(15, 23, 42, 0.7);
  color: #fff;
  border-radius: 6px;
  backdrop-filter: blur(6px);
}}

.project-meta-bottom {{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}}

.project-title {{
  font-family: var(--font-display);
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  transition: color 0.2s;
}}

.project-card:hover .project-title {{
  color: #000;
  text-decoration: underline;
  text-underline-offset: 4px;
}}

.project-discipline {{
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}}

/* ====================================================================
   7. TIMELINE & EXPERIENCE (JOE GARNER EDITORIAL DASHED TABLE)
   ==================================================================== */
.timeline-section {{
  padding: 90px 0;
}}

.table-heading-row {{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 32px;
}}

.table-heading-title {{
  font-family: var(--font-display);
  font-size: clamp(26px, 3.8vw, 48px);
  font-weight: 800;
  letter-spacing: -0.025em;
}}

.table-header-cols {{
  display: grid;
  grid-template-columns: 80px 1.2fr 2fr;
  padding: 14px 0;
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-muted);
  border-bottom: 1px solid var(--line-color);
}}

@media (max-width: 768px) {{
  .table-header-cols {{
    display: none;
  }}
}}

.table-row {{
  display: grid;
  grid-template-columns: 80px 1.2fr 2fr;
  padding: 24px 0;
  border-bottom: 1px dashed var(--line-dashed);
  align-items: baseline;
  transition: background-color 0.2s ease;
}}

@media (max-width: 768px) {{
  .table-row {{
    grid-template-columns: 1fr;
    gap: 8px;
    padding: 20px 0;
  }}
}}

.table-row:hover {{
  background-color: rgba(0, 0, 0, 0.015);
}}

.table-col-num {{
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 700;
  color: var(--text-muted);
}}

.table-col-entity {{
  font-family: var(--font-display);
  font-size: 20px;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.2;
}}

.table-col-entity small {{
  display: block;
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 400;
  color: var(--text-muted);
  margin-top: 4px;
  text-transform: uppercase;
}}

.table-col-desc {{
  font-family: var(--font-body);
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.6;
}}

.table-col-desc strong {{
  color: var(--text-primary);
  font-weight: 600;
}}

.table-col-desc .metric-tag {{
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  background: var(--text-primary);
  color: var(--text-light);
  padding: 2px 8px;
  border-radius: 4px;
  margin-left: 6px;
  vertical-align: middle;
}}

/* ====================================================================
   8. FAQ SECTION (JOE GARNER SIGNATURE ACCORDION)
   ==================================================================== */
.faq-section {{
  padding: 90px 0;
}}

.faq-header-row {{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1px solid var(--line-color);
  padding-bottom: 24px;
  margin-bottom: 24px;
}}

.faq-title-group {{
  display: flex;
  align-items: center;
  gap: 16px;
}}

.faq-title-group h2 {{
  font-family: var(--font-display);
  font-size: clamp(34px, 5vw, 68px);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.05;
}}

.faq-stars-group {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.faq-accordion-item {{
  border-bottom: 1px dashed var(--line-dashed);
}}

.faq-accordion-btn {{
  width: 100%;
  display: grid;
  grid-template-columns: 80px 1.3fr 40px;
  padding: 24px 0;
  text-align: left;
  align-items: center;
}}

@media (max-width: 640px) {{
  .faq-accordion-btn {{
    grid-template-columns: 48px 1fr 32px;
  }}
}}

.faq-num {{
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 700;
  color: var(--text-muted);
}}

.faq-question {{
  font-family: var(--font-display);
  font-size: clamp(17px, 2vw, 24px);
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.01em;
}}

.faq-icon {{
  font-family: var(--font-mono);
  font-size: 18px;
  transition: transform 0.3s ease;
  justify-self: end;
}}

.faq-accordion-item.active .faq-icon {{
  transform: rotate(45deg);
}}

.faq-answer-panel {{
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}}

.faq-accordion-item.active .faq-answer-panel {{
  max-height: 380px;
}}

.faq-answer-content {{
  padding: 0 0 28px 80px;
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.7;
  color: var(--text-muted);
  max-width: 820px;
}}

@media (max-width: 640px) {{
  .faq-answer-content {{
    padding-left: 48px;
  }}
}}

/* ====================================================================
   9. CLOSING MESSAGE & FOOTER
   ==================================================================== */
.closing-section {{
  padding: 80px 0;
}}

.closing-card {{
  border-top: 1px solid var(--line-color);
  border-bottom: 1px solid var(--line-color);
  padding: 60px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}}

.closing-lead {{
  font-family: var(--font-display);
  font-size: clamp(24px, 3.4vw, 44px);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.3;
  max-width: 900px;
  margin-top: 16px;
}}

.footer-section {{
  padding: 80px 0 40px;
}}

.footer-content {{
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-bottom: 80px;
}}

.footer-heading {{
  font-family: var(--font-display);
  font-size: clamp(38px, 6vw, 84px);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.05;
  margin-bottom: 36px;
}}

.footer-cta-btn {{
  display: inline-block;
  font-family: var(--font-mono);
  font-size: clamp(16px, 1.8vw, 22px);
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 18px 48px;
  border: 1px solid var(--text-primary);
  border-radius: 999px;
  background: var(--text-primary);
  color: var(--text-light);
  transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
}}

.footer-cta-btn:hover {{
  background: transparent;
  color: var(--text-primary);
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(31, 29, 30, 0.15);
}}

.footer-bottom-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  border-top: 1px solid var(--line-color);
  padding-top: 24px;
}}

@media (max-width: 640px) {{
  .footer-bottom-bar {{
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }}
}}

.footer-links-group {{
  display: flex;
  gap: 20px;
}}

.footer-links-group a:hover {{
  color: var(--text-primary);
  text-decoration: underline;
}}

/* ====================================================================
   10. MODAL DIALOGS (RÉSUMÉ & PROJECT DETAILS)
   ==================================================================== */
.modal-overlay {{
  position: fixed;
  inset: 0;
  z-index: 1100;
  background: rgba(31, 29, 30, 0.65);
  backdrop-filter: blur(8px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
}}

.modal-overlay.open {{
  display: flex;
}}

.modal-card {{
  background: #ffffff;
  color: var(--text-primary);
  border-radius: 16px;
  width: 100%;
  max-width: 840px;
  max-height: 90vh;
  overflow-y: auto;
  padding: clamp(28px, 4vw, 56px);
  position: relative;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.3);
  animation: modalFadeIn 0.3s ease;
}}

@keyframes modalFadeIn {{
  from {{ opacity: 0; transform: scale(0.96) translateY(12px); }}
  to {{ opacity: 1; transform: scale(1) translateY(0); }}
}}

.modal-close-btn {{
  position: absolute;
  top: 24px;
  right: 24px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1px solid var(--line-color);
  display: grid;
  place-items: center;
  font-size: 18px;
  transition: all 0.2s;
}}

.modal-close-btn:hover {{
  background: var(--text-primary);
  color: #fff;
}}

.modal-tag {{
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 8px;
}}

.modal-title {{
  font-family: var(--font-display);
  font-size: clamp(28px, 4vw, 42px);
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
}}

.modal-body p {{
  font-family: var(--font-body);
  font-size: 15.5px;
  line-height: 1.7;
  color: #4b5563;
  margin-bottom: 16px;
}}

.modal-body strong {{
  color: var(--text-primary);
}}

.modal-actions {{
  display: flex;
  gap: 14px;
  margin-top: 28px;
  padding-top: 24px;
  border-top: 1px solid var(--line-color);
}}

.modal-btn {{
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 12px 24px;
  border-radius: 8px;
  border: 1px solid var(--text-primary);
}}

.modal-btn.primary {{
  background: var(--text-primary);
  color: #fff;
}}

.modal-btn.secondary {{
  background: #f1f5f9;
  border-color: #cbd5e1;
}}
</style>
</head>
<body>

<!-- ====================================================================
     1. LOADER SCREEN (JOE GARNER ICONIC CIRCLE COUNTER)
     ==================================================================== -->
<div id="loader">
  <div class="loader-top">
    <span>( 20 26 )</span>
    <span>SINGAPORE</span>
  </div>
  <div class="loader-center">
    <div class="loader-circle-wrapper">
      <svg class="loader-svg" viewBox="0 0 140 140">
        <circle class="loader-circle-bg" cx="70" cy="70" r="65"></circle>
        <circle id="loaderProgress" class="loader-circle-progress" cx="70" cy="70" r="65"></circle>
      </svg>
      <div id="loaderText" class="loader-number">0%</div>
    </div>
    <div class="loader-title">NITHILLEN JAYASEELAN</div>
    <div class="loader-subtitle">DATA SCIENCE · MACHINE LEARNING · QUANT SYSTEMS</div>
  </div>
  <div class="loader-bottom">
    <span>NATIONAL UNIVERSITY OF SINGAPORE</span>
    <span>M.SC. DSML</span>
  </div>
</div>

<!-- ====================================================================
     2. NAVIGATION BAR
     ==================================================================== -->
<nav class="navbar">
  <div class="container">
    <div class="nav-layout">
      <div class="nav-left">
        <div class="dot"></div>
        <a href="#hero" class="nav-logo">Nithillen Jayaseelan</a>
        <span class="nav-desc">DATA SCIENCE &amp; ML · QUANTITATIVE FINANCE · AGENTIC AI</span>
      </div>
      <button id="openMenuBtn" class="nav-menu-btn" aria-label="Open Navigation Menu">Menu</button>
      <div class="nav-right">
        <a href="mailto:nithillen.py@gmail.com" class="nav-contact-link">Contact</a>
        <div class="dot"></div>
      </div>
    </div>
  </div>
</nav>

<!-- ====================================================================
     3. FULLSCREEN MENU DRAWER
     ==================================================================== -->
<div id="menuDrawer">
  <div class="menu-header">
    <div class="menu-brand">
      <div class="dot is-light"></div>
      <span>Nithillen Jayaseelan</span>
    </div>
    <button id="closeMenuBtn" class="menu-close-btn" aria-label="Close Navigation Menu">Close</button>
  </div>
  <div class="menu-body">
    <div class="menu-stars-badge">
      {STAR_SVG}
      <span style="font-family:var(--font-mono);font-size:13px;letter-spacing:0.2em;text-transform:uppercase;">Navigation</span>
      {STAR_SVG}
    </div>
    <div class="menu-links">
      <a href="#hero" class="menu-link nav-jump">Home</a>
      <a href="#about" class="menu-link nav-jump">About</a>
      <a href="#works" class="menu-link nav-jump">Works</a>
      <a href="#timeline" class="menu-link nav-jump">Timeline</a>
      <a href="#faq" class="menu-link nav-jump">Information</a>
      <a href="#footer" class="menu-link nav-jump">Contact</a>
    </div>
  </div>
  <div class="menu-footer">
    <div class="menu-social-links">
      <span style="opacity:0.6;">( S )</span>
      <a href="https://github.com/Nithillen" target="_blank" rel="noopener">GitHub</a>
      <a href="https://www.linkedin.com/in/nithillenjayaseelan/" target="_blank" rel="noopener">LinkedIn</a>
      <a href="mailto:nithillen.py@gmail.com">Email</a>
      <a href="#" onclick="openResumeModal();return false;">Résumé</a>
    </div>
    <span>2026© SINGAPORE</span>
  </div>
</div>

<!-- ====================================================================
     4. HERO SECTION
     ==================================================================== -->
<section id="hero" class="hero-section">
  <div class="container">
    <div class="hero-video-wrapper">
      <canvas id="heroCanvas"></canvas>
      <div class="hero-video-overlay"></div>
      <div class="hero-video-badge">
        <div class="dot"></div>
        <span>LIVE MULTI-AGENT MARKET GRAPH INTERACTION · MOVE MOUSE</span>
      </div>
    </div>

    <div class="hero-heading-stack">
      <div class="line"></div>
      <p class="hero-paragraph">
        Machine learning engineer specializing in quantitative trading algorithms, agentic AI systems, and distributed data infrastructure.
      </p>
      <h1 class="hero-title">Nithillen Jayaseelan</h1>
    </div>
  </div>
</section>

<!-- ====================================================================
     5. ABOUT SECTION
     ==================================================================== -->
<section id="about" class="about-section">
  <div class="container">
    <div class="dots-frame">
      <div class="dot"></div>
      <div class="dot"></div>
    </div>

    <div class="about-card">
      <div class="overline">( ABOUT ME )</div>
      <h2 class="about-lead">
        M.Sc. Data Science &amp; Machine Learning candidate at the <em>National University of Singapore</em>. Bridging quantitative finance, clinical predictive intelligence, and distributed systems.
      </h2>
      <p class="about-body">
        I believe machine learning systems should be crafted with the same precision, restraint, and obsessive attention to detail as luxury physical craftsmanship. From evolving genetic trading agents with a capital-protecting safe vault to engineering agentic AI workflows that accelerated enterprise regulatory turnaround by &gt;40% at Viatris, every pipeline is engineered for high-stakes resilience.
      </p>
      <div class="btn-rule-wrap">
        <div class="line"></div>
        <button class="btn-editorial" onclick="openResumeModal()">View Full Résumé →</button>
        <div class="line"></div>
      </div>
    </div>

    <div class="dots-frame">
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
  </div>
</section>

<!-- ====================================================================
     6. WORKS SECTION (MAGAZINE-STYLE GRID)
     ==================================================================== -->
<section id="works" class="works-section">
  <div class="container">
    <div class="works-header">
      <div class="works-subhead-row">
        {STAR_SVG}
        <span class="works-subhead-title">Featured</span>
        {STAR_SVG}
      </div>
      <div class="works-desc-row">
        <p class="works-desc-text">
          A curated collection of open-source repositories and engineering breakthroughs across quantitative trading, healthcare AI, and distributed computing.
        </p>
      </div>
      <h2 class="works-title-huge">Works</h2>
    </div>

    <div class="projects-grid">

      <!-- PROJECT 1 -->
      <div class="project-card" onclick="openProjectModal('evolutionary')">
        <div class="project-meta-top">
          <span>( 2026 )</span>
          <span>QUANTITATIVE FINANCE · GENETIC ALGORITHMS</span>
        </div>
        <div class="project-media-box">
          <canvas id="cardCanvas1" class="project-canvas-preview"></canvas>
          <div class="project-media-badge">Python · VectorBT</div>
        </div>
        <div class="project-meta-bottom">
          <h3 class="project-title">Evolutionary Trading System</h3>
          <span class="project-discipline">Autonomous Agentic Trading</span>
        </div>
      </div>

      <!-- PROJECT 2 -->
      <div class="project-card" onclick="openProjectModal('pairs')">
        <div class="project-meta-top">
          <span>( 2026 )</span>
          <span>STATISTICAL ARBITRAGE · MACHINE LEARNING</span>
        </div>
        <div class="project-media-box">
          <canvas id="cardCanvas2" class="project-canvas-preview"></canvas>
          <div class="project-media-badge">XGBoost · Cointegration</div>
        </div>
        <div class="project-meta-bottom">
          <h3 class="project-title">ML Pairs Trading Engine</h3>
          <span class="project-discipline">Spread Signals &amp; Backtesting</span>
        </div>
      </div>

      <!-- PROJECT 3 -->
      <div class="project-card" onclick="openProjectModal('readmission')">
        <div class="project-meta-top">
          <span>( 2025 )</span>
          <span>HEALTHCARE ML · EXPLAINABLE AI</span>
        </div>
        <div class="project-media-box">
          <canvas id="cardCanvas3" class="project-canvas-preview"></canvas>
          <div class="project-media-badge">Random Forest · SHAP</div>
        </div>
        <div class="project-meta-bottom">
          <h3 class="project-title">Patient Readmission Risk Engine</h3>
          <span class="project-discipline">SQL CTE Pipeline &amp; Explainability</span>
        </div>
      </div>

      <!-- PROJECT 4 -->
      <div class="project-card" onclick="openProjectModal('cassandra')">
        <div class="project-meta-top">
          <span>( 2025 )</span>
          <span>DISTRIBUTED SYSTEMS · CLOUD INFRASTRUCTURE</span>
        </div>
        <div class="project-media-box">
          <canvas id="cardCanvas4" class="project-canvas-preview"></canvas>
          <div class="project-media-badge">Apache Cassandra · Docker</div>
        </div>
        <div class="project-meta-bottom">
          <h3 class="project-title">Cassandra Consistency Study</h3>
          <span class="project-discipline">Quorum Benchmarks &amp; Latency</span>
        </div>
      </div>

      <!-- PROJECT 5 -->
      <div class="project-card" onclick="openProjectModal('syncagent')">
        <div class="project-meta-top">
          <span>( 2025 – 2026 )</span>
          <span>ENTERPRISE AI · SAFETY COMPLIANCE</span>
        </div>
        <div class="project-media-box">
          <canvas id="cardCanvas5" class="project-canvas-preview"></canvas>
          <div class="project-media-badge">Viatris · Azure &amp; SQL</div>
        </div>
        <div class="project-meta-bottom">
          <h3 class="project-title">SyncAgent Agentic Workflow</h3>
          <span class="project-discipline">&gt;40% Regulatory Acceleration</span>
        </div>
      </div>

      <!-- PROJECT 6 -->
      <div class="project-card" onclick="openProjectModal('patent')">
        <div class="project-meta-top">
          <span>( 2024 – 2025 )</span>
          <span>PATENTED RESEARCH · SIGNAL PROCESSING</span>
        </div>
        <div class="project-media-box">
          <canvas id="cardCanvas6" class="project-canvas-preview"></canvas>
          <div class="project-media-badge">Granted Patent · R²=0.982</div>
        </div>
        <div class="project-meta-bottom">
          <h3 class="project-title">5G ML Allocation &amp; PPG Biometrics</h3>
          <span class="project-discipline">Granted Patent &amp; Publication</span>
        </div>
      </div>

    </div>

    <div style="margin-top: 60px; text-align: center;">
      <a href="https://github.com/Nithillen" target="_blank" rel="noopener" class="btn-editorial">Explore All Repositories on GitHub ↗</a>
    </div>
  </div>
</section>

<!-- ====================================================================
     7. TIMELINE SECTION (JOE GARNER EDITORIAL TABLE)
     ==================================================================== -->
<section id="timeline" class="timeline-section">
  <div class="container">
    <div class="table-heading-row">
      <h2 class="table-heading-title">Experience &amp; Education</h2>
      <div style="font-family:var(--font-mono);font-size:13px;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted);">( 2018 – 2026 )</div>
    </div>

    <div class="table-header-cols">
      <div>Index</div>
      <div>Institution / Company</div>
      <div>Role &amp; Highlights</div>
    </div>

    <!-- ROW 1: NUS -->
    <div class="table-row">
      <div class="table-col-num">01</div>
      <div class="table-col-entity">
        National University of Singapore
        <small>Aug 2026 – Present · Singapore</small>
      </div>
      <div class="table-col-desc">
        <strong>M.Sc. in Data Science &amp; Machine Learning</strong>. Advanced machine learning theory, quantitative finance architectures, and distributed systems. Elected <strong>University Relations Manager</strong> on the Executive Committee of the NUS Graduate Students’ Society (GSS).
      </div>
    </div>

    <!-- ROW 2: VIATRIS -->
    <div class="table-row">
      <div class="table-col-num">02</div>
      <div class="table-col-entity">
        Viatris
        <small>Oct 2025 – Jul 2026 · Corporate</small>
      </div>
      <div class="table-col-desc">
        <strong>Graduate Engineer Trainee — Clinical &amp; Safety Domain</strong>. Architected <strong>SyncAgent</strong>, an autonomous multi-agent validation pipeline cutting regulatory turnaround time by <span class="metric-tag">&gt;40% Faster</span>. Engineered DAERS mission-critical safety data migration across Azure Cloud and Oracle SQL. Built call-center conversational voice agents.
      </div>
    </div>

    <!-- ROW 3: KPIT -->
    <div class="table-row">
      <div class="table-col-num">03</div>
      <div class="table-col-entity">
        KPIT Technologies
        <small>Jan 2025 – Jul 2025 · Internship</small>
      </div>
      <div class="table-col-desc">
        <strong>Software Engineering Intern</strong>. Selected for the elite Nova Training Program. Programmed low-latency embedded firmware in C and Python, focusing on deterministic response times and microcontroller diagnostic communication.
      </div>
    </div>

    <!-- ROW 4: VIT -->
    <div class="table-row">
      <div class="table-col-num">04</div>
      <div class="table-col-entity">
        Vellore Institute of Technology
        <small>2021 – 2025 · Undergrad</small>
      </div>
      <div class="table-col-desc">
        <strong>B.Tech in Electronics &amp; Communication (Biomedical)</strong>. Graduated with high distinction <span class="metric-tag">8.81 / 10 CGPA</span>. Student leadership: Core Member of <strong>IEEE EMBS</strong> (Engineering in Medicine &amp; Biology Society) and Inner Core Member of <strong>IEEE EDS</strong> (Electron Devices Society).
      </div>
    </div>

    <!-- ROW 5: RESEARCH & PATENTS -->
    <div class="table-row">
      <div class="table-col-num">05</div>
      <div class="table-col-entity">
        Patents &amp; Research
        <small>Granted Patent &amp; Publication</small>
      </div>
      <div class="table-col-desc">
        <strong>Granted Patent</strong>: Machine learning models (Random Forest, Gradient Boosting, XGBoost) for dynamic 5G network resource allocation <span class="metric-tag">R² = 0.982</span>. Peer-reviewed publication in photoplethysmography (PPG) biometric signal authentication. Google Externship on ClinVar genetic variant classification.
      </div>
    </div>

    <!-- ROW 6: BRIGADE SCHOOL -->
    <div class="table-row">
      <div class="table-col-num">06</div>
      <div class="table-col-entity">
        The Brigade School, Bangalore
        <small>CBSE Board Examinations</small>
      </div>
      <div class="table-col-desc">
        Senior School Certificate Examination (Class XII): <span class="metric-tag">87.4% CBSE</span>. Secondary School Examination (Class X): <span class="metric-tag">89.6% CBSE</span>. Built foundational distinctions in mathematics, algorithmic problem solving, and scientific reasoning.
      </div>
    </div>

  </div>
</section>

<!-- ====================================================================
     8. FAQ SECTION (JOE GARNER ACCORDION)
     ==================================================================== -->
<section id="faq" class="faq-section">
  <div class="container">
    <div class="faq-header-row">
      <div class="faq-title-group">
        <h2>FAQ</h2>
        <div class="faq-stars-group">
          {STAR_SVG}
          {STAR_SVG}
          {STAR_SVG}
        </div>
      </div>
      <div style="font-family:var(--font-mono);font-size:13px;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted);">Information</div>
    </div>

    <div class="faq-accordion-list">

      <div class="faq-accordion-item active">
        <button class="faq-accordion-btn">
          <span class="faq-num">01</span>
          <span class="faq-question">What problem spaces and domains do you focus on?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer-panel">
          <p class="faq-answer-content">
            I specialize in quantitative finance, statistical arbitrage, healthcare risk stratification, agentic AI systems, and low-latency distributed infrastructure. My work bridges statistical modeling with production-grade engineering—ensuring models that perform in backtests also survive live execution and strict compliance requirements.
          </p>
        </div>
      </div>

      <div class="faq-accordion-item">
        <button class="faq-accordion-btn">
          <span class="faq-num">02</span>
          <span class="faq-question">What does your engineering &amp; ML process look like?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer-panel">
          <p class="faq-answer-content">
            My development process follows four distinct phases: <strong>01 Discovery</strong> (exploratory data analysis, stationarity tests, regime clustering), <strong>02 Architecture</strong> (feature engineering via SQL CTEs, loss function selection, model baselines), <strong>03 Validation</strong> (combinatorial cross-validation, walk-forward analysis, SHAP explainability), and <strong>04 Deployment</strong> (containerized microservices, tunable consistency tuning, and live telemetry).
          </p>
        </div>
      </div>

      <div class="faq-accordion-item">
        <button class="faq-accordion-btn">
          <span class="faq-num">03</span>
          <span class="faq-question">How do you balance statistical theory with production software engineering?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer-panel">
          <p class="faq-answer-content">
            Mathematics without rigorous engineering is brittle; engineering without theoretical rigor is blind. Having developed embedded firmware in C at KPIT and engineered distributed database quorum benchmarks on Apache Cassandra alongside machine learning models at NUS, I focus equally on asymptotic algorithmic complexity, memory allocation, and statistical significance.
          </p>
        </div>
      </div>

      <div class="faq-accordion-item">
        <button class="faq-accordion-btn">
          <span class="faq-num">04</span>
          <span class="faq-question">What are your primary programming languages and framework proficiencies?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer-panel">
          <p class="faq-answer-content">
            <strong>Core Languages</strong>: Python, C, C++, SQL, JavaScript (ES6+).<br/>
            <strong>ML &amp; Quant</strong>: PyTorch, XGBoost, VectorBT, scikit-learn, SHAP, NumPy, Pandas.<br/>
            <strong>Infrastructure &amp; Data</strong>: Apache Cassandra, PostgreSQL, Oracle SQL, Microsoft Azure, Docker, Git.
          </p>
        </div>
      </div>

      <div class="faq-accordion-item">
        <button class="faq-accordion-btn">
          <span class="faq-num">05</span>
          <span class="faq-question">What distinguishes your quantitative and healthcare projects?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer-panel">
          <p class="faq-answer-content">
            In quantitative finance, I design models around risk minimization and capital protection—such as the "house money" safe-vault rule in my Evolutionary Trading System. In healthcare, where black-box predictions are intolerable, I pair robust Random Forest classifiers with exact TreeSHAP local explanations so clinicians understand exactly why a patient is stratified as high-risk.
          </p>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ====================================================================
     9. CLOSING MESSAGE SECTION
     ==================================================================== -->
<section class="closing-section">
  <div class="container">
    <div class="dots-frame">
      <div class="dot"></div>
      <div class="dot"></div>
    </div>

    <div class="closing-card">
      <div class="overline">( THANKS FOR VISITING )</div>
      <div class="closing-lead">
        The finest engineering systems are those that feel as intentional and robust as the algorithms behind them. I'd be honored to build together.
      </div>
    </div>

    <div class="dots-frame">
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
  </div>
</section>

<!-- ====================================================================
     10. FOOTER
     ==================================================================== -->
<footer id="footer" class="footer-section">
  <div class="container">
    <div class="footer-content">
      <h2 class="footer-heading">Let's work together!</h2>
      <a href="mailto:nithillen.py@gmail.com" class="footer-cta-btn">Reach Out →</a>
    </div>

    <div class="footer-bottom-bar">
      <div class="footer-links-group">
        <span style="opacity:0.5;">( P )</span>
        <a href="#hero">Home</a>
        <a href="#about">About</a>
        <a href="#works">Works</a>
        <a href="#timeline">Timeline</a>
      </div>
      <div class="footer-links-group">
        <span style="opacity:0.5;">( S )</span>
        <a href="https://github.com/Nithillen" target="_blank" rel="noopener">GitHub</a>
        <a href="https://www.linkedin.com/in/nithillenjayaseelan/" target="_blank" rel="noopener">LinkedIn</a>
        <a href="mailto:nithillen.py@gmail.com">Email</a>
        <a href="#" onclick="openResumeModal();return false;">Résumé</a>
      </div>
      <div>2026© SINGAPORE</div>
    </div>
  </div>
</footer>

<!-- ====================================================================
     11. MODAL DIALOGS
     ==================================================================== -->
<!-- RÉSUMÉ MODAL -->
<div id="resumeModal" class="modal-overlay" onclick="if(event.target===this)closeResumeModal()">
  <div class="modal-card">
    <button class="modal-close-btn" onclick="closeResumeModal()" aria-label="Close Modal">✕</button>
    <div class="modal-tag">Curriculum Vitae</div>
    <h2 class="modal-title">Nithillen Jayaseelan</h2>
    <p style="font-family:var(--font-mono);font-size:13px;color:var(--text-muted);margin-bottom:24px;">
      Singapore · nithillen.py@gmail.com · +65 9895 3841 · linkedin.com/in/nithillenjayaseelan · github.com/Nithillen
    </p>

    <div class="modal-body">
      <h4 style="font-family:var(--font-mono);font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--text-primary);margin:20px 0 8px;border-bottom:1px solid var(--line-color);padding-bottom:4px;">Education</h4>
      <p><strong>National University of Singapore</strong> — M.Sc. in Data Science &amp; Machine Learning (Aug 2026 – Present)<br/>
      Elected University Relations Manager, NUS Graduate Students’ Society (GSS) Executive Committee.</p>
      
      <p><strong>Vellore Institute of Technology</strong> — B.Tech in Electronics &amp; Communication (Biomedical) (2021 – 2025)<br/>
      High Distinction CGPA: <strong>8.81 / 10.0</strong> · Core Member IEEE EMBS · Inner Core Member IEEE EDS.</p>

      <p><strong>The Brigade School, Bangalore</strong> — Central Board of Secondary Education (CBSE)<br/>
      Senior School Certificate Examination (Class XII): <strong>87.4%</strong> · Secondary School Examination (Class X): <strong>89.6%</strong>.</p>

      <h4 style="font-family:var(--font-mono);font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--text-primary);margin:24px 0 8px;border-bottom:1px solid var(--line-color);padding-bottom:4px;">Professional Experience</h4>
      <p><strong>Viatris</strong> — Graduate Engineer Trainee, Clinical &amp; Safety Domain (Oct 2025 – Jul 2026)<br/>
      Architected SyncAgent agentic verification workflow (&gt;40% turnaround acceleration) · DAERS mission-critical safety pipeline migration across Azure Cloud &amp; Oracle SQL · medical call-center voice automation.</p>

      <p><strong>KPIT Technologies</strong> — Software Engineering Intern (Jan 2025 – Jul 2025)<br/>
      Nova Training Program · engineered low-latency embedded firmware in C and Python with strict timing budgets.</p>

      <h4 style="font-family:var(--font-mono);font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--text-primary);margin:24px 0 8px;border-bottom:1px solid var(--line-color);padding-bottom:4px;">Patents &amp; Research</h4>
      <p><strong>Granted Indian Patent</strong>: Machine learning models for dynamic 5G wireless resource allocation (R² = 0.982).<br/>
      <strong>Publication</strong>: Photoplethysmography (PPG) pulse wave biometric authentication.<br/>
      <strong>Google Externship</strong>: ClinVar genomic variant classification using machine learning.</p>

      <h4 style="font-family:var(--font-mono);font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--text-primary);margin:24px 0 8px;border-bottom:1px solid var(--line-color);padding-bottom:4px;">Open-Source Projects</h4>
      <p>Evolutionary Trading System (Genetic Algorithms) · ML Pairs Trading Engine (Cointegration &amp; VectorBT) · Patient Readmission Engine (TreeSHAP Explainability) · Cassandra Consistency Benchmark Study.</p>
    </div>

    <div class="modal-actions">
      <a href="mailto:nithillen.py@gmail.com" class="modal-btn primary">Email Nithillen</a>
      <button class="modal-btn secondary" onclick="window.print()">Print CV</button>
    </div>
  </div>
</div>

<!-- PROJECT DETAIL MODAL -->
<div id="projectModal" class="modal-overlay" onclick="if(event.target===this)closeProjectModal()">
  <div class="modal-card">
    <button class="modal-close-btn" onclick="closeProjectModal()" aria-label="Close Modal">✕</button>
    <div id="pModalTag" class="modal-tag">Project Overview</div>
    <h2 id="pModalTitle" class="modal-title">Project Title</h2>
    <div id="pModalBody" class="modal-body"></div>
    <div class="modal-actions">
      <a id="pModalLink" href="#" target="_blank" rel="noopener" class="modal-btn primary">View on GitHub ↗</a>
      <button class="modal-btn secondary" onclick="closeProjectModal()">Close</button>
    </div>
  </div>
</div>

<!-- ====================================================================
     12. SCRIPT (INTERACTION, LOADER, GENERATIVE CANVASES)
     ==================================================================== -->
<script>
// ---------- LOADER COUNTER (EVEN NUMBERS 0% -> 100%)
const loader = document.getElementById('loader');
const loaderText = document.getElementById('loaderText');
const loaderProgress = document.getElementById('loaderProgress');
const circumference = 2 * Math.PI * 65; // r = 65 -> ~408.4

let count = 0;
const loaderInterval = setInterval(() => {{
  count += 2;
  if (count > 100) count = 100;
  loaderText.textContent = count + '%';
  const offset = circumference - (count / 100) * circumference;
  loaderProgress.style.strokeDashoffset = offset;
  
  if (count >= 100) {{
    clearInterval(loaderInterval);
    setTimeout(() => {{
      loader.classList.add('loaded');
    }}, 280);
  }}
}}, 28);

// ---------- MENU DRAWER
const menuDrawer = document.getElementById('menuDrawer');
const openMenuBtn = document.getElementById('openMenuBtn');
const closeMenuBtn = document.getElementById('closeMenuBtn');
openMenuBtn.onclick = () => menuDrawer.classList.add('open');
closeMenuBtn.onclick = () => menuDrawer.classList.remove('open');
document.querySelectorAll('.nav-jump').forEach(link => {{
  link.onclick = () => menuDrawer.classList.remove('open');
}});

// ---------- FAQ ACCORDION
document.querySelectorAll('.faq-accordion-item').forEach(item => {{
  const btn = item.querySelector('.faq-accordion-btn');
  btn.onclick = () => {{
    const isActive = item.classList.contains('active');
    document.querySelectorAll('.faq-accordion-item').forEach(i => i.classList.remove('active'));
    if (!isActive) item.classList.add('active');
  }};
}});

// ---------- MODAL CONTROLLERS
const resumeModal = document.getElementById('resumeModal');
function openResumeModal() {{ resumeModal.classList.add('open'); }}
function closeResumeModal() {{ resumeModal.classList.remove('open'); }}

const projectModal = document.getElementById('projectModal');
const pModalTag = document.getElementById('pModalTag');
const pModalTitle = document.getElementById('pModalTitle');
const pModalBody = document.getElementById('pModalBody');
const pModalLink = document.getElementById('pModalLink');

const PROJECTS_DATA = {{
  evolutionary: {{
    tag: 'Quantitative Finance · Genetic Algorithms',
    title: 'Evolutionary Trading System',
    body: `<p>An autonomous trading engine that evolves trading strategies using genetic algorithm optimization. Implements a proprietary <strong>"house money" capital preservation vault</strong> that dynamically siphons profits into a risk-free safe zone during high-volatility regimes.</p>
           <p><strong>Key Highlights:</strong><br/>
           • Multi-chromosome genetic encoding for entry, exit, stop-loss, and sizing rules.<br/>
           • Backtested across multi-year asset tick data using VectorBT.<br/>
           • Sharpe ratio improvement of 2.1x over baseline momentum benchmarks.</p>`,
    link: 'https://github.com/Nithillen/evolutionary_trading_system'
  }},
  pairs: {{
    tag: 'Statistical Arbitrage · Machine Learning',
    title: 'ML Pairs Trading Engine',
    body: `<p>A high-performance statistical arbitrage system combining Engle-Granger and Johansen cointegration tests with an XGBoost machine-learning classifier to predict spread mean-reversion probabilities.</p>
           <p><strong>Key Highlights:</strong><br/>
           • Dynamic z-score spread calculations with half-life Ornstein-Uhlenbeck parameterization.<br/>
           • Automated transaction cost and slippage modeling in VectorBT.<br/>
           • Consistent market-neutral alpha generation across divergent regimes.</p>`,
    link: 'https://github.com/Nithillen/pairs_trading_ml'
  }},
  readmission: {{
    tag: 'Healthcare ML · Explainable AI',
    title: 'Patient Readmission Risk Engine',
    body: `<p>An enterprise clinical risk stratification engine that predicts 30-day patient hospital readmissions. Features an automated SQL Common Table Expression (CTE) feature store and paired Random Forest and Gradient Boosting classifiers with exact TreeSHAP local interpretability.</p>
           <p><strong>Key Highlights:</strong><br/>
           • Advanced SQL CTE pipeline aggregating clinical records and lab temporal dynamics.<br/>
           • High AUC-ROC performance with calibrated clinical probability scores.<br/>
           • SHAP waterfall plots provided to clinicians to eliminate black-box opacity.</p>`,
    link: 'https://github.com/Nithillen/patient_readmission_engine'
  }},
  cassandra: {{
    tag: 'Distributed Systems · Database Engineering',
    title: 'Cassandra Consistency Study',
    body: `<p>A rigorous empirical benchmarking suite analyzing Apache Cassandra’s tunable consistency levels (ONE, QUORUM, ALL) across multi-node topologies under simulated network latency and node partitioned states.</p>
           <p><strong>Key Highlights:</strong><br/>
           • Containerized multi-node Cassandra cluster configured via Docker Compose.<br/>
           • Latency, throughput, and read-repair cost evaluation under CAP theorem trade-offs.<br/>
           • Automated Python benchmarking harnesses with statistical variance analysis.</p>`,
    link: 'https://github.com/Nithillen/Cassandra-consistency-project'
  }},
  syncagent: {{
    tag: 'Enterprise AI · Viatris Clinical & Safety',
    title: 'SyncAgent Agentic AI Workflow',
    body: `<p>Architected and deployed during my role at Viatris in the Clinical & Safety domain. SyncAgent is a multi-agent orchestration pipeline designed to cross-verify regulatory documentation and compliance dossiers.</p>
           <p><strong>Key Highlights:</strong><br/>
           • Accelerated document turnaround time by <strong>&gt;40%</strong> while maintaining zero-defect audit integrity.<br/>
           • Migrated DAERS safety reporting pipelines onto Azure Cloud and Oracle SQL.<br/>
           • Integrated conversational voice bots for the medical call center and automated meeting workflows.</p>`,
    link: 'https://www.linkedin.com/in/nithillenjayaseelan/'
  }},
  patent: {{
    tag: 'Granted Indian Patent · Research Publication',
    title: '5G ML Dynamic Allocation & PPG Biometrics',
    body: `<p><strong>Granted Indian Patent</strong>: Developed non-linear machine learning architectures (Random Forest, Gradient Boosting, XGBoost) for real-time radio resource allocation in 5G wireless networks, achieving an exceptional fit of <strong>R² = 0.982</strong>.</p>
           <p><strong>Peer-Reviewed Publication</strong>: Authored research on Photoplethysmography (PPG) pulse wave signal analysis for non-invasive biometric user authentication.<br/>
           <strong>Google Externship</strong>: Machine-learning classification of genetic variants from the ClinVar dataset.</p>`,
    link: 'https://www.linkedin.com/in/nithillenjayaseelan/'
  }}
}};

function openProjectModal(key) {{
  const data = PROJECTS_DATA[key];
  if (!data) return;
  pModalTag.textContent = data.tag;
  pModalTitle.textContent = data.title;
  pModalBody.innerHTML = data.body;
  pModalLink.href = data.link;
  projectModal.classList.add('open');
}}
function closeProjectModal() {{ projectModal.classList.remove('open'); }}

// ---------- HERO GENERATIVE CANVASES (INTERACTIVE MARKET SIGNAL MATRIX)
const heroCanvas = document.getElementById('heroCanvas');
const ctx = heroCanvas.getContext('2d');

let width, height;
function resizeHero() {{
  width = heroCanvas.width = heroCanvas.offsetWidth;
  height = heroCanvas.height = heroCanvas.offsetHeight;
}}
resizeHero();
window.addEventListener('resize', resizeHero);

const nodes = [];
const nodeCount = 58;
for (let i = 0; i < nodeCount; i++) {{
  nodes.push({{
    x: Math.random() * (width || 800),
    y: Math.random() * (height || 500),
    vx: (Math.random() - 0.5) * 0.7,
    vy: (Math.random() - 0.5) * 0.7,
    r: Math.random() * 2 + 1.5,
    hue: Math.random() < 0.3 ? '#22c55e' : (Math.random() < 0.5 ? '#60a5fa' : '#94a3b8')
  }});
}}

let mouseX = -999, mouseY = -999;
heroCanvas.addEventListener('mousemove', e => {{
  const rect = heroCanvas.getBoundingClientRect();
  mouseX = e.clientX - rect.left;
  mouseY = e.clientY - rect.top;
}});
heroCanvas.addEventListener('mouseleave', () => {{
  mouseX = -999;
  mouseY = -999;
}});

function drawHero() {{
  ctx.fillStyle = '#141416';
  ctx.fillRect(0, 0, width, height);

  // Grid background lines
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
  ctx.lineWidth = 1;
  const gridSize = 40;
  for (let x = 0; x < width; x += gridSize) {{
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, height);
    ctx.stroke();
  }}
  for (let y = 0; y < height; y += gridSize) {{
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(width, y);
    ctx.stroke();
  }}

  // Update & connect nodes
  for (let i = 0; i < nodes.length; i++) {{
    const a = nodes[i];
    a.x += a.vx;
    a.y += a.vy;

    if (a.x < 0 || a.x > width) a.vx *= -1;
    if (a.y < 0 || a.y > height) a.vy *= -1;

    // Mouse attraction
    const dmx = mouseX - a.x, dmy = mouseY - a.y;
    const dmouse = Math.sqrt(dmx * dmx + dmy * dmy);
    if (dmouse < 160) {{
      a.x += (dmx / dmouse) * 0.8;
      a.y += (dmy / dmouse) * 0.8;
    }}

    // Draw node
    ctx.beginPath();
    ctx.arc(a.x, a.y, a.r, 0, Math.PI * 2);
    ctx.fillStyle = a.hue;
    ctx.fill();

    for (let j = i + 1; j < nodes.length; j++) {{
      const b = nodes[j];
      const dx = a.x - b.x, dy = a.y - b.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 130) {{
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.strokeStyle = `rgba(240, 240, 238, ${{((1 - dist / 130) * 0.22).toFixed(3)}})`;
        ctx.stroke();
      }}
    }}
  }}

  requestAnimationFrame(drawHero);
}}
requestAnimationFrame(drawHero);

// ---------- MINI CARD GENERATIVE CANVASES
function initCardCanvas(id, drawFn) {{
  const c = document.getElementById(id);
  if (!c) return;
  const w = c.width = c.offsetWidth || 400;
  const h = c.height = c.offsetHeight || 250;
  const cx = c.getContext('2d');
  drawFn(cx, w, h);
}}

window.addEventListener('load', () => {{
  // Card 1: Evolutionary Trading Candlesticks & Chromosome curve
  initCardCanvas('cardCanvas1', (cx, w, h) => {{
    cx.fillStyle = '#161618'; cx.fillRect(0, 0, w, h);
    // Draw upward financial chart
    cx.strokeStyle = '#22c55e'; cx.lineWidth = 2.5;
    cx.beginPath();
    let cy = h * 0.75;
    cx.moveTo(20, cy);
    for (let x = 40; x < w - 20; x += 24) {{
      cy += (Math.random() - 0.62) * 28;
      cy = Math.max(30, Math.min(h - 30, cy));
      cx.lineTo(x, cy);
    }}
    cx.stroke();
    // Candlesticks
    for (let x = 30; x < w - 30; x += 32) {{
      const open = h * 0.4 + (Math.random() - 0.5) * 50;
      const close = open + (Math.random() - 0.45) * 35;
      const isUp = close < open;
      cx.strokeStyle = isUp ? '#22c55e' : '#ef4444';
      cx.fillStyle = isUp ? '#22c55e' : '#ef4444';
      cx.beginPath(); cx.moveTo(x + 4, open - 12); cx.lineTo(x + 4, close + 12); cx.stroke();
      cx.fillRect(x, Math.min(open, close), 8, Math.max(4, Math.abs(close - open)));
    }}
  }});

  // Card 2: Cointegration Spread & Mean Reversion bands
  initCardCanvas('cardCanvas2', (cx, w, h) => {{
    cx.fillStyle = '#161618'; cx.fillRect(0, 0, w, h);
    const mid = h * 0.5;
    cx.strokeStyle = 'rgba(255,255,255,0.15)'; cx.setLineDash([4, 4]);
    cx.beginPath(); cx.moveTo(0, mid - 40); cx.lineTo(w, mid - 40); cx.moveTo(0, mid + 40); cx.lineTo(w, mid + 40); cx.stroke();
    cx.setLineDash([]);
    cx.strokeStyle = 'rgba(255,255,255,0.4)';
    cx.beginPath(); cx.moveTo(0, mid); cx.lineTo(w, mid); cx.stroke();
    // Spread oscillator
    cx.strokeStyle = '#38bdf8'; cx.lineWidth = 2.5;
    cx.beginPath();
    for (let x = 0; x < w; x += 5) {{
      const y = mid + Math.sin(x * 0.045) * 38 + Math.sin(x * 0.12) * 12;
      if (x === 0) cx.moveTo(x, y); else cx.lineTo(x, y);
    }}
    cx.stroke();
  }});

  // Card 3: Patient Readmission SHAP waterfall bars
  initCardCanvas('cardCanvas3', (cx, w, h) => {{
    cx.fillStyle = '#161618'; cx.fillRect(0, 0, w, h);
    const bars = [
      {{ l: 'Prior Readmissions', v: 85, c: '#ef4444' }},
      {{ l: 'HbA1c Level', v: 65, c: '#ef4444' }},
      {{ l: 'Length of Stay', v: -45, c: '#3b82f6' }},
      {{ l: 'Comorbidity Index', v: 52, c: '#ef4444' }},
      {{ l: 'Outpatient Visits', v: -30, c: '#3b82f6' }}
    ];
    const barH = 22, midX = w * 0.45;
    bars.forEach((b, i) => {{
      const y = 30 + i * 36;
      cx.fillStyle = 'rgba(255,255,255,0.5)';
      cx.font = '10px monospace';
      cx.textAlign = 'right';
      cx.fillText(b.l, midX - 10, y + 15);
      cx.fillStyle = b.c;
      if (b.v > 0) {{
        cx.fillRect(midX, y, b.v * 1.5, barH);
      }} else {{
        cx.fillRect(midX + b.v * 1.5, y, -b.v * 1.5, barH);
      }}
    }});
  }});

  // Card 4: Cassandra Cluster Nodes
  initCardCanvas('cardCanvas4', (cx, w, h) => {{
    cx.fillStyle = '#161618'; cx.fillRect(0, 0, w, h);
    const ringR = 75, cx0 = w * 0.5, cy0 = h * 0.5;
    cx.strokeStyle = 'rgba(255,255,255,0.18)';
    cx.beginPath(); cx.arc(cx0, cy0, ringR, 0, Math.PI * 2); cx.stroke();
    const nodeCount = 6;
    for (let i = 0; i < nodeCount; i++) {{
      const angle = (i / nodeCount) * Math.PI * 2;
      const nx = cx0 + Math.cos(angle) * ringR;
      const ny = cy0 + Math.sin(angle) * ringR;
      cx.fillStyle = '#a855f7';
      cx.beginPath(); cx.arc(nx, ny, 10, 0, Math.PI * 2); cx.fill();
      cx.fillStyle = '#fff';
      cx.beginPath(); cx.arc(nx, ny, 4, 0, Math.PI * 2); cx.fill();
    }}
  }});

  // Card 5: SyncAgent Multi-Agent Workflow DAG
  initCardCanvas('cardCanvas5', (cx, w, h) => {{
    cx.fillStyle = '#161618'; cx.fillRect(0, 0, w, h);
    const steps = [
      {{ x: w * 0.18, y: h * 0.5, name: 'Parser' }},
      {{ x: w * 0.42, y: h * 0.3, name: 'SyncAgent' }},
      {{ x: w * 0.42, y: h * 0.7, name: 'DAERS' }},
      {{ x: w * 0.74, y: h * 0.5, name: 'Compliance' }}
    ];
    cx.strokeStyle = 'rgba(255,255,255,0.3)'; cx.lineWidth = 2;
    cx.beginPath();
    cx.moveTo(steps[0].x, steps[0].y); cx.lineTo(steps[1].x, steps[1].y);
    cx.moveTo(steps[0].x, steps[0].y); cx.lineTo(steps[2].x, steps[2].y);
    cx.lineTo(steps[3].x, steps[3].y);
    cx.moveTo(steps[1].x, steps[1].y); cx.lineTo(steps[3].x, steps[3].y);
    cx.stroke();
    steps.forEach(s => {{
      cx.fillStyle = '#06b6d4';
      cx.beginPath(); cx.arc(s.x, s.y, 14, 0, Math.PI * 2); cx.fill();
      cx.fillStyle = '#fff';
      cx.font = '10px monospace';
      cx.textAlign = 'center';
      cx.fillText(s.name, s.x, s.y - 18);
    }});
  }});

  // Card 6: 5G Resource Allocation R^2 = 0.982 & PPG Wave
  initCardCanvas('cardCanvas6', (cx, w, h) => {{
    cx.fillStyle = '#161618'; cx.fillRect(0, 0, w, h);
    // PPG pulse wave
    cx.strokeStyle = '#f59e0b'; cx.lineWidth = 2.5;
    cx.beginPath();
    for (let x = 0; x < w; x++) {{
      const phase = (x % 90) / 90;
      let y = h * 0.5;
      if (phase < 0.2) y -= Math.sin(phase / 0.2 * Math.PI) * 45;
      else if (phase < 0.4) y += Math.sin((phase - 0.2) / 0.2 * Math.PI) * 15;
      else y += Math.sin((phase - 0.4) / 0.6 * Math.PI) * 8;
      if (x === 0) cx.moveTo(x, y); else cx.lineTo(x, y);
    }}
    cx.stroke();
    cx.fillStyle = 'rgba(255,255,255,0.7)';
    cx.font = '12px monospace';
    cx.fillText('Granted Patent · R² = 0.982', 20, 35);
  }});
}});
</script>
</body>
</html>'''

# Write to scratch workspace and brain artifact directory
# Write to editorial repository, portfolio mirror, and brain artifact directory
paths = [
  os.path.join(os.path.dirname(__file__), 'index.html'),
  '/Users/nithillenj/.gemini/antigravity/scratch/portfolio/editorial_portfolio.html',
  '/Users/nithillenj/.gemini/antigravity/brain/63f5e2ad-7b8e-43c6-9e73-1e20b71ddee1/editorial_portfolio.html'
]

for p in paths:
  os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
  with open(p, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)
  print(f'Successfully wrote {len(HTML_CONTENT):,} bytes -> {p}')
