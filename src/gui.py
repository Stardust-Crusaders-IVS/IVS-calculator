""" @package gui
    @author: Tadeas Vintrlik <xvintr04>
    Documentation for main GUI package
"""
import gi
from gi.repository import Gtk
gi.require_version("Gtk", "3.0")


def main():
    """ @brief Main gui function
    Start the cycle for gui drawing
    """
    builder = Gtk.Builder()
    builder.add_from_file("../gui/prototype1.glade")
    window = builder.get_object("window1")
    window.show_all()
    Gtk.main()


if __name__ == "__main__":
    APP = Gtk.Application(application_id='Calc')
    APP.connect('activate', main)
    APP.run(None)
    main()
