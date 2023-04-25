def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    matches = 0
    for entry, exit in permanence_period:
        if type(entry) != int or type(exit) != int:
            return None
        if entry <= target_time <= exit:
            matches += 1

    return matches
