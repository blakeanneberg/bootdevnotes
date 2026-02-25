def convert_hours_to_seconds(hours):
    # ?
    return 3600 * hours
# Don't touch below this line


def test(hours):
    secs = convert_hours_to_seconds(hours)
    print(f"{hours} hours is {secs} seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)
