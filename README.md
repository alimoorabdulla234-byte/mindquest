# MindQuest — account-enabled version

## What is included
- Responsive app for desktop and Android tablets/phones
- Email + password sign up and login using Supabase Auth
- Email verification (when enabled in Supabase)
- First-login display-name setup
- Cloud profile and progress storage with per-user Row Level Security
- Mystery cases, brain battles, XP, ranks and daily missions

## Important: connect Supabase before using real accounts

The app needs a Supabase project. This is what makes the accounts real and stores profiles securely.

1. Create a project at https://supabase.com/ .
2. In Supabase, open **Project Settings → API** (or **Connect**) and copy:
   - Project URL
   - Publishable key / anon public key
3. Open `index.html` in a code editor.
4. Replace these two placeholders near the top of the script:
   - `PASTE_YOUR_SUPABASE_PROJECT_URL_HERE`
   - `PASTE_YOUR_SUPABASE_ANON_KEY_HERE`
5. In Supabase, open **SQL Editor → New query**.
6. Paste all of `supabase_setup.sql` and run it.
7. In **Authentication → URL Configuration**, add your deployed Netlify site URL to the allowed redirect URLs / Site URL.
8. In **Authentication → Providers → Email**, keep Email enabled. For a school demo, email confirmation can be enabled; users will need to click the verification email before logging in.
9. Upload the updated folder to Netlify again (drag the folder to the deploy area).

## Security notes
- Only use the Supabase **publishable/anon public key** in the browser app.
- NEVER put the `service_role` or secret key in `index.html`.
- The `profiles` table uses Row Level Security so each signed-in user can read and update only their own row.
- Passwords are handled by Supabase Auth; this app does not store passwords itself.

## Install on Android
Open the deployed HTTPS Netlify URL in Chrome → menu ⋮ → Install app / Add to Home screen.

## Limitations of this prototype
This is a real email-authentication integration once configured, but it is not a full production launch. It does not yet include password reset UI, admin moderation, multiplayer matchmaking, or anti-cheat controls. Progress syncs when a challenge is completed.
