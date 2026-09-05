def generate_response(results, role_rules):

    if not results:
        return {
            "answer": "Unknown. No approved information found.",
            "citations": []
        }

    return {
        "answer": results[0]["content"],
        "citations": [
            results[0]["source"]
        ],
        "rules_applied": role_rules
    }
