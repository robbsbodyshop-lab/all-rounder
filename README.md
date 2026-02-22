# The All Rounder — Dual-User Workout Tracker

A hybrid athlete program tracker for two users (husband & wife) to track workouts independently from separate devices. Based on the Viada "All Rounder" program (Chapter 9 & 10).

## Features

- **Dual-user profiles** with optional PIN protection
- **Per-user color theming** (cyan for user 1, coral for user 2)
- **Real-time sync** via Firebase — changes appear instantly across devices
- **Offline fallback** — works without internet using localStorage cache
- **Full program tracker**: 7-day schedule, standard/deload phases, 12-week cycle
- **Workout builder** with exercise dropdowns and prescribed parameters
- **Workout log** with session history
- **Exercise library** from Chapter 9 (Viada)
- **Weekly notes** per user

---

## Setup Instructions

### Step 1: Create a Firebase Project (Free)

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **"Add project"**
3. Name it something like `all-rounder-tracker`
4. Disable Google Analytics (not needed) and click **Create Project**

### Step 2: Enable Realtime Database

1. In your Firebase project, go to **Build > Realtime Database** in the left sidebar
2. Click **"Create Database"**
3. Choose a location closest to you (e.g., `us-central1`)
4. Select **"Start in test mode"** (we'll set proper rules next)
5. Click **Enable**

### Step 3: Set Security Rules

In the Realtime Database section, click the **Rules** tab and replace the content with:

```json
{
  "rules": {
    "allRounder": {
      ".read": true,
      ".write": true
    }
  }
}
```

> **Note:** These rules allow open read/write access. This is fine for a private 2-person app. The optional PIN system provides basic access separation between profiles. If you want stricter security, you can add Firebase Authentication later.

Click **Publish**.

### Step 4: Get Your Firebase Config

1. In your Firebase project, click the **gear icon** (top-left) > **Project settings**
2. Scroll down to **"Your apps"** section
3. Click the **web icon** (`</>`) to add a web app
4. Register it with a nickname (e.g., `all-rounder-web`)
5. You'll see a config snippet like this:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyD...",
  authDomain: "all-rounder-tracker.firebaseapp.com",
  databaseURL: "https://all-rounder-tracker-default-rtdb.firebaseio.com",
  projectId: "all-rounder-tracker",
  storageBucket: "all-rounder-tracker.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123"
};
```

### Step 5: Add Your Config to the App

Open `index.html` and find the `FIREBASE_CONFIG` object near the top of the `<script>` section. Replace the placeholder values with your actual Firebase config:

```javascript
const FIREBASE_CONFIG = {
  apiKey: "YOUR_ACTUAL_API_KEY",
  authDomain: "your-project.firebaseapp.com",
  databaseURL: "https://your-project-default-rtdb.firebaseio.com",
  projectId: "your-project",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "000000000000",
  appId: "YOUR_ACTUAL_APP_ID"
};
```

---

## Deploy to GitHub Pages (Free Hosting)

### Step 1: Create a GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Name the repo `all-rounder` (or any name you like)
3. Set it to **Public** (required for free GitHub Pages) or **Private** (requires GitHub Pro for Pages)
4. Click **Create repository**

### Step 2: Push the Code

Open a terminal in the `all-rounder` folder and run:

```bash
git init
git add .
git commit -m "Initial commit: dual-user All Rounder tracker"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/all-rounder.git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repo on GitHub
2. Click **Settings** > **Pages** (in the left sidebar)
3. Under **Source**, select **Deploy from a branch**
4. Choose **main** branch, **/ (root)** folder
5. Click **Save**

Your app will be live at: `https://YOUR_USERNAME.github.io/all-rounder/`

It may take 1-2 minutes for the first deployment.

---

## Usage

1. Open the app URL on each device
2. **First time:** Click "Customize Profiles" to set names and optional PINs
3. Each person taps their profile card to enter
4. Track workouts independently — all data syncs automatically
5. Use the **Switch** button in the header to change profiles

---

## Offline Mode

If Firebase is not configured (or if you lose internet), the app works entirely with localStorage. Each device will store its own data locally. When Firebase connectivity is restored, data syncs automatically.

The sync indicator in the top-right corner shows:
- **Syncing...** (gold) — saving to Firebase
- **Synced** (green) — data saved successfully
- **Offline** (red) — using local storage only
