

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "pid", "cid"]
# ecl is optional


def is_valid(passport_text):
    """
    Returns True if the passport contains all required fields
    (eye color ecl is optional).
    """
    fields = passport_text.replace("\n", " ").split()
    keys = [field.split(":")[0] for field in fields]

    for req in REQUIRED_FIELDS:
        if req not in keys:
            return False
    return True


def main():
    filename = input("Enter the name of the file: ")

    with open(filename, "r") as infile:
        content = infile.read()

    # Split passports by blank lines
    passports = content.strip().split("\n\n")

    valid_passports = []

    for passport in passports:
        if is_valid(passport):
            valid_passports.append(passport)

    # Write valid passports to output file
    with open("valid_passports.txt", "w") as outfile:
        for i, passport in enumerate(valid_passports):
            outfile.write(passport)
            if i != len(valid_passports) - 1:
                outfile.write("\n\n")

    print(f"There are {len(valid_passports)} valid passports")


if __name__ == "__main__":
    main()

