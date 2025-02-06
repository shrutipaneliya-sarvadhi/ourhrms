// Copyright (c) 2025, sarvadhi and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Timesheet", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on('Timesheet', {
//     refresh: function(frm) {
//         // If Clock In is not set, show "Start Clock" button
//         if (!frm.doc.clock_in) {
//             frm.add_custom_button('Start Clock', function() {
//                 frappe.model.set_value(frm.doctype, frm.docname, 'clock_in', frappe.datetime.now_datetime());
//                 frm.save();
//             }).addClass('btn-primary');
//         }
//         // If Clock In is set but Clock Out is empty, show "Stop Clock" button
//         else if (frm.doc.clock_in && !frm.doc.clock_out) {
//             frm.add_custom_button('Stop Clock', function() {
//                 frappe.model.set_value(frm.doctype, frm.docname, 'clock_out', frappe.datetime.now_datetime());
//                 frm.save();
//             }).addClass('btn-danger');
//         }
//     },

//     clock_out: function(frm) {
//         if (frm.doc.clock_in && frm.doc.clock_out) {
//             let diff = moment(frm.doc.clock_out).diff(moment(frm.doc.clock_in), 'hours', true);
//             frappe.model.set_value(frm.doctype, frm.docname, 'total_hours', diff.toFixed(2));
//         }
//     }
// });

// frappe.ui.form.on('Timesheet', {
//     refresh: function(frm) {
//         frm.fields_dict["timesheet_detail"].grid.add_custom_button("Start Clock", function() {
//             let selected_row = frm.fields_dict["timesheet_detail"].grid.get_selected();
//             if (selected_row.length > 0) {
//                 let row = locals["Timesheet Detail"][selected_row[0]];
//                 frappe.model.set_value("Timesheet Detail", row.name, "clock_in", frappe.datetime.now_datetime());
//                 frm.refresh_field("timesheet_detail");
//             } else {
//                 frappe.msgprint("Please select a row in the child table.");
//             }
//         }).addClass("btn-primary");

//         frm.fields_dict["timesheet_detail"].grid.add_custom_button("Stop Clock", function() {
//             let selected_row = frm.fields_dict["timesheet_detail"].grid.get_selected();
//             if (selected_row.length > 0) {
//                 let row = locals["Timesheet Detail"][selected_row[0]];
//                 frappe.model.set_value("Timesheet Detail", row.name, "clock_out", frappe.datetime.now_datetime());
//                 frm.refresh_field("timesheet_detail");
//             } else {
//                 frappe.msgprint("Please select a row in the child table.");
//             }
//         }).addClass("btn-danger");
//     }
// });

// frappe.ui.form.on('Timesheet', {
//     // Add Start Time button
//     refresh: function(frm) {
//         if(!frm.is_new()){
//             frm.add_custom_button(__('Start Time'), function() {
//                 // Prompt the user to enter the task name
//                 frappe.prompt([
//                     {
//                         label: 'Task Name',
//                         fieldname: 'task_name',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     }
//                 ], (values) => {
//                     // Get the task name and start time
//                     const task_name = values.task_name;
//                     const start_time = frappe.datetime.now_datetime();
    
//                     // Add a new entry to the child table Timesheet Details
//                     frm.add_child('tasks_worked_on', {
//                         task_name: task_name,
//                         clock_in: start_time
//                     });
    
//                     // Refresh the Timesheet Details field to show the updated data
//                     frm.refresh_field('timesheet_details');
    
//                     // Show a message indicating that the task has started
//                     frappe.msgprint(`Started task: ${task_name} at ${clock_in}`);
//                 });
//             });
    
//             // Add Stop Time button
//             frm.add_custom_button(__('Stop Time'), function() {
//                 // Find the active task (one that doesn't have an end time)
//                 const active_task = frm.doc.timesheet_details.find(detail => !detail.end_time);
//                 if (active_task) {
//                     // Capture the current stop time
//                     const stop_time = frappe.datetime.now_datetime();
    
