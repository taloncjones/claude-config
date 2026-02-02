# /worktree - Git worktree management

Create and manage git worktrees for parallel development.

## Usage

- `/worktree` - Create new worktree with auto-generated name
- `/worktree <name>` - Create worktree with specific branch name
- `/worktree list` - List existing worktrees
- `/worktree remove <name>` - Remove a worktree

## Create Worktree

**Step 1: Fetch latest**

```bash
git fetch origin
```

**Step 2: Determine default branch**

```bash
DEFAULT_BRANCH=$(git remote show origin 2>/dev/null | grep "HEAD branch" | cut -d: -f2 | xargs)
if [ -z "$DEFAULT_BRANCH" ]; then
    if git branch -r | grep -q "origin/main"; then
        DEFAULT_BRANCH="main"
    else
        DEFAULT_BRANCH="master"
    fi
fi
```

**Step 3: Generate branch name** (if not provided)

```bash
# Find next available worktree number
HIGHEST=$(git branch --list 'worktree*' | sed 's/.*worktree//' | sort -n | tail -1)
NEXT=$((${HIGHEST:-0} + 1))
BRANCH_NAME="worktree$NEXT"
```

**Step 4: Create worktree**

```bash
# Create in parent directory
WORKTREE_PATH="../$BRANCH_NAME"
git worktree add --track -b "$BRANCH_NAME" "$WORKTREE_PATH" "origin/$DEFAULT_BRANCH"
```

**Step 5: Report**

```
Created worktree at: ../worktree1
Branch: worktree1 (tracking origin/main)
cd ../worktree1 to start working
```

## List Worktrees

```bash
git worktree list
```

## Remove Worktree

```bash
git worktree remove <path>
git branch -d <branch>  # if branch should also be deleted
```

Worktrees allow working on multiple branches simultaneously without stashing or committing incomplete work.

---

Related commands:

- `/start` - Jira-integrated worktree creation (recommended)
- `/done` - cleanup worktree after PR merge
