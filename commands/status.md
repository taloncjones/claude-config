# /status - Check current work status

Quick overview of current branch, Jira ticket, and PR status.

## Usage

- `/status` - Show status of current worktree/branch

## Instructions

**Step 1: Gather git and worktree context**

```bash
# Current branch
git branch --show-current

# Current worktree and list of all worktrees
git worktree list

# Commits ahead/behind main
git rev-list --left-right --count origin/main...HEAD

# Check if branch is pushed
git rev-parse --abbrev-ref @{upstream} 2>/dev/null
```

Show worktree context if multiple worktrees exist:

```
Worktree: <topic> (1 of 3)
```

**Step 2: Extract Jira ticket from branch**

Parse branch name for Jira key pattern (e.g., `<user>/<PROJ-###>/topic` -> `PROJ-###`)

If found:

- Call `getAccessibleAtlassianResources` to get site
- Fetch ticket details using `getJiraIssue`
- Get ticket summary and status

**Step 3: Check PR status**

```bash
gh pr view --json number,title,state,url,mergedAt,mergeable 2>/dev/null
```

**Step 4: Display status**

```
Branch:   <user>/<PROJ-###>/<topic>
          N commits ahead of main, M behind

Jira:     PROJ-123 - <ticket summary>
          Status: In Progress
          https://<site>.atlassian.net/browse/PROJ-123

PR:       #<number> - <scope>: <summary>
          Status: Open (mergeable)
          https://github.com/<org>/<repo>/pull/<number>
```

**Step 5: Show warnings and suggestions**

Show relevant warnings/suggestions (no prompts, just info):

- If uncommitted changes: "Uncommitted changes - use /commit"
- If branch is behind main: "Branch is M commits behind main - use /rebase"
- If branch is not pushed: "Branch not pushed"
- If PR is merged: "PR merged - use /done to clean up"
- If PR has conflicts: "PR has conflicts - use /rebase"
- If Jira is still "To Do": "Jira still To Do - use /jira progress"

---

Related commands:

- `/jira` - ticket operations (comment, transition, assign)
- `/checks` - detailed CI status
- `/rebase` - sync with main
- `/pr` - create pull request
- `/done` - cleanup after merge
