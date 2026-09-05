ROLE_RULES = {

"Executive": [
    "focus on decisions",
    "focus on risks",
    "focus on business impact"
],

"Phoenix Construction": [
    "focus on schedule",
    "focus on cost",
    "focus on delivery"
],

"Property Management": [
    "focus on occupancy",
    "focus on revenue",
    "focus on operations"
],

"Finance": [
    "focus on verified numbers",
    "show calculations",
    "show assumptions"
],

"Investor Relations": [
    "separate facts, calculations, forecasts, unknowns",
    "use approved communication"
]

}


def get_role_rules(role):
    return ROLE_RULES.get(
        role,
        ROLE_RULES["Executive"]
    )
