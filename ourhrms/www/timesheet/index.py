# import frappe

# def get_context(context):
#     user_email = frappe.session.user  # Get logged-in user's email

#     # Fetch the Employee record associated with the logged-in user
#     employee = frappe.get_value("Employee", {"email": user_email}, "name")

#     if employee:
#         # Fetch all timesheets for the identified employee
#         timesheets = frappe.get_all("Timesheet", 
#             filters={"employee": employee}, 
#             fields=["name","employee", "date", "total_hours", "tasks"]
#         )
#         context.timesheets = timesheets  # Assign timesheets to context
#     else:
#         context.timesheets = []  # No timesheets if no matching employee is found

#     return context




# import frappe

# def get_context(context):
#     user_email = frappe.session.user  # Get logged-in user's email

#     # Fetch the Employee record associated with the logged-in user
#     employee = frappe.get_value("Employee", {"email": user_email}, "name")

#     if employee:
#         # Fetch all timesheets for the identified employee
#         timesheets = frappe.get_all(
#             "Timesheet",
#             filters={"employee": employee},
#             fields=["name", "employee", "date", "total_hours"]
#         )

#         # Fetch tasks separately if they are in a child table
#         for ts in timesheets:
#             tasks = frappe.get_all(
#                 "Timesheet Details",  # Assuming "Timesheet Details" is the child table
#                 filters={"parent": ts["name"]},
#                 fields=["task_name"]
#             )
#             ts["tasks"] = ", ".join([task["task_name"] for task in tasks]) if tasks else "No tasks"

#         context.timesheets = timesheets  # Assign timesheets to context
#     else:
#         context.timesheets = []  # No timesheets if no matching employee is found

#     return context



import frappe

def get_context(context):
    user_email = frappe.session.user  # Get logged-in user's email
    print(f"Logged-in user email: {user_email}")  # Debugging

    # Fetch the Employee record associated with the logged-in user
    employee = frappe.get_value("Employee", {"email": user_email}, "name")
    print(f"Employee Name: {employee}")  # Debugging

    if employee:
        timesheets = frappe.get_all(
            "Timesheet",
            filters={"employee": employee},
            fields=["name", "date", "total_hours"]
        )
        print(f"Fetched Timesheets: {timesheets}")  # Debugging

        for ts in timesheets:
            tasks = frappe.get_all(
                "Timesheet Details",
                filters={"parent": ts["name"]},
                fields=["task_name"]
            )
            print(f"Tasks for {ts['name']}: {tasks}")  # Debugging
            ts["tasks"] = ", ".join([task["task_name"] for task in tasks]) if tasks else "No tasks"

        context.timesheets = timesheets  # Assign timesheets to context
    else:
        context.timesheets = []  # No timesheets if no matching employee is found

    return context
