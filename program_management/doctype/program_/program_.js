// Copyright (c) 2024, Kushika and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Program_", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Program_', {
    refresh: function(frm) {
        // Add New Item Button
        frm.add_custom_button(__('Add New Item'), function() {
            open_add_new_item_dialog(frm);
        }, __('Actions'));

        // Update Item Button
        frm.add_custom_button(__('Update Item'), function() {
            open_update_item_dialog(frm);
        }, __('Actions'));
    }
});

function open_add_new_item_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: __('Add New Item'),
        fields: [
            {
                fieldname: 'item_group',
                label: __('Item Group'),
                fieldtype: 'Link',
                options: 'Item Group',
                reqd: 1,
                change: function() {
                    // Filter Item field based on selected Item Group
                    d.get_field('item').get_query = function() {
                        return {
                            filters: {
                                'item_group': d.get_value('item_group')
                            }
                        };
                    };
                }
            },
            {
                fieldname: 'item',
                label: __('Item'),
                fieldtype: 'Link',
                options: 'Item',
                reqd: 1,
                change: function() {
                    // Fetch Item Name based on selected Item
                    frappe.db.get_value('Item', d.get_value('item'), 'item_name', function(value) {
                        d.set_value('item_name', value.item_name);
                    });
                }
            },
            {
                fieldname: 'item_name',
                label: __('Item Name'),
                fieldtype: 'Data',
                read_only: 1
            },
            {
                fieldname: 'quantity',
                label: __('Quantity'),
                fieldtype: 'Int',
                reqd: 1
            },
            {
                fieldname: 'finish',
                label: __('Finish'),
                fieldtype: 'Check'
            },
            {
                fieldname: 'description',
                label: __('Description'),
                fieldtype: 'Small Text'
            }
        ],
        primary_action_label: __('Add Item'),
        primary_action(values) {
            // Add the new item to the Program Items table
            let new_item = frm.add_child('program_items', {
                item_group: values.item_group,
                item: values.item,
                item_name: values.item_name,
                quantity: values.quantity,
                finish: values.finish,
                description: values.description
            });
            frm.refresh_field('program_items');
            d.hide();
        }
    });

    d.show();
}

function open_update_item_dialog(frm) {
    let items = frm.doc.program_items.filter(item => !item.finish);

    let fields = [
        {
            fieldname: 'program_item',
            label: __('Program Item'),
            fieldtype: 'Select',
            options: items.map(item => ({
                value: item.name,
                label: `${item.item_name} (${item.item})`
            })),
            reqd: 1,
            change: function() {
                let selected_item = items.find(item => item.name === d.get_value('program_item'));
                d.set_value('quantity', selected_item.quantity);
                d.set_value('finish', selected_item.finish);
                d.set_value('description', selected_item.description);
            }
        },
        {
            fieldname: 'quantity',
            label: __('Quantity'),
            fieldtype: 'Int',
            reqd: 1
        },
        {
            fieldname: 'finish',
            label: __('Finish'),
            fieldtype: 'Check'
        },
        {
            fieldname: 'description',
            label: __('Description'),
            fieldtype: 'Small Text'
        }
    ];

    let d = new frappe.ui.Dialog({
        title: __('Update Item'),
        fields: fields,
        primary_action_label: __('Update Item'),
        primary_action(values) {
            // Update the selected item in the Program Items table
            let selected_item = frm.doc.program_items.find(item => item.name === values.program_item);
            selected_item.quantity = values.quantity;
            selected_item.finish = values.finish;
            selected_item.description = values.description;
            frm.refresh_field('program_items');
            d.hide();
        }
    });

    d.show();
}
