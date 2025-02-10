# import frappe

# def get_context(context):
#     context.employees = frappe.get_all("Employee", 
#         fields=["first_name", "last_name", "email", "date_of_joining", "department", "designation", "contact_number"]
#     )
#     return context
import frappe

def get_context(context):
    user_email = frappe.session.user  # Get logged-in user's email

    # Fetch employee details for the logged-in user
    employee = frappe.get_all("Employee", 
        filters={"email": user_email}, 
        fields=["first_name", "last_name", "email", "date_of_joining", "department", "designation", "contact_number"]
    )

    if employee:
        context.employee = employee[0]  # Assign the first (and only) record to context
    else:
        context.employee = None  # If no employee found, return None

    return context
