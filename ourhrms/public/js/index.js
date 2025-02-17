frappe.ready(() => {
    document.getElementById("timelogs-btn").addEventListener("click", function () {
        let dialog = new frappe.ui.Dialog({
            title: "Add Timelog",
            fields: [
                {
                    label: "Task",
                    fieldname: "task",
                    fieldtype: "Data",
                    reqd: 1
                },
                {
                    label: "Hours Worked",
                    fieldname: "hours",
                    fieldtype: "Float",
                    reqd: 1
                },
                {
                    label: "Date",
                    fieldname: "date",
                    fieldtype: "Date",
                    reqd: 1
                }
            ],
            primary_action_label: "Save",
            primary_action(values) {
                console.log(values);
                frappe.msgprint("Timelog Added Successfully!");
                dialog.hide();
            }
        });
        dialog.show();
    });
});
