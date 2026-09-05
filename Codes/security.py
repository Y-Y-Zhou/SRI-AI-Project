RESTRICTED_TERMS = [
    "ssn",
    "social security",
    "bank account",
    "wire information",
    "password",
    "api key",
    "private key"
]


def check_permission(question, role="Executive"):

    lower = question.lower()

    for item in RESTRICTED_TERMS:
        if item in lower:
            return {
                "allowed": False,
                "reason": "Restricted information."
            }

    return {
        "allowed": True,
        "reason": None
    }