//                     // Update the Timesheet Details child table with the stop time
//                     frappe.model.set_value('Timesheet Details', active_task.name, 'end_time', stop_time);
    
//                     // Refresh the field to reflect the stop time
//                     frm.refresh_field('timesheet_details');
    
//                     // Show a message indicating that the task has stopped
//                     frappe.msgprint(`Stopped task: ${active_task.task} at ${stop_time}`);
//                 } else {
//                     // If there are no active tasks, show an error message
//                     frappe.msgprint('No active task to stop.');
//                 }
//             });
//         }
        
//     }
// });
// frappe.ui.form.on('Timesheet', {
//     // Add Start Time button
//     refresh: function(frm) {
//         if (!frm.is_new()) {
//             // Add Start Time button
//             frm.add_custom_button(__('Start Time'), function() {
//                 // Prompt the user to enter the task name
//                 frappe.prompt([
//                     {
//                         label: 'Task Name',
//                         fieldname: 'task_name',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     }
//                 ], (values) => {
//                     // Get the task name and start time
//                     const task_name = values.task_name;
//                     const start_time = frappe.datetime.now_datetime();

//                     // Add a new entry to the child table Timesheet Details
//                     frm.add_child('tasks_worked_on', {
//                         task_name: task_name,
//                         clock_in: start_time
//                     });

//                     // Refresh the Timesheet Details field to show the updated data
//                     frm.refresh_field('tasks_worked_on');

//                     // Show a message indicating that the task has started
//                     frappe.msgprint(`Started task: ${task_name} at ${start_time}`);
//                 });
//             });

//             // Add Stop Time button
//             frm.add_custom_button(__('Stop Time'), function() {
//                 // Find the active task (one that doesn't have an end time)
//                 const active_task = frm.doc.tasks_worked_on.find(detail => !detail.clock_out_time);
//                 if (active_task) {
//                     // Capture the current stop time (for the UI)
//                     const stop_time = frappe.datetime.now_datetime();

//                     // Show a message indicating that the task has stopped (UI side)
//                     frappe.msgprint(`Stopped task: ${active_task.task_name} at ${stop_time}`);
//                 } else {
//                     // If there are no active tasks, show an error message
//                     frappe.msgprint('No active task to stop.');
//                 }
//             });

        
//         }
//     }
// });
// frappe.ui.form.on('Timesheet', {
//     // Add Start Time button
//     refresh: function(frm) {
//         if (!frm.is_new()) {
//             // Add Start Time button
//             frm.add_custom_button(__('Start Time'), function() {
//                 // Prompt the user to enter the task name
//                 frappe.prompt([
//                     {
//                         label: 'Task Name',
//                         fieldname: 'task_name',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     }
//                 ], (values) => {
//                     // Get the task name and start time
//                     const task_name = values.task_name;
//                     const start_time = frappe.datetime.now_datetime();

//                     // Add a new entry to the child table Timesheet Details
//                     frm.add_child('tasks_worked_on', {
//                         task_name: task_name,
//                         clock_in: start_time
//                     });

//                     // Refresh the Timesheet Details field to show the updated data
//                     frm.refresh_field('tasks_worked_on');

//                     // Show a message indicating that the task has started
//                     frappe.msgprint(`Started task: ${task_name} at ${clock_in}`);
//                 });
//             });

//             // Add Stop Time button
//             frm.add_custom_button(__('Stop Time'), function() {
//                 // Find the active task (one that doesn't have an end time)
//                 const active_task = frm.doc.tasks_worked_on.find(detail => !detail.clock_out);

//                 if (active_task) {
//                     // Capture the current stop time (for the UI)
//                     const stop_time = frappe.datetime.now_datetime();

//                     // Update the child table with the stop time (clock_out field)
//                     frappe.model.set_value('Timesheet Details', active_task.name, 'clock_out', stop_time);

//                     // Refresh the Timesheet Details field to show the updated data
//                     frm.refresh_field('tasks_worked_on');

