# /start - Start new work

Begin work on a new task with optional Jira integration and worktree creation.

## Usage

- `/start <topic>` - Create worktree with topic name (no Jira)
- `/start PROJ-123` - Start work on existing Jira ticket (requires Atlassian plugin)
- `/start` - Interactive: ask for topic or search Jira tickets

## Examples

```
/start voltage-sink-tests
/start PROJ-123
/start
```

## Instructions

**Step 1: Check for Atlassian plugin**

Try calling `getAccessibleAtlassianResources`:

- If successful: Jira integration is available, store site URL and cloud ID
- If fails or no sites returned: Jira not available, proceed without it

**Step 2: Determine task**

If argument looks like a Jira key (e.g., `PROJ-123`, `PROJ-456`) AND Jira is available:

- Fetch the ticket details using `getJiraIssue`
- Show ticket summary and status for confirmation
- Extract topic from ticket summary

If argument looks like a Jira key but Jira is NOT available:

- Warn: "Jira plugin not available. Use `/start <topic>` instead."
- Stop

If argument is free text (topic):

- Use it as the topic slug directly
- If Jira available, optionally ask: "Link to a Jira ticket?" (default: no)

If no argument (interactive):

- If Jira available, ask: "Link to a Jira ticket?"
  - **Yes**: Offer options:
    - Pick from open tickets (To Do, In Progress) assigned to user
    - Enter a ticket key directly
    - Create a new ticket (ask for project and summary)
  - **No**: Ask for topic name only, proceed without Jira
- If Jira not available: Ask for topic name for the branch

**Step 3: Check for existing worktree**

Check if a worktree already exists for this topic/ticket:

```bash
git worktree list | grep -i "<topic-or-jira-key>"
```

If found, run `/switch <match>` instead of creating a duplicate.

**Step 4: Transition ticket (Jira only)**

If Jira ticket is linked and not "In Progress":

- Transition it to "In Progress"

**Step 5: Generate branch name**

With Jira: `<user>/<PROJ-###>/<topic-slug>`
Without Jira: `<user>/<topic-slug>`

- User: extract from git config `user.email` (part before @), lowercase
- Topic: slugified (lowercase, hyphens, max 40 chars, remove filler words)

Examples:

- With Jira: `talon/PROJ-123/voltage-sink-tests`
- Without Jira: `talon/voltage-sink-tests`

**Step 6: Create worktree and switch to it**

```bash
git fetch origin

# Determine default branch
DEFAULT_BRANCH=$(git remote show origin 2>/dev/null | grep "HEAD branch" | cut -d: -f2 | xargs)
if [ -z "$DEFAULT_BRANCH" ]; then
    DEFAULT_BRANCH="main"
fi

# Create worktree in parent directory using topic slug as folder name
WORKTREE_PATH="../$TOPIC_SLUG"
git worktree add --track -b "$BRANCH_NAME" "$WORKTREE_PATH" "origin/$DEFAULT_BRANCH"

# Switch to the new worktree
cd "$WORKTREE_PATH"
```

**Step 7: Report**

With Jira:

```
Started work on PROJ-123: <ticket summary>

Worktree: ../<topic-slug>
Branch:   <user>/PROJ-123/<topic-slug>
Jira:     https://<site>.atlassian.net/browse/PROJ-123
Status:   In Progress

Ready to begin.
```

Without Jira:

```
Started work: <topic>

Worktree: ../<topic-slug>
Branch:   <user>/<topic-slug>

Ready to begin.
```

---

Related commands:

- `/jira mine` - list tickets to pick from
- `/status` - check current work status
- `/pr` - create pull request when done
