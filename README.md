# 🚌 Bus Tracking System (TravelBuddy)

A real-time college and institutional transit tracking web platform. TravelBuddy provides live GPS tracking, dynamic route navigation, estimated time of arrival (ETA), incident alerts, and administrative fleet management for educational institutions.

---

## 🌟 Key Features

### 🛡️ Admin Portal (`/admin`)
- **Fleet Command Center:** View all active buses, drivers, and routes in real time on an interactive Leaflet map.
- **Route & Stop Management:** Configure stops, geo-coordinates, schedules, and route paths.
- **Bus & Driver Allocation:** Assign drivers to buses and link buses to designated routes.
- **Alert & Safety Center:** Monitor emergency SOS alerts, breakdown notifications, traffic delays, and speeding events.
- **Capacity & Analytics:** Track passenger loads across routes and generate/export PDF trip and fleet reports.
- **Special Event Logistics:** Manage custom shuttle services and coordinate special event registrations.

### 🚍 Driver Portal (`/driver`)
- **Trip Management:** Start, pause, and conclude designated trips with status synchronization.
- **Real-Time GPS Broadcasting:** Stream live location coordinates to students and administrators via WebSockets (Socket.io).
- **Interactive Stop Checklist:** View route stops in sequence and receive real-time student stop pickup requests.
- **Incident & Emergency Reporting:** Send one-tap alerts for breakdowns, heavy traffic, schedule delays, or SOS emergencies.
- **Passenger Capacity Logging:** Update current passenger count to inform students of bus occupancy before boarding.

### 🎓 Student Portal (`/student`)
- **Live Bus Tracking:** Track assigned or selected buses live on the map with custom markers.
- **ETA & Route Stops:** View arrival times, remaining distance, and intermediate stops along the route.
- **Stop Requests:** Notify drivers in advance of intended boarding or deboarding points.
- **Service Announcements & Alerts:** Stay informed on delays, route diversions, or bus changes.
- **Special Event Bookings:** Register for extracurricular or event transit services.

---

## 🛠️ Tech Stack

| Domain | Technologies |
| :--- | :--- |
| **Frontend** | React 19, Vite, Tailwind CSS, React Router v7, Leaflet, React-Leaflet, Socket.io-client, Lucide React, Axios, jsPDF |
| **Backend** | Node.js, Express, Socket.io (WebSockets), Sequelize ORM, MySQL (`mysql2`), JWT, Bcrypt |
| **Data & Utilities** | Python (`scrape_kiot.py` for route data scraping), Batch scripts (`start_all.bat`) |

---

## 📁 Project Structure

```text
c:\Bts
├── client/                     # Frontend Vite + React application
│   ├── public/                 # Static web assets
│   ├── src/
│   │   ├── components/         # Reusable UI (Map, DataTable, StatsCard, Layout)
│   │   ├── context/            # AuthContext & state providers
│   │   ├── pages/              # AdminDashboard, DriverDashboard, StudentDashboard, Login
│   │   ├── App.jsx             # Route definitions & Role-based protected routes
│   │   └── main.jsx            # React root mount
│   ├── package.json
│   └── vite.config.js
│
├── server/                     # Backend Node.js + Express application
│   ├── src/
│   │   ├── controllers/        # Auth, Admin, Driver, and Student controllers
│   │   ├── middleware/         # JWT authentication & role-verification middleware
│   │   ├── models/             # Sequelize database models (User, Bus, Route, Trip, Alert, etc.)
│   │   ├── routes/             # RESTful API route definitions
│   │   ├── seed.js             # Initial database schema setup & data seeder
│   │   └── server.js           # Server entry point & Socket.io handler
│   ├── create_db.js            # MySQL database initialization script
│   ├── migrate.js              # Database migration helper
│   ├── package.json
│   └── TROUBLESHOOTING.md      # Common server troubleshooting steps
│
├── routes.json                 # Pre-configured bus routes and stop coordinates
├── scrape_kiot.py              # Python scraper for extracting institutional bus routes
├── start_all.bat               # One-click Windows launcher for both client and server
├── CREDENTIALS.md              # Test accounts and credentials reference
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Node.js** (v18.x or later recommended) & **npm**
- **MySQL Server** installed and running on port `3306`

---

### 2. Database Configuration & Initialization

1. Verify your MySQL server is running.
2. The database connection defaults to:
   - **Host:** `localhost`
   - **User:** `root`
   - **Password:** `sARAVANA@12345` *(change in [`server/src/models/index.js`](server/src/models/index.js) and [`server/create_db.js`](server/create_db.js) if different)*
   - **Database:** `bts_db`
3. Initialize the database and load seed data:
   ```powershell
   cd c:\Bts\server
   node create_db.js
   node src/seed.js
   ```
   *(You should see confirmation that `bts_db` exists and the database was seeded with sample users, routes, and buses).*

---

### 3. Running the Application

#### Option A: One-Click Quick Start (Windows)
Double-click [`start_all.bat`](start_all.bat) or run from PowerShell:
```powershell
cd c:\Bts
.\start_all.bat
```
This launches two separate command prompt windows running both services concurrently.

#### Option B: Manual Start (Two Terminals)

**Terminal 1 — Backend Server:**
```powershell
cd c:\Bts\server
npm run dev
```
*Server starts on `http://localhost:5000`.*

**Terminal 2 — Frontend Client:**
```powershell
cd c:\Bts\client
npm run dev
```
*Vite dev server starts on `http://localhost:5173`.*

---

## 🔑 Default Test Accounts

After running the seed script, log in with any of the pre-configured accounts:

| Role | Email Address | Password | Default Dashboard |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin@travelbuddy.com` | `password123` | [`/admin`](http://localhost:5173/admin) |
| **Driver** | `driver@travelbuddy.com` | `password123` | [`/driver`](http://localhost:5173/driver) |
| **Student** | `student@travelbuddy.com` | `password123` | [`/student`](http://localhost:5173/student) |

---

## 🔌 API & WebSocket Overview

### REST Endpoints
- **Authentication:** `POST /api/auth/login`, `GET /api/auth/me`
- **Admin Management:** `GET/POST /api/admin/buses`, `GET/POST /api/admin/routes`, `GET /api/admin/reports`
- **Driver Operations:** `POST /api/driver/trip/start`, `POST /api/driver/trip/end`, `POST /api/driver/alert`
- **Student Services:** `GET /api/student/routes`, `POST /api/student/stop-request`, `GET /api/student/bus/:id`

### Socket.io Real-Time Events
- `driver_location`: Broadcasts live latitude/longitude, speed, and heading.
- `bus_status_update`: Emits trip start/pause/complete status transitions.
- `emergency_alert`: Dispatches instant safety alerts to student and admin consoles.
- `stop_request_submitted`: Pushes stop pickup requests directly to the assigned driver.

---

## ❓ Troubleshooting

- **`listen EADDRINUSE: address already in use :::5000`**:
  A previous Node process is still holding port 5000. Run:
  ```powershell
  netstat -ano | findstr :5000
  taskkill /F /PID <PID>
  ```
  *(See [`server/TROUBLESHOOTING.md`](server/TROUBLESHOOTING.md) for full steps).*
- **"Invalid email or password" on login**:
  Re-run the database seeder to reset user credentials:
  ```powershell
  cd c:\Bts\server
  node src/seed.js
  ```
- **Map tiles not displaying**:
  Ensure an active internet connection so Leaflet can fetch OpenStreetMap tiles.

---

## 📜 License
ISC License. Built for institutional campus transit monitoring.

