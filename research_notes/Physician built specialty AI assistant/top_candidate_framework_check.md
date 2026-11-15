# Top-candidate framework check: which agent framework three physicians' personal assistants run on (as of 15 Nov 2026)

Method note (applies to all three sections): pages were fetched and their text read or full-text searched on 15 Nov 2026. "Opened" means the page text itself was retrieved; "snippet only" means seen only in a search result and is unverified. No fetched page contained instructions aimed at an automated reader. None of the three physicians was found to have a personal assistant built on Grok Bot or OpenMausBot.

## Key question 1: Dr Chukwuma Onyeije (MFM) — what does "Hark" run on, any Grok Bot / OpenMausBot mention, anything published?

### Takeaway
His only documented framework is Hermes Agent (self-hosted on a VPS, 17 May 2026); the 25 Oct 2026 post that names the agent "Hark" does not state any framework, model or harness. Across all 49 posts he published from 1 Aug to 14 Nov 2026, the words Grok, Grok Bot, OpenMausBot, MausBot, OpenGrokBot and x.ai appear zero times, and no skills, template, repo or share link for his assistant is published.

### Cited Findings

Scope actually checked
- The blog's RSS feed lists 49 posts dated 1 Aug 2026 to 14 Nov 2026 (the same 49 appear on the archive page). All 49, plus the two 17 May 2026 Hermes posts, were downloaded and full-text searched (case-insensitive) for: grok, grok bot, grokbot, openmausbot, mausbot, opengrokbot, x.ai, hark, hermes, openclaw, github.com/. Result: zero hits for every Grok/Maus/x.ai term in all 51 pages — [RSS feed](https://www.doctorswhocode.blog/rss.xml); [archive](https://www.doctorswhocode.blog/blog/)
- "Hark" appears in exactly one post (25 Oct 2026). "Hermes"/"OpenClaw" appear in the body text of only the 17 May posts and the 3 Sep 2026 posts; other hits (7 Sep, 19 Sep, 20 Sep) are just the related-article teaser for the 3 Sep post — [archive](https://www.doctorswhocode.blog/blog/)

The "Hark" post (25 Oct 2026)
- Decisive sentence: "This week my AI agent, Hark, did something I could have done myself in five minutes. Its morning brief flagged that HostGator couldn't charge my card for onyeije.net and asked whether it should renew the hosting for about $185." — [The Most Important Thing My AI Agent Did Was Nothing, 25 Oct 2026](https://www.doctorswhocode.blog/blog/the-most-important-thing-my-ai-agent-did-was-nothing/)
- The post body names no framework, harness, model or vendor. A search of the full page for hermes, openclaw, claude, codex, gpt, framework, harness, skill, telegram and github found nothing in the article text. The framework Hark runs on is NOT stated — [same post](https://www.doctorswhocode.blog/blog/the-most-important-thing-my-ai-agent-did-was-nothing/)
- What Hark does in that post is administrative, not clinical: a morning brief, a dashboard item, signing in to an old hosting account, checking renewal/payment/domain pages, and reporting evidence. He calls it "a small, safe, non-clinical example" and says "Spending money requires my approval every time." — [same post](https://www.doctorswhocode.blog/blog/the-most-important-thing-my-ai-agent-did-was-nothing/)

Framework statements elsewhere
- 17 May 2026: "Three weeks into running Hermes Agent in production, I can say this: the real value is not the model. It is the workflow ecosystem wrapped around it." and "The bot is the front end for Hermes Agent — a self-hosted, multi-model AI system running on a VPS." — [I Gave an AI Agent 94 Skills…, 17 May 2026](https://www.doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows/)
- 17 May 2026 (companion post): "Running Hermes Agent in production taught me that 24/7 AI operations are not about replacing physician judgment." — [The Architecture Behind My 24/7 AI Operations Partner, 17 May 2026](https://www.doctorswhocode.blog/blog/hermes-agent-production-architecture-healthcare-ai/)
- 3 Sep 2026: "In 2026, I experimented with OpenClaw, then Hermes, as persistent agents that could meet me through a messaging interface." and "Hermes extended the pattern for me. It combines a personal agent runtime with reusable skills, memory, tool access, and messaging." — [The Harness Is the Workplace, 3 Sep 2026](https://www.doctorswhocode.blog/blog/the-harness-is-the-workplace/)
- The 3 Sep post's harness list is "Claude Code, Codex, Antigravity, OpenClaw, Hermes, and Omarchy"; Grok Bot is not in it even though the post is dated three weeks after Grok Bot's 11 Aug announcement — [The Harness Is the Workplace, 3 Sep 2026](https://www.doctorswhocode.blog/blog/the-harness-is-the-workplace/)

Specialty-specific (MFM) work — documented only for the May Hermes build
- "The current build has 94 specialized skills distributed across clinical, technical, theological, productivity, research, DevOps, GitHub, and creative workflows." — [17 May 2026](https://www.doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows/)
- "A skill knows that my MFM letters need to be concise, clinically structured, and readable by a busy referring physician who has thirty seconds to understand the plan." A listed skill is a "Signout-to-APSO pipeline for inpatient MFM documentation". — [17 May 2026](https://www.doctorswhocode.blog/blog/ai-operations-partner-hermes-agent-physician-workflows/)
- Clinical data is fenced: "Lane 2: De-identified clinical scenarios. Useful for drafting templates, generic counseling language, and workflow planning." Deeper integration is listed as future work: "specialty-specific documentation structures that reflect how MFM actually works." — [17 May 2026 architecture post](https://www.doctorswhocode.blog/blog/hermes-agent-production-architecture-healthcare-ai/)

Other agents he has built (separate from Hark)
- 19 Sep 2026: "DWC-Bot is a voice AI assistant designed around Doctors Who Code." It is a public phone line (calls recorded and transcribed) for reader guidance and his own idea capture; the page says "This line does not provide medical advice". No framework or voice vendor is named (searched for Hermes, OpenClaw, Grok, Vapi, Twilio, ElevenLabs, Retell). — [I Gave Doctors Who Code a Phone Number, 19 Sep 2026](https://www.doctorswhocode.blog/blog/i-gave-doctors-who-code-a-phone-number/)
- 20 Sep 2026: "AgenticBuilderMD will document how I construct agentic systems. I intend to show working experiments, failed approaches, architecture decisions, and code where it helps explain the work." This is a stated intention, not a published repo. — [I Built an AI Agent. Now I Am Building the Laboratory Around It., 20 Sep 2026](https://www.doctorswhocode.blog/blog/building-the-agenticbuildermd-laboratory/)

Public code / skills / templates / share links
- The only github.com links in the 51 pages are third-party: github.com/hermes-agent-org/hermes (labelled "Hermes Agent repository") and github.com/deepseek-ai/deepseek-harness docs. There is no link to a personal GitHub profile, a skills repo, a template or an x.ai/bot link — [The Harness Is the Workplace, 3 Sep 2026](https://www.doctorswhocode.blog/blog/the-harness-is-the-workplace/); [RSS feed](https://www.doctorswhocode.blog/rss.xml)
- The blog home page shows no GitHub profile or repository link — [home page](https://www.doctorswhocode.blog)
- Source discrepancy: Onyeije links Hermes Agent to github.com/hermes-agent-org/hermes, while Dr Pean's post links it to github.com/nousresearch/hermes-agent. Neither repo was opened — [Onyeije 3 Sep 2026](https://www.doctorswhocode.blog/blog/the-harness-is-the-workplace/); [Pean 23 Sep 2026](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)

### Inferences
- Hark is probably the Hermes-based "AI Operations Partner" from May under a new name (same always-on, brief-and-errand pattern; Hermes is the last framework he named, on 3 Sep). This is an inference only: no post links the name Hark to Hermes, and the 3 Sep post describes Hermes in the past tense ("experimented").
- He is not a Grok Bot or OpenMausBot match on the public record: no mention in any post since Grok Bot launched.
- His MFM skills exist but are private; there is nothing a reader could install or copy.

### Gaps
- What Hark runs on today: not stated in any opened post.
- agenticbuildermd.com (his separate build-log site) was not opened; it may name the stack or hold code.
- Posts before 1 Aug 2026 other than the two 17 May posts were not searched (for example the 28 Jul 2026 GitHub Gists post), so a personal GitHub/Gist handle may be given there.
- His X/LinkedIn/newsletter posts and the newsletter "starter bundle" were not checked.

## Key question 2: Dr Christian Pean (orthopedic trauma) — where he describes "Multivac", his verdict on Grok Bot, what he runs now, any orthopedics-specific use

### Takeaway
Multivac was his name for a Clawdbot (later OpenClaw) instance described on his Techy Surgeon Substack on 30 Jan 2026; by 23 Sep 2026 he wrote "OpenClaw died on the vine for me", had tried Instinct, Muse, Grok Bot and Hermes Agent, and named Instinct his early favorite. He found Grok Bot powerful but "clunky", keeps all of these agents away from patients, and nothing he describes is orthopedics-specific, so he is not a match.

### Cited Findings

Multivac on Clawdbot (30 Jan 2026, free post, opened in full)
- "I named mine Multivac, after Isaac Asimov's fictional supercomputer that solves humanity's greatest challenges." — [ClawdBot First Impressions from a Clinician-Founder, 30 Jan 2026](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a)
- Setup: "I launched clawdbot in telegram." and "I ran Clawdbot on the Claude Opus 4.5 API for maximum capability. My first full day of heavy usage cost $12." — [same post](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a)
- The "Nothing clinical" quote in full: "Nothing clinical. My Duke research work through Clawdbot is strictly limited to publicly available information and personal productivity. Zero patient data. Zero clinical systems. Zero exceptions." — [same post](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a)
- Verdict then: "After a week of testing, here's my honest assessment: the technology is genuinely impressive. And it should stay nowhere near clinical medicine." The post's subtitle is "The Agentic AI That Actually Works (and Why Clinicians Should Stay Far Away)". — [same post](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a)
- What Multivac did was startup and productivity work, not orthopedics: "For RevelAi Health (my startup): Research clinically integrated networks and ACOs that might be strong partners for our AI care orchestration platform… Draft personalized outreach emails. Create visual go-to-market strategy materials." Also "Folder of CMS relevant documents and RFAs? Searched, saved, filed." — [same post](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a)
- He flagged an early exit: "Low threshold to discontinue the experiment: Where I can, I am apt to use Claude Cowork and identify additional means of achieving what Clawdbot does without the security risks." — [same post](https://techysurgeon.substack.com/p/clawdbot-first-impressions-from-a)
- 21 Feb 2026 Substack note, full text: "'Paging Dr. OpenClaw' Dropping soon on Techy Surgeon". — [Substack note, 21 Feb 2026](https://substack.com/@techysurgeon/note/c-217864463)

Grok Bot, Hermes and the current state (23 Sep 2026, paid-only post; the publicly served text, about 17,000 characters ending at the subscribe prompt, was opened)
- "Over the past few weeks I have used four of the new AI agent assistants: Instinct, Meta's Muse, SpaceXAI's Grok Bot and Nous Research's open-source Hermes Agent… Instinct is my early favorite, but using all four has convinced me that everyday knowledge work is about to split in two." — [Instinct, Muse, Grok Bot and Hermes: A Techy Surgeon's First Weeks With Agent Assistants, 23 Sep 2026](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- On OpenClaw: "I think OpenClaw was my first time really recognizing how powerful a chat-thread-based AI agent could be, but I love my complex artifacts, and the setup was intimidating for any non-technical user. Eventually, OpenClaw died on the vine for me." — [same post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- On Grok Bot (decisive paragraph): "SpaceXAI's Grok Bot entered beta on August 11 and costs $120 per seat per month for teams. Its onboarding is the most intuitive of the four. It removes the decision between skills and connectors, you never think about scheduled tasks, and the result feels like a small team of bots coordinated by a chief-of-staff bot. Bots learn a workflow when you demonstrate it and operate software through its normal interface. In daily use I found it clunky, and managing a team of bots became overwhelming. It's still very functional." — [same post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- Also on Grok Bot: "Muse is also fantastic, and the GrokBot team of agents has been tremendously powerful. I also am a big fan of the Grokbot voice interaction." — [same post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- On Hermes Agent: "It is excellent, and it gave me the same magical feeling I had when I first set up OpenClaw. But it's definitely also a developer's tool, and most knowledge workers will find the setup intimidating." — [same post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- Clinical boundary: "I let these assistants research broadly and prepare aggressively, and I keep four checks in place for myself: anything sent in my name, anything published, anything signed and anything that spends money. I also keep them away from anything that touches patients." — [same post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- Orthopedics is a future promise only: "I am building in this space to work out what an autonomous clinical AI care agent should look like. I'll share what I think that means for musculoskeletal care soon." — [same post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)
- The name "Multivac" does not appear in the retrieved text of the 23 Sep post. A Substack archive search for "Multivac" returns only the 30 Jan 2026 post — [archive search](https://techysurgeon.substack.com/api/v1/archive?sort=new&search=Multivac&limit=25)
- 26 Sep 2026 (paid-only video post; only title and subtitle readable): "How I split my work between ChatGPT, Claude Cowork and three agent assistants, and how I build presentations by talking". Which three is not stated in the readable part. — [Substack Live: A Snippet of My Evolving AI OS, 26 Sep 2026](https://techysurgeon.substack.com/p/substack-live-a-snippet-of-my-evolving)

Public code / share links
- Neither post contains an x.ai/bot share link or a repo of his own. The only relevant links are to the Clawdbot and Hermes Agent projects and to x.ai/news/introducing-grok-bot. The paid section offers an Instinct invite link, "a brief on my setup" and an "ASC Landscape Report Drafted by Instinct", none of it readable. — [23 Sep 2026 post](https://techysurgeon.substack.com/p/instinct-muse-grok-bot-and-hermes)

### Inferences
- "Multivac" as a persistent named agent appears to have ended with his OpenClaw use; there is no evidence it was moved to Grok Bot, Hermes or Instinct.
- His current daily driver is most likely Instinct (his stated favorite and the one he gives subscribers an invite to), alongside ChatGPT and Claude Cowork. Grok Bot was a trial he found clunky.
- He is ruled out as a specialty-assistant match: every described use is founder, research-admin or personal productivity, and he states twice (Jan and Sep) that the agents stay away from clinical work.

### Gaps
- The paywalled "brief on my setup" (23 Sep) and the 26 Sep video were not readable, so the exact three agent assistants he uses now are unconfirmed.
- No post after 26 Sep 2026 on this topic was found in the archive searches for Grok Bot, Hermes, OpenClaw, Clawdbot or Multivac; the promised musculoskeletal-care piece was not found.
- Whether the "Paging Dr. OpenClaw" piece was ever published was not determined.

## Key question 3: Dr Michał Nedoszytko (interventional cardiology, Abridge) — any write-up, repo, template or x.ai/bot link for a cardiology assistant on Grok Bot?

### Takeaway
No. His 7 Nov 2026 AHA session is confirmed as a 30-minute live build of "a healthcare AI agent", but neither the AHA page nor his own site names Grok Bot, and no write-up, repo, template or x.ai/bot link from him was found. The claim that he demonstrated Grok Bot and said it built a demo app and his private server could not be verified from any page opened.

### Cited Findings
- AHA session page (opened): "November 7th — Opening Session: Designing and Deploying Real-World AI Agents — 9:15 am-9:45 am CT (30 min) — Health Innovation Pavilion". Description: "Live Demo: Watch Dr. Michał Nedoszytko, whose Postvisit.ai earned top honors at Anthropic's 2026 hackathon, build and demonstrate a healthcare AI agent from idea to agent right before your eyes." The page text contains no mention of Grok, xAI or any tool name. — [AHA Center for Health Technology & Innovation session page](https://ahahealthtech.org/sessions/designing-and-deploying-real-world-ai-agents/)
- The same page describes him as "an interventional cardiologist, clinician scientist at Abridge, and longtime software builder" who "builds clinical AI at Abridge". — [AHA session page](https://ahahealthtech.org/sessions/designing-and-deploying-real-world-ai-agents/)
- His own site lists the talk as "Nov 7, 2026 — Designing and Deploying Real-World AI Agents — AHA Scientific Sessions · Health Innovation Pavilion · Chicago · live build". A search of the whole page found no occurrence of Grok, x.ai, OpenMausBot, MausBot, Hermes, OpenClaw or github. — [nedoszytko.com](https://nedoszytko.com/index.html)
- His site's listed 2026 work is all PostVisit.ai / Anthropic / Abridge related: "In February 2026 I built PostVisit.ai for Anthropic's hackathon… I moved to San Francisco and joined Abridge as a clinician scientist"; a NEJM AI Perspective "Vibe Coding versus Clinical Reality" (Nov 4, 2026, DOI 10.1056/AIp2600342); NEJM AI Grand Rounds podcast (Oct 21, 2026); The 229 Podcast (Oct 8, 2026). None of these was opened. — [nedoszytko.com](https://nedoszytko.com/index.html)
- What he is documented to have built is PostVisit.ai, a post-visit patient support product built with Claude Code, not a personal always-on assistant: "PostVisit.ai — a post-visit patient support suite — placed third in Anthropic's Built with Opus 4.6 Claude Code hackathon." — [nedoszytko.com](https://nedoszytko.com/index.html)
- Three web searches combining his name with "Grok Bot", AHA and "private server" returned no page linking him to Grok Bot. — search results only; nothing to cite beyond the pages above
- Snippet only, unverified (LinkedIn, not opened): the session was billed as "Instead of a talk, we'll start with a real clinical problem from someone in the room, see how far we can get toward a working AI agent in one session, and talk about what it would take to make it safe for real patients." — [LinkedIn profile surfaced by search](https://www.linkedin.com/in/mnedoszytko/)

### Inferences
- If he did use Grok Bot on stage, it was as a build tool for a one-off live demo, not as a published, persistent cardiology assistant. Nothing public supports calling him a match.
- His public record points to Claude Code as his build tool and to Abridge as where his clinical AI work now sits.

### Gaps
- No recap, recording or transcript of the 7 Nov 2026 session was found, so what tool he used and what he said about a private server remain unverified.
- GitHub accounts named "mnedoszytko" and "nedoszytko" exist (user search), but their repositories could not be listed from this environment, so a repo check is outstanding.
- His X and LinkedIn posts after 7 Nov 2026 were not readable; the Cardiovascular Business AHA trends article returned HTTP 403.
- Unverified leads outside this task's scope, seen only as search-result titles and not opened: x.ai/bot share links titled "Health Pot" (https://x.ai/bot/E6O_rj5aW0sWo_s-GEa2y) and "Health Helper" (https://x.ai/bot/nVZ7_iBke2l0zXsHhsYME), an untitled one (https://x.ai/bot/zaPQpEv_sEbZ4pmRFcIcT), and "Your Personal Longevity Assistant: Evipedia Grok Bot" (https://lifespan.io/?p=158773). No evidence yet that a physician built any of them.
