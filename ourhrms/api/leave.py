import frappe
from frappe import whitelist
import json

@whitelist()
def apply_leave():
    try:
        user_email = frappe.session.user
        if user_email in ["Guest", None]:
            frappe.throw("You must be logged in to apply for leave.")

        employee = frappe.db.get_value("Employee", {"email": user_email}, "name")
        if not employee:
            frappe.throw("Employee record not found for this user.")

        leave_type = frappe.form_dict.get("leave_type")
        from_date = frappe.form_dict.get("from_date")
        to_date = frappe.form_dict.get("to_date")
        leave_reason = frappe.form_dict.get("leave_reason")
        leave_dates = json.loads(frappe.form_dict.get("leave_dates", "[]"))
        holiday_types = json.loads(frappe.form_dict.get("holiday_types", "[]"))
        leave_type_childs = json.loads(frappe.form_dict.get("leave_type_childs", "[]"))

        print(leave_dates)
        print(holiday_types)
        print(leave_type_childs)

        leave_application = frappe.get_doc({
            "doctype": "Leave Application",
            "employee": employee,
            "leave_type": leave_type,
            "from_date": from_date,
            "to_date": to_date,
            "leave_reason": leave_reason,
            "status": "Pending",
        })

        for leave_date, holiday_type, leave_type_child in zip(leave_dates, holiday_types, leave_type_childs):
            print(f"{leave_date} ... {holiday_type} ... {leave_type_child}")
            leave_application.append("leave_details", {
                "leave_date": leave_date,
                "holiday_type": holiday_type,
                "leave_details_child": leave_type_child,
            })

        leave_application.insert()
        frappe.db.commit()

        return {"message": "Leave application submitted successfully"}

    except Exception as e:
        frappe.log_error(f"Error applying leave: {str(e)}")
        return {"error": str(e)}

@frappe.whitelist()
def get_holiday_details(from_date, to_date):
    holiday_data = {}

    holiday_list = frappe.get_all(
        "Weekend and Holiday List",
        filters={"date": ["between", [from_date, to_date]]},
        fields=["date", "holiday_name", "is_weekend", "is_public_holiday", "description"]
    )

    for holiday in holiday_list:
        holiday_type = []
        # if holiday.get("is_weekend"):
        #     holiday_type.append("Weekend")
        # if holiday.get("is_public_holiday"):
        #     holiday_type.append("Public Holiday")

        # Include holiday name if available
        holiday_name = holiday.get("holiday_name", "").strip()
        if holiday_name:
            holiday_type.append(holiday_name)  # Add holiday name to the type list

        # Store the details in holiday_data
        holiday_data[holiday["date"].strftime('%Y-%m-%d')] = ", ".join(holiday_type).strip()

    print(holiday_data)  # Debugging output
    return {"message": holiday_data}
