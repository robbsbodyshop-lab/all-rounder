# Specialty-by-specialty sweep and scholarly/professional literature: physician-built specialty assistants on always-on "VM agent" frameworks

> Research date: 15 November 2026. Coverage window: late 2025 to today.
> Evidence tags: **[opened]** = I fetched the page and read the extraction; **[snippet]** = seen only in a search-result summary, not opened; **[API]** = returned by a GitHub or YouTube API call; **[transcript]** = auto-generated YouTube captions that I read in full.
> **Framing correction (verified independently, and consistent with the coordinator's mid-task note):** "Grok Bot" and "OpenMausBot" are real, literal products, not garbled names for OpenClaw (sources in Key Question 1, section A). This file therefore holds two sweeps: the original OpenClaw-family sweep, kept as fallback, and a literal-name re-sweep focused on August to November 2026 (Key Question 1, section F).
> Prompt-injection check: no opened page contained text directing the agent to do anything. Search summaries mentioned odd embedded "proprietary and confidential" notices inside third-party mirror copies of OpenClaw medical skill files; I did not open or act on those.

## Key Question 1: For each specialty, is there a named physician who built an OpenClaw/Moltbot/Clawdbot-based (or Manus/OpenManus/Hermes-Agent/Grok-based) assistant for that specialty? What is it called and where is it described?

### Takeaway
On the literal names (Grok Bot / OpenMausBot) no physician-built specialty assistant was found in any of the 24 specialties; the nearest verified items are an interventional cardiologist who used Grok Bot on stage at AHA Scientific Sessions on 7 Nov 2026 (Michał Nedoszytko, MD, PhD), the company-built Longevity Grok, and a Grok Bot teaching community run by a self-described retired dermatologist. If a comparable self-hosted framework is acceptable, the one item that meets all three criteria is Dr. Chukwuma Onyeije's Hermes Agent "AI operations partner" (maternal-fetal medicine; VPS-hosted, Telegram, 94 skills including MFM documentation skills; 17 May 2026), with a pathologist's OpenClaw society talk (Yosep Chong, MD, PhD) and an orthopedic surgeon's non-clinical Clawdbot agent "Multivac" (Christian Pean, MD, MS) as weaker fallbacks.

### Cited Findings

#### A. What the frameworks actually are (framing correction)
- **Grok Bot is a real product.** It is an early-beta agent product from SpaceXAI (formerly xAI), launched 11 Aug 2026; users create persistent Bots with a defined role that operate apps and websites on their behalf; "Each Bot operates through its own computer environment" and keeps working when the laptop is closed. Pricing reported: $200/month individual, $120/seat/month teams. No healthcare examples are given. [opened] — [VentureBeat](https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month)
- Trade press called Grok Bot "OpenClaw-style". [snippet] — [Neowin](https://www.neowin.net/news/spacexai-launches-openclaw-style-grok-bot-that-can-work-across-apps-on-its-own/)
- Custom Grok Bots are shared at x.ai/bot/<id> links, and a third-party directory lists "10,266+ Grok Bots". [opened] — [ReadMultiplex directory](https://readmultiplex.com/grokbot-rocks/)
- Conflict on isolation: a physician-audience explainer says "all Bots on an account share one cloud computer" and that xAI's docs say not to treat separate Bots as a security boundary [opened] — [Passive Income MD](https://passiveincomemd.com/blog/tech/what-is-grok-bot-for-physicians/); this differs in wording from "Each Bot operates through its own computer environment" [opened] — [VentureBeat](https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month). The docs URL I tried returned 404 — [docs.x.ai](https://docs.x.ai/grok-bot/overview.md).
- **OpenMausBot is a real product.** GitHub repository `milind-soni/OpenMausBot`, description "Open-source Grok Bot alternative with a virtual machine that bots can use", 23,264 stars on 15 Nov 2026. [API] — [GitHub](https://github.com/milind-soni/OpenMausBot)
- OpenMausBot is also known as MausBot and was formerly called "OpenGrokBot"; Apache-2.0; each bot can get a cloud Linux desktop, an isolated local VM, or the user's own computer; bots run on the `claude`, `codex` and `grok` CLIs; a whole team can be installed from one Markdown file with YAML frontmatter imported from disk or a public GitHub URL. The README has no showcase and mentions no medical or physician bots. [opened] — [GitHub README](https://github.com/milind-soni/OpenMausBot)
- The author announced it on X as an open-source version of Grok Bot that "can spin up virtual machines". [snippet] — [X post by Milind S](https://x.com/milindlabs/status/2087289803964559746)
- The official community templates repo lists six team playbooks (SEO Growth, Engineering, 100x Marketing, Reddit Lead Miner, Competitor Watch, Inbox Follow-up); none are medical. [opened] — [openmausbot-teams](https://github.com/milind-soni/openmausbot-teams)
- A GitHub repository search for "openmausbot" and "mausbot" returned roughly 50 forks, skills repos and clones; none has a medical, clinical or physician description. [API] — [GitHub search](https://github.com/search?q=openmausbot&type=repositories)
- A fork exists under the username `dr-biko`; the page gives no name, bio or profession and no medical content, so it is not evidence of a physician build. [opened] — [dr-biko/MausBot](https://github.com/dr-biko/MausBot)
- OpenMausBot's "Built with Composio" showcase page lists no downstream projects. [opened] — [Composio](https://composio.dev/built-with/openmausbot)

#### B. Candidates, with match strength

**B1. Chukwuma Onyeije, MD, FACOG — maternal-fetal medicine (OB/GYN subspecialty) — Hermes Agent on a VPS — match: STRONG on the three criteria (verifiable physician, specialty-specific skills, built on a named comparable framework); does NOT match the literal names Grok Bot/OpenMausBot.** (Candidate was first reported by another researcher; the items below are my own verification.)
- Credentials verified independently: MD, Howard University College of Medicine (1992); board certified in Obstetrics and Gynecology (1999) and Maternal and Fetal Medicine (2002), American Board of Obstetrics and Gynecology; practice Atlanta Perinatal Associates, Atlanta, GA. [opened] — [Emory Healthcare provider profile](https://www.emoryhealthcare.org/providers/chukwuma-onyeije-778536)
- "I Gave an AI Agent 94 Skills and Let It Help Run My Clinical, Coding, and Theology Workflows", 17 May 2026: Hermes Agent, described as "a self-hosted, multi-model AI system running on a VPS", reached through a Telegram bot, framed as "a 24/7 AI operations partner"; three weeks in production at time of writing. Specialty-specific skills named: a signout-to-APSO pipeline for inpatient MFM documentation (outputs include physician sign-out, patient-friendly explanation, referral note, outpatient workup plan, missing-data list, care coordination plan, draft message to the referring provider) and MFM letters; other skill clusters cover content, DevOps, GitHub, productivity, research. Models are not named in this post. "The HIPAA considerations are real and required deliberate architectural decisions"; specifics deferred to a companion architecture post. No GitHub link for the agent, its skills or its config. [opened] — [Doctors Who Code](https://doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows)
- Blog archive shows the sequence: "I Built an OpenClaw Agent to Understand What Developers Are Actually Doing" (10 Feb 2026); "Post-Mortem: Why I'm Stepping Back from My OpenClaw Experiment" (12 Feb 2026); the Hermes Agent post and "The Architecture Behind My 24/7 AI Operations Partner" (17 May 2026); "I Gave Doctors Who Code a Phone Number" (DWC-Bot voice assistant, 19 Sep 2026); "I Built an AI Agent. Now I Am Building the Laboratory Around It." (AgenticBuilderMD, 20 Sep 2026). No title or excerpt mentions Grok Bot, OpenMausBot or Manus. [opened] — [Doctors Who Code archive](https://doctorswhocode.blog/blog/)
- "The Harness Is the Workplace" (3 Sep 2026) compares Claude Code, Codex, Google Antigravity, OpenClaw, Hermes and Omarchy; says he tested OpenClaw then Hermes in 2026 as persistent agents reached through messaging; does not mention Grok Bot or OpenMausBot; advises against putting PHI or institutional credentials into a personal agent environment. [opened] — [Doctors Who Code](https://doctorswhocode.blog/blog/the-harness-is-the-workplace)
- "The Most Important Thing My AI Agent Did Was Nothing" (25 Oct 2026) names "my AI agent, Hark"; the framework and hosting are not stated in that post; the task was a non-clinical billing errand. [opened] — [Doctors Who Code](https://doctorswhocode.blog/blog/the-most-important-thing-my-ai-agent-did-was-nothing)
- Related public repositories under his account: `doctorswhocode-engine` ("Telegram-driven research ingestion, analysis, MDX drafting, PDF export, and editorial workflow infrastructure for physician-builders", created 1 Apr 2026) and `pgis-manus-skill` (a Manus skill for endurance training with type 2 diabetes, "Built by a physician-developer", created 25 Feb 2026). Neither is the MFM agent. [API] — [GitHub search](https://github.com/search?q=doctorswhocode&type=repositories)

**B2. Michał Nedoszytko, MD, PhD — interventional cardiology — Grok Bot (literal name) — match: PARTIAL (verified physician; Grok Bot named in his own words at a cardiology society meeting; used as a general build/operations agent, not a persistent named specialty assistant; no public template).**
- Session "Opening Session: Designing and Deploying Real-World AI Agents", American Heart Association Scientific Sessions 2026, Health Innovation Pavilion, McCormick Place, Chicago, 7 Nov 2026, 9:15–9:45 AM; speaker "Michał Nedoszytko, MD, PhD, Clinician Scientist, Abridge"; posted to the AHA YouTube channel 13 Nov 2026. [API] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- In the talk he says "I'm an interventional cardiologist", trained in Poland (Medical University of Gdańsk; internal medicine, cardiology, PhD in cardiovascular genetics), moved to Belgium in 2019 and led a team of 15 cardiologists, and now works full-time for Abridge. [transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- He names three tools used live: Codex (OpenAI), Claude Code (Anthropic) and Grok Bot (the auto-captions render it variously as "Rockbot", "Grok bot", "Grokbot", "Clockbot"). Audience ideas were assigned to each: a 10-year CVD risk calculator for caregivers (Claude Code), a heart-failure "digital twin" (Codex), and a patient disease-education helper for coronary disease, hypercholesterolemia, heart failure and atrial fibrillation (Grok Bot). [transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- On Grok Bot specifically: "this whole framework, this application was actually built by Grok bot"; the demo "is actually happening on my own private server that was set up by Grok"; he says he handed over the server keys ("Maybe it was dangerous"); he describes Grok Bot spawning sub-agents and letting him work from his phone while it runs in the cloud. [transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- He cautions that building with real healthcare data needs a BAA and zero data retention from the AI vendor. [transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- Background: he built PostVisit.ai in seven days and placed third at Anthropic's hackathon on 20 Feb 2026. [snippet] — [Let's Data Science](https://letsdatascience.com/news/cardiologist-builds-ai-patient-care-platform-in-seven-days-6215e242)

**B3. Yosep Chong, MD, PhD, MIAC — pathology — OpenClaw — match: PARTIAL (physician + specialty-specific + society venue; no named assistant or public artifact; OpenClaw, not the literal names).**
- Digital Pathology Association, Pathology Visions 2026 (PV26), Sunday 18 Oct 2026, 1:35–1:55 PM PT; speaker "Yosep Chong, MD, PhD, MIAC, Professor, The Catholic University of Korea College of Medicine". Page title as fetched: "LLM agents in the pathologist's workflow: From daily productivity to diagnostic decision support". [opened] — [PV26 session 262](https://digitalpathologyassociation.org/pv26-agenda/show/session/262)
- The same session is indexed as "OpenClaw for pathologists: From daily productivity to diagnostic workflow support"; speaker page describes him as a pathologist focused on cytopathology, digital pathology and AI. [snippet] — [PV26 speaker page](https://digitalpathologyassociation.org/speakers/show/id/148/agenda/6)
- Abstract: OpenClaw as "an agentic workflow environment" for routine productivity (inbox, scheduling, reminders, meeting prep) and pathology support (case summarization, retrieval of prior materials, sign-out checklists, draft report organization, differential diagnosis assistance under pathologist oversight); value framed as a "supervised copilot"; OpenClaw is the only tool named; no model, hosting, assistant name or code is given. [opened] — [PV26 session 262](https://digitalpathologyassociation.org/pv26-agenda/show/session/262)

**B4. Christian Pean, MD, MS ("Techy Surgeon") — orthopedic trauma surgery — Clawdbot/OpenClaw, later Grok Bot and Hermes Agent — match: PARTIAL (physician + named personal agent; explicitly non-clinical; no public config).**
- "ClawdBot First Impressions from a Clinician-Founder", 30 Jan 2026: author identified as orthopedic trauma surgeon at Duke Health and CEO of RevelAi Health; agent named "Multivac"; Claude Opus 4.5 API; Telegram; used for startup research and outreach drafts, newsletter assets and organizing public CMS policy PDFs; "Nothing clinical."; "Clawdbot is a friggin' security nightmare."; no config shared. [opened] — [Techy Surgeon](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a)
- "Instinct, Muse, Grok Bot and Hermes: A Techy Surgeon's First Weeks With Agent Assistants", 23 Sep 2026 (partly paywalled): tested Grok Bot for several weeks ("clunky" in daily use) and Hermes Agent; uses Instinct daily for admin; OpenClaw "died on the vine for me"; "I also keep them away from anything that touches patients."; names no other physician builder. [opened] — [Techy Surgeon](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- "Substack Live: A Snippet of My Evolving AI OS", 26 Sep 2026: "How I split my work between ChatGPT, Claude Cowork and three agent assistants"; no clinical use visible (paywalled). [opened] — [Techy Surgeon](https://techysurgeon.substack.com/p/substack-live-a-snippet-of-my-evolving)
- A 21 Feb 2026 note teased "Paging Dr. OpenClaw"; the title is absent from the archive I fetched. [opened] — [Substack note](https://substack.com/@techysurgeon/note/c-217864463); [archive](https://techysurgeon.substack.com/archive)

**B5. Longevity Grok / PLSI — longevity (preventive) medicine — Grok Bot (literal name) — match: PARTIAL (specialty-specific, on Grok Bot, open source, physician tier; built by a company led by PhDs, not by an individual physician).**
- "Longevity Grok is a team of AI agents on Grok Bot", led by PLSI; 30 bots: 8 core, 13 optional specialists, 4 "Clinic" (physician role, early access by application: Patient Coordinator, Visit Assistant, Evidence Analyst, Clinic Liaison) and 4 "Lab". Code public on GitHub 30 Oct 2026; v0.2.0 on 5 Nov 2026; MIT licence; needs a Grok Bot account; "does not provide medical care". Named people (Insilico Medicine, Alex Zhavoronkov, David Sinclair, Fedor Galkin, Dominika Wilczok, Evelyne "Eva" Bischof, Dr. Fah Wanviput) are listed without medical credentials. [opened] — [longevitygrok.si](https://longevitygrok.si/)
- Press dated 9 Nov 2026 names David A. Sinclair, Ph.D. and Alex Zhavoronkov, Ph.D.; no MD listed; no physician quoted. [opened] — [BioPharma APAC](https://biopharmaapac.com/news/31/8649/insilico-medicine-launches-open-source-longevity-grok-with-harvard-researcher-david-sinclair.html)
- README: "multi-agent health toolbelt for Grok Bot"; PLSI Clinic has four workers (Panel, Visit Prep, Clinical Evidence, Liaison); 85 stars, 26 forks, 11 commits; outputs "are not reviewed by any clinician, scientist or team member before you see them."; OpenMausBot and VMs not mentioned. [opened] — [Insilico-org/plsi](https://github.com/Insilico-org/plsi)

**B6. "Grok-Bot Dr" (Skool) — Reinhold "Dr. Lautner", self-described retired dermatologist — Grok Bot (literal name) — match: PARTIAL/WEAK (physician-run teaching on the exact framework; no named specialty assistant visible; credentials unverified).**
- "a physician-led community for xAI Grok Bot"; run solo by Reinhold, "Dr. Lautner", self-described retired dermatologist living in Nicaragua; free, private; modules: Start Here, Install & First Bot, Clinical-style prompts, Three tested workflows, Privacy; office hours twice a month; 60 members at fetch; no named bot on the public page. [opened] — [Skool: Grok-Bot Dr](https://www.skool.com/grok-bot-dr-5856)
- A name search for him as a dermatologist returned no independent profile; credentials remain self-reported. [snippet-level negative] — [Skool: Grok-Bot Dr](https://www.skool.com/grok-bot-dr-5856)

**B7. Weak items**
- "Pulse", a Grok Bot by "Wilson" (@qpzm620), listed as a "Doctor-built health coach" (diet, exercise, sleep), first seen 6 Oct 2026; no full name, credentials or specialty on the page; consumer health coach. Match: WEAK. [opened] — [ReadMultiplex bot page](https://builder.grokbot.rocks/bot/DdNlDzU_cYi-JJv2YR2CS/)
- `kavanthompson/radiology-ai-skills` (created 19 Aug 2026, 0 stars): "Curated collection of high-value AI agent skills for radiology residents and physicians ... Optimized for Claude Code, Cursor, Grok, and ResidentShield / TemplateGuards workflows. Maintained by Dr. Kavan R. Thompson." A skills collection, not a persistent assistant; it names "Grok", not Grok Bot; I did not verify the maintainer's credentials. Match: WEAK. [API] — [GitHub search](https://github.com/search?q=radiology-ai-skills&type=repositories)
- `aryaniyaps/openbot-radiology` exists (created 28 Sep 2026, 0 stars, no description). Match: WEAK (nothing verifiable from metadata). [API] — [GitHub search](https://github.com/search?q=openbot-radiology&type=repositories)
- OpenHuman issue #4258, "Doctor-assistant templates with specialty workflows and clinical safety boundaries", opened 29 Jun 2026 on behalf of an unnamed interventional cardiologist; "Partially shipped" as of 11 Sep 2026 (generic `doctor` persona only). Match: WEAK (requested, not built, by a physician; different framework). [opened] — [tinyhumansai/openhuman #4258](https://github.com/tinyhumansai/openhuman/issues/4258)
- Not corroborated by my own searches (no hits; pages not opened): "CuraClaw" by Sohaib Qadri and "Yukio" by TJ Ahn, DPM, both reported by other researchers. [snippet-level negative] — [nearest hit returned for the CuraClaw query](https://github.com/sponsors/careagent)

#### C. Specialty-by-specialty result
Query IDs refer to section D (Q = original sweep, R = literal-name re-sweep, G = GitHub).

| Specialty | Literal names (Grok Bot / OpenMausBot) | Comparable frameworks (OpenClaw family, Hermes Agent, Manus) | Queries tried |
|---|---|---|---|
| Radiology | none found | none found; weak: radiology-ai-skills repo (B7); research: MedOpenClaw (KQ2) | Q2, Q20, Q26, Q32, Q40, R1, G |
| Pathology | none found | PARTIAL: Yosep Chong, OpenClaw, PV26 (B3) | Q12, Q18, Q48, R2, G |
| Emergency medicine | none found | none found | Q5, Q36, Q42, R3, G |
| Anesthesiology | none found | none found | Q8, Q36, Q40, Q42, R4, G |
| Critical care | none found | none found (near-miss: "Miss ICU" concept paper) | Q45, R4 |
| Cardiology | PARTIAL: Nedoszytko used Grok Bot at AHA, 7 Nov 2026 (B2) | weak: unnamed cardiologist's OpenHuman request (B7) | Q9, Q26, Q40, Q48, R5, R19, G |
| Oncology/hematology | none found | none found (near-miss: MeDucation AI) | Q11, Q26, Q48, R6, G |
| Neurology | none found | none found | Q15, Q47, R7 |
| Psychiatry | none found | none found | Q10, Q26, Q36, Q40, R7, G |
| Dermatology | PARTIAL/WEAK: Grok-Bot Dr community (B6); vendor "Skin Health Analyzer" template | none found | Q14, Q30, Q37, Q40, R8, R20, G |
| Orthopedics and other surgical fields | weak: Pean tested Grok Bot, non-clinical (B4) | PARTIAL: Pean's "Multivac" on Clawdbot, non-clinical (B4) | Q7, Q24, Q36, Q40, R9, G |
| Ophthalmology | none found | none found | Q14, Q48, R11 |
| Primary care (family/internal medicine) | none found | none found | Q13, Q48, R10, G |
| Hospital medicine | none found | none found | Q16, Q36, Q40, R10, G |
| Pediatrics | none found | none found | Q17, Q40, Q47, R11, G |
| OB/GYN (incl. maternal-fetal medicine) | none found | STRONG: Onyeije, Hermes Agent on a VPS with MFM skills (B1) | Q17, Q47, R11, R20 |
| Nephrology | none found | none found | Q15, Q47, R12 |
| Gastroenterology | none found | none found (near-miss: Samir Grover, Claude Code, non-clinical) | Q15, Q47, R12 |
| Infectious disease | none found | none found | Q46, R12 |
| Endocrinology | none found | none found (near-miss: Onyeije's Manus skill for type 2 diabetes training, not his specialty) | Q15, Q47, R12 |
| PM&R | none found | none found | Q46, R13 |
| Urology | none found | none found | Q17, Q47, R13 |
| ENT | none found | none found | Q17, Q47, R13 |
| Clinical informatics | none found | none found | Q21, Q42, R13 |
| (Not on the list) Longevity/preventive medicine | PARTIAL: Longevity Grok / PLSI, company-built (B5) | — | Q38, Q39, Q41 |

- Vendor "OpenClaw for doctors" guides list per-specialty use cases but have no named physician builder. [snippet] — [Ampere.sh](https://www.ampere.sh/blog/openclaw-for-doctors); [OpenClaw Playbook](https://www.openclawplaybook.ai/guides/openclaw-for-doctors)

#### D. Queries run (web search unless noted)
Original sweep, OpenClaw-family reading:
- Q1 `physician built OpenClaw assistant medical specialty`
- Q2 `radiologist OpenClaw agent "I built"`
- Q3 `OpenClaw clinical medicine preprint arXiv medRxiv physician agent`
- Q4 `doctor Clawdbot Moltbot personal assistant clinic "MD"`
- Q5 `emergency physician OpenClaw personal AI agent`
- Q6 `OpenClaw healthcare JMIR OR "npj Digital Medicine" OR "NEJM AI" viewpoint`
- Q7 `techysurgeon substack OpenClaw surgeon agent`; `"Paging Dr. OpenClaw" Techy Surgeon Christian Pean`
- Q8 `anesthesiologist OpenClaw OR Clawdbot OR Moltbot "my agent"`
- Q9 `cardiologist built OpenClaw agent cardiology assistant`
- Q10 `psychiatrist OpenClaw personal agent built practice`
- Q11 `oncologist OpenClaw agent "oncology" personal assistant built physician`
- Q12 `pathologist OpenClaw agent pathology "I built" OR "my assistant"`
- Q13 `family physician OpenClaw "primary care" personal AI agent built doctor`
- Q14 `dermatologist OR ophthalmologist OpenClaw agent built own practice`
- Q15 `"OpenClaw" neurologist OR nephrologist OR gastroenterologist OR endocrinologist built personal agent`
- Q16 `hospitalist OR "hospital medicine" OpenClaw agent physician built "my OpenClaw"`
- Q17 `pediatrician OR "OB/GYN" OR urologist OR otolaryngologist OpenClaw agent built physician`
- Q18 `Yosep Chong OpenClaw pathologist agent`; `Yosep Chong OpenClaw pathology paper OR webinar OR lecture agent pathologist workflow 2026`
- Q19 `physician "Hermes Agent" OR "OpenManus" OR "Manus" personal assistant built doctor specialty`
- Q20 `OpenClaw RSNA OR SIIM OR AMIA 2026 abstract radiology agent personal assistant`
- Q21 `"OpenClaw" physician "clinical informatics" OR "CMIO" built personal agent blog`
- Q22 `doctor YouTube "OpenClaw for doctors" OR "OpenClaw for physicians" MD course setup`
- Q23 `OpenClaw PubMed 2026 letter editorial clinicians "OpenClaw" medicine journal`
- Q44 Chinese-language: `医生 OpenClaw 龙虾 科室 个人助手 搭建 放射科 OR 病理科 OR 心内科 OR 外科`

First literal-name pass (run before the coordinator's note, after I found the names were real):
- Q24 `"Grok Bot" physician OR doctor OR surgeon built custom assistant specialty`
- Q25 `"OpenMaus" OR "OpenMausBot" OR "MausBot" agent`
- Q26 `"Grok Bot" radiologist OR cardiologist OR oncologist OR psychiatrist "I built" bot medical`
- Q27 `physician built specialty assistant on agent assistant framework VM "Grok Bot" OR "Instinct" OR "Muse" OR "Hermes" medicine November 2026`
- Q28 `OpenMausBot physician OR doctor OR medical OR clinical assistant built on top`
- Q29 `"OpenMausBot" medical specialty personal assistant github physician` (extended)
- Q30 `"MausBot" OR "OpenMausBot" doctor "specialty" assistant playbook clinic dermatology OR radiology OR cardiology OR surgery` (extended)
- Q31 `"Grok Bot" "physician" built "specialty" personal assistant bot playbook "fellow physicians"` (extended)
- Q32 `"Grok Bot" "radiology" OR "radiologist" bot built by radiologist x.ai/bot share`
- Q33 `"Grok Bot" physician-built OR "doctor-built" OR "built by a physician" OR "built by a doctor" bot for doctors specialty` (extended)
- Q34 `"Grok Bot" kevinmd OR doximity OR medscape OR "physician" "I built" bot "my specialty"`
- Q35 `"Grok Bot" OR "OpenMausBot" medRxiv OR arXiv OR JMIR clinical physician evaluation persistent agent 2026`
- Q36 `"Grok Bot" surgeon OR anesthesiologist OR "emergency physician" OR hospitalist OR psychiatrist substack "my bot" clinic workflow built`
- Q37 `Dr. Lautner dermatologist "Grok Bot" physician-led community bot`
- Q38 `"Longevity Grok" OR "longevitygrok" physician built Grok Bot clinic team longevity medicine`
- Q39 `physician built "Grok Bot" team for "longevity" OR "functional medicine" OR "concierge" OR "lifestyle medicine" doctor MD personal assistant open source OpenMausBot`
- Q40 `"Grok Bot for" radiologists OR surgeons OR psychiatrists OR dermatologists OR cardiologists OR anesthesiologists OR hospitalists OR pediatricians`
- Q41 `physician "Grok Bot" OR "MausBot" "specialty" assistant "open source" github doctor built "for my practice" OR "for my specialty" OR "for fellow physicians" October OR November 2026` (extended)
- Q42 `"OpenClaw" OR "Grok Bot" session OR abstract OR webinar 2026 society physicians "USCAP" OR "CAP26" OR "SIIM" OR "RSNA 2026" OR "AMIA 2026" OR "ASCO" OR "ACEP26" OR "ANESTHESIOLOGY 2026"` (extended)
- Q43 `physician newsletter OR podcast "OpenClaw" OR "Hermes Agent" OR "Grok Bot" "my agent" named radiologist OR psychiatrist OR "emergency physician" OR hospitalist OR oncologist "I named"` (extended)
- Q45 `intensivist OR "critical care" physician OpenClaw OR "Grok Bot" OR OpenMausBot personal agent built ICU`
- Q46 `"infectious disease" OR "PM&R" OR physiatrist physician OpenClaw OR "Grok Bot" OR "Hermes Agent" personal agent built "I built"`
- Q47 `"Grok Bot" neurologist OR nephrologist OR gastroenterologist OR endocrinologist OR pediatrician OR urologist OR "OB/GYN" OR otolaryngologist bot built doctor`
- Q48 `"Grok Bot" OR "OpenMausBot" cardiologist OR oncologist OR ophthalmologist OR pathologist OR "family physician" OR "internist" built bot "MD" assistant`

Literal-name re-sweep after the coordinator's scope correction (all 24 specialties):
- R1 `"Grok Bot" radiologist "my bot" OR "I built" OR "bot team"`
- R2 `"Grok Bot" pathologist OR pathology bot built MD`
- R3 `"Grok Bot" "emergency medicine" OR "ER doctor" OR "emergency physician" bot built`
- R4 `"Grok Bot" anesthesiologist OR intensivist OR "critical care" "my bot" OR "I built"`
- R5 `"Grok Bot" cardiologist "bot team" OR "my bot" OR "I built"`
- R6 `"Grok Bot" oncologist OR hematologist "my bot" OR "I built" OR "bot team"`
- R7 `"Grok Bot" neurologist OR psychiatrist "my bot" OR "I built" OR "bot team" doctor`
- R8 `"Grok Bot" dermatologist OR dermatology "my bot" OR "I built" OR "bot team"`
- R9 `"Grok Bot" orthopedic OR surgeon "my bot" OR "I built" OR "bot team"`
- R10 `"Grok Bot" "family medicine" OR "primary care" OR internist OR hospitalist doctor "I built" bot`
- R11 `"Grok Bot" pediatrician OR obstetrician OR "OB/GYN" OR ophthalmologist "I built" OR "my bot"`
- R12 `"Grok Bot" nephrologist OR gastroenterologist OR endocrinologist OR "infectious disease" doctor built bot`
- R13 `"Grok Bot" physiatrist OR urologist OR otolaryngologist OR "clinical informatics" doctor built bot`
- R14 `"x.ai/bot" physician OR "MD" OR clinician specialty bot "for doctors" OR "for physicians"`
- R15 `"OpenGrokBot" OR "GrokBot" physician OR doctor OR clinic OR medical specialty assistant 2026`
- R16 `"MausBot" OR "OpenMausBot" doctor OR physician "I built" OR "my bot" OR "bot team" clinic OR practice OR specialty`
- R17 `"Grok Bot" ACR OR RSNA OR ACEP OR ASA OR AAD OR APA OR AAFP OR ACP OR SHM OR AMIA physicians blog OR podcast OR webinar agent 2026`
- R18 `"Grok Bot" PubMed OR SSRN OR medRxiv OR "npj Digital Medicine" OR "NEJM AI" OR JAMA clinician agent viewpoint OR letter 2026`
- R19 `Nedoszytko American Heart Association Scientific Sessions 2026 "AI agent" live build "Grok Bot" OR OpenMausBot OR OpenClaw OR "Claude"`; `Nedoszytko "Grok Bot" cardiologist agent "my bot" OR "Grok Bot" Abridge physician hackathon Shack15`; `"Vibe Coding" "Clinical Reality" Nedoszytko NEJM November 2026`
- R20 verification searches: `Reinhold Lautner Dermatologe OR dermatologist Dr. Lautner Hautarzt Nicaragua`; `doctorswhocode.blog Onyeije "Hermes Agent" maternal-fetal medicine agent`; `Kavan Thompson radiology-ai-skills radiologist github OpenClaw OR "Grok Bot" OR Claude skills`; `"CuraClaw" Sohaib Qadri physician OpenClaw`; `"TJ Ahn" DPM "Yukio" OpenClaw podiatrist agent`

Other tools:
- G: GitHub repository search (API): `openmausbot`, `mausbot` (results, none medical); 25 phrase queries of the form `grok bot <term>` / `openmausbot <term>` / `grokbot <term>` for physician, clinic, doctor, medical, radiology, surgeon, psychiatry, cardiology, dermatology, oncology, hospitalist, emergency medicine, anesthesia, pathology, pediatrics, primary care, clinician, clinical, residency (zero repositories each); `radiology-ai-skills`, `openbot-radiology`, `doctorswhocode` (results); `curaclaw`, `hermes agent physician`, `hermes-agent medical` (zero).
- YouTube search (API): `doctor built Grok Bot assistant for physicians specialty`; `OpenMausBot doctor physician medical assistant`; full transcript read for the AHA session.
- Directory scan: ReadMultiplex "Every Grok Bot" directory, top-30-per-category view only. [opened] — [ReadMultiplex directory](https://readmultiplex.com/grokbot-rocks/)

#### E. Near-miss list (and why each misses)
- **SecondMed** (Grok Bot), "I Built My Own AI Health Assistant (Grok Bot)", Beginners in AI channel, 11 Sep 2026. Misses: builder not presented as a physician; patient-side. [API] — [YouTube](https://www.youtube.com/watch?v=d7I82Ji45II)
- **Evipedia Grok Bot** (11 Sep 2026): "A specialized AI assistant offering an evidence-based 2nd opinion on health and longevity interventions", on the AI4L framework hosted under the Forever Healthy GitHub organization. Misses: no physician builder named; consumer-facing. [opened] — [Lifespan.io](https://lifespan.io/?p=158773)
- **Grok Bot directory health bots**: Medical Bill Auditor (Brian Roemmele), Clinical Orchestrator (Santi), Cost-Smart Health Brief (Amina Guleid), "Consider It Marketed" (clinic-marketing team by "Cindy", first seen 21 Sep 2026). Misses: no physician credentials; not specialty-specific. [opened] — [ReadMultiplex directory](https://readmultiplex.com/grokbot-rocks/)
- **Third-party x.ai/bot health bots** surfaced in the re-sweep: Health Pot, Health Helper, My First Health Bot (by TrevorGilman), Medical Bill Review (by Marc), Copay Compass, Appeal Desk. Misses: no clinical credential on any listing; patient-side. [snippet] — [Health Pot](https://x.ai/bot/E6O_rj5aW0sWo_s-GEa2y); [My First Health Bot](https://x.ai/bot/31D69UiAib5rf67Ag1_Ba); [Medical Bill Review](https://x.ai/bot/M9c2tC_-mwY8XNTmSbkUY)
- **Vendor Grok Bot templates** "Skin Health Analyzer", "Oral Health Analyzer", "Occupational Health Analyzer", "Rehabilitation Analyzer" credited to TemplatesGrokBot.com. Misses: no individual or physician author; paywalled. [opened] — [Complete AI Training](https://completeaitraining.com/grokbot-templates/bot/skin-health-analyzer/)
- **"Doctor" Grok Bot template** by Vincenzo Palazzo (first listed 28 Sep 2026): "Doctor assistant for visit prep and question lists, not diagnosis". Misses: patient-facing; no credentials. [opened] — [grokbotwiki](https://www.grokbotwiki.com/bots/doctor)
- **Samir C. Grover, MD** (Scarborough Health Network), "The AI agent-augmented physician", 13 Feb 2026: supervises a Claude Code agent that "writes code, debugs systems, manages infrastructure, and sends messages across platforms". Misses: Claude Code, not a personal-agent framework; non-clinical; no specialty content. [opened] — [Substack](https://samirgrovermd.substack.com/p/the-ai-agent-augmented-physician)
- **"Health CLAW" / personal OpenClaw health agent** by Eugene Vestel (24 Feb 2026): OpenClaw + Claude with a FHIR guardrail proxy. Misses: no physician credentials stated; patient-side. [opened] — [Substack](https://evestel.substack.com/p/how-i-build-my-personal-openclaw)
- **Tula** (OpenClaw-based) by RealActivity CEO Paul Swider, a self-described biohacker. Misses: not a physician. [snippet] — [Cloud Wars](https://cloudwars.com/copilot-podcast/ai-agent-and-copilot-podcast-openclaw-powered-healthcare-assistant-builds-patient-agency/)
- **MeDucation AI** by oncologist Roupen Odabashian: personalized oncology updates by email. Misses: framework not stated; a service for others. [snippet] — [OncoDaily](https://oncodaily.com/voices/roupen-odabashian-585488)
- **FreedomIntelligence OpenClaw-Medical-Skills** (radgpt-radiology-reporter, precision-oncology-agent, computational-pathology-agent). Misses: research-group skills library. [snippet] — [Open Skill Index](https://openskillindex.com/skills/freedomintelligence-openclaw-medical-skills-radgpt-radiology-reporter)
- **Baidu Health "DoctorClaw"** (OpenClaw-based assistant for doctors, internal testing). Misses: commercial. [snippet] — [Habr](https://habr.com/ru/post/1013388)
- **ibl.ai healthcare agents** and setup services. Misses: commercial. [snippet] — [ibl.ai](https://ibl.ai/solutions/medical-healthcare/agents.md)
- **Hermes Agent for doctors** vendor guide. Misses: no physician builder. [snippet] — [Hermify](https://www.hermify.io/blog/ai-agent-for-doctors)
- **CareAgent** GitHub organization (contact at medomatic.ai): no public members or repositories. Misses: nothing verifiable. [opened] — [GitHub](https://github.com/sponsors/careagent)
- **Prahlad Menon's post on MedOpenClaw** (31 Mar 2026): commentary; no physician credential stated; no personal build. [opened] — [The Menon Lab](https://themenonlab.blog/blog/medopenclaw-when-more-tools-makes-ai-worse)
- **"Miss ICU"**: conceptual ICU agent from the University of Parma's anesthesiology and critical care division. Misses: not on these frameworks; concept only. [snippet] — [Acta Biomedica](https://mattioli1885journals.com/index.php/actabiomedica/article/download/18512/13416/158141)

#### F. Addendum: literal-name re-sweep (Grok Bot / GrokBot / OpenMausBot / MausBot / OpenGrokBot / x.ai/bot), August to November 2026
- Result by specialty: 13 specialty-grouped queries (R1–R13) covering all 24 specialties returned no physician-built specialty bot on Grok Bot or OpenMausBot; the recurring hits were the Grok-Bot Dr community, the SecondMed tutorial, Evipedia, and patient-side x.ai/bot health bots without clinical credentials. [snippet] — [Skool: Grok-Bot Dr](https://www.skool.com/grok-bot-dr-5856); [Health Pot](https://x.ai/bot/E6O_rj5aW0sWo_s-GEa2y)
- "OpenGrokBot" plus medical terms and "MausBot"/"OpenMausBot" plus physician terms (R15, R16) returned nothing medical. [snippet-level negative] — [OpenMausBot](https://github.com/milind-soni/OpenMausBot)
- The one new literal-name finding is from a society recording, not from web search: an interventional cardiologist using Grok Bot on stage at AHA Scientific Sessions (B2). [transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- Many search hits for "Grok" plus a specialty concern the Grok chatbot (for example radiologists testing image reading in 2024), not Grok Bot; these are irrelevant to the target. [snippet] — [Becker's](https://www.beckershospitalreview.com/radiology/radiologists-test-elon-musks-image-ai-tool.html)
- A secondary blog reports that on 3 Nov 2026 Grok Bot gained the ability to research doctors and book appointments by phone; it is patient-side and unverified against a primary source. [snippet] — [PromptZone](https://www.promptzone.com/aleksandr_herrera/grok-ai-can-now-research-and-call-doctors-to-book-appointments-2nmm.md)

### Inferences
- The request's wording ("Grok Bot / OpenMausBot-style VM agent framework") matches real products exactly, so the asker probably saw something published between 11 Aug 2026 and today; "style" also leaves room for a look-alike framework such as Hermes Agent on a VPS.
- If look-alikes count, Onyeije's MFM agent is the only item found that is physician-built, specialty-specific and on an always-on self-hosted agent framework; if only the literal products count, nothing found qualifies and Nedoszytko's AHA demonstration is the nearest physician item.
- The 23 Sep 2026 Techy Surgeon post is the only physician-authored article I found whose title names "Grok Bot"; it may be where the asker met the terminology, but it describes no specialty assistant.
- Because an OpenMausBot team is one shareable Markdown file and a Grok Bot is one share link, a physician's specialty build could live only in a social post or closed community and stay invisible to web and repository-name search.

### Gaps
- I could not search X, LinkedIn, Reddit, Doximity, Sermo or Discord directly.
- GitHub code search (file contents) was unavailable; only repository names and descriptions were searched.
- The Skool "Grok-Bot Dr" classroom is private; Dr. Lautner's credentials are self-reported and no independent profile was found.
- The Grok Bot directory was read only in its top-30-per-category view.
- Onyeije: the companion architecture post (model stack, PHI boundary) was not opened; whether "Hark" (Oct 2026) is the same Hermes Agent deployment is not stated; the agent's skills are not public.
- Nedoszytko: the evidence is auto-generated captions, so product names are transcribed inconsistently; he showed no persistent cardiology assistant and published no template that I found.
- Chong: assistant name, model, hosting and any public template are unknown. Pean: paid sections were unreadable.
- Whether any Longevity Grok contributor is a practising physician was not established from the pages opened. (Background knowledge, not verified this session: Evelyne Bischof is publicly known as a longevity physician.)
- Kavan Thompson's credentials and the content of `aryaniyaps/openbot-radiology` were not verified; "CuraClaw" and "Yukio" could not be found by my searches.

## Key Question 2: Have any papers, preprints, journal viewpoints or conference abstracts described a physician's personal specialty agent built on these frameworks, or evaluated OpenClaw-style agents for clinical/physician work?

### Takeaway
Scholarly output exists on OpenClaw in medicine (two arXiv preprints from March 2026 and one unreviewed JMIR viewpoint preprint from July 2026), but none describes a physician's personal specialty assistant, and I found no scholarly item at all on Grok Bot or OpenMausBot. The conference-program items that do feature a physician using these frameworks are the PV26 pathology talk (OpenClaw) and the AHA 2026 session (Grok Bot).

### Cited Findings
- "When OpenClaw Meets Hospital: Toward an Agentic Operating System for Dynamic Clinical Workflows" (Wenxian Yang, Hanzheng Qiu, Bangqun Zhang, Chengquan Li, Zhiyong Huang, Xiaobin Feng, Rongshan Yu, Jiahong Dong), arXiv v1 12 Mar 2026, v2 21 Mar 2026: design proposal implemented on OpenClaw (restricted execution environment, document-centric patient/clinician agents, page-indexed memory, medical skills library); tested on 100 de-identified MIMIC-IV records with 300 queries (recall 0.877 vs 0.876 for a RAG baseline; precision 0.779 vs 0.352). No hospital deployment; not specialty-specific; author credentials not shown. [opened] — [arXiv 2603.11721](https://arxiv.org/abs/2603.11721)
- "MedOpenClaw and MedFlowBench: Auditing Medical Agents in Full-Study Workflows", arXiv, March 2026: an auditable runtime that lets vision-language models operate inside medical viewers such as 3D Slicer, with a full-study benchmark (brain MRI, lung CT/PET); performance degrades when professional support tools are enabled. Research system, not a physician's personal assistant. [snippet] — [arXiv 2603.24649](https://arxiv.org/abs/2603.24649)
- "OpenClaw and the Automation of Medical Artificial Intelligence: Autonomy, Security, and Regulation" (Lee, Wang, Kho), JMIR Preprints ID 108483, submitted 31 Jul 2026 to JMIR AI, unreviewed: argues near-term use should be confined to research and administrative contexts; cites a malicious-skills campaign on ClawHub and CVE-2026-32025. [snippet; the page returned an empty/maintenance response when fetched] — [JMIR Preprints 108483](https://preprints.jmir.org/preprint/108483)
- An npj Digital Medicine study that tested OpenManus and Manus on medical benchmarks reported modest accuracy gains over baseline LLMs (60.3% and 28.0% on AgentClinic MedQA and MIMIC) with >10× token usage and >2× latency. [snippet, via an aggregator] — [Synapse Social listing](https://synapsesocial.com/papers/W7130481397)
- Conference program, pathology: PV26, 18 Oct 2026, Yosep Chong, MD, PhD — OpenClaw in the pathologist's workflow. [opened] — [PV26 session 262](https://digitalpathologyassociation.org/pv26-agenda/show/session/262)
- Conference program, cardiology: AHA Scientific Sessions 2026 Health Innovation Pavilion, 7 Nov 2026, Michał Nedoszytko, MD, PhD — live build using Codex, Claude Code and Grok Bot. [API + transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- In that session he says that three days earlier his first article was published in the "New England Journal of Medicine", titled "Vibe Coding versus Clinical Reality"; my search did not locate the article, so title, journal (NEJM vs NEJM AI or another NEJM Group title) and date are unverified. [transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- Literal-name scholarly searches (Q35, R18) found no paper, preprint, viewpoint or letter on Grok Bot or OpenMausBot; the nearest hit is a January 2026 medRxiv preprint on agentic clinical history-taking that uses the Grok-3 model (DOI 10.64898/2026.01.23.26344723), which is not Grok Bot. [snippet] — [Listing of that preprint](https://www.immunosensation.de/publications/comparative-performance-of-agentic-ai-and-physicians-in-taking-clinical-history-across-leading-large-language-models-llms)
- PhysicianBench includes the Grok-4.20 model, not Grok Bot. [snippet] — [PhysicianBench](https://healthrex.github.io/PhysicianBench/)
- Searches for OpenClaw or Grok Bot sessions/abstracts at USCAP, CAP26, SIIM, RSNA 2026, AMIA 2026, ASCO, ACEP26 and ANESTHESIOLOGY 2026 returned none. [snippet-level negative] — [OpenClaw events listing surfaced by that search](https://www.createwith.com/tool/openclaw/events)
- An October 2026 Radiology review of agentic AI in radiology surfaced; the retrieved snippets do not mention OpenClaw. [snippet] — [Radiology](https://pubs.rsna.org/doi/epdf/10.1148/radiol.253226)

### Inferences
- The literature treats OpenClaw-style agents as an infrastructure and safety problem, not as a platform for individual physicians' specialty assistants.
- Grok Bot is three months old, so the absence of scholarly items on it is expected rather than informative; society stages and physician blogs are where it shows up first.

### Gaps
- OpenAlex lookup failed in this session (HTTP 429 and timeouts) and PubMed/Google Scholar were not queried directly; the scholarly sweep rests on general web search.
- The JMIR preprint page could not be opened, so author degrees and affiliations are unverified.
- RSNA 2026 (late November) had not taken place at the research date.
- arXiv 2603.24649 and the npj Digital Medicine article were not opened.

## Key Question 3: Have specialty societies or their blogs/podcasts, or clinical-informatics groups, featured such a physician-built assistant?

### Takeaway
Two society-stage items were verified: the Digital Pathology Association's PV26 program (OpenClaw, 18 Oct 2026) and the American Heart Association's Scientific Sessions Health Innovation Pavilion (Grok Bot used live, 7 Nov 2026). Nothing was found from ACR, RSNA, ACEP, ASA, AAD, APA, AAFP, ACP, SHM, AMIA or SIIM.

### Cited Findings
- Digital Pathology Association, Pathology Visions 2026: 20-minute session by Yosep Chong, MD, PhD, MIAC on OpenClaw for pathologists, with learning objectives on email/scheduling/task management, case preparation and report drafting, and safeguards for human oversight. [opened] — [PV26 session 262](https://digitalpathologyassociation.org/pv26-agenda/show/session/262)
- American Heart Association: "Opening Session: Designing and Deploying Real-World AI Agents", Scientific Sessions 2026, Center for Health Technology and Innovation's Health Innovation Pavilion, 7 Nov 2026; speaker Michał Nedoszytko, MD, PhD, Clinician Scientist, Abridge. [API] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- In that session he states that the interactive demo application and his private server were set up by Grok Bot, and he assigns a cardiology patient-education build to Grok Bot live. [transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- He also announces a physician hackathon held in July 2026 in San Francisco (about 200 people) and a repeat on 6 February with OpenAI. [transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- A society-name search for Grok Bot (R17) returned no society blog, podcast or webinar. [snippet-level negative] — [Result page cited for general Grok health coverage](https://www.eweek.com/news/bmj-open-ai-chatbots-health-misinformation-study/)
- A Rock Health / AAFP survey surfaced in the primary-care search (81% want more training to trust AI at work); it is not about any such assistant. [snippet] — [Rock Health](https://rockhealth.com/rock-weekly/ai-joins-the-primary-care-practice/)

### Inferences
- Cardiology (AHA) is the only specialty society found to have put the literal Grok Bot product on stage with a physician; pathology (DPA) is the only one found to have programmed OpenClaw for specialty workflow.

### Gaps
- Society sites, member-only forums, podcasts and grand-rounds listings were not crawled individually.
- No clinical-informatics community page (AMIA, SIIM) was opened directly.
- The AHA session was a build demonstration; whether its code or the Grok Bot configuration was shared with attendees is not stated.

## Key Question 4: Are there physician-run courses, newsletters or YouTube channels teaching colleagues to set up such an assistant, and does the teacher have their own named specialty assistant?

### Takeaway
Three physician-run teaching sources were verified: Doctors Who Code (Chukwuma Onyeije, MD, FACOG; Hermes Agent with MFM skills; a later agent he calls "Hark"), Techy Surgeon (Christian Pean, MD, MS; Clawdbot agent "Multivac", non-clinical) and the Grok-Bot Dr Skool community (self-described retired dermatologist; Grok Bot; no named assistant visible). Only the first has a teacher with a specialty-relevant assistant of his own.

### Cited Findings
- Doctors Who Code: written "from Maternal-Fetal Medicine practice" by Chukwuma Onyeije, MD, FACOG; the archive header reports 221 articles, including agent tutorials ("From Chatbot to Agent: The Mental Model Every Physician Needs", 3 Sep 2026; "Your First Agentic Workflow", 7 Sep 2026; "Design the Workflow Before You Build the Agent", 22 Sep 2026) and a public lab called AgenticBuilderMD (20 Sep 2026). [opened] — [Doctors Who Code archive](https://doctorswhocode.blog/blog/)
- His own assistant: Hermes Agent on a VPS with Telegram and 94 skills including MFM documentation (17 May 2026). [opened] — [Doctors Who Code](https://doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows)
- A later post names "my AI agent, Hark" (25 Oct 2026) without stating its framework. [opened] — [Doctors Who Code](https://doctorswhocode.blog/blog/the-most-important-thing-my-ai-agent-did-was-nothing)
- Techy Surgeon (Christian Pean, MD, MS): Clawdbot post (30 Jan 2026, agent "Multivac"), agent-assistants post covering Grok Bot and Hermes (23 Sep 2026), live session on his "AI OS" (26 Sep 2026); all agent use kept away from patient work. [opened] — [Clawdbot post](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a); [agent assistants post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes); [live session](https://techysurgeon.substack.com/p/substack-live-a-snippet-of-my-evolving)
- Grok-Bot Dr (Skool): "a physician-led community for xAI Grok Bot"; curriculum covers install, a named Bot with a real job, clinical-style prompts, three tested workflows, privacy; 60 members at fetch; no specific assistant named publicly. [opened] — [Skool: Grok-Bot Dr](https://www.skool.com/grok-bot-dr-5856)
- Passive Income MD, "What Is Grok Bot? xAI's AI Agent Explained for Physicians", 15 Oct 2026, no byline: business-admin framing, keep patient information out absent a written BAA, no bot built by the author. [opened] — [Passive Income MD](https://passiveincomemd.com/blog/tech/what-is-grok-bot-for-physicians/)
- No physician YouTube course on these frameworks for a specialty appeared in two YouTube searches; health-related Grok Bot videos found are consumer tutorials by non-physician channels. [API] — [SecondMed video](https://www.youtube.com/watch?v=d7I82Ji45II); ["Dr. Bot" video](https://www.youtube.com/watch?v=FmVYS_uTKp0)

### Inferences
- If the asker's "fellow physician" is someone who teaches other physicians, Onyeije (blog plus public lab) and Dr. Lautner (Grok Bot classroom) are the two most plausible people to check with the asker; only Dr. Lautner teaches the literal product.
- Physician educators consistently draw a line at patient data without a BAA, which helps explain the scarcity of public clinical specialty assistants on consumer agent products.

### Gaps
- Passive Income MD's article has no byline.
- YouTube search quota was limited (two searches).
- Private or paid course content (Skool classroom, paid Substack sections) was not accessible.

## Key Question 5: Which specialty appears to have the most activity, and which single candidate across all specialties best fits "medical specialty custom personal assistant built by a physician on this kind of framework"?

### Takeaway
OB/GYN (maternal-fetal medicine) has the deepest single body of work, cardiology and pathology have the only society-stage items, and longevity medicine has the only specialty-specific open-source build on Grok Bot. The best-fitting single candidate is Dr. Chukwuma Onyeije's VPS-hosted Hermes Agent with MFM skills, with the explicit caveat that it is not on Grok Bot or OpenMausBot; on the literal products no candidate satisfies all criteria.

### Cited Findings
- Onyeije: verified MFM physician; Hermes Agent "self-hosted, multi-model AI system running on a VPS", Telegram, 94 skills with a signout-to-APSO pipeline for inpatient MFM documentation; 17 May 2026; agent code not public. [opened] — [Emory profile](https://www.emoryhealthcare.org/providers/chukwuma-onyeije-778536); [Doctors Who Code](https://doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows)
- Nedoszytko: interventional cardiologist; Grok Bot used to build and host his AHA session demo and a cardiology patient-education app, 7 Nov 2026; no persistent named assistant or public template. [API + transcript] — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- Longevity Grok / PLSI: "a team of AI agents on Grok Bot", MIT, public 30 Oct 2026, physician "Clinic" tier; leads named in press are PhDs. [opened] — [longevitygrok.si](https://longevitygrok.si/); [BioPharma APAC](https://biopharmaapac.com/news/31/8649/insilico-medicine-launches-open-source-longevity-grok-with-harvard-researcher-david-sinclair.html)
- Chong: OpenClaw for pathology productivity and diagnostic-workflow support at PV26, 18 Oct 2026. [opened] — [PV26 session 262](https://digitalpathologyassociation.org/pv26-agenda/show/session/262)
- Pean: Clawdbot agent "Multivac" (30 Jan 2026) and Grok Bot/Hermes testing (23 Sep 2026), all non-clinical. [opened] — [Clawdbot post](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a); [agent assistants post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- Grok-Bot Dr: physician-run Grok Bot classroom by a self-described retired dermatologist. [opened] — [Skool: Grok-Bot Dr](https://www.skool.com/grok-bot-dr-5856)
- No OpenMausBot-based medical or physician project was found in the README, official team templates, Composio showcase, or about 50 name-matched GitHub repositories. [opened/API] — [OpenMausBot](https://github.com/milind-soni/OpenMausBot); [openmausbot-teams](https://github.com/milind-soni/openmausbot-teams)

### Inferences
- Ranking on the stated criteria (verifiable physician, specialty-specific, built on the framework), allowing comparable frameworks: (1) Onyeije — strong; (2) Chong — partial; (3) Nedoszytko — partial; (4) Pean — partial; (5) Longevity Grok — partial, not physician-built; (6) Grok-Bot Dr — partial/weak.
- Ranking if only Grok Bot/OpenMausBot count: (1) Nedoszytko — physician verified, Grok Bot verified, cardiology-themed but not a persistent assistant; (2) Longevity Grok — specialty and framework verified, builder not a physician; (3) Grok-Bot Dr — framework verified, credentials and specialty assistant unverified. None is a strong match.
- No candidate should be given to the asker as "the" match without confirmation; one clarifying detail from the asker (specialty, where seen, or month) would settle it, because the likely venue is a social post or closed physician community that this sweep could not reach.
- Suggested follow-ups: open Onyeije's architecture post and check his September–November 2026 posts for any move to Grok Bot or OpenMausBot; search X/LinkedIn for x.ai/bot share links by physicians; search GitHub file contents for OpenMausBot team files with specialty terms; check forks and contributors of Insilico-org/plsi for physician authors; look inside physician communities (Skool, Doximity, Sermo, Discord).

### Gaps
- The true target may postdate search indexing (Grok Bot launched 11 Aug 2026), so absence in web search is weak evidence of absence.
- Match-strength labels are my judgments from public posts, abstracts, captions and landing pages, not from inspecting any assistant's configuration.
