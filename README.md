# The All Rounder

This repo hosts three standalone tools:

- **`index.html`** — a dual-user workout tracker (below)
- **`maintenance.html`** — [Upkeep](#upkeep--maintenance-tracker), a maintenance schedule tracker for possessions, vehicles, and household items
- **`mascot-pendant-optimizer.html`** — [Mascot Pendant Optimizer](#mascot-pendant-optimizer), a 3D-printable pendant STL generator

---

## Dual-User Workout Tracker

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

## Design Refresh

The UI now follows a Not Boring iOS-inspired design direction:

- Softer layered surfaces with cleaner elevation and reduced neon glow
- More readable iOS-style typography in controls and data-heavy screens
- Tactile, touch-first buttons/toggles with clearer interaction states
- Updated motion/accessibility support (`:focus-visible`, reduced-motion handling)
- Existing workflows and program logic remain unchanged

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

---

## Upkeep — Maintenance Tracker

`maintenance.html` is a standalone tool for keeping up with recurring maintenance on cars, appliances, and other possessions — sauna cleaning, water heater/HVAC service, cleaning and oiling firearms, changing home air filters, and anything else on a schedule.

It's linked from the workout tracker's start screen (and links back), but works completely independently — just open `maintenance.html` directly.

### Features

- **Inventory** of items (vehicles, home systems, firearms, appliances, recreation gear, or anything else), each with one or more recurring maintenance tasks
- **Custom intervals** per task — every N days/weeks/months/years
- **Due view** — all tasks across every item, sorted soonest-first and grouped into Overdue / Due Soon / Upcoming
- **One-tap "Done"** — marks a task complete today, recalculates the next due date, and keeps a history of past completions
- **Add / edit / delete** items and tasks at any time
- **Search and category filters**
- **Export / Import** — download a JSON backup of your full inventory and history, or restore from one

### Data storage & family sync

Upkeep syncs in real time through the **same Firebase project as the workout tracker** (see `FIREBASE_CONFIG` in `maintenance.html`), under its own database path (`upkeepMaintenance`) so it doesn't collide with workout data. Whoever adds an item or hits "Done" on one device, everyone else sees it appear on theirs — no separate copies per person.

It also keeps a `localStorage` cache on each device, so the app still works offline and simply resumes syncing once the connection is back. The sync indicator in the header shows **Syncing…** / **Synced** / **Offline**.

**One-time setup:** the shared Firebase Realtime Database needs a rule permitting reads/writes on the `upkeepMaintenance` path (in addition to the existing `allRounder` rule for the workout tracker). In the Firebase Console → Realtime Database → Rules, use:

```json
{
  "rules": {
    "allRounder": {
      ".read": true,
      ".write": true
    },
    "upkeepMaintenance": {
      ".read": true,
      ".write": true
    }
  }
}
```

Click **Publish**. Until this rule is added, Upkeep still works perfectly fine on a single device — it just falls back to local-only storage and shows "Offline" in the sync indicator.

Regardless of sync, **use the Export button regularly** to save a JSON backup — Import restores from one on any device.

The app ships with a few example items (Car, Sauna, H2C System, Forces USA FTR, Home Air Filters) based on common recurring maintenance — rename, edit, or delete any of them and add your own to build out your full inventory.

---

## Mascot Pendant Optimizer

`mascot-pendant-optimizer.html` is a separate, self-contained tool for turning a mascot/logo image into a 3D-printable hype-chain pendant STL, tuned for **Bambu Studio** on the **H2C** with **AMS Pro 2**. It has no connection to the workout tracker or its Firebase data — open the file directly in a browser (no build step, no server required).

**Pipeline:** upload an image → the tool traces its silhouette (using transparency if present, or auto-detected background chroma-keying otherwise) → cleans up speckle noise and simplifies/smooths the outline → builds a 3D pendant with a raised mascot relief on a backing plate (or a pure silhouette cutout) plus an integrated chain bail → exports a print-ready binary STL.

Highlights:
- Live mask preview (adjustable threshold + eyedropper background picker) and an interactive 3D preview (drag to orbit) before exporting
- "Backing plate + relief" mode keeps thin mascot details (ears, legs, text) from snapping off, and supports **two-tone export** — separate `pendant-plate.stl` / `pendant-relief.stl` files that align at the same origin, so you can assign each one a different AMS filament color in Bambu Studio
- Automatic warnings for printability issues (e.g. an overly thin bail wall)
- A "Download print notes" button that exports the recommended Bambu Studio slicer settings (layer height, walls, infill, supports, brim, filament) alongside the STL(s)