//                     // Show a message indicating that the task has stopped and clock-out time
//                     frappe.msgprint(`Stopped task: ${active_task.task_name} at ${stop_time}`);
//                 } else {
//                     // If there are no active tasks, show an error message
//                     frappe.msgprint('No active task to stop.');
//                 }
//             });
//         }
//     }
// });
// frappe.ui.form.on('Timesheet', {
//     // Add Start Time button
//     refresh: function(frm) {
//         if (!frm.is_new()) {
//             // Add Start Time button
//             frm.add_custom_button(__('Start Time'), function() {
//                 // Prompt the user to enter the task name
//                 frappe.prompt([
//                     {
//                         label: 'Task Name',
//                         fieldname: 'task_name',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     }
//                 ], (values) => {
//                     // Get the task name and start time
//                     const task_name = values.task_name;
//                     const start_time = frappe.datetime.now_datetime();

//                     // Add a new entry to the child table Timesheet Details
//                     let child = frm.add_child('tasks_worked_on', {
//                         task_name: task_name,
//                         clock_in: start_time
//                     });

//                     // Refresh the Timesheet Details field to show the updated data
//                     frm.refresh_field('tasks_worked_on');

//                     // Show a message indicating that the task has started
//                     frappe.msgprint(`Started task: ${task_name} at ${clock_in}`);
//                 });
//             });

//             // Add Stop Time button
//             frm.add_custom_button(__('Stop Time'), function() {
//                 // Find the active task (one that doesn't have an end time)
//                 const active_task = frm.doc.tasks_worked_on.find(detail => !detail.clock_out);

//                 if (active_task) {
//                     // Capture the current stop time
//                     const stop_time = frappe.datetime.now_datetime();

//                     // Calculate the total hours by finding the difference between stop_time and clock_in
//                     const clock_in = active_task.clock_in;
//                     const start_time_obj = moment(clock_in); // Use Moment.js to parse the start time
//                     const end_time_obj = moment(stop_time); // Use Moment.js to parse the stop time
                    
//                     // Calculate the difference in hours
//                     const duration = moment.duration(end_time_obj.diff(start_time_obj));
//                     const total_hours = duration.asHours(); // Get total hours as a floating point number

//                     // Update the child table with the stop time and total_hours
//                     frappe.model.set_value('Timesheet Details', active_task.name, 'clock_out', stop_time);
//                     frappe.model.set_value('Timesheet Details', active_task.name, 'total_hours', total_hours);

//                     // Refresh the Timesheet Details field to show the updated data
//                     frm.refresh_field('tasks_worked_on');

//                     // Show a message indicating that the task has stopped, clock-out time, and total hours worked
//                     frappe.msgprint(`Stopped task: ${active_task.task_name} at ${stop_time}. Total hours worked: ${total_hours}`);
//                 } else {
//                     // If there are no active tasks, show an error message
//                     frappe.msgprint('No active task to stop.');
//                 }
//             });
//         }
//     }
// });


