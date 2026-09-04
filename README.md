# Python SOC Monitor

A Python-based security monitoring and detection project.

## Project Goal

The goal of this project is to build a small SOC monitoring system that collects security events, normalizes them, applies detection rules, and generates alerts for suspicious activity.

## Current Features

- Synthetic security events
- Event processing with Python
- Failed login detection prototype
- Alert triggered after 3 failed login events

## Project Architecture

Security Events
→ Collector
→ Normalization
→ Detection Engine
→ Alerts
→ Database
→ API
→ Dashboard

## Current Status

- Phase 1: Project Setup and Git - Completed
- Phase 2: Synthetic Events MVP - Completed
- Phase 3: Event Schema and Normalization - Completed
- Phase 4: Detection Engine - Next