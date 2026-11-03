# Login Credentials & Testing Guide

## Test Accounts

After running the seed script, use these credentials to log in:

### Admin Account
- **Email**: `admin@travelbuddy.com`
- **Password**: `password123`
- **Access**: Full system management, view all routes/buses/users/alerts

### Driver Account
- **Email**: `driver@travelbuddy.com`
- **Password**: `password123`
- **Access**: Start/end trips, broadcast GPS location, view assigned route

### Student Account
- **Email**: `student@travelbuddy.com`
- **Password**: `password123`
- **Access**: Track bus location, view route details, see ETA

## How to Use

1. **Seed the Database** (first time only or to reset):
   ```bash
   cd C:\Bts\server
   node src/seed.js
   ```
   You should see: "Database seeded!"

2. **Start the Backend**:
   ```bash
   cd C:\Bts\server
   node src/server.js
   ```
   You should see: "Server running on port 5000"

3. **Start the Frontend** (in a new terminal):
   ```bash
   cd C:\Bts\client
   node node_modules/vite/bin/vite.js
   ```
   You should see: "VITE ready" with a local URL

4. **Login**:
   - Visit the login page (usually `http://localhost:5173`)
   - Enter one of the test accounts above
   - You'll be redirected to the appropriate dashboard based on role

## What Was Fixed

The login was failing because:
1. Backend was sending plain text error messages instead of JSON
2. Frontend couldn't parse the plain text response
3. Fixed: All backend responses now return proper JSON format

## Troubleshooting

- **"Invalid email or password"**: Run the seed script first (`node src/seed.js`)
- **Login button doesn't work**: Check browser console (F12) for errors
- **Backend not running**: You should see "Server running on port 5000" message  
- **Frontend not loading**: Check that Vite is running and showing the URL
