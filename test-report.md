# Test Report — PythonDemo

**Generated:** 2025-11-26  
Summary: concise, clickable report with pass/fail badges and detailed sections.

## Overview
- Total tests: 6  
- Passed: 4 ![passed](https://img.shields.io/badge/Passed-4-brightgreen)  
- Failed: 2 ![failed](https://img.shields.io/badge/Failed-2-red)

Quick links: [All Tests](#test-cases) · [Failures](#failures)

---

## Test Cases

| ID | Title | Status | Link | Duration | Owner |
|---:|---|---:|---|---:|---|
| TC-001 | Login — valid credentials | [![PASS](https://img.shields.io/badge/Status-PASS-brightgreen)](#tc-001---login---valid-credentials) | [Details](#tc-001---login---valid-credentials) | 8s | alice |
| TC-002 | Login — invalid password | [![FAIL](https://img.shields.io/badge/Status-FAIL-red)](#tc-002---login---invalid-password) | [Details](#tc-002---login---invalid-password) | 5s | bob |
| TC-003 | Create item — minimal fields | [![PASS](https://img.shields.io/badge/Status-PASS-brightgreen)](#tc-003---create-item---minimal-fields) | [Details](#tc-003---create-item---minimal-fields) | 12s | carol |
| TC-004 | Create item — duplicate name | [![PASS](https://img.shields.io/badge/Status-PASS-brightgreen)](#tc-004---create-item---duplicate-name) | [Details](#tc-004---create-item---duplicate-name) | 7s | dave |
| TC-005 | Export CSV — large dataset | [![FAIL](https://img.shields.io/badge/Status-FAIL-red)](#tc-005---export-csv---large-dataset) | [Details](#tc-005---export-csv---large-dataset) | 45s | alice |
| TC-006 | UI — responsive layout | [![PASS](https://img.shields.io/badge/Status-PASS-brightgreen)](#tc-006---ui---responsive-layout) | [Details](#tc-006---ui---responsive-layout) | 6s | carol |

---

## Failures

### TC-002 — Login — invalid password
<a name="tc-002---login---invalid-password"></a>

Status: ![FAIL](https://img.shields.io/badge/Status-FAIL-red)

- Priority: High
- Steps:
  1. Open login page
  2. Enter valid username
  3. Enter invalid password
  4. Click "Sign in"
- Expected: "Invalid credentials" error displayed
- Actual: No error; user redirected to dashboard (security issue)
- Logs / evidence:
<details>
<summary>Show logs & screenshot</summary>

```
2025-11-26 10:12:34 INFO Attempt login user=alice
2025-11-26 10:12:34 WARN Invalid password for user=alice not handled
Screenshot: ./artifacts/TC-002-login-invalid-password.png
```

</details>

Suggested fix: Harden login validation and re-check redirect logic.

---

### TC-005 — Export CSV — large dataset
<a name="tc-005---export-csv---large-dataset"></a>

Status: ![FAIL](https://img.shields.io/badge/Status-FAIL-red)

- Priority: Medium
- Steps:
  1. Populate dataset with 200k rows
  2. Navigate to Export > CSV
  3. Click "Export"
- Expected: CSV generated and downloaded within 60s
- Actual: Timeout after 120s, service returns 504
- Logs / evidence:
<details>
<summary>Show logs & stacktrace</summary>

```
2025-11-26 11:01:05 ERROR Export job timeout id=job-98765 duration=120s
Stack: requests.exceptions.ReadTimeout: HTTPSConnectionPool...
```

</details>

Suggested fix: Implement server-side streaming export or async job with notification.

---

## Passed tests (short)
- TC-001 — Login — valid credentials — checks: auth token, redirect
- TC-003 — Create item — minimal fields — checks: DB insert
- TC-004 — Create item — duplicate name — checks: proper 409 response
- TC-006 — UI — responsive layout — checks: mobile/tablet breakpoints

---

## How to use this report
- Click a badge or "Details" link to jump to the test's section.
- Expand "Show logs" for full evidence.
- Triage failures by priority (High → Medium → Low) and assign fixes.

---

If you want an HTML-styled version or automatic generation from test runner output (JUnit/pytest JSON), I can add a script to convert results into this format.

