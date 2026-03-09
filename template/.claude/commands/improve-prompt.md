Take the user's raw prompt and refine it into a well-structured prompt optimized for Claude Code plan mode.

## Step 1: Capture the Raw Prompt

The user's raw prompt is provided as the argument: $ARGUMENTS

If no argument was provided, ask the user to paste their prompt.

## Step 2: Analyze Against Quality Dimensions

Evaluate the raw prompt against each dimension. For each, note whether it's adequate or has a gap:

1. **Objective clarity** — Is there a single, unambiguous goal? Or is it vague / multi-headed?
2. **Technical specificity** — Are relevant files, classes, systems, or patterns named? Or is it abstract?
3. **Scope boundaries** — Is it clear what's in-scope and out-of-scope? Or is scope unbounded?
4. **Constraints** — Are there performance, compatibility, or style requirements that matter?
5. **Acceptance criteria** — How will "done" be verified? Is there a testable outcome?
6. **Context / motivation** — Is there enough background to understand *why* this change is needed?
7. **Ambiguity** — Are there words or phrases with multiple interpretations?
8. **Dependencies** — Does this touch systems that interact with other systems?

## Step 3: Ask Clarifying Questions (If Needed)

If there are **critical gaps** — where guessing wrong would waste significant effort or produce the wrong result — ask the user 1-3 targeted clarifying questions using AskUserQuestion.

Skip this step if the prompt is already clear enough. Don't over-question simple requests.

## Step 4: Produce the Improved Prompt

Output the improved prompt in this structure:

**Goal:** One sentence — what should be accomplished.

**Context:** Why this change is needed and what prompted it.

**Scope:**
- In-scope: [what to do]
- Out-of-scope: [what NOT to do]

**Technical details:** Relevant files, systems, patterns, or constraints worth mentioning up front.

**Acceptance criteria:** How to verify the change works correctly.

## Rules

- **Preserve intent exactly** — improve the expression, not the idea. Don't add requirements the user didn't imply.
- **Stay concise** — plan mode handles deep exploration. The prompt just needs to point it in the right direction.
- **Don't over-engineer** — if the prompt is already clear and specific, say so. Not every prompt needs all five sections.
- **Use what you know** — if you can identify relevant files or systems from the codebase, include them. This saves plan mode from redundant exploration.
- **Show your work briefly** — before the improved prompt, list 2-3 bullet points on what you changed and why, so the user can learn the pattern.
