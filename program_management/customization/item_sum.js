frappe.ui.form.on('Item', {
    refresh: function(frm) {
        calculate_total_cost_for_all_rows(frm);
    },
    onload: function(frm) {
        calculate_total_cost_for_all_rows(frm);
    }
});

frappe.ui.form.on('Item Child', {
    quantity: function(frm, cdt, cdn) {
        calculate_total_cost(frm, cdt, cdn);
    },
    unit_cost: function(frm, cdt, cdn) {
        calculate_total_cost(frm, cdt, cdn);
    }
});

function calculate_total_cost(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    
    if (child.quantity && child.unit_cost) {
        let total_cost = child.quantity * child.unit_cost;
        frappe.model.set_value(cdt, cdn, 'total_cost', total_cost);
    }
}

function calculate_total_cost_for_all_rows(frm) {
    (frm.doc.custom_item_child || []).forEach(function(child) {
        if (child.quantity && child.unit_cost) {
            let total_cost = child.quantity * child.unit_cost;
            frappe.model.set_value(child.doctype, child.name, 'total_cost', total_cost);
        }
    });
}
