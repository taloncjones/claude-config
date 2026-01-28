# /debug - Systematic debugging

Debug issues using structured root cause analysis.

## Usage

- `/debug` - Debug issue from recent context/error
- `/debug <error message>` - Debug specific error
- `/debug <file:line>` - Debug starting from location

## Workflow

Using debugger agent methodology:

**Phase 1: Understand the Symptom**

Establish facts before diving into code:
- What exactly is the error/behavior?
- When does it happen? (always, sometimes, specific conditions)
- What's expected vs actual?

**Phase 2: Reproduce**

Trace the execution path:
```
Input → Function A → Function B → [FAILURE] → Expected
                         ↑
                    What happened here?
```

- Identify entry point
- Trace data flow
- Find branch points
- Locate failure point

**Phase 3: Form Hypotheses**

Based on error type, rank likely causes:

**NullPointer/AttributeError:**
1. Value not initialized
2. Value set to null somewhere
3. Wrong object type

**Wrong Output:**
1. Logic error in condition
2. Wrong variable used
3. Off-by-one error

**Intermittent:**
1. Race condition
2. Uninitialized state
3. External dependency timing

**Regression:**
1. Recent change in this file
2. Change in dependency
3. Config/environment change

**Phase 4: Investigate**

For each hypothesis (highest probability first):
- What would prove/disprove it?
- Read relevant code
- Check git history: `git log -p <file>`
- Gather evidence, evaluate

**Phase 5: Fix and Verify**

```
## Debug Analysis

### Symptom
[Exact error]

### Hypotheses (ranked)
1. [Most likely]
2. [Second likely]

### Root Cause
[The actual issue]

### Fix
[Code change]

### Prevention
- [ ] Test to add
- [ ] Similar code to check
```

**Anti-patterns to avoid:**
- Shotgun debugging (random changes)
- Symptom patching (not fixing root cause)
- Assumption jumping (skipping verification)
