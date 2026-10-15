from flask import Flask, render_template_string, jsonify

import os



app = Flask(__name__)



# =====================================================

# GYM CONFIGURATION — CUSTOMIZE THESE DETAILS

# =====================================================



GYM_NAME = "IRON PEAK FITNESS"

GYM_TAGLINE = "BUILT BY DISCIPLINE. DEFINED BY STRENGTH."



GYM_PHONE = "918889056138"       # Country code + number

GYM_EMAIL = "hello@example.com"

GYM_ADDRESS = "Vijay Nagar, Indore, Madhya Pradesh"

GYM_MAPS_URL = (

    "https://www.google.com/maps/search/"

    "?api=1&query=Vijay+Nagar+Indore+Madhya+Pradesh"

)

INSTAGRAM_URL = "https://www.instagram.com/"
FACEBOOK_URL = "https://www.facebook.com/"


# Sample service prices in INR

SERVICES = {

    "General Gym Access": 1000,

    "Cardio Zone": 700,

    "CrossFit": 1500,

    "Zumba": 800,

    "Yoga": 600,

    "HIIT Conditioning": 1200

}



# Sample trainer prices in INR per month

TRAINERS = {

    "No Personal Trainer": 0,

    "Rahul Sharma": 2000,

    "Priya Verma": 1800,

    "Arjun Mehta": 2200

}



# Sample trainer information

TRAINER_DETAILS = [

    {

        "name": "Rahul Sharma",

        "specialty": "STRENGTH & MUSCLE BUILDING",

        "phone": "919876543211",

        "image": (

            "https://images.unsplash.com/"

            "photo-1567013127542-490d757e51fc"

            "?auto=format&fit=crop&w=700&q=85"

        ),

        "description": (

            "Build strength, improve technique, "

            "and develop a stronger physique."

        )

    },

    {

        "name": "Priya Verma",

        "specialty": "FAT LOSS & ZUMBA",

        "phone": "919876543212",

        "image": (

            "https://images.unsplash.com/"

            "photo-1546483875-ad9014c88eba"

            "?auto=format&fit=crop&w=700&q=85"

        ),

        "description": (

            "Improve fitness, build consistency, "

            "and enjoy energetic training sessions."

        )

    },

    {

        "name": "Arjun Mehta",

        "specialty": "FUNCTIONAL FITNESS & HIIT",

        "phone": "918889056138",

        "image": (

            "https://images.unsplash.com/"

            "photo-1581009146145-b5ef050c2e1e"

            "?auto=format&fit=crop&w=700&q=85"

        ),

        "description": (

            "Boost speed, stamina, and athletic performance "

            "with focused functional training."

        )

    }

]



# Plan durations

PLAN_MULTIPLIERS = {

    "weekly": 0.35,

    "monthly": 1,

    "yearly": 10

}



# =====================================================

# SINGLE PAGE WEBSITE

# =====================================================



