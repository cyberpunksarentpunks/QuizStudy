def continue_or_end():
    decision = input("Chcete pokračovat(ano) nebo program ukončit?(ne): ").strip().lower()
    if decision in ["ano", "a", "y", "yes"]:
        return "yes"
    if decision in ["ne", "n", "no"]:
        return "no"