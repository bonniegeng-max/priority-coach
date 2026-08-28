## Description:

Priority Coach is a gentle personal-growth coaching skill that helps users narrow cluttered priorities into the 1-3 things that matter now and a small action they can begin today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and personal-productivity users use this skill to clarify priorities, plan a low-pressure first step, start or close a day, and shift into a lighter mode when overloaded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist local records (session summaries and full result cards) containing personal reflections on the user's device.

Mitigation: All local writes are strictly opt-in — no file is written without the user's explicit consent, raw answers require a second consent, records stay on-device only (no network, no upload, no telemetry), and users can delete any record via `record.py delete` at any time.

Risk: Coaching outputs are advisory and may not fit every user's situation.

Mitigation: The skill explicitly avoids making final life decisions for the user, avoids empty motivational filler, and routes users showing crisis-level distress to trusted personal contacts and professional/local emergency support instead of continuing coaching.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [Router](references/router.md)
- [States](references/states.md)
- [Cold Start](references/cold-start.md)
- [Daily Flows](references/daily-flows.md)
- [Memory Schema](references/memory-schema.md)
- [Copy Tone](references/copy-tone.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, local record-management commands]

**Output Format:** [Markdown guidance with structured coaching cards and optional local record-management commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce priority cards, action cards, wrap-up cards, low-burden mode cards, and local record-management commands when appropriate.]

## Skill Version(s):

0.2.2 (source: frontmatter, release evidence, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
