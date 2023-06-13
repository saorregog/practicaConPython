def format_duration(seconds):
    if (seconds == 0):
        return "now"

    result = list()

    if (seconds >= (60 * 60 * 24 * 365)):
        years = seconds // (60 * 60 * 24 * 365)
        seconds -= years * (60 * 60 * 24 * 365)
        if (years == 1):
            result.append(f"{years} year")
        else:
            result.append(f"{years} years")

    if (seconds >= (60 * 60 * 24)):
        days = seconds // (60 * 60 * 24)
        seconds -= days * (60 * 60 * 24)
        if (days == 1):
            result.append(f"{days} day")
        else:
            result.append(f"{days} days")

    if (seconds >= (60 * 60)):
        hours = seconds // (60 * 60)
        seconds -= hours * (60 * 60)
        if (hours == 1):
            result.append(f"{hours} hour")
        else:
            result.append(f"{hours} hours")

    if (seconds >= (60)):
        minutes = seconds // (60)
        seconds -= minutes * (60)
        if (minutes == 1):
            result.append(f"{minutes} minute")
        else:
            result.append(f"{minutes} minutes")

    if (seconds > (0)):
        if (seconds == 1):
            result.append(f"{seconds} second")
        else:
            result.append(f"{seconds} seconds")

    return (((", ".join(result))[::-1]).replace(" ,", " dna ", 1))[::-1]

print(format_duration(205851834))
print(format_duration(33243586))