HTML = r"""

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1">



<title>{{ gym_name }} | Premium Fitness Club</title>



<meta name="description"

content="Train stronger, move better, and reach your fitness goals with {{ gym_name }}.">



<link rel="preconnect" href="https://fonts.googleapis.com">

<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>



<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&display=swap"

rel="stylesheet">



<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"

rel="stylesheet">



<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"

rel="stylesheet">



<style>

:root {

    --bg: #0a0a0a;

    --panel: #101010;

    --panel-light: #151515;

    --accent: #c8ff32;

    --text: #f6f6f6;

    --muted: #a3a3a3;

    --border: rgba(255,255,255,.10);

}



* {

    box-sizing: border-box;

}



html {

    scroll-behavior: smooth;

    scroll-padding-top: 85px;

}



body {

    margin: 0;

    background:

        radial-gradient(circle at 8% 10%, rgba(200,255,50,.07), transparent 25rem),

        radial-gradient(circle at 92% 45%, rgba(200,255,50,.045), transparent 22rem),

        var(--bg);

    color: var(--text);

    font-family: 'Inter', sans-serif;

    overflow-x: hidden;

}



a {

    text-decoration: none;

}



section {

    padding: 100px 0;

}



.section-label {

    color: var(--accent);

    font-size: 12px;

    font-weight: 800;

    letter-spacing: 3px;

    text-transform: uppercase;

}



.section-title {

    font-family: 'Barlow Condensed', sans-serif;

    font-size: clamp(42px, 6vw, 68px);

    font-weight: 800;

    line-height: .98;

    text-transform: uppercase;

    margin: 16px 0;

    position: relative;

}



.section-title:after {

    background: var(--accent);

    content: "";

    display: block;

    height: 4px;

    margin-top: 22px;

    width: 58px;

}



.section-description {

    color: var(--muted);

    line-height: 1.8;

    max-width: 580px;

}



.btn-accent {

    display: inline-flex;

    align-items: center;

    justify-content: center;

    gap: 10px;

    padding: 15px 24px;

    border: 1px solid var(--accent);

    background: var(--accent);

    color: #101010;

    font-weight: 800;

    text-transform: uppercase;

    font-size: 12px;

    letter-spacing: 1px;

    transition: .25s;

}



.btn-accent:hover {

    background: transparent;

    color: var(--accent);

    transform: translateY(-3px);

}



.btn-outline-light-custom {

    display: inline-flex;

    align-items: center;

    gap: 10px;

    padding: 15px 24px;

    border: 1px solid rgba(255,255,255,.45);

    color: white;

    font-size: 12px;

    font-weight: 700;

    text-transform: uppercase;

    transition: .25s;

}



.btn-outline-light-custom:hover {

    background: white;

    color: black;

}



/* NAVIGATION */



.navbar {

    background: rgba(8,8,8,.94);

    border-bottom: 1px solid var(--border);

    padding: 17px 0;

    backdrop-filter: blur(15px);

}



.navbar-brand {

    color: white !important;

    font-family: 'Barlow Condensed', sans-serif;

    font-size: 28px;

    font-weight: 900;

    letter-spacing: 1px;

}



.brand-mark {

    color: var(--accent);

}



.navbar .nav-link {

    color: #d0d0d0;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 1px;

    text-transform: uppercase;

    margin: 0 8px;

}



.navbar .nav-link:hover {

    color: var(--accent);

}



.navbar-toggler {

    border-color: #555;

}



.navbar-toggler-icon {

    filter: invert(1);

}



/* HERO */



.hero {

    min-height: 92vh;

    display: flex;

    align-items: center;

    position: relative;

    background:

        linear-gradient(90deg, rgba(0,0,0,.95) 0%,

        rgba(0,0,0,.73) 48%, rgba(0,0,0,.25) 100%),

        linear-gradient(0deg, var(--bg), transparent 25%),

        url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=2200&q=90')

        center 40% / cover no-repeat;

    padding-top: 100px;

}



.hero-content {

    max-width: 780px;

    padding: 70px 0;

}



.hero-eyebrow {

    display: inline-flex;

    align-items: center;

    gap: 10px;

    color: var(--accent);

    font-size: 12px;

    font-weight: 800;

    letter-spacing: 3px;

    margin-bottom: 25px;

}



.hero-eyebrow:before {

    content: "";

    width: 35px;

    height: 2px;

    background: var(--accent);

}



.hero h1 {

    font-family: 'Barlow Condensed', sans-serif;

    font-size: clamp(65px, 11vw, 125px);

    line-height: .83;

    font-weight: 900;

    text-transform: uppercase;

    letter-spacing: -2px;

    margin-bottom: 30px;

}



.hero h1 span {

    color: var(--accent);

}



.hero p {

    max-width: 530px;

    color: #d0d0d0;

    line-height: 1.9;

    font-size: 15px;

    margin-bottom: 30px;

}



.hero-actions {

    display: flex;

    flex-wrap: wrap;

    gap: 12px;

}



.hero-note {

    margin-top: 50px;

    color: #c4c4c4;

    font-size: 11px;

    letter-spacing: 2px;

    text-transform: uppercase;

}



/* STATS */



.stats-strip {

    background: var(--accent);

    color: #101010;

    padding: 27px 0;

}



.stat-item {

    text-align: center;

    padding: 10px;

}



.stat-number {

    font-family: 'Barlow Condensed', sans-serif;

    font-size: 35px;

    font-weight: 900;

}



.stat-label {

    font-size: 10px;

    letter-spacing: 1.5px;

    font-weight: 800;

    text-transform: uppercase;

}



/* ABOUT */



.about-image {

    width: 100%;

    height: 480px;

    object-fit: cover;

    border-radius: 3px;

    filter: grayscale(35%);

}



.about-image-wrap {

    position: relative;

}



.about-image-wrap:after {

    content: "";

    position: absolute;

    inset: 18px -18px -18px 18px;

    border: 1px solid var(--accent);

    z-index: -1;

}



.feature-list {

    margin-top: 28px;

}



.feature-item {

    display: flex;

    align-items: flex-start;

    gap: 15px;

    margin-bottom: 22px;

}



.feature-icon {

    width: 42px;

    height: 42px;

    flex-shrink: 0;

    display: grid;

    place-items: center;

    background: rgba(200,255,50,.10);

    color: var(--accent);

}



.feature-item h4 {

    font-size: 14px;

    font-weight: 800;

    margin: 0 0 7px;

}



.feature-item p {

    color: var(--muted);

    font-size: 12px;

    line-height: 1.7;

    margin: 0;

}



/* SERVICES */



.services-section {

    background: #101010;

}



.service-card {

    background: var(--panel);

    border: 1px solid var(--border);

    box-shadow: 0 15px 35px rgba(0,0,0,.18);

    height: 100%;

    overflow: hidden;

    transition: transform .3s, border-color .3s;

}



.service-card:hover {

    transform: translateY(-8px);

    border-color: var(--accent);

}



.service-image {

    width: 100%;

    height: 240px;

    object-fit: cover;

    filter: grayscale(30%);

    transition: .5s;

}



.service-card:hover .service-image {

    filter: grayscale(0%);

    transform: scale(1.035);

}



.service-image-wrap {

    overflow: hidden;

}



.service-content {

    padding: 25px;

}



.service-content h3 {

    font-family: 'Barlow Condensed', sans-serif;

    font-size: 27px;

    font-weight: 800;

    text-transform: uppercase;

}



.service-content p {

    color: var(--muted);

    font-size: 12px;

    line-height: 1.8;

}



.service-price {

    color: var(--accent);

    font-size: 12px;

    font-weight: 800;

    margin-top: 18px;

}



/* TRAINERS */



.trainer-card {

    background: var(--panel);

    border: 1px solid var(--border);

    overflow: hidden;

    box-shadow: 0 15px 35px rgba(0,0,0,.18);

    height: 100%;

    transition: .3s;

}



.trainers-row {

    align-items: stretch;

}



.trainer-card:hover {

    border-color: var(--accent);

    transform: translateY(-5px);

}



.trainer-image {

    width: 100%;

    height: 300px;

    object-fit: cover;

    object-position: center;

    filter: grayscale(25%);

}



.trainer-content {

    padding: 20px;

}



.trainer-content h3 {

    font-family: 'Barlow Condensed', sans-serif;

    font-size: 26px;

    font-weight: 800;

    text-transform: uppercase;

}



.trainer-specialty {

    color: var(--accent);

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1px;

}



.trainer-description {

    color: var(--muted);

    font-size: 12px;

    line-height: 1.8;

    margin-top: 10px;

}



.trainer-actions {

    margin-top: 16px;

}



.book-trainer {

    background: var(--accent);

    border: 0;

    color: #101010;

    display: block;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: .5px;

    padding: 12px;

    text-align: center;

    text-transform: uppercase;

    transition: background .2s, transform .2s;

    width: 100%;

}



.book-trainer:hover {

    background: #fff;

    color: #101010;

    transform: translateY(-2px);

}



.trainer-actions a {

    color: #101010;

}



/* GALLERY */



.gallery-section {

    background: #101010;

}



.gallery-grid {

    display: grid;

    grid-template-columns: repeat(4, 1fr);

    grid-auto-rows: 210px;

    gap: 12px;

}



.gallery-item {

    position: relative;

    overflow: hidden;

    background: #222;

    border: 1px solid transparent;

    transition: border-color .3s;

}



.gallery-item:first-child {

    grid-column: span 2;

    grid-row: span 2;

}



.gallery-item img {

    width: 100%;

    height: 100%;

    object-fit: cover;

    transition: transform .5s;

    filter: grayscale(25%);

}



.gallery-item:hover img {

    transform: scale(1.08);

    filter: grayscale(0%);

}



.gallery-item:hover {

    border-color: var(--accent);

}



.gallery-caption {

    position: absolute;

    inset: auto 0 0;

    padding: 35px 15px 15px;

    background: linear-gradient(transparent, rgba(0,0,0,.9));

    font-size: 12px;

    font-weight: 800;

    letter-spacing: 1px;

    text-transform: uppercase;

}



/* PLAN BUILDER */



.plan-section {

    background:

        radial-gradient(circle at 100% 0%,

        rgba(200,255,50,.07), transparent 40%),

        var(--bg);

}



.plan-form,
.price-summary {
    padding: 26px;
    background: linear-gradient(145deg, #171717, #0e0e0e);
    border: 1px solid var(--border);
    border-radius: 14px;
    height: 100%;
    box-shadow: 0 18px 45px rgba(0,0,0,.22);
}

.form-label-custom {

    display: block;

    color: #ddd;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 1px;

    text-transform: uppercase;

    margin-bottom: 12px;

}



.custom-select,

.custom-input {

    width: 100%;

    background: #0b0b0b;

    border: 1px solid #383838;

    color: white;

    border-radius: 0;

    padding: 14px;

    margin-bottom: 25px;

    outline: none;

}



.custom-select:focus,

.custom-input:focus {

    border-color: var(--accent);

}



.service-checks {

    display: grid;

    grid-template-columns: repeat(2, 1fr);

    gap: 10px;

    margin-bottom: 25px;

}



.trainer-checks {

    display: grid;

    gap: 10px;

    grid-template-columns: repeat(2, 1fr);

    margin-bottom: 25px;

}



.trainer-check {

    align-items: center;

    background: #0b0b0b;

    border: 1px solid #333;

    cursor: pointer;

    display: flex;

    font-size: 12px;

    gap: 9px;

    padding: 12px;

}



.trainer-check:has(input:checked),

.service-check:has(input:checked) {

    border-color: var(--accent);

    background: rgba(200,255,50,.08);

}



.trainer-check input {

    accent-color: var(--accent);

}



.service-check {

    display: flex;

    align-items: center;

    gap: 9px;

    background: #0b0b0b;

    border: 1px solid #333;

    padding: 12px;

    font-size: 12px;

    cursor: pointer;

}



.service-check input {

    accent-color: var(--accent);

}



.price-summary h3 {

    font-family: 'Barlow Condensed', sans-serif;

    font-size: 32px;

    font-weight: 800;

    text-transform: uppercase;

    margin-bottom: 25px;

}



.price-row {

    display: flex;

    justify-content: space-between;

    gap: 12px;

    color: #c0c0c0;

    font-size: 12px;

    padding: 14px 0;

    border-bottom: 1px solid var(--border);

}



.price-row strong {

    color: white;

    text-align: right;

}



.price-row.total {

    font-size: 16px;

    color: white;

    font-weight: 800;

    border-bottom: none;

    padding-top: 22px;

}



.price-row.total strong {

    color: var(--accent);

    font-size: 23px;

}



.price-note {

    color: #929292;

    font-size: 11px;

    line-height: 1.8;

    margin-top: 20px;

}



/* CONTACT */



.contact-section {

    background: #111;

}



.contact-card {

    align-items: center;

    background: transparent;

    border: 0;

    display: flex;

    flex-direction: column;

    justify-content: center;

    padding: 10px;

    height: 100%;

}



.contact-icon {

    align-items: center;

    background: var(--accent);

    border-radius: 50%;

    color: var(--accent);

    display: inline-flex;

    font-size: 23px;

    height: 64px;

    justify-content: center;

    margin-bottom: 20px;

    transition: transform .2s ease, background .2s ease;

    width: 64px;

}



.quick-contact {

    align-items: center;

    display: flex;

    gap: 14px;

    justify-content: flex-end;

    padding-top: 8px;

}



.quick-contact .contact-icon {

    margin: 0;

}



.location-box {

    align-items: center;

    background: #111;

    border: 1px solid var(--accent);

    color: var(--text);

    display: flex;

    gap: 18px;

    justify-content: space-between;

    padding: 24px;

    text-decoration: none;

}



.location-box:hover {

    color: var(--text);

}



.location-box-icon {

    align-items: center;

    background: var(--accent);

    border-radius: 50%;

    color: #111;

    display: flex;

    flex: 0 0 52px;

    font-size: 20px;

    height: 52px;

    justify-content: center;

    width: 52px;

}



.location-box-label {

    color: var(--accent);

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1.5px;

}



.location-box h3 {

    font-family: 'Barlow Condensed', sans-serif;

    font-size: 26px;

    margin: 4px 0;

    text-transform: uppercase;

}



.location-box p {

    color: var(--muted);

    font-size: 12px;

    margin: 0;

}



.location-box-button {

    background: var(--accent);

    color: #111;

    font-size: 10px;

    font-weight: 800;

    padding: 12px 14px;

    white-space: nowrap;

}



.contact-card h4,

.contact-card p,

.contact-card > a:not(.contact-icon) {

    display: none;

}



.contact-card .contact-icon {

    margin-bottom: 0;

}



.contact-icon i {

    color: #111;

}



.contact-action:hover .contact-icon,

.contact-card:hover .contact-icon {

    background: #fff;

    color: #111;

    transform: scale(1.08);

}



.contact-card h4 {

    font-size: 14px;

    font-weight: 800;

    margin-bottom: 12px;

}



.contact-card p,

.contact-card a {

    color: var(--muted);

    font-size: 12px;

    line-height: 1.8;

    overflow-wrap: anywhere;

}



.contact-action {

    color: inherit;

    display: block;

    text-decoration: none;

}



.contact-action a {

    color: var(--muted);

}



.contact-card a:hover {

    color: var(--accent);

}



/* FOOTER */
footer {
    background:
        radial-gradient(circle at 10% 0%, rgba(200,255,50,.07), transparent 24rem),
        #070707;
    border-top: 1px solid var(--border);
    padding: 58px 0 24px;
}

.footer-brand {
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 30px;
    font-weight: 900;
    letter-spacing: .5px;
}

.footer-description {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.8;
    max-width: 360px;
    margin-top: 14px;
}

.footer-map-wrap {
    margin-top: 18px;
    overflow: hidden;
    border: 1px solid rgba(200,255,50,.35);
    border-radius: 12px;
    background: #111;
    box-shadow: 0 18px 42px rgba(0,0,0,.25);
}

.footer-map-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 12px 16px;
    color: #fff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
}

.footer-map-heading i { color: var(--accent); font-size: 17px; }

.footer-map {
    display: block;
    width: 100%;
    height: 185px;
    border: 0;
    filter: grayscale(1) invert(.88) contrast(.88);
}

.footer-location {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 16px;
    background: #101010;
    border-top: 1px solid var(--border);
}

.footer-location-icon {
    display: grid;
    place-items: center;
    flex: 0 0 40px;
    width: 40px;
    height: 40px;
    border-radius: 9px;
    color: #101010;
    background: var(--accent);
    font-size: 19px;
}

.footer-location-label {
    color: var(--accent);
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.footer-location p {
    color: #d0d0d0;
    font-size: 12px;
    margin: 0;
    line-height: 1.6;
}

.footer-map-button {
    margin-left: auto;
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 12px;
    border-radius: 7px;
    background: var(--accent);
    color: #101010;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: .5px;
    text-transform: uppercase;
    transition: .2s;
}
.footer-map-button:hover { background: #fff; color: #111; }

.footer-contact-title {
    color: #fff;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 25px;
    font-weight: 800;
    text-transform: uppercase;
    margin: 0 0 16px;
}

.footer-contact-links {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

.footer-contact-link {
    display: grid;
    place-items: center;
    width: 42px;
    height: 42px;
    padding: 0;
    border: 1px solid rgba(200,255,50,.3);
    border-radius: 11px;
    color: var(--accent);
    background: rgba(200,255,50,.08);
    font-size: 17px;
    transition: .2s;
}
.footer-contact-link i {
    color: inherit;
}
.footer-contact-link:hover {
    color: #111;
    border-color: var(--accent);
    background: var(--accent);
    transform: translateY(-2px);
}

.footer-social {
    display: flex;
    gap: 10px;
    margin-top: 22px;
}
.footer-social a {
    display: grid;
    place-items: center;
    width: 42px;
    height: 42px;
    border: 1px solid rgba(200,255,50,.3);
    border-radius: 11px;
    background: rgba(200,255,50,.08);
    color: var(--accent);
    font-size: 17px;
    transition: .2s;
}
.footer-social a:hover {
    color: #111;
    background: var(--accent);
    transform: translateY(-3px);
}

.footer-bottom {
    border-top: 1px solid var(--border);
    margin-top: 30px;
    padding-top: 20px;
    color: #777;
    font-size: 11px;
}
.footer-bottom a { text-decoration: none; }

/* ANIMATIONS */



.reveal {

    opacity: 0;

    transform: translateY(25px);

    transition: opacity .7s ease, transform .7s ease;

}



.reveal.visible {

    opacity: 1;

    transform: translateY(0);

}



@media (prefers-reduced-motion: reduce) {

    html {

        scroll-behavior: auto;

    }



    *, *::before, *::after {

        animation-duration: .01ms !important;

        transition-duration: .01ms !important;

    }



    .reveal {

        opacity: 1;

        transform: none;

    }

}



/* RESPONSIVE */



@media (max-width: 991px) {

    section {

        padding: 75px 0;

    }



    .hero {

        min-height: 80vh;

        background-position: 60% center;

    }



    .about-image {

        height: 400px;

    }



    .gallery-grid {

        grid-template-columns: repeat(2, 1fr);

        grid-auto-rows: 190px;

    }



    .gallery-item:first-child {

        grid-column: span 2;

        grid-row: span 1;

    }

}



@media (max-width: 575px) {

    section {

        padding: 65px 0;

    }



    .hero {

        min-height: 78vh;

        background-position: 57% center;

    }



    .hero h1 {

        font-size: 65px;

    }



    .hero p {

        font-size: 13px;

    }



    .hero-actions a {

        width: 100%;

    }



    .about-image {

        height: 320px;

    }



    .about-image-wrap:after {

        inset: 10px -8px -10px 8px;

    }



    .gallery-grid {

        grid-auto-rows: 150px;

        gap: 8px;

    }



    .gallery-caption {

        font-size: 10px;

        padding: 25px 8px 8px;

    }



    .location-box {

        align-items: flex-start;

        flex-wrap: wrap;

        padding: 20px;

    }



    .location-box-button {

        margin-left: 70px;

        width: calc(100% - 70px);

    }



    .quick-contact {

        justify-content: center;

        padding-top: 0;

    }



    .plan-form,

    .price-summary {

        padding: 22px;

    }



    .service-checks {

        grid-template-columns: 1fr;

    }



    .stat-number {

        font-size: 27px;

    }



    .stat-label {

        font-size: 9px;

        letter-spacing: .5px;

    }

}


/* Final refinements: compact plan calculator and mobile-friendly footer */
.plan-section .section-title { margin-bottom: 12px; }
.plan-form .form-label-custom { margin-top: 3px; }
.service-check, .trainer-check { min-height: 48px; }
.price-summary { display: flex; flex-direction: column; justify-content: center; }
.price-summary .price-row.total { margin-top: 8px; }
.footer-map-wrap { width: 100%; }
.footer-map { min-height: 190px; }
.footer-contact-link:focus-visible, .footer-map-button:focus-visible,
.footer-social a:focus-visible { outline: 2px solid #fff; outline-offset: 3px; }

@media (max-width: 575px) {
    .plan-form, .price-summary { padding: 18px; }
    .plan-section .section-title { font-size: 48px; }
    .service-checks, .trainer-checks { grid-template-columns: 1fr; }
    .footer-map { height: 180px; min-height: 180px; }
    .footer-location { align-items: flex-start; flex-wrap: wrap; padding: 15px; }
    .footer-map-button { margin-left: 61px; }
    .footer-map-heading { align-items: flex-start; flex-direction: column; }
    .footer-social { gap: 10px; }
    .footer-social a { width: 40px; height: 40px; }
}
</style>

</head>



<body>



<!-- NAVIGATION -->

<nav class="navbar navbar-expand-lg navbar-dark fixed-top">

<div class="container">



<a class="navbar-brand" href="#home">

    <span class="brand-mark">◆</span>

    {{ gym_name }}

</a>



<button class="navbar-toggler" type="button"

data-bs-toggle="collapse" data-bs-target="#mainNav"

aria-controls="mainNav" aria-expanded="false"

aria-label="Toggle navigation">

    <span class="navbar-toggler-icon"></span>

</button>



<div class="collapse navbar-collapse" id="mainNav">

<ul class="navbar-nav ms-auto align-items-lg-center">



<li class="nav-item"><a class="nav-link" href="#home">Home</a></li>

<li class="nav-item"><a class="nav-link" href="#about">About</a></li>

<li class="nav-item"><a class="nav-link" href="#services">Services</a></li>

<li class="nav-item"><a class="nav-link" href="#trainers">Trainers</a></li>

<li class="nav-item"><a class="nav-link" href="#gallery">Gallery</a></li>



<li class="nav-item ms-lg-3 mt-3 mt-lg-0">

<a href="#plans" class="btn-accent">Join Now <i class="fa-solid fa-arrow-right"></i></a>

</li>



</ul>

</div>

</div>

</nav>



<!-- HERO -->

<section class="hero" id="home">

<div class="container">

<div class="hero-content">



<div class="hero-eyebrow">YOUR FITNESS. YOUR RULES.</div>



<h1>

PUSH<br>

YOUR<br>

<span>LIMITS.</span>

</h1>



<p>

{{ tagline }} Train with purpose, challenge your limits,

and become stronger every day in an environment built for progress.

</p>



<div class="hero-actions">

<a href="#plans" class="btn-accent">

Build Your Plan <i class="fa-solid fa-arrow-right"></i>

</a>



<a href="#services" class="btn-outline-light-custom">

Explore Training <i class="fa-solid fa-dumbbell"></i>

</a>

</div>



<div class="hero-note">

<i class="fa-solid fa-bolt" style="color:var(--accent)"></i>

&nbsp; NO SHORTCUTS. JUST RESULTS.

</div>



</div>

</div>

</section>



<!-- STATS -->

<div class="stats-strip">

<div class="container">

<div class="row">



<div class="col-4 stat-item">

<div class="stat-number">06+</div>

<div class="stat-label">Training Options</div>

</div>



<div class="col-4 stat-item">

<div class="stat-number">24/7</div>

<div class="stat-label">Fitness Mindset</div>

</div>



<div class="col-4 stat-item">

<div class="stat-number">100%</div>

<div class="stat-label">Focus on You</div>

</div>



</div>

</div>

</div>



<!-- ABOUT -->

<section id="about">

<div class="container">

<div class="row align-items-center g-5">



<div class="col-lg-6 reveal">

<div class="about-image-wrap me-lg-3">

<img class="about-image"

src="https://images.unsplash.com/photo-1571902943202-507ec2618e8f?auto=format&fit=crop&w=1100&q=85"

alt="Modern gym training area"

loading="lazy">

</div>

</div>



<div class="col-lg-6 reveal">



<div class="section-label">MORE THAN A GYM</div>



<h2 class="section-title">

TRAIN HARD.<br>

LIVE STRONG.

</h2>



<p class="section-description">

We believe fitness is a lifestyle, not a temporary goal.

Our training environment is designed to help you move better,

build confidence, and make progress at your own pace.

</p>



<div class="feature-list">



<div class="feature-item">

<div class="feature-icon"><i class="fa-solid fa-dumbbell"></i></div>

<div>

<h4>Training for Every Level</h4>

<p>Start where you are and build strength through consistent training.</p>

</div>

</div>



<div class="feature-item">

<div class="feature-icon"><i class="fa-solid fa-user-check"></i></div>

<div>

<h4>Trainer Guidance</h4>

<p>Choose personalized support for your fitness goals.</p>

</div>

</div>



<div class="feature-item">

<div class="feature-icon"><i class="fa-solid fa-heart-pulse"></i></div>

<div>

<h4>A Complete Fitness Experience</h4>

<p>Explore strength, cardio, group workouts, and mindful movement.</p>

</div>

</div>



</div>



<a href="#plans" class="btn-accent mt-3">

Start Training <i class="fa-solid fa-arrow-right"></i>

</a>



</div>

</div>

</div>

</section>



<!-- SERVICES -->

<section class="services-section" id="services">

<div class="container">



<div class="text-center mb-5 reveal">

<div class="section-label">WHAT WE OFFER</div>

<h2 class="section-title">TRAIN YOUR WAY.</h2>

<p class="section-description mx-auto">

Find your style, build your routine, and choose the services

that support your fitness goals.

</p>

</div>



<div class="row g-4">



{% for service in services %}

<div class="col-md-6 col-lg-4 reveal">

<div class="service-card">



<div class="service-image-wrap">

<img class="service-image"

src="{{ service.image }}"

alt="{{ service.name }}"

loading="lazy">

</div>



<div class="service-content">

<h3>{{ service.name }}</h3>

<p>{{ service.description }}</p>



<div class="service-price">

FROM ₹{{ "{:,.0f}".format(service.price) }} / MONTH

</div>



<a href="#plans"

class="btn-outline-light-custom mt-3"

style="padding:10px 14px">

Choose Service <i class="fa-solid fa-arrow-right"></i>

</a>



</div>

</div>

</div>

{% endfor %}



</div>

</div>

</section>



<!-- TRAINERS -->

<section id="trainers">

<div class="container">



<div class="text-center mb-5 reveal">

<div class="section-label">MEET YOUR COACHES</div>

<h2 class="section-title">BUILT BY EXPERTS.</h2>

<p class="section-description mx-auto">

Get guidance from trainers who can help you stay focused

on your individual fitness journey.

</p>

</div>



<div class="row g-3 trainers-row">



{% for trainer in trainers %}

<div class="col-md-4 reveal">

<div class="trainer-card">



<img class="trainer-image"

src="{{ trainer.image }}"

alt="{{ trainer.name }}"

loading="lazy">



<div class="trainer-content">



<div class="trainer-specialty">{{ trainer.specialty }}</div>

<h3 class="mt-2">{{ trainer.name }}</h3>



<p class="trainer-description">{{ trainer.description }}</p>



<div class="trainer-actions">

<button type="button"

class="book-trainer"

data-trainer="{{ trainer.name }}">

Book Trainer

</button>

</div>



</div>

</div>

</div>

{% endfor %}



</div>

</div>

</section>



<!-- GALLERY -->

<section class="gallery-section" id="gallery">

<div class="container">



<div class="text-center mb-5 reveal">

<div class="section-label">INSIDE THE GYM</div>

<h2 class="section-title">THE TRAINING FLOOR.</h2>

<p class="section-description mx-auto">

A look at the equipment, training spaces, and fitness experiences

that make every workout count.

</p>

</div>



<div class="gallery-grid reveal">



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1100&q=85"

alt="Gym floor and strength equipment" loading="lazy">

<div class="gallery-caption">Strength Training</div>

</div>



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1579758629938-03607ccdbaba?auto=format&fit=crop&w=700&q=85"

alt="Workout equipment" loading="lazy">

<div class="gallery-caption">Training Zone</div>

</div>



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1576678927484-cc907957088c?auto=format&fit=crop&w=700&q=85"

alt="Fitness training" loading="lazy">

<div class="gallery-caption">Fitness Floor</div>

</div>



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=700&q=85"

alt="Yoga and stretching" loading="lazy">

<div class="gallery-caption">Yoga & Mobility</div>

</div>



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1534258936925-c58bed479fcb?auto=format&fit=crop&w=700&q=85"

alt="Personal fitness training" loading="lazy">

<div class="gallery-caption">Personal Training</div>

</div>



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=700&q=85"

alt="Member workout session" loading="lazy">

<div class="gallery-caption">Member Workouts</div>

</div>



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1538805060514-97d9cc17730c?auto=format&fit=crop&w=700&q=85"

alt="Athlete lifting weights" loading="lazy">

<div class="gallery-caption">Power & Progress</div>

</div>



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=700&q=85"

alt="Modern strength equipment" loading="lazy">

<div class="gallery-caption">Premium Equipment</div>

</div>



<div class="gallery-item">

<img src="https://images.unsplash.com/photo-1599058917212-d750089bc07e?auto=format&fit=crop&w=700&q=85"

alt="Recovery and mobility training" loading="lazy">

<div class="gallery-caption">Recovery & Mobility</div>

</div>



</div>

</div>

</section>



<!-- MEMBERSHIP PLAN BUILDER -->
<section class="plan-section" id="plans">
  <div class="container">
    <div class="row mb-4">
      <div class="col-lg-8 reveal">
        <div class="section-label">SIMPLE. FLEXIBLE. YOURS.</div>
        <h2 class="section-title">FIND YOUR<br>FIT.</h2>
        <p class="section-description">
          Explore membership options, select your training services, and see an estimated price instantly.
        </p>
      </div>
    </div>

    <div class="row g-4 align-items-stretch">
      <div class="col-lg-7 reveal">
        <div class="plan-form">
          <label class="form-label-custom" for="plan-duration">Choose membership duration</label>
          <select class="custom-select" id="plan-duration">
            <option value="weekly">Weekly Plan</option>
            <option value="monthly" selected>Monthly Plan</option>
            <option value="yearly">Yearly Plan</option>
          </select>

          <label class="form-label-custom">Choose your training</label>
          <div class="service-checks">
            {% for service in services %}
            <label class="service-check">
              <input type="checkbox" class="service-option" value="{{ service.name }}"
                {% if service.name == "General Gym Access" %}checked{% endif %}>
              <span>{{ service.name }}</span>
            </label>
            {% endfor %}
          </div>

          <label class="form-label-custom">Trainer preference</label>
          <div class="trainer-checks" id="plan-trainer">
            {% for name, price in trainer_prices.items() %}
            <label class="trainer-check">
              <input type="radio" name="trainer-option" class="trainer-option" value="{{ name }}"
                {% if name == "No Personal Trainer" %}checked{% endif %}>
              <span>{{ name }}{% if price > 0 %} — ₹{{ "{:,.0f}".format(price) }}/month{% endif %}</span>
            </label>
            {% endfor %}
          </div>
          <p class="price-note mb-0">Prices shown are estimates based on the sample membership rates. Confirm the final price with the gym before joining.</p>
        </div>
      </div>

      <div class="col-lg-5 reveal">
        <div class="price-summary">
          <div class="section-label">YOUR MEMBERSHIP ESTIMATE</div>
          <h3 class="mt-2">YOUR PLAN</h3>
          <div class="price-row">
            <span>Duration</span>
            <strong id="summary-duration">Monthly</strong>
          </div>
          <div class="price-row">
            <span>Selected services</span>
            <strong id="summary-services">1</strong>
          </div>
          <div class="price-row">
            <span>Training cost</span>
            <strong id="service-cost">₹1,000</strong>
          </div>
          <div class="price-row">
            <span>Trainer cost</span>
            <strong id="trainer-cost">₹0</strong>
          </div>
          <div class="price-row total">
            <span>ESTIMATED TOTAL</span>
            <strong id="grand-total">₹1,000</strong>
          </div>
          <a class="btn-accent w-100 mt-3" href="https://wa.me/{{ gym_phone }}?text={{ 'Hi, I would like to know more about gym membership.' | urlencode }}" target="_blank" rel="noopener noreferrer">
            Ask About Membership <i class="fa-solid fa-arrow-right"></i>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER: LOCATION PREVIEW + ALL CONTACT ICONS -->
<footer id="contact">
  <div class="container">
    <div class="row g-4 align-items-start">
      <div class="col-lg-5">
        <a class="footer-brand" href="#home"><span class="brand-mark">◆</span> {{ gym_name }}</a>
        <p class="footer-description">
          {{ tagline }} Your journey toward a stronger, healthier lifestyle begins with your next workout.
        </p>
        <div class="footer-social" aria-label="Social media links">
          <a href="{{ instagram }}" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          <a href="{{ facebook }}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="tel:+{{ gym_phone }}" aria-label="Call the gym">
            <i class="fa-solid fa-phone"></i>
          </a>
          <a href="mailto:{{ email }}" aria-label="Email the gym">
            <i class="fa-solid fa-envelope"></i>
          </a>
        </div>
      </div>

      <div class="col-lg-7">
        <h3 class="footer-contact-title">Find your way to better fitness</h3>
        <div class="footer-map-wrap">
          <div class="footer-map-heading">
            <span><i class="fa-solid fa-map-location-dot me-2"></i> Gym location preview</span>
            <span>Vijay Nagar · Indore</span>
          </div>
          <iframe
            class="footer-map"
            title="Map showing {{ address }}"
            src="https://maps.google.com/maps?q={{ address | urlencode }}&amp;z=15&amp;output=embed"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen>
          </iframe>
          <div class="footer-location">
            <div class="footer-location-icon"><i class="fa-solid fa-location-dot"></i></div>
            <div>
              <div class="footer-location-label">Visit the gym</div>
              <p>{{ address }}</p>
            </div>
            <a class="footer-map-button" href="{{ maps_url }}" target="_blank" rel="noopener noreferrer">
              Directions <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </a>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bottom d-flex flex-column flex-md-row justify-content-between gap-2">
      <span>© <span id="copyright-year"></span> {{ gym_name }}. All rights reserved.</span>
      <a href="#home" style="color:var(--accent)">BACK TO TOP ↑</a>
    </div>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>



<script>

/* Data provided by Flask */
const servicePrices = {{ service_prices | tojson }};
const trainerPrices = {{ trainer_prices | tojson }};

/* Helpers */
const formatINR = amount => new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 0
}).format(amount);

function selectedServices() {
    return Array.from(document.querySelectorAll(".service-option:checked"))
        .map(item => item.value);
}

function selectedTrainer() {
    const selected = document.querySelector(".trainer-option:checked");
    return selected ? selected.value : "No Personal Trainer";
}

/* Live membership estimate */
function updatePricing() {
    const duration = document.getElementById("plan-duration").value;
    const trainer = selectedTrainer();
    const selected = selectedServices();

    const monthlyServiceCost = selected.reduce(
        (total, name) => total + (Number(servicePrices[name]) || 0), 0
    );
    const monthlyTrainerCost = Number(trainerPrices[trainer]) || 0;

    const multipliers = {
        weekly: 0.35,
        monthly: 1,
        yearly: 10
    };
    const multiplier = multipliers[duration] || 1;
    const serviceCost = monthlyServiceCost * multiplier;
    const trainerCost = monthlyTrainerCost * multiplier;

    const labels = { weekly: "Weekly", monthly: "Monthly", yearly: "Yearly" };
    document.getElementById("summary-duration").textContent = labels[duration];
    document.getElementById("summary-services").textContent = String(selected.length);
    document.getElementById("service-cost").textContent = formatINR(serviceCost);
    document.getElementById("trainer-cost").textContent = formatINR(trainerCost);
    document.getElementById("grand-total").textContent = formatINR(serviceCost + trainerCost);
}

document.getElementById("plan-duration").addEventListener("change", updatePricing);
document.querySelectorAll(".trainer-option, .service-option").forEach(item => {
    item.addEventListener("change", updatePricing);
});

/* Trainer cards can preselect the same trainer in the calculator */
document.querySelectorAll(".book-trainer").forEach(button => {
    button.addEventListener("click", function () {
        const trainerName = this.dataset.trainer;
        const trainerOption = Array.from(document.querySelectorAll(".trainer-option"))
            .find(item => item.value === trainerName);
        if (trainerOption) {
            trainerOption.checked = true;
            updatePricing();
        }
        document.getElementById("plans").scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });
});

/* Reveal animations */

const revealElements = document.querySelectorAll(".reveal");



if ("IntersectionObserver" in window) {

    const observer = new IntersectionObserver(entries => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("visible");

                observer.unobserve(entry.target);

            }

        });

    }, { threshold: 0.12 });



    revealElements.forEach(element => observer.observe(element));

} else {

    revealElements.forEach(element => element.classList.add("visible"));

}



/* Close mobile navigation after choosing a section */

document.querySelectorAll("#mainNav .nav-link").forEach(link => {

    link.addEventListener("click", () => {

        const nav = document.getElementById("mainNav");



        if (nav.classList.contains("show")) {

            bootstrap.Collapse.getOrCreateInstance(nav).hide();

        }

    });

});



document.getElementById("copyright-year").textContent =

    new Date().getFullYear();



/* Initial price display */

updatePricing();

</script>



</body>

</html>

"""



