def calc_schofield_multiplier(gender, occupation_activity, non_occupation_activity):
    """Work out the Multiplier used in the Schofield equation"""
    if gender.lower() == 'male':
        if occupation_activity == 1 and non_occupation_activity == 1:
            schofield_multiplier = 1.4
        elif occupation_activity == 1 and non_occupation_activity == 2:
            schofield_multiplier = 1.5
        elif occupation_activity == 1 and non_occupation_activity == 3:
            schofield_multiplier = 1.6
        elif occupation_activity == 2 and non_occupation_activity == 1:
            schofield_multiplier = 1.6
        elif occupation_activity == 2 and non_occupation_activity == 2:
            schofield_multiplier = 1.7
        elif occupation_activity == 2 and non_occupation_activity == 3:
            schofield_multiplier = 1.8
        elif occupation_activity == 3 and non_occupation_activity == 1:
            schofield_multiplier = 1.7
        elif occupation_activity == 3 and non_occupation_activity == 2:
            schofield_multiplier = 1.8
        elif occupation_activity == 3 and non_occupation_activity == 3:
            schofield_multiplier = 1.9
        return schofield_multiplier
    elif gender.lower() == 'female':
        if occupation_activity == 1 and non_occupation_activity == 1:
            schofield_multiplier = 1.4
        elif occupation_activity == 1 and non_occupation_activity == 2:
            schofield_multiplier = 1.5
        elif occupation_activity == 1 and non_occupation_activity == 3:
            schofield_multiplier = 1.6
        elif occupation_activity == 2 and non_occupation_activity == 1:
            schofield_multiplier = 1.5
        elif occupation_activity == 2 and non_occupation_activity == 2:
            schofield_multiplier = 1.6
        elif occupation_activity == 2 and non_occupation_activity == 3:
            schofield_multiplier = 1.7
        elif occupation_activity == 3 and non_occupation_activity == 1:
            schofield_multiplier = 1.5
        elif occupation_activity == 3 and non_occupation_activity == 2:
            schofield_multiplier = 1.6
        elif occupation_activity == 3 and non_occupation_activity == 3:
            schofield_multiplier = 1.7
        return schofield_multiplier


def calc_schofield_calories(gender, age, weight, schofield_multiplier):
    """Calculate daily calorie intake using the Schofield"""
    if gender.lower() == 'male':
        if age <= 17:
            schofield_calories = ((11.5 * weight) + 873) * schofield_multiplier
        elif age <= 29:
            schofield_calories = ((15.1 * weight) + 692) * schofield_multiplier
        elif age <= 59:
            schofield_calories = ((11.5 * weight) + 873) * schofield_multiplier
        elif age <= 74:
            schofield_calories = ((11.9 * weight) + 700) * schofield_multiplier
        return schofield_calories
    elif gender.lower() == 'female':
        if age <= 17:
            schofield_calories = ((17.7 * weight) + 657) * schofield_multiplier
        elif age <= 29:
            schofield_calories = ((14.8 * weight) + 487) * schofield_multiplier
        elif age <= 59:
            schofield_calories = ((8.3 * weight) + 846) * schofield_multiplier
        elif age <= 74:
            schofield_calories = ((9.2 * weight) + 687) * schofield_multiplier
        return schofield_calories
