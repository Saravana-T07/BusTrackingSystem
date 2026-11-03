# Login Troubleshooting Checklist

## IMPORTANT: Did you restart the backend server?
The auth controller fix won't work until you **restart** the server!

### Steps to Restart:
1. Stop the current server (Ctrl+C in the terminal running it)
2. Start it again: `node src/server.js`

---

## What error are you seeing?

Please check one of these:

### A. Browser shows "Invalid email or password"
**Solution**: Run the seed script to create test users:
```bash
cd C:\Bts\server
node src/seed.js
```
Then use these credentials:
- Email: `admin@travelbuddy.com`
- Password: `password123`

### B. Login button does nothing / Page hangs
**Solution**: Check browser console (Press F12, go to Console tab)
- Look for CORS errors
- Look for network errors
- Take a screenshot and share

### C. "Cannot read property 'data' of undefined" error
**Solution**: Backend is not running
```bash
cd C:\Bts\server
node src/server.js
```

### D. Network error / Connection refused
**Solutions**:
1. Make sure backend is running on port 5000
2. Check if another app is using port 5000
3. Try: `netstat -ano | findstr :5000`

---

## Quick Test (Do this in order):

1. **Is backend running?**
   ```bash
   cd C:\Bts\server
   node src/server.js
   ```
   Should see: "Server running on port 5000"

2. **Are there users in the database?**
   ```bash
   node src/seed.js
   ```
   Should see: "Database seeded!"

3. **Test login with curl (or skip if you don't have curl)**:
   ```bash
   curl -X POST http://localhost:5000/api/auth/login -H "Content-Type: application/json" -d "{\"email\":\"admin@travelbuddy.com\",\"password\":\"password123\"}"
   ```
   Should return JSON with token

4. **Is frontend running?**
   ```bash
   cd C:\Bts\client
   node node_modules/vite/bin/vite.js
   ```
   Should show a URL like `http://localhost:5173`

5. **Open browser console before logging in**:
   - Open browser (Chrome/Edge)
   - Press F12
   - Go to Console tab
   - Try to log in
   - **Copy any red error messages you see**

---

## Tell me:
1. Which error type (A, B, C, or D) are you seeing?
2. What does the browser console show? (F12 > Console tab)
3. Did you restart the backend server after I made the fix?
