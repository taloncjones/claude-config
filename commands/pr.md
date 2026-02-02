# /pr - Create a pull request

Create a pull request with proper formatting and Jira integration.

## Instructions

1. First, gather context:
   - Run `git status` to check for uncommitted changes
   - Run `git log main..HEAD --oneline` to see commits to include
   - Run `git diff main...HEAD --stat` to see files changed
   - Check if behind main: `git rev-list --left-right --count origin/main...HEAD`

2. If there are uncommitted changes, ask if user wants to commit first

3. If branch is behind main, suggest running `/rebase` first to avoid merge conflicts

4. If not on a feature branch, ask for branch name (suggest based on changes)

5. Push the branch if not already pushed:

   ```bash
   git push -u origin <branch>
   ```

6. **Jira Integration** (requires Atlassian plugin):

   **Discover Atlassian site:**
   - Call `getAccessibleAtlassianResources` to get available sites
   - Extract the site URL (e.g., `https://example.atlassian.net`)
   - If multiple sites, ask user to pick

   **Determine Jira project (in priority order):**
   1. Explicit key in branch: `user/PROJ-123/topic` -> use PROJ, link to PROJ-123 directly
   2. Project segment in branch: `user/proj/topic` -> uppercase to PROJ
   3. Ask user for project key

   **Find matching ticket:**
   - Extract keywords from topic segment of branch name
   - Search for tickets in the determined project assigned to current user
   - If matching ticket(s) found:
     - Show the ticket(s) with key, summary, and status
     - Ask user to confirm: "Link this ticket to the PR?" with options:
       - Yes, use this ticket
       - No, search with different terms
       - No, create a new ticket
       - No, skip Jira linking
   - If no ticket found, ask: "No matching Jira ticket found. What would you like to do?"
     - Create a new ticket (assign to user, add to current sprint, set to In Progress)
     - Skip Jira linking

   **Add link to PR:**
   - Format: `[PROJ-###](https://<site>.atlassian.net/browse/PROJ-###)`

7. Check for existing PR on this branch:
   - If exists, ask to update description with Jira link if missing
   - If not, create new PR

8. Create/update PR using gh CLI with this format:

   ```bash
   gh pr create --title "<scope>: <summary>" --body "$(cat <<'EOF'
   ## Summary
   <1-3 bullets describing the change>

   ## Test plan
   - [ ] <how to verify the change>

   [PROJ-###](https://<site>.atlassian.net/browse/PROJ-###)
   EOF
   )"
   ```

9. Use commit scope for title (e.g., `dcdc:`, `test:`, `docs:`)

10. Return the PR URL when done

---

Related commands:

- `/jira` - ticket operations (comment, transition)
- `/checks` - view CI status
- `/rebase` - sync with main before PR
- `/done` - cleanup after merge
