import re

START_DATE = r"01/Jul/1995:02:19"
END_DATE = r"01/Jul/1995:07:55"
if __name__ == '__main__':
    log_file = open("access_log_Jul95", "r")
    errors_counter = 0
    is_right_date = False
    for line in log_file:
        if re.search(START_DATE, line) != None:
            is_right_date = True
        if is_right_date and re.match(r".*((GET)|(POST)).*html.*(\" [^(200)]).*", line) != None:
            errors_counter += 1
        if re.search(END_DATE, line) != None:
            is_right_date = False
            break
    print(f"{errors_counter} html GET/POST errors between {START_DATE} and {END_DATE} found")
    log_file.close()