frappe.ui.form.on('Timesheet', {
    // Add Start Time button
    refresh: function(frm) {
        if (!frm.is_new()) {
            // Add Start Time button
            frm.add_custom_button(__('Start Time'), function() {
                // Check if there is an active task (one without clock_out)
                const active_task = frm.doc.tasks_worked_on.find(detail => !detail.clock_out);
                if (active_task) {
                    // If there's an active task, show an error message
                    frappe.msgprint('Please stop the active task before starting a new one.');
                    return; // Prevent starting a new task
                }

                // Prompt the user to enter the task name
                frappe.prompt([
                    {
                        label: 'Task Name',
                        fieldname: 'task_name',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ], (values) => {
                    // Get the task name and start time
                    const task_name = values.task_name;
                    const start_time = frappe.datetime.now_datetime();

                    // Add a new entry to the child table Timesheet Details
                    let child = frm.add_child('tasks_worked_on', {
                        task_name: task_name,
                        clock_in: start_time
                    });

                    // Refresh the Timesheet Details field to show the updated data
                    frm.refresh_field('tasks_worked_on');

                    // Show a message indicating that the task has started
                    frappe.msgprint(`Started task: ${task_name} at ${clock_in}`);
                });
            });


                        // Add Stop Time button
                frm.add_custom_button(__('Stop Time'), function() {
                    // Find the active task (one that doesn't have an end time)
                    const active_task = frm.doc.tasks_worked_on.find(detail => !detail.clock_out);

                    if (active_task) {
                        // Capture the current stop time
                        const stop_time = frappe.datetime.now_datetime();

                        // Calculate the total hours by finding the difference between stop_time and clock_in
                        const clock_in = active_task.clock_in;
                        const start_time_obj = moment(clock_in); // Use Moment.js to parse the start time
                        const end_time_obj = moment(stop_time); // Use Moment.js to parse the stop time
                        
                        // Calculate the difference in hours
                        const duration = moment.duration(end_time_obj.diff(start_time_obj));
                        const total_hours = duration.asHours(); // Get total hours as a floating point number

                        // Update the child table with the stop time and total_hours
                        frappe.model.set_value('Timesheet Details', active_task.name, 'clock_out', stop_time);
                        frappe.model.set_value('Timesheet Details', active_task.name, 'total_hours', total_hours);

                        // Calculate the total_hours for all tasks worked on
                        const parent_total_hours = frm.doc.tasks_worked_on.reduce((sum, task) => {
                            return sum + (task.total_hours || 0);
                        }, 0);
                        frappe.msgprint(`total_hoursssss: ${parent_total_hours}`);

                        // Update the parent total_hours field with the sum of total hours from all tasks
                        frappe.model.set_value(frm.doctype, frm.docname, 'total_hours', parent_total_hours);

                        // Refresh the Timesheet Details field to show the updated data
                        frm.refresh_field('tasks_worked_on');
                        frm.refresh_field('total_hours'); // Refresh the parent total_hours field

                        // Show a message indicating that the task has stopped, clock-out time, and total hours worked
                        frappe.msgprint(`Stopped task: ${active_task.task_name} at ${stop_time}. Total hours worked: ${total_hours}`);
                    } else {
                        // If there are no active tasks, show an error message
                        frappe.msgprint('No active task to stop.');
                    }
                });

            // // Add Stop Time button
            // frm.add_custom_button(__('Stop Time'), function() {
            //     // Find the active task (one that doesn't have an end time)
            //     const active_task = frm.doc.tasks_worked_on.find(detail => !detail.clock_out);

            //     if (active_task) {
            //         // Capture the current stop time
            //         const stop_time = frappe.datetime.now_datetime();

            //         // Calculate the total hours by finding the difference between stop_time and clock_in
            //         const clock_in = active_task.clock_in;
            //         const start_time_obj = moment(clock_in); // Use Moment.js to parse the start time
            //         const end_time_obj = moment(stop_time); // Use Moment.js to parse the stop time
                    
            //         // Calculate the difference in hours
            //         const duration = moment.duration(end_time_obj.diff(start_time_obj));
            //         const total_hours = duration.asHours(); // Get total hours as a floating point number

            //         // Update the child table with the stop time and total_hours
            //         frappe.model.set_value('Timesheet Details', active_task.name, 'clock_out', stop_time);
            //         frappe.model.set_value('Timesheet Details', active_task.name, 'total_hours', total_hours);

            //         // Refresh the Timesheet Details field to show the updated data
            //         frm.refresh_field('tasks_worked_on');

            //         // Show a message indicating that the task has stopped, clock-out time, and total hours worked
            //         frappe.msgprint(`Stopped task: ${active_task.task_name} at ${stop_time}. Total hours worked: ${total_hours}`);
            //     } else {
            //         // If there are no active tasks, show an error message
            //         frappe.msgprint('No active task to stop.');
            //     }
            // });
        }
    }
});
