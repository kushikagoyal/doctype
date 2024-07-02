frappe.ui.form.on('Dialog', {
    refresh: function(frm) {
        // Bind click event to the button field
        frm.fields_dict.input_values.$input.on('click', function() {
            open_task_input_dialog(frm);
        });
    }
});

function open_task_input_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Enter Task Details',
        fields: [
            {
                label: 'Task Name',
                fieldname: 'task_name',
                fieldtype: 'Data'
            },
            {
                label: 'Task ID',
                fieldname: 'task_id',
                fieldtype: 'Data'
            },
            {
                label: 'Time to complete in hours',
                fieldname: 'time_to_complete_in_hours',
                fieldtype: 'Int'
            }
        ],
        primary_action_label: 'Add Task',
        primary_action(values) {
            add_task_to_child_table(values, frm);
            d.hide();
        }
    });

    d.show();
}

function add_task_to_child_table(values, frm) {
    let child = frm.add_child('tasks'); // Replace 'tasks' with your actual child table fieldname
    child.task_name = values.task_name;
    child.task_id = values.task_id;
    child.time_to_complete_in_hours = values.time_to_complete_in_hours;
    frm.refresh_field('tasks'); // Replace 'tasks' with your actual child table fieldname
    frappe.msgprint('Task Added Successfully');
}
