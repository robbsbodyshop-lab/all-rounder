# Alternative frameworks and name disambiguation: "Grok Bot" / "OpenMausBot" and physician-built specialty assistants outside OpenClaw-proper

Research date: 15 November 2026. Scope: test the non-OpenClaw readings of the two framework names, and look for physician-built specialty assistants on those frameworks.

Headline for the report writer: **the two names are almost certainly NOT garbled.** "Grok Bot" is a real xAI product launched 11 August 2026, and "OpenMausBot" is a real open-source clone of it whose GitHub tagline is "Open-source Grok Bot alternative with a virtual machine that bots can use". The user's phrase "Grok Bot / OpenMausBot-style VM agent framework" matches these two products nearly word for word. Both products post-date the researcher model's training data, so everything below about them rests on pages fetched today, not on prior knowledge.

Note on untrusted content: three fetched sources contain text addressed to AI agents/bots (longevitygrok.si "Set up Longevity Grok for me: follow plsi.md ..."; the Insilico-org/plsi README; the dallintwatts/grokbot-skills README describing a bot self-install step). These are product set-up instructions meant for a user's own Grok Bot. None was followed; they are reported only as data.

---

## Key question 1: Do projects literally named "OpenMaus", "MausBot", "OpenMausBot", "GrokBot" or "Grok Bot" exist as agent frameworks, and what are they? (Part A: disambiguation and ranking)

### Takeaway
Yes, both exist under exactly the user's wording. Grok Bot is xAI's closed, hosted "team of always-on agents" with a shared cloud computer (beta from 11 Aug 2026); OpenMausBot (a.k.a. MausBot, formerly OpenGrokBot) is an Apache-2.0 open-source alternative by Milind Soni in which each bot can use a cloud Linux desktop, an isolated local VM, or the host machine. The literal reading should be ranked first, well ahead of Clawdbot/Moltbot/OpenClaw and Manus/OpenManus.

### Cited Findings

