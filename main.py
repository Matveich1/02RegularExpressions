import csv
import re


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        contacts_list = list(reader)

        return contacts_list


def full_names(correct_number_list):
    result_list = list()
    for contact in correct_number_list:
        full_name_list = " ".join(contact[0:3]).split()
        if len(full_name_list) != 3:
            full_name_list.append("")
        result = full_name_list + contact[3:]
        result_list.append(result)
    print(result_list)
    return result_list


def clear_phones(contacts_list):
    phone_pattern = (
        r"(\+7|8)(\s*)(\(*)(\d{3})(\-*)(\)*)(\s*)(\d{3})(\-*)"
        r"(\s*)(\d{2})(\-*)(\s*)(\d{2})(\s*)(\(*)(доб\.)*(\s*)(\d+)*(\)*)"
    )
    phone_replace = r"+7(\4)\8-\11-\14\15\17\19"

    correct_number_list = list()
    for contact in contacts_list:
        string_value = ','.join(contact)
        clear_string = re.sub(phone_pattern, phone_replace, string_value)
        list_value = clear_string.split(',')
        correct_number_list.append(list_value)
    return correct_number_list


def final_format(result_list):
    final_list = list()
    for c in result_list:
        for contact_in_final_list in final_list:
            if contact_in_final_list[:1] == c[:1]:
                final_list.remove(contact_in_final_list)
                c = [x if x != "" else y for x,
                     y in zip(contact_in_final_list, c)]
        final_list.append(c)

    print(final_list)
    return final_list


def write_file(result_list):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(result_list)


if __name__ == '__main__':
    contacts = read_file('phonebook_raw.csv')
    contacts = clear_phones(contacts)
    contacts = full_names(contacts)
    contacts = final_format(contacts)
    write_file(contacts)
