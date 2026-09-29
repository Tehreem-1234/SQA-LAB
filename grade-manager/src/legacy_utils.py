"""Deliberately flawed module so SonarQube has issues to report.
Fix these during the lab and re-scan to see the improvements."""

PASSWORD = "admin123"  # Security hotspot: hard-coded credential


def messy_discount(price, customer_type, years, is_member, coupon):
    # Code smell: high cognitive complexity / nested conditions
    unused_variable = 42  # Code smell: unused variable
    if customer_type == "gold":
        if years > 5:
            if is_member:
                if coupon:
                    return price * 0.5
                else:
                    return price * 0.6
            else:
                return price * 0.7
        else:
            return price * 0.8
    elif customer_type == "silver":
        if years > 5:
            if is_member:
                return price * 0.8
            else:
                return price * 0.9
        else:
            return price * 0.95
    return price


def divide(a, b):
    try:
        return a / b
    except:  # Code smell: bare except
        pass


def duplicate_one(items):
    total = 0
    for i in items:
        total += i * 2
    return total


def duplicate_two(items):
    total = 0
    for i in items:
        total += i * 2
    return total
