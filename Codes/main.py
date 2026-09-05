from config import PINE_RIDGE_CORPUS
from retrieval import Retriever
from security import check_permission
from roles import get_role_rules
from response_generator import generate_response


def answer_question(question, role="Executive"):

    permission = check_permission(
        question,
        role
    )

    if not permission["allowed"]:
        return permission

    retriever = Retriever(
        PINE_RIDGE_CORPUS
    )

    results = retriever.search(question)

    return generate_response(
        results,
        get_role_rules(role)
    )


if __name__ == "__main__":
    print(
        answer_question(
            "What is Pine Ridge NOI?"
        )
    )
