# /start - Start new work

Begin work on a new task with Jira integration and worktree creation.

## Usage

- `/start <summary>` - Create new Jira ticket with summary, then worktree
- `/start PROJ-123` - Start work on existing Jira ticket
- `/start` - Interactive: search for existing ticket or create new one

## Examples

```
/start <ticket summary text>
/start PROJ-123
/start
```

## Instructions

**Step 1: Discover Atlassian site**

- Call `getAccessibleAtlassianResources` to get available sites
- Extract the site URL and cloud ID
- If multiple sites, ask user to pick

**Step 2: Determine Jira ticket**

If argument looks like a Jira key (e.g., `BESS-123`, `PROJ-456`):

- Fetch the ticket details using `getJiraIssue`
- Show ticket summary and status for confirmation

If argument is free text (summary):

- Ask user for project key (or suggest based on recent tickets)
- Create new ticket with the provided summary
- Assign to current user
- Add to current sprint
- Show created ticket for confirmation

If no argument (interactive):

- Ask user: "What would you like to work on?"
  - **Use existing ticket**: Search for "To Do" tickets assigned to user, let them pick
  - **Create new ticket**: Ask for project and summary

**Step 3: Check for existing worktree**

Check if a worktree already exists for this ticket:

```bash
git worktree list | grep -i "<JIRA-KEY>"
```

If found, run `/switch <JIRA-KEY>` instead of creating a duplicate.

**Step 4: Transition ticket**

- If ticket is not "In Progress", transition it to "In Progress"

**Step 5: Generate branch name**

Format: `<user>/<PROJECT-###>/<topic-slug>`

- User: extract from git config `user.email` (part before @), lowercase
- Project/ticket: from Jira key (e.g., `PROJ-123`)
- Topic: slugified from ticket summary (lowercase, hyphens, max 40 chars, remove filler words like "add", "update", "the")

Examples:

- "Expand EOL test coverage for coil sequence verification" -> `eol-test-coverage-coil-sequence`
- "Add voltage sink tests" -> `voltage-sink-tests`

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

```
Started work on PROJ-123: <ticket summary>

Worktree: ../<topic-slug>
Branch:   <user>/PROJ-123/<topic-slug>
Jira:     https://<site>.atlassian.net/browse/PROJ-123
Status:   In Progress

Ready to begin.
```

---

Related commands:

- `/jira mine` - list tickets to pick from
- `/status` - check current work status
- `/pr` - create pull request when done