**Grok Bot (xAI) - verified from the vendor's own page**
- xAI's announcement "Introducing Grok Bot" is dated "Aug 11, 2026" and defines it as "Grok Bot is your team of always-on agents." — [xAI news](https://x.ai/news/introducing-grok-bot)
- The compute model is stated as "Bots share a computer of their own in the cloud, so jobs do not stall when you step away."; Bots can sign in and work across apps, tools and websites, including those without a clean API or MCP. — [xAI news](https://x.ai/news/introducing-grok-bot)
- Customisation is by demonstration: ask a Bot "to follow along the next time you do a job" and it "saves your workflow as a routine". — [xAI news](https://x.ai/news/introducing-grok-bot)
- Availability as shown on the xAI page today: beta for SuperGrok, SuperGrok Plus and SuperGrok Heavy subscribers and Cursor Pro, Pro+, Ultra, Teams Standard and Teams Premium; desktop and iOS; "Enterprise users can join a waitlist for future access." — [xAI news](https://x.ai/news/introducing-grok-bot). Secondary sources describe a narrower launch-day set (SuperGrok Heavy, Cursor Ultra, eligible Cursor team plans), so the page may have been widened after launch — [Composio guide, 20 Aug 2026](https://composio.dev/blog/guide-to-frok-bot)
- A secondary guide says "All Bots on your account share the same cloud computer, files, browser sessions, and command-line credentials" and warns not to treat separate Bots as separate security boundaries; it also describes roles, memory, reusable skills, routines, plugins/MCP and a plugin marketplace. — [Composio guide, 20 Aug 2026](https://composio.dev/blog/guide-to-frok-bot)
- A comparison article (published 23 Oct 2026, updated 4 Nov 2026) calls Grok Bot "closed and Grok-only", not self-hostable, and describes its computer as "a Firecracker microVM running in Cursor's cloud" shared by all bots on an account. — [Bitdoze](https://www.bitdoze.com/best-open-source-grok-bot-alternatives/)
- Bots can be shared as templates: a community wiki says a public template is a share link starting with x.ai/bot/ that copies the bot's identity, instructions, skills and routines (never the creator's computer, logins or history), and that the Grok Bot Marketplace lives at x.ai/bot/marketplace. — [Grok Bot Wiki listing](https://www.grokbotwiki.com/bots/doctor); the Marketplace page itself shows categories "From Grok Bot Team, Engineering, Sales, Marketing, Design, Personal, Recruiting & People, Product, Operations" and no health/medical category — [x.ai/bot/marketplace](https://x.ai/bot/marketplace)
- Company naming is inconsistent across sources: a physician-site explainer says "an AI agent from xAI (also called SpaceXAI)" — [Passive Income MD, 15 Oct 2026](https://passiveincomemd.com/blog/tech/what-is-grok-bot-for-physicians/); the Marketplace footer carries a "SpaceX Super Intelligence LLC" copyright — [x.ai/bot/marketplace](https://x.ai/bot/marketplace). The xAI page's download buttons point to a cursor.sh domain — [xAI news](https://x.ai/news/introducing-grok-bot)

**OpenMausBot / MausBot / OpenGrokBot - verified from the repo**
- Repo `milind-soni/OpenMausBot`, description "Open-source Grok Bot alternative with a virtual machine that bots can use"; 23.3k stars, 3.2k forks, Apache-2.0 (with a separately licensed `enterprise/` folder) at fetch time on 15 Nov 2026. — [GitHub](https://github.com/milind-soni/OpenMausBot)
- README tagline: "The open-source Grok Bot alternative: your own team of AI bots, in a chat app."; naming line: "Also known as MausBot; formerly OpenGrokBot."; copyright "© 2026 Milind Soni". — [README](https://raw.githubusercontent.com/milind-soni/OpenMausBot/main/README.md)
- Compute: "Each bot can use a cloud Linux desktop, an isolated Local VM, or" the host machine ("This computer", opt-in); the cloud computer provider is named as Boat (boat.dev), a sponsor. — [README](https://raw.githubusercontent.com/milind-soni/OpenMausBot/main/README.md)
- Bots are "Claude or Codex running locally under the hood" (also a `grok` CLI option), i.e. it drives CLIs the user already has logged in; custom/OpenAI-compatible providers are configurable. — [GitHub](https://github.com/milind-soni/OpenMausBot)
- Disclaimer: "Not affiliated with xAI, Meta, OpenAI or Manus." — [README](https://raw.githubusercontent.com/milind-soni/OpenMausBot/main/README.md)
- The README positions it against five closed products: Grok Bot ("xAI's roster of bots on one shared cloud computer, Grok only, from a SuperGrok or Cursor plan"), Meta Muse ("Meta's single personal agent in a Meta cloud VM, US and Canada only"), OpenAI dots ("OpenAI's always-on agent inside ChatGPT"), Cue by Manus ("Manus's invite-only agents with their own phone, email and wallet") and Instinct AI by Spear Street; it says "Four closed personal-agent products shipped in seven weeks of 2026". — [README](https://raw.githubusercontent.com/milind-soni/OpenMausBot/main/README.md)
- Team templates: "Browse outcome-driven teams on BotMRR, then choose Add to OpenMausBot"; playbook repo `milind-soni/openmausbot-teams`. — [README](https://raw.githubusercontent.com/milind-soni/OpenMausBot/main/README.md)
- Timing: a 13 Aug 2026 article says "About a day later [after 11 Aug], a free clone called OpenMausBot showed up on GitHub" (803 stars at the time). — [Enterprise DNA](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-13-a-free-clone-of-a-200-paywalled-product-shipped-in-about-a-d). The author's own X post reads "I made an Open Source version of the Grok Bot complete with all the features ... It can spin up virtual machines ... uses @trycua for computer use". — [Milind S on X](https://x.com/milindlabs/status/2087289803964559746)
- It has a website and a phone companion app listed as "MausBot". — [mausbot.com](https://mausbot.com/); [Google Play](https://play.google.com/store/apps/details?id=com.openmausbot.companion&hl=en_US)
- Star counts in secondary sources vary by snapshot date (5.5k on 23 Oct 2026 per Bitdoze; 23.3k on 15 Nov 2026 per GitHub). — [Bitdoze](https://www.bitdoze.com/best-open-source-grok-bot-alternatives/); [GitHub](https://github.com/milind-soni/OpenMausBot)

**Other frameworks the names could have pointed to (short factual descriptions)**

| Candidate | What it is / who / where it runs | Source |
|---|---|---|
| Rakazo | Self-hosted Grok Bot-style bot roster by `elie222`; Apache-2.0, 5.3k stars (23 Oct 2026); bot computers in local Docker, a hosted sandbox, or the user's own machine | [Bitdoze](https://www.bitdoze.com/best-open-source-grok-bot-alternatives/) |
| OpenBot (CopilotKit) | "An open source Grok Bot that works with ANY agent harness"; MIT, 7k stars; one container with Chromium per coworker on your infrastructure | [Atai Barkai on X](https://x.com/ataiiam/status/2090125716767773120); [Bitdoze](https://www.bitdoze.com/best-open-source-grok-bot-alternatives/) |
| OpenHuman, Eigent, Paperclip, Lorca, Rerun | Other open-source "Grok Bot alternatives" (personal assistant, parallel-task desktop app, org-chart dashboard, encrypted single-user roster, AI coworkers each with a watchable computer) | [Bitdoze](https://www.bitdoze.com/best-open-source-grok-bot-alternatives/) |
| OpenClaw (ex-Clawdbot, ex-Moltbot) | MIT assistant that lives in existing chat apps (WhatsApp, Telegram); runs on the user's own machine or VPS; 392.8k-395k stars | [Bitdoze](https://www.bitdoze.com/best-open-source-grok-bot-alternatives/); [ClawClones](https://clawclones.com/) |
| Hermes Agent (Nous Research) | MIT single agent that writes its own skills and runs scheduled jobs; runs local, Docker, SSH, Daytona, Singularity or Modal; 256k-264k stars | [Bitdoze](https://www.bitdoze.com/best-open-source-grok-bot-alternatives/); [ClawClones](https://clawclones.com/) |
| NanoClaw | MIT messaging-only agent runner with each agent in its own container; 31k stars. Repo owner given as `nanocoai` by one source and `qwibitai` by another | [Bitdoze](https://www.bitdoze.com/best-open-source-grok-bot-alternatives/); [ClawClones](https://clawclones.com/) |
| nanobot / ZeroClaw / PicoClaw / IronClaw / Agent Zero / Moltis | OpenClaw-family alternatives: HKUDS/nanobot (Python, 50k), zeroclaw-labs/zeroclaw (Rust, 33k), sipeed/picoclaw (Go, 30k), nearai/ironclaw (Rust, 13k), agent0ai/agent-zero (Python, 20k), moltis-org/moltis (Rust, 3.0k); index dated 15 Nov 2026 | [ClawClones](https://clawclones.com/) |
| OpenManus | Open-source project "aimed at replicating the capabilities of the Manus AI agent"; containerised/sandbox run mode; public by 9 Mar 2025 | [henryalps/OpenManus](https://github.com/henryalps/OpenManus); [video summary](https://yt.chop.dev/en/v/W2Ur7FGqsJE) |
| Manus / "Cue by Manus" | Proprietary general agent; in 2026 offers "invite-only agents with their own phone, email and wallet" (as characterised by a competitor README) | [OpenMausBot README](https://raw.githubusercontent.com/milind-soni/OpenMausBot/main/README.md) |
| Moltbook | AI-agents-only social network built by Matt Schlicht on OpenClaw, launched late January 2026 (one source: 28 Jan 2026); not an agent framework | [DigitalOcean](https://www.digitalocean.com/resources/articles/what-is-moltbook); [Built In](https://builtin.com/articles/what-is-moltbook-openclaw) |

- No evidence was found of any product literally named "OpenMaus" on its own; every hit for that string resolves to OpenMausBot. — [SourceForge mirror](https://sourceforge.net/projects/openmausbot.mirror/); [AlternativeTo](https://alternativeto.net/software/openmausbot/about/)
- The older, unrelated sense of "Grok bot" (the Grok chatbot answering on X) also exists, e.g. 2024 coverage of "Dr. Grok" and uploading scans to Grok. — [Fox News](https://www.foxnews.com/health/elon-musk-wants-people-submit-medical-scans-grok-ai-chatbot)

### Inferences
Reasoned ranking of readings (inference, not verified fact):
1. **Literal: xAI Grok Bot and its open-source clone OpenMausBot (very likely, roughly 85-90%).** Both names match character for character; the unusual attribute "VM" matches OpenMausBot's own tagline ("with a virtual machine that bots can use") and Grok Bot's cloud computer; the pairing "Grok Bot / OpenMausBot" mirrors how every listing describes OpenMausBot ("open-source Grok Bot alternative"); and the timing fits (Aug-Nov 2026). A garbled dictation would be unlikely to reproduce two real, paired product names by accident.
2. **Category reading: any "Grok Bot-style" always-on agent with its own computer (Rakazo, OpenBot, Hermes Agent, OpenClaw, Meta Muse, OpenAI dots, Cue by Manus).** The user's word "-style" suggests the assistant might be built on a sibling framework and merely described by analogy. This keeps OpenClaw- and Hermes-based physician builds relevant even under the literal reading.
3. **Clawdbot / Moltbot / OpenClaw as a mis-hearing (low, perhaps 5-10%).** "Moltbot" and "MausBot" are phonetically close and "OpenClaw" shares the "Open-" prefix, but this reading requires two independent errors that happen to land on two real products.
4. **Manus / OpenManus as a mis-typing (low, under 5%).** "OpenMaus" is one letter from "OpenManus", but there is no "Bot" suffix in that family and OpenMausBot explicitly disclaims affiliation with Manus.
5. **A generic Grok-chatbot-on-X bot or Telegram/Discord "Grok bot" wrapper (very low).** Nothing in that family is a VM agent framework.

Practical consequence: the search target should be "a physician who shared a specialty bot/template built on Grok Bot (x.ai/bot/... share link or Marketplace template) or on OpenMausBot (team playbook / fork)", with Hermes/OpenClaw builds as fallbacks.

### Gaps
- OpenHands, Open Interpreter and Perplexity Computer/Comet were not individually verified this session (one search returned nothing for "Perplexity Computer"); they were deprioritised once the literal reading was confirmed. No description of them above is sourced, so none is given.
- The reason and date of the OpenGrokBot to OpenMausBot rename were not found; the README only says "formerly OpenGrokBot".
- "Meta Muse", "OpenAI dots", "Cue by Manus" and "Instinct AI (Spear Street)" are taken only from the OpenMausBot README (a competitor's characterisation, read through a summarising fetch tool); they were not confirmed against the vendors' own pages.
- The xAI changelog (x.ai/changelog/bot) returned HTTP 403, so dates for templates (reported as 28 Aug 2026), enterprise opening (reported as 3 Sep 2026) and a "1.0" release (reported as 11 Nov 2026) are from secondary snippets only and should be treated as unverified.
- Whether MetaGPT contributors built the original OpenManus could not be confirmed from the sources retrieved (one blog says so, the repo found credits a different lineage).
- No community Telegram/Discord "Grok bot" framework was researched in depth.

---

## Key question 2: What is the documented rename history of Clawdbot to Moltbot to OpenClaw, and is there evidence people mis-hear or mis-write those names like the user's wording?

### Takeaway
The project's own docs give Warelay, then Clawd/Clawdbot (25 Nov 2025 to 27 Jan 2026), then Moltbot (27 Jan 2026, after an Anthropic trademark email), then OpenClaw (30 Jan 2026, final). No evidence was found of anyone rendering these names as "Grok Bot" or "OpenMausBot"; those are separate real products.

### Cited Findings
- Original name was Warelay, "a sensible name for a WhatsApp gateway"; the mascot entry reads "Formerly known as Clawd (Nov 25, 2025 - Jan 27, 2026)". — [OpenClaw docs: lore](https://docs.openclaw.ai/start/lore)
- "In January 2026, Anthropic sent a polite email asking for a name change (trademark stuff)."; the docs place the email at 5am on 27 Jan 2026 and say Moltbot was chosen in a community vote. — [OpenClaw docs: lore](https://docs.openclaw.ai/start/lore)
- "On January 30, 2026, the lobster molted one more time into its final form: OpenClaw."; stated reason: "Moltbot never quite rolled off the tongue". — [OpenClaw docs: lore](https://docs.openclaw.ai/start/lore)
- Secondary accounts agree on the dates (Clawdbot Nov 2025; Moltbot 27 Jan 2026; OpenClaw 30 Jan 2026) and on Anthropic's "Clawd" trademark concern as the trigger. — [Business Today, 30 Jan 2026](https://www.businesstoday.in/technology/news/story/the-lobster-sheds-its-shell-for-the-third-time-as-clawdbot-becomes-openclaw-513650-2026-01-30); [DEV Community](https://dev.to/jordanolsen/openclaw-rebrand-clawdbot-to-moltbot-to-openclaw-explained-522m)
- Name confusion did cause impersonation: secondary reports say old "clawdbot"/"moltbot" handles were grabbed by crypto promoters and that downloads under old names may be malicious. — [Morph: Clawdbot](https://www.morphllm.com/clawdbot)
- OpenClaw was first published in November 2025 by Austrian developer Peter Steinberger (per search summary of Wikipedia). — [Wikipedia: OpenClaw](https://en.wikipedia.org/wiki/OpenClaw)
- OpenMausBot also warns about name-squatting tokens: "Any coin using the OpenMausBot, Maus, or SupaMaus name is not created, endorsed, or affiliated". — [OpenMausBot README](https://raw.githubusercontent.com/milind-soni/OpenMausBot/main/README.md)

### Inferences
- The triple rename is a genuine source of confusion in this product family, which made the "garbled name" hypothesis reasonable; but the existence of products named exactly "Grok Bot" and "OpenMausBot" makes it unnecessary.
- Because OpenClaw is routinely described as "the open-source agent Grok Bot is most often compared to" (see PhiClaw under question 5), a physician describing an OpenClaw-based build could plausibly call it "Grok Bot-style"; the OpenClaw researchers' candidates remain relevant as fallbacks.

### Gaps
- Sources disagree on whether the Moltbot-to-OpenClaw rename was voluntary; the project docs frame it as a naming preference, not a second legal demand.
- No source documenting dictation or spelling errors specifically turning "Moltbot" into "MausBot" (or vice versa) was found.

---

## Key question 3: Is there a Grok-powered (xAI) personal-agent or bot framework that physicians have built specialty assistants on? Has any physician publicly described a Grok-based specialty assistant? (Part B, Grok Bot and OpenMausBot)

### Takeaway
Grok Bot is exactly such a framework and shared bots/templates exist by the thousand, but no verifiable physician-built, specialty-specific Grok Bot or OpenMausBot assistant was found. The nearest items are Insilico's open-source "Longevity Grok" (a physician-facing longevity team on Grok Bot, built by a PhD-led company team), an unverified "Doctor-built" health-coach bot, and a medical-imaging research skill pack of unknown authorship.

### Cited Findings

**Candidates (Grok Bot)**

1. **Longevity Grok / PLSI (Personal Longevity Superintelligence)** - match strength: PARTIAL
   - URL: [longevitygrok.si](https://longevitygrok.si/); code [Insilico-org/plsi](https://github.com/Insilico-org/plsi) (MIT; 85 stars, 26 forks at fetch).
   - Framework use: installs on the user's own Grok Bot account; a "Chief Orchestrator" (PLSI) coordinates 29 other bots (8 Core, 13 Specialists, 4 Clinic, 4 Lab); skills, agent definitions and routines sync from the public GitHub repo. — [longevitygrok.si](https://longevitygrok.si/)
   - Physician-facing part: a Clinic team (Patient Coordinator, Visit Assistant, Evidence Analyst, Clinic Liaison) for "Patient list, visit briefs, clinical evidence and patient messages you approve"; physician tools "rolling out by invitation". — [longevitygrok.si](https://longevitygrok.si/)
   - Builders: Insilico Medicine with Harvard's David A. Sinclair, Ph.D.; Alex Zhavoronkov, Ph.D. (founder/CEO); press release dated 6 Nov 2026 contains no physician quotes and lists no MD. — [Insilico press release](https://insilico.com/news/pr9a97f0dc951d9596ade1-insilico-open-sources-24-7-personal-longevity-superintelligence-to-turn-quantified-self-data-into-pr)
   - The site also names Fedor Galkin ("Science and implementation lead") and, for the Longevity Education Hub ("Longevity medicine courses for physicians"), Dominika Wilczok and Evelyne "Eva" Bischof. — [longevitygrok.si](https://longevitygrok.si/)
   - Evelyne Bischof is described elsewhere as MD, PhD, MPH, Swiss board-certified internist (FMH), FEFIM, and medical director of the Sheba Longevity Center; her role in building the software is not stated. — [Longevity Investors profile](https://www.longevityinvestors.ch/davos-2026-speakers/evelyne-yehudit-bischof%2C-md%2C-phd%2C-mph); [GESDA profile](https://radar.gesda.global/people/evelyne-bischof)
   - Dates: code public 30 Oct 2026; v0.2.0 on 5 Nov 2026; announced 6 Nov 2026; page updated 7 Nov 2026. — [longevitygrok.si](https://longevitygrok.si/)
   - Disclaimer: it "does not provide medical care, does not diagnose, treat or prescribe". — [longevitygrok.si](https://longevitygrok.si/)
   - A Substack post about the launch titles it "Launched: Longevity GrokBot by Insilico" (author Dominika Wilczok, 6 Nov 2026). — [Regeneration.AI](https://www.regeneration.ai/p/launched-longevity-grokbot-by-insilico)
   - Why partial: literally built on Grok Bot, domain-specific (longevity medicine), public MIT template, has a physician Clinic team and a physician associated with the programme. Misses: built by a company/PhD-led team rather than "a fellow physician"; no evidence a physician authored it; it is a patient/consumer-first product.

2. **Pulse ("Doctor-built health coach")** - match strength: WEAK
   - Shared Grok Bot by "Wilson" (@qpzm620); description: "Doctor-built health coach that learns your diet, exercise, and sleep from chat, meal photos, and sleep screenshots"; first seen 6 Oct 2026; share link x.ai/bot/DdNlDzU_cYi-JJv2YR2CS. — [GrokBot.Rocks builder page](https://builder.grokbot.rocks/bot/DdNlDzU_cYi-JJv2YR2CS/)
   - Why weak: the "Doctor-built" claim is the creator's own, with no name, credentials or specialty; it is a consumer wellness coach, not tied to a specialty or the builder's clinical work.

3. **loopnownow/MY-SKILLS ("Medical/imaging research skills for Grok")** - match strength: WEAK
   - Public MIT repo describing "six Grok Bot seats" for medical/imaging research (intent routing/QC, data-to-analysis incl. imaging prep and statistics, study design/literature/ethics forms, scientific writing, peer review, reviewer responses); "Maintained by Aitor for loopnownow"; 712 commits, 0 stars; internal notes dated 27 Oct and 1 Nov 2026. — [GitHub](https://github.com/loopnownow/MY-SKILLS)
   - Why weak: specialty-flavoured (medical imaging research) and built for Grok Bot with public code, but the maintainer's identity and any medical credentials are not stated; it is a research-writing workflow, not a clinical personal assistant.

**Near-misses (Grok Bot / OpenMausBot)**
- "Doctor" template by Vincenzo Palazzo (first listed 28 Sep 2026): "A personal health follow-up assistant: tracks dental work, allergy tests, medicines and supplements"; patient-side, no credentials listed. — [Grok Bot Wiki](https://www.grokbotwiki.com/bots/doctor)
- SecondMed, a Grok Bot "AI health assistant" for understanding results, checking bills and preparing for appointments; YouTube, 11 Sep 2026, channel Beginners in AI; patient-side, not a physician. — [YouTube](https://www.youtube.com/watch?v=d7I82Ji45II)
- Clinical Orchestrator by Santi (@spastorr), first seen 29 Sep 2026: "A personal clinical orchestrator: warm 1:1 check-ins, 1-2 lenses per update (CBT, psychodynamic, systemic, affective tone)"; no credentials; a self-reflection bot. — [GrokBot.Rocks builder page](https://builder.grokbot.rocks/bot/pipXVVxoIV8Efwk_lvUyD/)
- Menopause Coach, Vaccine and Checkup Tracker and Test Date Coach (MCAT etc.) by @drbellahqw; consumer templates; the "dr" in the handle is unverified. — [grokbotusecases.com](https://grokbotusecases.com/)
- Medical Bill Auditor (@BrianRoemmele), Health Insurance Claims (@amartins02), Cost-Smart Health Brief (Amina Guleid; "helps doctors, patients, and families turn a health question into a short brief"), Health Assistant (Arlo Health): billing/consumer tools, no physician builder identified. — [grokbotusecases.com](https://grokbotusecases.com/); [ReadMultiplex directory](https://readmultiplex.com/grokbot-rocks/)
- "What Is Grok Bot? xAI's AI Agent Explained for Physicians" (15 Oct 2026): an unsigned explainer on a physician-finance site; gives no example of a physician-built specialty bot and advises keeping patient information out absent a BAA. — [Passive Income MD](https://passiveincomemd.com/blog/tech/what-is-grok-bot-for-physicians/)
- Vendor/SEO guides: "Grok Bot for Medical Practices" (uxcontinuum) and "Is Grok Bot HIPAA Compliant?" (PhiClaw); marketing, not physician builds. PhiClaw states "As of October 2026, xAI has published no BAA for Grok Bot." — [uxcontinuum](https://uxcontinuum.com/grok-bot-for-doctors); [PhiClaw](https://phiclaw.ai/hipaa-grok-bot-alternative/)
- dallintwatts/grokbot-skills ("Second Opinion Council" and "Fleet Doctor" Grok Bot templates): purpose not stated on the page; owner has no bio; cannot be classed as medical. — [GitHub](https://github.com/dallintwatts/grokbot-skills)
- OpenMausBot official team playbooks: six teams (SEO Growth, Engineering, 100x Marketing, Reddit Lead Miner, Competitor Watch, Inbox Follow-up); none medical. — [openmausbot-teams](https://github.com/milind-soni/openmausbot-teams)
- Fork `dr-biko/MausBot`: an unmodified-looking fork (0 stars, README unchanged); the owner profile shows no name, bio or medical credentials and unrelated repos (personal finance app, iPhone farm). The "dr" handle is not evidence of a physician. — [GitHub fork](https://github.com/dr-biko/MausBot); [profile](https://github.com/dr-biko)
- Community directories list very large numbers of shared bots (4,754 templates on one wiki; 902 on another as of 15 Nov 2026; "10,266+" on a third) and none surfaced a clinician-specialty bot in the portions read. — [Grok Bot Wiki](https://www.grokbotwiki.com/bots); [grokbotusecases.com](https://grokbotusecases.com/); [ReadMultiplex directory](https://readmultiplex.com/grokbot-rocks/)

### Inferences
- If the user's target exists on Grok Bot, it is most likely a shared bot (x.ai/bot/... link) or a small GitHub skills repo posted on X by a physician; such posts are poorly indexed by web search, which probably explains the null result more than true absence.
- The lack of a published BAA for Grok Bot (per vendor and physician-site sources) makes it likely that any physician build is framed as non-PHI: literature, education, admin, documentation templates.
- Longevity Grok is the only substantial, open, medicine-specific Grok Bot build found; if the user half-remembered "a medical speciality assistant on Grok Bot with a physician involved", this is the best literal-framework fit, but it does not satisfy "built by a fellow physician" on the evidence available.

### Gaps
- X (Twitter) posts could not be searched directly; only a handful of indexed posts appeared. A physician's thread sharing a Grok Bot link would likely be missed.
- The official Marketplace has no health category and cannot be keyword-searched via fetch; the Grok Bot Wiki "health" tag (83 bots) and roughly 160k characters of the ReadMultiplex directory (including its Research section) were not enumerated.
- No authenticated GitHub code/topic search was run (forks of OpenMausBot number about 3.2k; only one was inspected).
- The identity and credentials of "Wilson" (Pulse), "Aitor" (MY-SKILLS), @drbellahqw and Amina Guleid are unknown.
- Who at Insilico actually authored PLSI, and whether Dr Bischof or another physician designed the Clinic team, is not stated in the repo (contributors section empty in the fetch).

---

## Key question 4: Has any physician built a specialty assistant on Manus or OpenManus, or on Hermes Agent, Agent Zero, Open Interpreter, OpenHands, NanoClaw, nanobot or similar? (Part B, other frameworks)

### Takeaway
One credible, well-documented case exists on Hermes Agent: maternal-fetal medicine specialist Dr Chukwuma Onyeije runs a self-hosted, always-on Hermes "AI Operations Partner" on a VPS with 94 skills including MFM documentation workflows (posts dated 17 May 2026; no public code). Nothing credible was found for Manus/OpenManus, Agent Zero, Open Interpreter, OpenHands, NanoClaw or nanobot.

### Cited Findings

**Candidate (Hermes Agent)**

4. **Dr Chukwuma Onyeije's Hermes "24/7 AI Operations Partner"** - match strength: PARTIAL (strongest verified physician candidate in this scope)
   - URLs: [Part 1, "I Gave an AI Agent 94 Skills and Let It Help Run My Clinical, Coding, and Theology Workflows"](https://www.doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows); [Part 2, "The Architecture Behind My 24/7 AI Operations Partner"](https://www.doctorswhocode.blog/blog/hermes-agent-production-architecture-healthcare-ai). Both dated 17 May 2026.
   - Physician: "Dr. Chukwuma Onyeije, MD, FACOG", Maternal-Fetal Medicine specialist, "Medical Director at Atlanta Perinatal Associates", founder of CodeCraftMD and OpenMFM.org (self-described on his own blog; licensure not independently checked). — [Part 1](https://www.doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows); [Part 2](https://www.doctorswhocode.blog/blog/hermes-agent-production-architecture-healthcare-ai)
   - Framework and hosting: Hermes Agent, "a self-hosted, multi-model AI system running on a VPS" with a Telegram bot front end; "The system runs on a Hostinger VPS using Docker and Traefik"; primary model `moonshotai/kimi-k2` via OpenRouter with Claude Sonnet 4 failover; about $89/month VPS and about $127/month tokens. — [Part 2](https://www.doctorswhocode.blog/blog/hermes-agent-production-architecture-healthcare-ai)
   - What it does: 94 skills spanning "clinical, technical, theological, productivity, research, DevOps, GitHub, and creative workflows"; named clinical skills include a "Signout-to-APSO pipeline for inpatient MFM documentation" and "Voice memo to action plan for clinical and operational next steps"; a voice memo can become a sign-out, patient-friendly explanation, referral note, outpatient workup plan and draft message to the referring provider. "The physician remains responsible for accuracy, judgment, counseling, and final recommendations." — [Part 1](https://www.doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows)
   - PHI stance: "My Hermes deployment is not a hospital-grade enterprise system."; four data lanes; "do not casually route patient data into tools that were not designed, contracted, configured, and governed for that purpose." He lists specialty-specific MFM skills as a next step: "An MFM physician should help design MFM skills." — [Part 2](https://www.doctorswhocode.blog/blog/hermes-agent-production-architecture-healthcare-ai)
   - Public code/template: none linked in either post. — [Part 1](https://www.doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows)
   - Later context (3 Sep 2026): "In 2026, I experimented with OpenClaw, then Hermes, as persistent agents that could meet me through a messaging interface."; that post compares Claude Code, Codex, Google Antigravity, OpenClaw, Hermes and Omarchy and does not mention Grok Bot, OpenMausBot or Manus. — ["The Harness Is the Workplace"](https://www.doctorswhocode.blog/blog/the-harness-is-the-workplace/)
   - Why partial: verified-looking physician, a named specialty, an always-on personal agent on a rented server, tied to his own clinical work. Misses: framework is Hermes Agent, not Grok Bot/OpenMausBot (his posts pre-date Grok Bot's 11 Aug 2026 launch); no public template; MFM-specific skills are only partly built.

**Near-misses (Hermes, Manus/OpenManus, others)**
- `samahn0601/hermes-doctor`: "Read-only health-check CLI for long-running Hermes Agent installations"; README says "It started as a family physician's tool for treating a different kind of patient: my personal AI agent." Evidence that a family physician runs a personal Hermes agent, but the tool is agent hygiene, not a medical assistant; author unnamed; 0 stars; MIT. — [GitHub](https://github.com/samahn0601/hermes-doctor)
- Hermify "AI Agent for Doctors: A Practical Guide for 2026": vendor guide positioning Hermes as a personal-admin layer; not a physician build. — [Hermify](https://www.hermify.io/blog/ai-agent-for-doctors)
- DEV Community Hermes Agent Challenge entries (a Telegram medication-safety companion; "CareSync" by an engineering student): health-themed, builders not physicians. — [DEV: medication safety companion](https://dev.to/rpreetha/i-built-a-medication-safety-companion-for-home-care-with-hermes-agent-jki); [DEV: CareSync](https://dev.to/naomi_pereira_28531c3d5de/caresync-a-local-health-memory-agent-for-family-caregivers-337c)
- OpenManus in research: a February 2026 npj Digital Medicine benchmark evaluated OpenManus "extended with medically customized agents" alongside proprietary Manus; agent systems gave only modest accuracy gains (60.3% and 28.0% on AgentClinic MedQA and MIMIC) with more than 10x token use and more than 2x latency. A research benchmark, not a personal assistant. — [TU Dresden research portal](https://fis.tu-dresden.de/portal/en/publications/benchmarking-large-language-modelbased-agent-systems-for-clinical-decision-tasks(4a6869bd-684b-4865-95a9-76d6e4216d35).html)
- `openmanusv2` on PyPI (Mohamed Elsaeidy): a general daily-use OpenManus fork, not medical, author not identified as a physician. — [PyPI](https://pypi.org/project/openmanusv2/)
- NanoClaw in a clinical-research context: an arXiv paper ("Vibe Medicine") discusses agent frameworks for biomedical research and, per the search summary, calls NanoClaw's container isolation a promising starting point; not a physician's assistant. — [arXiv 2604.23674](https://arxiv.org/pdf/2604.23674)
- No physician-built specialty assistant was found on Manus/Cue by Manus, Agent Zero, Open Interpreter, OpenHands, nanobot, ZeroClaw, PicoClaw, IronClaw, Rakazo, OpenBot or BotMRR in the searches run (results returned only generic comparisons or unrelated vendor products). — [search-result example: OpenClaw alternatives comparison](https://aimultiple.com/openclaw-alternatives)

### Inferences
- Dr Onyeije's build is "Grok Bot-style" in function (persistent, messaging-fronted, skills, always on, hosted on a server) even though it uses Hermes; if the user's "-style" was loose, or if he has since ported to Grok Bot/OpenMausBot, he is a plausible identity for the "fellow physician". There is no evidence of such a port as of his 3 Sep 2026 post.
- The hermes-doctor README suggests at least one more physician (family medicine) running a personal Hermes agent, but nothing ties it to specialty work.
- Physician builders in this space appear to cluster on OpenClaw and Hermes (self-hosted, model-agnostic, controllable data flow) rather than on Manus-type hosted VMs, consistent with PHI concerns.

### Gaps
- Agent Zero, Open Interpreter, OpenHands, nanobot, ZeroClaw, PicoClaw and IronClaw were covered only by combined queries; a dedicated per-framework search might surface small physician projects.
- No GitHub fork/topic search of OpenManus or hermes-agent with medical keywords was run with an authenticated tool.
- Dr Onyeije's credentials were taken from his own site; a state medical board or practice-site check was not done. His skills are not public, so the "94 skills" claim is self-reported.
- Whether the npj Digital Medicine benchmark's authors include physicians was not checked.

---

## Key question 5: Are there physician-led open-source "clinical agent" or "doctor's personal agent" projects described as "like OpenClaw/Manus for doctors", and who is behind them?

### Takeaway
Nothing was found that is both physician-led and open-source and pitched as "OpenClaw/Manus/Grok Bot for doctors". What exists is vendor products (PhiClaw, a paid "HIPAA build of OpenClaw"), an open-source company project with a physician-facing module (Longevity Grok), and individual physician-technologists publishing their own set-ups (Dr Onyeije).

### Cited Findings
- PhiClaw describes itself as "the HIPAA build of OpenClaw" and "the HIPAA-compliant version of what Grok Bot does"; managed service at $3,500/month plus $997 set-up with a BAA; its banner says "Dr. Alexander Rios joins as Chief Medical Officer" (credentials not given); no founder named; code not stated to be open. Vendor product, near-miss. — [PhiClaw](https://phiclaw.ai/hipaa-grok-bot-alternative/)
- Longevity Grok is open source (MIT) and includes physician tooling, but is company-built (see question 3). — [longevitygrok.si](https://longevitygrok.si/)
- Dr Onyeije also runs OpenMFM.org, which hosts a "Clinician AI Guide" deck on ambient scribes; it was not verified to be an agent framework. — [OpenMFM deck](https://openmfm.org/decks/ambient-scribe/index.html)
- Projects with "doctor" in the name that are not clinical: `AlekseiUL/openclaw-agent-doctor` (self-diagnostic toolkit for OpenClaw agents) and `OpenLAIR/dr-claw` ("A Super AI Lab with massive AI Doctors as Assistants", a research IDE). — [openclaw-agent-doctor](https://github.com/AlekseiUL/openclaw-agent-doctor); [dr-claw](https://github.com/OpenLAIR/dr-claw)
- A vendor blog titled "openclaw-for-doctors" exists (not read; OpenClaw-proper is covered by other researchers). — [Ampere](https://www.ampere.sh/blog/openclaw-for-doctors.md)
- Lead for other researchers: an American Heart Association session video (published 13 Nov 2026) features "Dr. Michał Nedoszytko, whose Postvisit.ai earned top honors at Anthropic's 2026 hackathon" building an AI agent live; framework and specialty were not verified here. — [YouTube](https://www.youtube.com/watch?v=t46Bdrf1t9k)
- A Dallas pediatrician, Joseph Schneider, MD, is profiled for training his own AI assistants, but on ChatGPT (custom assistants), not an agent framework. — [Texas Medicine](https://www.texmed.org/TexasMedicineDetail.aspx?id=67952)

### Inferences
- The phrase "like OpenClaw/Manus for doctors" is currently used mainly by vendors; genuine physician-built work shows up as personal blog posts and small repos rather than branded open-source projects.
- If Part B must name one best alternative-framework candidate, it is Dr Chukwuma Onyeije (MFM, Hermes Agent); if it must be literally on Grok Bot, it is Longevity Grok (company-built). Neither is a full match, and this should be said plainly: **no credible strong match was found on Grok Bot, OpenMausBot, Manus or OpenManus.**

### Gaps
- MediAgent (Axiom Core; reportedly MIT, MedGemma-based clinical decision support) appeared only in a search summary and was not opened; its builders' credentials and framework are unverified, so it is not listed as a finding.
- PhiClaw's founder identity and Dr Alexander Rios's credentials were not verified.
- LinkedIn, Reddit, Doximity and physician Slack/Discord communities were not searchable in this session; a physician sharing a Grok Bot or OpenMausBot build there would not have been found.
