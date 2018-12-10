import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("UIFiles/NTBSG_Main.glade")

main_window = builder.get_object("main_window")
main_window.show_all()


Gtk.main()














