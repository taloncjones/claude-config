# /pr - Create a pull request

Create a pull request with proper formatting.

## Instructions

1. First, gather context:
   - Run `git status` to check for uncommitted changes
   - Run `git log main..HEAD --oneline` to see commits to include
   - Run `git diff main...HEAD --stat` to see files changed

2. If there are uncommitted changes, ask if user wants to commit first

3. If not on a feature branch, ask for branch name (suggest based on changes)

4. Push the branch if not already pushed:
   ```bash
   git push -u origin <branch>
   ```

5. Create PR using gh CLI with this format:
   ```bash
   gh pr create --title "<scope>: <summary>" --body "$(cat <<'EOF'
   ## Summary
   <1-3 bullets describing the change>

   ## Test plan
   - [ ] <how to verify the change>

   EOF
   )"
   ```

6. Use commit scope for title (e.g., `dcdc:`, `test:`, `docs:`)

7. Return the PR URL when done
