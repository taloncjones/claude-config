# /perf-check - Performance analysis

Analyze code for performance bottlenecks, memory issues, and optimization opportunities.

## Usage

- `/perf-check` - Analyze recent git changes
- `/perf-check <path>` - Analyze specific file/directory
- `/perf-check --embedded` - Focus on embedded/real-time concerns

## Workflow

**Step 1: Determine scope**
- If paths provided: Analyze those files
- If no args: Use `git diff --name-only` for changed files

**Step 2: Identify context**
- Is this real-time/embedded code? (hard deadlines)
- Is this latency-sensitive? (user-facing)
- Is this throughput-focused? (batch processing)
- What are the resource constraints?

**Step 3: Analyze using performance-profiler methodology**

**Blocking Operations**
- Synchronous I/O on critical threads
- Long computations without yielding
- Lock contention
- Busy-waiting

**Memory Management**
- Unbounded allocations
- Memory leaks
- Large stack allocations
- Missing cleanup in error paths

**Algorithm Efficiency**
- O(n²) or worse in hot paths
- Repeated work that could be cached
- Unnecessary copies
- Suboptimal data structures

**Resource Leaks**
- Unclosed file handles
- Unreleased connections
- Unregistered callbacks
- Uncancelled timers

**Embedded/Real-Time** (if applicable)
- Dynamic allocation in ISRs
- Priority inversion risks
- Unbounded loops in critical sections
- Cache-unfriendly patterns

**Step 4: Report**

```
## Performance Analysis

**Scope**: [files analyzed]
**Context**: [embedded | latency | throughput | general]
**Health**: [OPTIMAL | MINOR ISSUES | BOTTLENECKS FOUND]

### Critical Issues
- [file:line] Issue with quantified impact and fix

### Moderate Issues
...

### Recommendations
1. Highest impact fix
2. ...

### Summary
[Overall assessment]
```

Focus on issues with real impact, not micro-optimizations.
