import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


store = Gtk.TreeStore(str, int)



builder = Gtk.Builder()
builder.add_from_file("UIFiles/NTBSG_Main.glade")


class Handler:

    global builder
    
    def add_list():
        print("hello")

    def new_session_overlay(self, button):
        dialog = builder.get_object('new_session_overlay')
        response = dialog.run()
        print(response)
        dialog.hide()

    def open_session_overlay(self, button):
        dialog = builder.get_object('open_session_overlay')
        response = dialog.run()
        print(response)
        dialog.hide()

    def close_session(self, button):
        print("close session")

    def workspace_launcher_overlay(self, button):
        dialog = builder.get_object('workspace_launcher_overlay')
        response = dialog.run()
        print(response)
        dialog.hide()

    def terminal_overlay(self, button):
        if os.name == 'nt':
            os.system("start cmd")
        elif os.name == 'posix':
            os.system("x-terminal-emulator -e /bin/bash")

    def pcap_overlay(self, button):
        dialog = builder.get_object('pcap_overlay')
        response = dialog.run()
        print(response)
        dialog.hide()

    def stage_one_setup(self, button):
        multi_set_show(builder, True,
                            "filter_area",
                            "packet_area",
                            "field_area",
                            "new_tab")
        multi_set_show(builder, False,
                            "dependency_tab",
                            "template_tab",
                            "state_machine_area",
                            "equivalency_tab",
                            "generation_tab")

    def stage_two_setup(self, button):
        multi_set_show(builder, True,
                            "packet_area",
                            "field_area",
                            "dependency_tab",
                            "template_tab")
        multi_set_show(builder, False,
                            "filter_area",
                            "new_tab",
                            "state_machine_area",
                            "equivalency_tab",
                            "generation_tab")

    def stage_three_setup(self, button):
        multi_set_show(builder, True,
                           "state_machine_area",
                            "field_area",
                            "equivalency_tab")
        multi_set_show(builder, False,
                            "filter_area",
                            "field_area",
                            "new_tab",
                            "dependency_tab",
                            "template_tab",
                            "generation_tab",
                            "packet_area")

    def stage_four_setup(self, button):
        multi_set_show(builder, True,
                            "generation_tab")
        multi_set_show(builder, False,
                            "filter_area",
                            "template_tab",
                            "packet_area",
                            "field_area",
                            "new_tab",
                            "dependency_tab",
                            "template_tab",
                            "state_machine_area",
                            "equivalency_tab")

    def pdml_state_save_as(self, button):
        print("pdml_state_save_as")

    def pdml_state_save(self, button):
        print("pdml_state_save")

    def pdml_state_close(self, button):
        print("pdml_state_close")

    def pdml_state_delete(self, button):
        print("pdml_state_delete")

    def pdml_state_rename(self, button):
        print("pdml_state_rename")

    def filter_apply(self, button):
        print("filter_apply")

    def filter_clear(self, button):
        print("filter_apply")

    def filter_save(self, button):
        print("filter_apply")

    def saved_filter_apply(self, button):
        print("filter_apply")

    def packet_remove(self, button):
        print("packet_remove")

    def packet_clear(self, button):
        print("packet_clear")

    def tag_area_update(self, button):
        print("tag_area_update")

    def tag_area_cancel(self, button):
        print("tag_area_cancel")
        
    def close_filter_overlay(self, button):
        print("close filter overlay")
        dialog = builder.get_object('filter_overlay')
        gtk_close_window(dialog);
        
    def close_new_session(self, button):
        print("close new session overlay")
        dialog = builder.get_object('new_session_overlay')
        response = gtk_close_window(dialog)
        print(response)
        
    def add_session_tree(self, button):
        print("add session")
        tree = builder.get_object('session_view_tree')
        tree.add_column_name("Session A",0)


def multi_set_show(obj, show, *args):
    for arg in args:
        if show:
            obj.get_object(arg).show()
        else:
            obj.get_object(arg).hide()

tree_iter = store.append(["Fake thingy", 3])
print(tree_iter)
for row in store:
    #Print values of all columns
    print(row[:])
            
#main_window = builder.get_object("main_window")
#builder.connect_signals(Handler())
## multi_set_show(builder, False, 'label1', 'label2')
#main_window.show_all()
#multi_set_show(builder, True,
#                            "filter_area",
#                            "packet_area",
#                            "field_area",
#                            "new_tab")
#multi_set_show(builder, False,
#                            "dependency_tab",
#                            "template_tab",
#                            "state_machine_area",
#                            "equivalency_tab",
#                            "generation_tab")
# multi_set_show(builder, False,
#                     "filter_area",
#                     "packet_area",
#                     "field_area_section",
#                     "new_tab",
#                     "dependency_tab",
#                     "template_tab",
#                     # "state_machine_area",
#                     "equivalency_tab",
#                     "generation_tab")


Gtk.main()













