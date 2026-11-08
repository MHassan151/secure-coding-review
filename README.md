# secure-coding-review
# Secure Coding Review (Python Flask)

**Tool:** Bandit (static analyzer)
**Note:** app.py is intentionally vulnerable, for learning only.

## Findings (app.py)
| Issue | Severity | Fix |
|---|---|---|
| Flask debug=True | High | debug=False |
| os.system command injection | High | subprocess with list + input validation |
| MD5 weak hash | High | SHA-256 / bcrypt |
| SQL injection | Medium | Parameterized queries |
| Hardcoded secret key | Low | Environment variable |

## Result
- Before: 3 High, 1 Medium, 1 Low
- After (fixed_app.py): 0 High, 0 Medium, 3 Low (informational)

## Files
- app.py: vulnerable version
- fixed_app.py: remediated version
- report.html: Bandit report