# =====================================================

# HOME ROUTE

# =====================================================



@app.route("/")

def home():



    service_descriptions = {

        "General Gym Access": (

            "Train with essential strength equipment and build "

            "a consistent fitness routine."

        ),

        "Cardio Zone": (

            "Improve endurance and cardiovascular fitness "

            "with dedicated cardio training."

        ),

        "CrossFit": (

            "Challenge your strength, conditioning, and "

            "work capacity through functional workouts."

        ),

        "Zumba": (

            "Combine movement, music, and energetic group "

            "sessions for an enjoyable workout."

        ),

        "Yoga": (

            "Improve flexibility, mobility, balance, and "

            "mind-body awareness."

        ),

        "HIIT Conditioning": (

            "Burn calories, improve stamina, and build total-body "

            "power through fast-paced interval training."

        )

    }



    service_images = {

        "General Gym Access": (

            "https://images.unsplash.com/"

            "photo-1583454110551-21f2fa2afe61"

            "?auto=format&fit=crop&w=800&q=85"

        ),

        "Cardio Zone": (

            "https://images.unsplash.com/"

            "photo-1579758629938-03607ccdbaba"

            "?auto=format&fit=crop&w=800&q=85"

        ),

        "CrossFit": (

            "https://images.unsplash.com/"

            "photo-1534438327276-14e5300c3a48"

            "?auto=format&fit=crop&w=800&q=85"

        ),

        "Zumba": (

            "https://images.unsplash.com/"

            "photo-1518611012118-696072aa579a"

            "?auto=format&fit=crop&w=800&q=85"

        ),

        "Yoga": (

            "https://images.unsplash.com/"

            "photo-1544367567-0f2fcb009e0b"

            "?auto=format&fit=crop&w=800&q=85"

        ),

        "HIIT Conditioning": (

            "https://images.unsplash.com/"

            "photo-1581009146145-b5ef050c2e1e"

            "?auto=format&fit=crop&w=800&q=85"

        )

    }



    services = [

        {

            "name": name,

            "price": price,

            "description": service_descriptions[name],

            "image": service_images[name]

        }

        for name, price in SERVICES.items()

    ]



    return render_template_string(

        HTML,

        gym_name=GYM_NAME,

        tagline=GYM_TAGLINE,

        gym_phone=GYM_PHONE,

        display_phone="+" + GYM_PHONE,

        email=GYM_EMAIL,

        address=GYM_ADDRESS,

        maps_url=GYM_MAPS_URL,

        instagram=INSTAGRAM_URL,

        facebook=FACEBOOK_URL,

        services=services,

        trainers=TRAINER_DETAILS,

        service_prices=SERVICES,

        trainer_prices=TRAINERS

    )





# =====================================================

# OPTIONAL HEALTH CHECK

# =====================================================



@app.route("/health")

def health():

    return jsonify({

        "status": "ok",

        "application": GYM_NAME

    })





# =====================================================

# RUN APPLICATION

# =====================================================



if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=int(os.environ.get("PORT", 5000)),

        debug=os.environ.get("FLASK_DEBUG", "0") == "1"

    )