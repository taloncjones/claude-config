# /switch - Switch between worktrees

List and switch Claude's working directory to a different worktree.

## Usage

- `/switch` - List worktrees and pick one
- `/switch <name>` - Switch to worktree matching name (partial match)

## Examples

```
/switch
/switch <topic>
/switch PROJ-123
/switch 2
```

## Instructions

**Step 1: List worktrees with context**

```bash
git worktree list
```

For each worktree, gather:

- Path
- Branch name
- Jira key (extracted from branch)
- Jira status (if Atlassian plugin available)
- Uncommitted changes (`git -C <path> status --porcelain`)
- Commits ahead of main

Display as numbered table:

```
Worktrees:

| # | Directory   | Branch                      | Jira                  | Changes |
|---|-------------|-----------------------------|-----------------------|---------|
| 1 | <repo>      | main                        | -                     | clean   |
| 2 | <topic-a>   | <user>/PROJ-123/<topic-a>   | PROJ-123 In Progress  | clean   |
| 3 | <topic-b>   | <user>/PROJ-124/<topic-b>   | PROJ-124 In Progress  | 2 files |

Current: <repo> (main)

Enter number, name, or Jira key to switch:
```

**Step 2: Match selection**

If argument provided, match against:

1. Worktree number (e.g., "2")
2. Directory name (partial match, e.g., "voltage")
3. Branch name (partial match)
4. Jira key (e.g., "PROJ-123")

If no argument, prompt user to pick.

**Step 3: Switch working directory**

```bash
cd <worktree-path>
```

This changes Claude's working directory for subsequent commands.

**Step 4: Confirm switch and show context**

```
Switched to: ~/Git/work/<topic>

Branch: <user>/PROJ-123/<topic>
Jira:   PROJ-123 - <ticket summary> (In Progress)
        https://<site>.atlassian.net/browse/PROJ-123

Status: N commits ahead of main, working tree clean

Last commit: <scope>: <summary> (<time> ago)
```

---

Related commands:

- `/start` - create new worktree for Jira ticket
- `/status` - detailed status of current worktree
- `/done` - cleanup worktree after PR merge
