# TDD Mode - Quick Start

## Enable TDD Mode (3 Steps)

### 1. Backup Original
```bash
cd .kiro/aws-aidlc-rule-details/construction/
cp code-generation.md code-generation-standard.md
```

### 2. Activate TDD
```bash
cp code-generation-tdd.md code-generation.md
```

### 3. Verify
Open `code-generation.md` and check for:
- ✓ Title says "(TDD Version)"
- ✓ Step 2 lists "Test Specifications Generation" first
- ✓ Testing steps appear before implementation steps

## Disable TDD Mode (1 Step)

```bash
cd .kiro/aws-aidlc-rule-details/construction/
cp code-generation-standard.md code-generation.md
```

## What You'll See with TDD Active

### During Planning
- Plan shows: Test → Implementation → Refactor for each layer
- Mentions "Red-Green-Refactor cycle"
- Maps acceptance criteria to test cases

### During Generation
- Test files created first
- AI runs tests using executeBash - reports RED phase (tests fail as expected)
- Implementation generated
- AI runs tests using executeBash - reports GREEN phase (tests pass)
- Refactoring generated
- AI runs tests using executeBash - reports tests still GREEN

### In Your Project
```
src/
├── components/
│   ├── __tests__/          ← Tests appear first
│   │   ├── Button.test.js
│   │   └── fixtures/
│   └── Button.jsx          ← Implementation after tests
```

## Quick Comparison

| Aspect | Standard Mode | TDD Mode |
|--------|--------------|----------|
| Order | Code → Tests | Tests → Code → Refactor |
| Focus | Implementation speed | Test coverage & quality |
| Best For | Prototypes, exploration | Production, critical code |
| Artifacts | Code + tests | Tests + fixtures + code |
| Cycle | Linear | Red-Green-Refactor |

## How to Use TDD Mode

### If TDD Mode is Active (code-generation.md replaced)

Just start normally with AI-DLC:

```
"Using AI-DLC, build a calculator app."
```

The AI will automatically follow TDD rules because `code-generation.md` contains the TDD version. No need to mention TDD explicitly.

### If TDD Mode is NOT Active (standard mode)

You can still request TDD for specific parts:

```
"For the authentication module, use TDD approach:
tests first, then implementation."
```

Or mention it upfront:

```
"Using AI-DLC, build a calculator app using TDD."
```

But this requires the AI to interpret your request. Better to activate TDD mode if you want it consistently.

## Troubleshooting

**AI generates code before tests?**
→ Check `code-generation.md` is the TDD version
→ Verify the plan file lists tests first
→ Request: "Please reorder to generate tests before implementation"

**Tests pass immediately?**
→ Request: "Generate tests that verify actual behavior, not just syntax"

**No test fixtures?**
→ Request: "Please generate test data fixtures"

## Files Involved

### Code Generation
- `.kiro/aws-aidlc-rule-details/construction/code-generation.md` ← Active version
- `.kiro/aws-aidlc-rule-details/construction/code-generation-tdd.md` ← TDD version
- `.kiro/aws-aidlc-rule-details/construction/code-generation-standard.md` ← Backup

### Build and Test (Optional)
- `.kiro/aws-aidlc-rule-details/construction/build-and-test.md` ← Active version
- `.kiro/aws-aidlc-rule-details/construction/build-and-test-tdd.md` ← TDD version
- `.kiro/aws-aidlc-rule-details/construction/build-and-test-standard.md` ← Backup


## Activate Both TDD Files (Recommended)

For complete TDD workflow, activate both:

```bash
cd .kiro/aws-aidlc-rule-details/construction/

# Activate TDD Code Generation
cp code-generation.md code-generation-standard.md
cp code-generation-tdd.md code-generation.md

# Activate TDD Build and Test
cp build-and-test.md build-and-test-standard.md
cp build-and-test-tdd.md build-and-test.md
```

This ensures both Code Generation and Build & Test understand TDD was used.

## Need More Help?

Read the full guide: `TDD-CUSTOMIZATION-GUIDE.md`
