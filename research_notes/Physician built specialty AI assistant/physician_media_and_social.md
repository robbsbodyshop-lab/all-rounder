# Physician media and social: physician-built specialty assistants on always-on "VM agent" frameworks (Grok Bot / OpenMausBot, and the OpenClaw family)

Research date: 15 November 2026. Evidence labels used throughout:
- **[opened]** = I fetched the page (or pulled the YouTube video's metadata/description) in this session. Quotes are as returned by the fetch tool, which summarises pages with a small model, so treat wording as near-verbatim, not certified verbatim.
- **[snippet]** = seen only in a search-result title/summary; not opened. Lower confidence.
- YouTube dates marked "approx." come from relative search listings ("2 months ago"); dates without that mark come from video metadata.
- No fetched page tried to direct my actions. One third-party OpenMausBot listing page was flagged by the search summariser as carrying unrelated "Open Agent Passport" text; I did not open or rely on it.

## 1. Which physicians have written posts saying they built a specialty-specific assistant on this kind of framework, and what exactly did they build and call it?

### Takeaway
**The naming hypothesis in the brief is wrong, or at least incomplete: "Grok Bot" and "OpenMausBot" are real products, not garbled versions of Clawdbot/Moltbot/OpenClaw.** Across both framework families I found **no clearly matching case** (named MD/DO/MBBS + specialty-specific personal assistant + built on Grok Bot/OpenMausBot or OpenClaw + described in the physician's own words); the closest items are partial: a podiatric surgeon's OpenClaw assistant "Yukio", a retired dermatologist's private "Grok-Bot Dr" teaching community, and a radiology OpenMausBot workspace built by a non-physician.

### Cited Findings

#### 1a. Framework naming check (do this first; it changes the search target)
- **Grok Bot is a real xAI product.** It launched in beta on 11 August 2026 and is described as "a team of always-on AI agents that get their own cloud computer"; users message a Bot "the way they would text a colleague, from desktop or iOS"; it is bundled into SuperGrok Heavy, Cursor Ultra ($200/mo) and Cursor Teams Premium ($120/seat/mo); the article mentions no medical uses and no HIPAA statement. [opened] — [Unite.AI, 11 Aug 2026](https://www.unite.ai/xai-launches-grok-bot-always-on-ai-teammates-with-their-own-cloud-computers/)
- The same article is internally inconsistent on hosting: "their own cloud computer" in one place, "Bots share a computer of their own in the cloud" in another. [opened] — [Unite.AI](https://www.unite.ai/xai-launches-grok-bot-always-on-ai-teammates-with-their-own-cloud-computers/)
- Other coverage dates the debut to 11–12 August 2026 and a business version to 3 September 2026. [snippet] — [iPhone in Canada, 12 Aug 2026](https://www.iphoneincanada.ca/2026/08/12/xai-debuts-grok-bot-ai-teammates-you-can-give-real-work-to/); [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/14458/xai-grok-bot-enterprise-agents-login)
- **OpenMausBot is a real open-source project.** Its README calls it "The open-source Grok Bot alternative: your own team of AI bots, in a chat app", "an independent project inspired by Grok Bot", not affiliated with xAI; formerly named OpenGrokBot, also known as MausBot; author Milind Soni; Apache-2.0 (separate licence for `enterprise/`); 23.3k stars at time of fetch. [opened] — [github.com/milind-soni/openmausbot](https://github.com/milind-soni/openmausbot)
- OpenMausBot is where the "VM" wording comes from: the repo tagline is "Open-source Grok Bot alternative with a virtual machine that bots can use" [snippet title] — [GitHub](https://github.com/milind-soni/OpenMausBot); each bot can use a cloud Linux desktop ("Boat"), an isolated Local VM, or the user's own computer after opt-in; bots run through local `claude`, `codex` or `grok` CLIs behind a harness server on 127.0.0.1; per-bot model selection; self-hosting via npx, Docker or a VPS. [opened] — [github.com/milind-soni/openmausbot](https://github.com/milind-soni/openmausbot)
- OpenMausBot's README does not mention OpenClaw anywhere. [opened] — [github.com/milind-soni/openmausbot](https://github.com/milind-soni/openmausbot)
- **OpenClaw is a separate, earlier lineage.** Clawdbot (Peter Steinberger, late 2025) was renamed Moltbot on 27 Jan 2026 after Anthropic trademark pressure and OpenClaw on 30 Jan 2026. [snippet] — [Business Today, 30 Jan 2026](https://www.businesstoday.in/technology/news/story/the-lobster-sheds-its-shell-for-the-third-time-as-clawdbot-becomes-openclaw-513650-2026-01-30); [AlternativeTo](https://alternativeto.net/news/2026/1/trending-open-source-ai-agent-clawdbot-rebrands-to-moltbot-after-pressure-from-anthropic); [Techloy](https://www.techloy.com/clawdbot-is-now-moltbot-everything-you-need-to-know-about-the-viral-personal-ai-assistant.md)
- A physician source independently confirms the OpenClaw rename chain: "an AI agent platform now called OpenClaw (formerly Clawdbot, then Moltbot)". [opened, video description] — [Dr. TJ Ahn Show, 7 Feb 2026](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- Other products in the same "always-on bot with its own computer" category surfaced in passing: Meta "Muse" (launched 8 Sep 2026) [opened] — [Passive Income MD, 30 Oct 2026](https://passiveincomemd.com/blog/tech/muse-ai-vs-grok-bot/); and "Rakazo", another open-source Grok Bot alternative [snippet] — [YouTube listing](https://www.youtube.com/watch?v=xk-aLMQRYfk). I did not search for physician builds on these.

#### 1b. Candidate list (clinician builders), best first

**Candidate 1 — Dr. TJ Ahn, DPM — "Yukio" (OpenClaw). Match: PARTIAL.**
- Credentials/specialty: "Dr. TJ Ahn, DPM", board-certified foot and ankle surgeon (American Board of Multiple Specialties in Podiatry); also cites MIT Sloan "Artificial Intelligence in Business". [opened] — [drtjahn.com, 9 Feb 2026](https://drtjahn.com/openclaw-yukio-my-hands-on-ai-assistant-guide). He also runs a separate minimally invasive surgery channel ("Modern MIS Pro"). [opened] — [YouTube description](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- Where described: blog post "OpenClaw & Yukio: My Hands-On AI Assistant Guide" (9 Feb 2026) [opened] — [drtjahn.com](https://drtjahn.com/openclaw-yukio-my-hands-on-ai-assistant-guide); YouTube video "This AI Agent Replaced My VA: OpenClaw for Doctors (With a Secure Setup)", 18:26, published 7 Feb 2026, 2,724 views at fetch [opened] — [YouTube](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- Assistant name: "my OpenClaw agent, which I named Yukio". [opened] — [YouTube description](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- What it does: runs 24/7; manages Google Calendar (read/create/move/delete events by voice); Google Tasks; reads and summarises email; 7 a.m. daily brief plus "heartbeat" reminders; Notion "second brain" with categories ideas, content, notes, learning, people, quotes. [opened] — [YouTube description](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- Practice-related uses he lists: patient follow-up/callback tracking, pulling recent studies, staff communication, meeting/consult prep, email triage with human review, task delegation. The page does not describe autonomous clinical decisions. [opened] — [drtjahn.com](https://drtjahn.com/openclaw-yukio-my-hands-on-ai-assistant-guide)
- Interface: Telegram, voice notes only. [opened] — [YouTube description](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- Hosting: cloud VPS (he uses Hostinger; mentions Hetzner CAX11 at about $4/mo as cheaper); no Mac mini. [opened] — [drtjahn.com](https://drtjahn.com/openclaw-yukio-my-hands-on-ai-assistant-guide)
- Model: cost table lists "Claude/GPT" API; Llama 3.2 mentioned only as an optional local model for background tasks; the exact model behind Yukio is not stated. [opened] — [drtjahn.com](https://drtjahn.com/openclaw-yukio-my-hands-on-ai-assistant-guide)
- Cost: about $30–$40/month total (hosting $8–$10, API $20–$30); "took a few days to configure". [opened] — [drtjahn.com](https://drtjahn.com/openclaw-yukio-my-hands-on-ai-assistant-guide); [YouTube description](https://www.youtube.com/watch?v=7xtWe3s_Tk8). Note an internal inconsistency: a video chapter is titled "How I replaced 80% of my VA for about $10/month". [opened] — [YouTube description](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- Code/template: none linked. He sells help instead: "If you'd like help implementing a custom AI assistant for your practice, use the link in the description", with a "Schedule A Call With Dr. TJ Ahn" booking link and a weekly newsletter ("The Private Practice Dispatch"). [opened] — [YouTube description](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- Why partial, not strong: (i) DPM is a podiatric physician/surgeon, not MD/DO/MBBS; (ii) the assistant is a general executive assistant and second brain, not podiatry-specific; (iii) it is on OpenClaw, not Grok Bot/OpenMausBot. It is, however, the only fully documented first-person clinician build with a named assistant that I found.

**Candidate 2 — Reinhold "Dr. Lautner", retired dermatologist — "Grok-Bot Dr" community (Grok Bot). Match: PARTIAL (weak on the "specific assistant" criterion).**
- Self-description: "I am Reinhold, Dr. Lautner. Retired dermatologist, living in Nicaragua, running this group alone." Credentials are self-stated on the page and not independently verified. [opened] — [Skool: Grok-Bot Dr](https://www.skool.com/grok-bot-dr-5856)
- What it is: "Grok-Bot Dr is a physician-led community for xAI Grok Bot" — "persistent AI coworkers that have a computer, use your apps, keep memory, and run routines"; summary line "Physician-led Grok Bot clinic. Setup, clinical-style prompts, three tested workflows, privacy." [opened] — [Skool](https://www.skool.com/grok-bot-dr-5856)
- Content: classroom modules "Start Here; Install & First Bot; Clinical-style prompts; Three tested workflows; Privacy"; live office hours twice a month; "Taught by a doctor. Clinical prompts. Tested workflows. No fluff." [opened] — [Skool](https://www.skool.com/grok-bot-dr-5856)
- Access: free, private, 60 members at fetch; creation date not shown. [opened] — [Skool](https://www.skool.com/grok-bot-dr-5856)
- No specific named assistant, no dermatology-specific bot, no shared bot link or repo is visible on the public page. [opened] — [Skool](https://www.skool.com/grok-bot-dr-5856)
- Why partial: right framework and a physician builder/teacher, but the public page shows a course, not a described specialty assistant; the workflows are behind the private wall.

**Candidate 3 — Dr. Kavan R. Thompson, D.O., PGY-3 diagnostic radiology — "radiology-ai-skills" skill pack. Match: PARTIAL (near-miss on framework).**
- Credentials: "Maintained by Dr. Kavan R. Thompson, D.O. (PGY-3 Diagnostic Radiology, HCA Florida / USF Morsani)". [opened] — [github.com/kavanthompson/radiology-ai-skills](https://github.com/kavanthompson/radiology-ai-skills)
- What it is: "Curated high-value AI agent skills for radiology residents and physicians", "Optimized for Claude Code, Cursor, Grok, and ResidentShield / TemplateGuards workflows"; initialised 19 Aug 2026; 17 commits; 0 stars; no licence stated. [opened] — [GitHub](https://github.com/kavanthompson/radiology-ai-skills)
- Skills described: book-to-skill (turn a textbook/PDF into a skill, for ABR Core preparation), medgemma-radiology (X-ray/CT/MRI/DICOM analysis with explanations), medgemma-assistant (labs, drug interactions, symptom evaluation). TemplateGuards is listed as a related "PACS template / structured reporting tool". [opened] — [GitHub](https://github.com/kavanthompson/radiology-ai-skills)
- The page does not mention Grok Bot, OpenMausBot or OpenClaw, defines no bot or assistant, and has no HIPAA/PHI statement. [opened] — [GitHub](https://github.com/kavanthompson/radiology-ai-skills)
- Why partial: verified physician, clearly specialty-specific, published; but it is a skills collection for coding agents, not an always-on VM assistant, and there is no narrative write-up.

**Candidate 4 — Francisco Salido, radiologist — "OPENCLAW" second-brain repo. Match: WEAK.**
- "OPENCLAW is the personal knowledge operating system of Francisco Salido, a radiologist and AI specialist (MBA in AI)."; covers "Radiology — Ultrasound, Doppler, MSK, and AI-augmented imaging" and projects such as MRICheck; MIT licence; 293 commits; 0 stars. [opened] — [github.com/franciscosalido/OPENCLAW](https://github.com/franciscosalido/OPENCLAW)
- The page never says it runs the OpenClaw agent framework; the only hints are the repo name and a `Dockerfile.openclaw-sandbox` file, alongside `.claude`/`CLAUDE.md` files. No hosting, model, chat channel or dates are stated, and medical degree is not spelled out. [opened] — [GitHub](https://github.com/franciscosalido/OPENCLAW)
- Why weak: specialty-tied and public, but framework use is unconfirmed and there is no first-person account.

**Candidate 5 — "Wilson" (@qpzm620) — "Pulse" (Grok Bot). Match: WEAK.**
- Listing text: "Doctor-built health coach that learns your diet, exercise, and sleep from chat"; first seen 6 Oct 2026; install link x.ai/bot/DdNlDzU_cYi-JJv2YR2CS; creator shown only as "Wilson", no name, credentials or specialty. [opened] — [builder.grokbot.rocks](https://builder.grokbot.rocks/bot/DdNlDzU_cYi-JJv2YR2CS/); [ReadMultiplex directory](https://readmultiplex.com/grokbot-rocks/)
- Why weak: right framework and a "doctor-built" claim, but unverifiable identity, and it is a consumer wellness coach, not an assistant for the doctor's own specialty work.

**Candidate 6 — Sohaib Qadri (YouTube handle @DrSohaibQadri) — "CuraClaw". Match: WEAK / unverified.**
- "CuraClaw is a personalized AI physician assistant that is designed to cut EMR chart review time by 30 mins per patient"; does "deep research on every patient on the list" via FHIR endpoints to produce a pre-rounding report and help with documentation; titled "Built with Opus 4.7 Hackathon"; published 26 Apr 2026; 91 views. [opened, video description] — [YouTube](https://www.youtube.com/watch?v=RF8fR4V3EN8)
- The description states neither the underlying framework nor the builder's credentials or specialty; a follow-up web search found nothing further on CuraClaw. [opened] — [YouTube](https://www.youtube.com/watch?v=RF8fR4V3EN8)

#### 1c. Near-miss list (and why each misses)

Non-physician builders of medical agents:
- **Aryan Iyappan — "openbot-radiology" (OpenMausBot).** The closest technical match found: "Operational files for the installed OpenMausBot, Bahmni HMS, DCM4CHEE PACS/worklist, OHIF and Weasis environment"; a sanitised export of an OpenMausBot team of "six profiles" including Sol ("preparation, coordination and drafting") and Astra ("image interpretation and independent checking"), three native radiology skills, read-only desktop connections, running on "the hospital VM"; evaluation described as "exploratory supervised-assistant results, not hospital clinical certification"; benchmark folders dated 30 Sep–1 Oct 2026; 8 commits, 0 stars, no licence. [opened] — [github.com/aryaniyaps/openbot-radiology](https://github.com/aryaniyaps/openbot-radiology). Misses because the builder's profile says he is "an IT student at CEG", Chennai, with a software bio and membership of the @hospitaljobsin org; nothing indicates a physician. [opened] — [github.com/aryaniyaps](https://github.com/aryaniyaps)
- **Eugene Vestel (@fhirdataguy)** — personal/family health agent on OpenClaw, Mac mini with its own account, Claude, private HAPI FHIR server behind a guardrail proxy (code at github.com/aks129/ModelContextProtocolFHIR); 24 Feb 2026. Patient-side; no medical credentials stated. [opened] — [Substack](https://evestel.substack.com/p/how-i-build-my-personal-openclaw)
- **Beginners in AI — "SecondMed" (Grok Bot)** — explains test results, checks bills, prepares appointment questions; 11 Sep 2026. Patient-side, explicitly "not a doctor". [opened, video description] — [YouTube](https://www.youtube.com/watch?v=d7I82Ji45II)
- **Marshall Moorman — "Medical Vault" (Grok Bot)** — medical-records agent on NAS/cloud drive "without sending PHI to cloud"; added 18 Oct 2026. Creator not described as a physician. [opened] — [grokdir.com](https://www.grokdir.com/bots/medical-vault)
- **Vincenzo Palazzo — "Doctor" template (Grok Bot)** — "Doctor assistant for visit prep and question lists, not diagnosis"; first listed 28 Sep 2026. Patient-side; no credentials. [opened] — [grokbotwiki.com](https://www.grokbotwiki.com/bots/doctor)
- **Brian Roemmele — Medical Bill Auditor, Claim Denial Fighter, New Patient Booker (Grok Bot)**; first seen 23 Oct–3 Nov 2026. Patient-side billing/booking bots. [opened] — [ReadMultiplex directory](https://readmultiplex.com/grokbot-rocks/)
- **"Cindy" — "Consider It Marketed" (Grok Bot)** — "Clinic CEO for a medical practice."; first seen 21 Sep 2026. Practice-marketing bot; builder not described as a physician. [opened, directory listing] — [ReadMultiplex directory](https://readmultiplex.com/grokbot-rocks/)
- **Marcio Fiuza — "Klaus" (OpenClaw, in a VM on a home Mac, later bare metal)**; 20 Oct 2026. M&A professional; nothing medical. [opened] — [Substack](https://practitionersnotes.substack.com/p/my-agent-will-talk-to-your-agent)

Organisation or vendor products:
- **Longevity Grok / "PLSI" (Insilico Medicine)** — "runs inside Grok Bot"; 30 agents including a 4-bot "Clinic" track for physicians (Patient Coordinator, Visit Assistant, Evidence Analyst, Clinic Liaison) available by invitation; MIT-licensed at github.com/Insilico-org/plsi; code public 30 Oct 2026, v0.2.0 on 5 Nov 2026. Company-built platform, not one physician's personal assistant; the page lists no medical credentials for its team. [opened] — [longevitygrok.si](https://longevitygrok.si/)
- **PhiClaw** — commercial "HIPAA OpenClaw for doctors" and "HIPAA Grok Bot alternative"; its blog features a "Dr. Alex Rios of True Bliss Medical" (med spa) as a user. Vendor marketing. [snippet] — [phiclaw.ai](https://phiclaw.ai/); [phiclaw.ai/blog](https://phiclaw.ai/blog/openclaw-for-solo-doctors/); [phiclaw.ai Grok Bot page](https://phiclaw.ai/hipaa-grok-bot-alternative/)
- **Continuum / "Landed" (Matt Turley, engineer)** — "Grok Bot for Medical Practices" guide selling setup services ($99 to $1,500); names no physician builder. [opened] — [uxcontinuum.com](https://uxcontinuum.com/grok-bot-for-doctors)
- **Generic vendor "OpenClaw for doctors" guides** with no named builder. [snippet] — [Ampere.sh](https://www.ampere.sh/blog/openclaw-for-doctors); [OpenClaw Playbook](https://www.openclawplaybook.ai/guides/openclaw-for-doctors); [Upwork gig](https://www.upwork.com/services/product/development-it-deploy-personal-ai-agent-with-openclaw-for-doctors-medical-professionals-2041665361458974137)

Research/institutional projects on OpenClaw (not personal assistants):
- OpenClaw-Medical-Skills, a library of about 869 skills (FreedomIntelligence). [snippet] — [GitHub](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)
- MedOpenClaw (imaging-agent runtime, arXiv 2603.24649). [snippet] — [arXiv](https://arxiv.org/html/2603.24649v1)
- MedgeClaw (biomedical research assistant, Xi'an Jiaotong University researcher). [snippet] — [themenonlab.blog](https://themenonlab.blog/blog/medgeclaw-biomedical-ai-research-assistant-openclaw)
- DoctorClaw (described on Habr as an OpenClaw adaptation to a professional vertical). [snippet] — [Habr](https://habr.com/ru/post/1013388)
- "Tula" personal health assistant adapted from OpenClaw by RealActivity's CEO. [snippet] — [Cloud Wars](https://cloudwars.com/copilot-podcast/ai-agent-and-copilot-podcast-openclaw-powered-healthcare-assistant-builds-patient-agency/)

### Inferences
- The user's phrase "Grok Bot / OpenMausBot-style VM agent framework" is precise, not garbled: Grok Bot gives bots a cloud computer and OpenMausBot's own tagline is "a virtual machine that bots can use". The primary search target should be Grok Bot/OpenMausBot, with OpenClaw as an older, adjacent family.
- Because Grok Bot launched 11 Aug 2026 and OpenMausBot followed, any matching physician build is at most about three months old; this likely explains why public write-ups are scarce.
- If the user is recalling a specific item, the three most plausible referents among what I found are: the private "Grok-Bot Dr" community (physician-led, Grok Bot), the "openbot-radiology" OpenMausBot workspace (specialty-specific, but student-built), or a bot shared inside a closed physician group that is not web-indexed.
- Dr. Thompson's SKILL.md-format radiology skills could plausibly be loaded into a Grok Bot/OpenMausBot bot, but his page does not say he has done so.

### Gaps
- No named MD/DO/MBBS was found describing, in first person, a specialty-specific assistant on Grok Bot or OpenMausBot. Absence in search does not prove absence: X, LinkedIn, Facebook physician groups, Discord and private Skool content are poorly indexed.
- I could not see inside the private "Grok-Bot Dr" classroom, so I do not know whether Dr. Lautner's "three tested workflows" include a dermatology-specific assistant.
- Identity and specialty of "Wilson" (Pulse) and credentials of Sohaib Qadri (CuraClaw) are unverified.
- I did not inspect file contents of the Salido or Iyappan repos beyond their README pages.
- Physician builds on Meta Muse, Rakazo or other Grok Bot derivatives were not searched.

## 2. Which YouTube videos, podcast episodes or talks feature a physician demonstrating such an assistant?

### Takeaway
One video clearly qualifies as a clinician demonstrating their own agent (Dr. TJ Ahn's OpenClaw "Yukio" demo, Feb 2026); nothing equivalent was found for Grok Bot or OpenMausBot, where the medical videos are patient-side or generic.

### Cited Findings
- **Dr. TJ Ahn Show — "This AI Agent Replaced My VA: OpenClaw for Doctors (With a Secure Setup)"**, 7 Feb 2026, 18:26; chapters include "Meet 'Yukio'", "Live demo: Telegram + voice-only control", "Daily briefs at 7 a.m. and heartbeat reminders", "Building a second brain with Yukio + Notion", "Rapid-fire AI use cases for physicians", "How I can help you implement a custom AI assistant". [opened, metadata] — [YouTube](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- **Sohaib Qadri — "CuraClaw - Built with Opus 4.7 Hackathon"**, 26 Apr 2026, 2:52; pre-rounding/chart-review assistant demo; framework and credentials not stated. [opened, metadata] — [YouTube](https://www.youtube.com/watch?v=RF8fR4V3EN8)
- **Copper Digital — "How I Turned Claude Into My Personal AI Assistant | Arvind Sarin x Dr. Rachel Rizal"**, 26 May 2026, 28:38; covers Claude Code, OpenClaw, NotebookLM and a "second brain", but the build described is Arvind Sarin's (CEO of Copper Digital): "How Arvind connected Claude to email, calendars, Loom transcripts & workflows". Dr. Rizal's credentials and any assistant of her own are not stated in the description. Near-miss. [opened, metadata] — [YouTube](https://www.youtube.com/watch?v=iiSwHzcnh1w)
- **American Heart Association — "Opening Session: Designing and Deploying Real-World AI Agents"**, session held 7 Nov 2026 at AHA Scientific Sessions (Chicago), posted 13 Nov 2026, 26:32; "Dr. Michał Nedoszytko, whose Postvisit.ai earned top honors at Anthropic's 2026 hackathon, build[s] an AI Agent live"; speaker listed as "Michał Nedoszytko, MD, PhD, Clinician Scientist, Abridge". Framework is not named, and Postvisit.ai is a patient-facing product, so this is a near-miss. [opened, metadata] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- **Beginners in AI — "I Built My Own AI Health Assistant (Grok Bot)"**, 11 Sep 2026, 9:15; "SecondMed" patient-side agent alongside sibling bots Lettuce, Wart and Coupon; full prompt published on the channel's site. Not a physician. [opened, metadata] — [YouTube](https://www.youtube.com/watch?v=d7I82Ji45II)
- Generic or adjacent listings, not opened: "OpenClaw Is Taking Over Hospitals (INSANE)" (Beau Johnson, approx. Apr 2026) [snippet] — [YouTube](https://www.youtube.com/watch?v=Og0QOLa9KpM); "Agentic AI in Regenerative Medicine: A Working Playbook" (Pravida Health, approx. Jul 2026, "the agentic AI workflow I would actually run in my Atlanta regenerative-medicine clinic next quarter" — hypothetical, framework unknown) [snippet] — [YouTube](https://www.youtube.com/watch?v=RRN4q1AgIFU); "How AI Makes Me a More Efficient Physician Assistant" (Michael Taylor PA-C, approx. late Oct 2026 — a PA, not a physician) [snippet] — [YouTube](https://www.youtube.com/watch?v=S6ziXBIwyA0)
- A This Week in Startups episode titled "We're now fixing health issues with OpenClaw!" appeared in results; no physician speaker was identified. [snippet] — [thisweekinstartups.com](https://www.thisweekinstartups.com/episodes/cc9f51-we-re-now-fixing-health-issues-with-openclaw)
- YouTube searches for "OpenMausBot" returned about 20 videos, all general tutorials/reviews from Aug–Nov 2026 (for example Julian Goldie SEO, Prism Labs, AwesomeFOSS); none medical. [opened, search listing] — [example: Prism Labs](https://www.youtube.com/watch?v=V8MHuPeYELY)

### Inferences
- Physician video content about these frameworks is, so far, mostly a private-practice "replace my VA" angle (Ahn) rather than specialty-clinical demonstrations.

### Gaps
- No transcripts were retrievable (the tool returned empty transcripts), so video findings rest on titles, descriptions and chapter lists.
- Podcast directories (Apple/Spotify show notes) were not searched directly.

## 3. Has physician-facing or tech media profiled a doctor running their own agent for their specialty?

### Takeaway
No. I found no profile of a named physician-builder in KevinMD, Medscape, STAT, MedPage Today, Fierce Healthcare, Becker's, Doximity, NEJM AI or the tech press; the only physician-facing coverage of Grok Bot is two generic explainers from Passive Income MD.

### Cited Findings
- Passive Income MD, "What Is Grok Bot? xAI's AI Agent Explained for Physicians", 15 Oct 2026: describes Grok Bot as "an AI agent from xAI (also called SpaceXAI) that launched in beta on August 11, 2026"; names no physician-built bot; no author byline visible. [opened] — [passiveincomemd.com](https://passiveincomemd.com/blog/tech/what-is-grok-bot-for-physicians/)
- Passive Income MD, "Muse AI vs. Grok Bot: Which AI Agent Fits Physicians Best?", 30 Oct 2026: use cases are hypothetical (a physician with a side business; a practice owner wanting weekly admin jobs); names no physician builder. [opened] — [passiveincomemd.com](https://passiveincomemd.com/blog/tech/muse-ai-vs-grok-bot/)
- Site-restricted searches for "OpenClaw" and for "Grok Bot" across kevinmd.com, medscape.com, statnews.com, medpagetoday.com, fiercehealthcare.com, beckershospitalreview.com and doximity.com returned no article about either agent framework. Hits on those domains concerned the Grok chatbot, for example a July 2025 KevinMD opinion on Grok 4 and a Becker's piece on radiologists testing Grok's image analysis. [snippet] — [KevinMD](https://kevinmd.com/2025/07/why-grok-4-could-be-the-next-leap-for-hipaa-compliant-clinical-ai.html); [Becker's](https://www.beckershospitalreview.com/radiology/radiologists-test-elon-musks-image-ai-tool/)
- Mainstream coverage of Grok Bot found in passing concerned businesses, not physicians (for example Gopuff using Grok Bot, 12 Nov 2026). [snippet] — [Philadelphia Inquirer](https://www.inquirer.com/business/gopuff-spacex-grok-bot-ai-grocery-orders-20261112.html)
- Health-tech commentary on OpenClaw exists but is industry forecast, not a doctor profile. [snippet] — [healthcare.digital](https://www.healthcare.digital/single-post/how-will-openclaw-impact-healthcare-technology-in-2026); [onhealthcare.tech](https://www.onhealthcare.tech/p/openclaw-in-the-clinic-a-business)

### Inferences
- Trade media have not yet picked up physician self-builds on these frameworks; any such story is living on personal channels and closed communities.

### Gaps
- The Verge, Wired, 404 Media and Business Insider were not searched site-by-site; none surfaced in general searches.
- Paywalled outlets (STAT+, Medscape login) may hold items invisible to search.

## 4. Are there physician-builder communities that showcase a member's assistant on these frameworks?

### Takeaway
One physician-led Grok Bot community exists ("Grok-Bot Dr", free, private, 60 members, run by a retired dermatologist), but its showcase content is not public; the large public bot directories contain essentially no physician-built, specialty-specific bots.

### Cited Findings
- "Grok-Bot Dr" (Skool): physician-led, free, private, 60 members, twice-monthly recorded office hours; explicitly "One product only" (Grok Bot) and "If you want n8n templates or agency tactics, this is the wrong room." [opened] — [Skool](https://www.skool.com/grok-bot-dr-5856)
- ReadMultiplex "Every Grok Bot: The Complete Directory" ("Updated daily"): read in full across four fetches (about 363k characters). Health entries are consumer coaches, billing/appeals helpers and visit-prep bots; the only "doctor-built" claim is Pulse; the only practice-facing entry is "Consider It Marketed"; no radiology, cardiology or other specialty bots. [opened] — [readmultiplex.com](https://readmultiplex.com/grokbot-rocks/)
- Grok Bot Index (611 templates): has no healthcare category (nearest is "Health, fitness and food", 37 templates); medical templates are patient-side (Body of Evidence, Checkup, Doctor Visit Prep for Women, Medicine & Appointment Reminders, T1D Helper, Health Helper); no creator described as a doctor. Read to about 200k of 213k characters. [opened] — [grokbotindex.com](https://grokbotindex.com/)
- OpenMausBot's official playbook repo lists six teams (SEO Growth, Engineering, 100x Marketing, Reddit Lead Miner, Competitor Watch, Inbox Follow-up); none medical. [opened] — [github.com/milind-soni/openmausbot-teams](https://github.com/milind-soni/openmausbot-teams)
- OpenMausBot teams can also be distributed through BotMRR ("Add to OpenMausBot") or imported from a file or public GitHub URL. [opened] — [github.com/milind-soni/openmausbot](https://github.com/milind-soni/openmausbot)
- Searches pairing Grok Bot/OpenMausBot/OpenClaw with "physicians who code", "doctors who code", "MD+", "vibe coding" and Reddit physician terms returned no physician showcase. [snippet-level null result] — [example result set: Creator Economy interview with Grok Bot's own team](https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan)

### Inferences
- A physician sharing a specialty bot today most likely does so via an x.ai/bot share link posted on X or inside a closed group, which is why directories show little.

### Gaps
- BotMRR, botdirectory.ai, skillsdojo.com/templates and grokbottemplates.app were not opened.
- Discord servers, physician Slack groups, Doximity and Facebook groups are not searchable from here.
- Reddit and Hacker News searches returned nothing relevant, but indexing of both is partial.

## 5. For each candidate, was a repo, template, skill pack or setup guide published, and is the assistant shared or sold?

### Takeaway
Only the radiology items have public code; the best-documented clinician build (Yukio) has a how-to narrative but no repo and is monetised through consulting.

### Cited Findings
- Dr. TJ Ahn (Yukio): written guide plus video; no code/template linked; paid implementation help offered via a booking link; newsletter sign-up. [opened] — [drtjahn.com](https://drtjahn.com/openclaw-yukio-my-hands-on-ai-assistant-guide); [YouTube](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- Dr. Lautner (Grok-Bot Dr): course modules inside a free private community; no public repo or bot link. [opened] — [Skool](https://www.skool.com/grok-bot-dr-5856)
- Dr. Kavan R. Thompson: public GitHub skill pack, install by `cp -r curated/* ~/.claude/skills/`; no licence stated. [opened] — [GitHub](https://github.com/kavanthompson/radiology-ai-skills)
- Francisco Salido: public MIT-licensed repo. [opened] — [GitHub](https://github.com/franciscosalido/OPENCLAW)
- "Wilson" (Pulse): publicly installable via x.ai/bot/DdNlDzU_cYi-JJv2YR2CS; instructions, skills and routines not listed. [opened] — [builder.grokbot.rocks](https://builder.grokbot.rocks/bot/DdNlDzU_cYi-JJv2YR2CS/)
- Sohaib Qadri (CuraClaw): demo video only; no repo link in the description. [opened] — [YouTube](https://www.youtube.com/watch?v=RF8fR4V3EN8)
- Near-miss with the most complete artefact: Aryan Iyappan's openbot-radiology publishes the team export, role guidance and radiology skills, but "is operational configuration, not a one-command fresh-machine installer"; importing "does not restore credentials, model selections, or permission grants". [opened] — [GitHub](https://github.com/aryaniyaps/openbot-radiology)
- Near-miss with open code and a physician track: Longevity Grok, MIT, github.com/Insilico-org/plsi. [opened] — [longevitygrok.si](https://longevitygrok.si/)

### Inferences
- A physician wanting to replicate a specialty assistant on OpenMausBot today would get more reusable material from openbot-radiology and the Thompson skill pack than from any physician narrative found.

### Gaps
- Licence and exact contents of the Thompson and Iyappan repos were not inspected at file level.

## 6. What concerns (HIPAA/PHI, framework security incidents) did they address?

### Takeaway
Clinician and physician-facing sources consistently say to keep patient data out: no HIPAA coverage or BAA is stated for Grok Bot, and the one clinician who documented an OpenClaw build led with server hardening rather than HIPAA.

### Cited Findings
- Dr. TJ Ahn opens his video with security ("we need to talk about security"; chapter "Security warning: Clawdbot → 'Moltbot' → OpenClaw") and lists his controls: VPS hosting, SSH key authentication, localhost-only gateway, Tailscale VPN, strict firewall rules, regular audits, frequent API key rotation. [opened] — [YouTube](https://www.youtube.com/watch?v=7xtWe3s_Tk8)
- His blog cites reports of exposed instances leaking API keys, says "it can keep data private if you secure it", keeps a human in the loop for outreach, and does not mention HIPAA or PHI. [opened] — [drtjahn.com](https://drtjahn.com/openclaw-yukio-my-hands-on-ai-assistant-guide)
- Passive Income MD on Grok Bot: "Nothing reviewed says Grok Bot is covered, so keep patient information out"; "The FAQ says Grok Bot requires cloud data storage and does not support Legacy Privacy Mode."; xAI's BAA request page concerns its APIs, not Grok Bot. [opened] — [passiveincomemd.com, 15 Oct 2026](https://passiveincomemd.com/blog/tech/what-is-grok-bot-for-physicians/)
- Passive Income MD on Muse and Grok Bot: "neither company says its agent is covered under HIPAA."; "Keep patient information out of both, and check with your compliance team." [opened] — [passiveincomemd.com, 30 Oct 2026](https://passiveincomemd.com/blog/tech/muse-ai-vs-grok-bot/)
- A vendor guide warns Grok Bot has no approval gate ("will act on its own judgment unless you constrain it"), that it signs in with the practice's real credentials, and cites reports of a prompt-injection weakness (attributed to Adversa AI, The Register and Malwarebytes; not verified by me). [opened] — [uxcontinuum.com](https://uxcontinuum.com/grok-bot-for-doctors)
- A competitor claims that, as of October 2026, xAI had published no BAA for Grok Bot. Competitor marketing; verify with xAI. [snippet] — [phiclaw.ai](https://phiclaw.ai/hipaa-grok-bot-alternative/)
- A Grok Bot review notes "no SOC 2, ISO 27001, GDPR, HIPAA, or FedRAMP claim was attached at launch". [snippet] — [buildfastwithai.com](https://www.buildfastwithai.com/blogs/grok-bot-review)
- Dr. Lautner's community lists "Privacy" as a core module and says "physician-led work and privacy are the filter", without HIPAA specifics on the public page. [opened] — [Skool](https://www.skool.com/grok-bot-dr-5856)
- Patient-side OpenClaw builder Eugene Vestel: "Open Claw is not a consumer-ready product", "It's unsafe by default", "Never allow direct access to raw PHI", "Never install random skills", run agents on isolated machines. [opened] — [Substack, 24 Feb 2026](https://evestel.substack.com/p/how-i-build-my-personal-openclaw)
- openbot-radiology keeps credentials out of Git, imports routines paused, and labels its results as not clinical certification; it has no HIPAA statement. [opened] — [GitHub](https://github.com/aryaniyaps/openbot-radiology)
- OpenClaw is "susceptible to prompt injection attacks". [snippet] — [Wikipedia: OpenClaw](https://en.wikipedia.org/wiki/OpenClaw)

### Inferences
- Security-first framing (as in Ahn's video) is a useful authenticity signal for clinician-authored content; vendor pages instead lead with HIPAA branding.
- For OpenMausBot, the local-VM and local-harness design plausibly reduces cloud exposure compared with Grok Bot, but no physician source I found evaluates this, and bots there are general coding agents with shell and file access.

### Gaps
- A search summary cited a SecurityScorecard scan of more than 135,000 internet-exposed OpenClaw instances with 63% vulnerable; I could not tie this to a specific page, so it is unverified.
- I did not open xAI's own Grok Bot documentation or terms, so the HIPAA/BAA position rests on third-party readings.
- No physician-authored account of a security or PHI incident with either framework was found.
