def require_inputs(**kwargs):
    missing = [
        key for key, value in kwargs.items()
        if value is None
    ]

    if missing:
        return {
            "status": "Unknown",
            "missing_inputs": missing
        }

    return None


def noi(egi, operating_expenses):
    check = require_inputs(
        egi=egi,
        operating_expenses=operating_expenses
    )

    if check:
        return check

    return {
        "formula": "NOI = EGI - Operating Expenses",
        "result": egi - operating_expenses
    }


def dscr(noi_value, debt_service):
    check = require_inputs(
        noi=noi_value,
        debt_service=debt_service
    )

    if check:
        return check

    return {
        "formula": "DSCR = NOI / Debt Service",
        "result": noi_value / debt_service
    }


def property_value(noi_value, cap_rate):
    return noi_value / cap_rate


def cost_variance(actual, budget):
    return {
        "difference": actual - budget,
        "percentage": (actual - budget) / budget
    }


def funding_gap(required, available):
    return required - available
