def rule_check(workflow):
    steps = [s.lower() for s in workflow.steps]
    issues = []

    issues.extend(check_duplicates(steps))
    issues.extend(check_validation_presence(steps))
    issues.extend(check_order_dependencies(steps))
    issues.extend(check_failure_handling(steps))
    issues.extend(check_idempotency(steps))

    if not issues:
        issues.append("No rule-based issues detected")

    return issues
def check_duplicates(steps):
    if len(steps) != len(set(steps)):
        return ["Duplicate steps detected"]
    return []


def check_validation_presence(steps):
    if not any("validate" in s for s in steps):
        return ["Missing input validation step"]
    return []
def check_order_dependencies(steps):
    issues = []

    def index(step):
        return steps.index(step) if step in steps else -1

    if "activate account" in steps and "verify email" in steps:
        if index("activate account") < index("verify email"):
            issues.append(
                "Account activation occurs before email verification"
            )

    if "process payment" in steps and "validate payment" in steps:
        if index("process payment") < index("validate payment"):
            issues.append(
                "Payment processed before validation"
            )

    return issues
def check_failure_handling(steps):
    if not any(
        keyword in " ".join(steps)
        for keyword in ["retry", "rollback", "compensate", "fallback"]
    ):
        return [
            "No explicit failure handling (retry/rollback) detected"
        ]
    return []
def check_idempotency(steps):
    risky_ops = ["create", "charge", "send", "process"]

    for step in steps:
        for op in risky_ops:
            if op in step and "idempotent" not in step:
                return [
                    f"Operation '{step}' may not be idempotent; repeated execution could cause inconsistencies"
                ]

    return []
