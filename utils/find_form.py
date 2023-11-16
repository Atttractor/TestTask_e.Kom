from tinydb import TinyDB
from config.config import DB_PATH


def find_suitable_form(request_dict):
    db = TinyDB(DB_PATH)
    forms = db.all()

    max_fields_matched_form = None
    matches = 0

    for form in forms:
        current_form_fields = list(form.items())[1:]
        number_of_fields_matched = 0

        for form_field in current_form_fields:
            if form_field not in list(request_dict.items()):
                break
            number_of_fields_matched += 1
        else:
            if number_of_fields_matched > matches:
                max_fields_matched_form = form
                matches = number_of_fields_matched

    return max_fields_matched_form