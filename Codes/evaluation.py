def evaluate(question_results):

    total = len(question_results)

    passed = sum(
        1 for item in question_results
        if item.get("pass")
    )

    return {
        "total": total,
        "passed": passed,
        "score": passed / total if total else 0
    }
