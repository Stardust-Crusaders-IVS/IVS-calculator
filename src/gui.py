""" @package gui
@author Tadeas Vintrlik <xvintr04>

Documentation for main GUI package
"""
from gi.repository import Gtk, Gdk, GdkPixbuf, Pango


def main():
    """ @brief Main gui function
    Start the cycle for gui drawing
    """
    builder = Gtk.Builder()
    builder.add_from_file("../gui/prototype1.glade")
    window_main = builder.get_object("window1")
    window_main.set_title("Kalkulačka")
    icon = GdkPixbuf.Pixbuf.new_from_file("../gui/icon.jpeg")
    window_main.set_icon(icon)
    change_fonts(builder, "")
    connect_signals(builder)
    window_main.show_all()
    builder.get_object("invalid").hide()
    Gtk.main()


def user_input(self, entry, builder):
    """ @brief inputs the desired symbol into the entry
    @param self the caller of the function
    @param entry the entry where to add the new symbol
    @param builder builder class for making gui from glade
    """
    label = self.get_label()
    if "√" in label:
        entry.set_text(label + entry.get_text())
    elif label == "Fib":
        entry.set_text(label + "(" + entry.get_text() + ")")
    else:
        entry.set_text(entry.get_text() + label)

    # if nth root move cursor to the begining for easier editing
    if label == "n√":
        entry.set_position(0)
    else:
        entry.set_position(len(entry.get_text()))

    validate_entry(entry, builder)


def user_result(self, entry):
    """ @brief calculates the result from the entry
    @param *self the caller of the function
    @param entry the entry where to show the result
    """
    del self  # Unused for now
    entry.set_text("This should show the result")
    entry.set_position(len(entry.get_text()))


def clear(self, entry, builder):
    """ @brief clears the entry
    @param *self the caller of the function
    @param entry the entry which to clear
    """
    del self  # Unused for now
    entry.set_text("")
    validate_entry(entry, builder)


def change_fonts(builder, font_param):
    """ @brief change fonts of all elements
    @param builder builder class for making gui from glade
    """
    if not font_param:
        font_param = 'Sans Bold 18'
    font = Pango.FontDescription(font_param)
    change_font_grid(builder, 'numbers', font, 4, 3)
    change_font_grid(builder, 'operators', font, 5, 2)
    entry = builder.get_object('entry')
    entry.modify_font(font)
    entry.set_alignment(1)


def on_key_pressed(widget, event, entry, builder):
    """ @brief handler for key-press-event
    @param widget widget active when key press occured
    @param event type of event that occured
    @param entry entry filed to modify
    @param builder builder class for making gui from glade
    """
    validate_entry(entry, builder)
    if event.keyval == Gdk.KEY_Return or chr(event.keyval) == "=":
        user_result(widget, entry)


def validate_entry(entry, builder):
    """ @brief checks if the entry is valid
    @param self the caller of the function
    @param entry the entry where to add the new symbol
    @param builder builder class for making gui from glade
    """
    # TODO: The condition should test if input can be calculated
    if len(entry.get_text()) > 3:
        builder.get_object("invalid").show()
    else:
        builder.get_object("invalid").hide()


def connect_signals(builder):
    """ @brief connect signals to all buttons
    @param builder builder class for making gui from glade
    """
    connect_signal_grid(builder, 'numbers', 4, 3)
    connect_signal_grid(builder, 'operators', 5, 2)
    entry = builder.get_object('entry')
    builder.get_object('equals').connect("clicked", user_result, entry)
    builder.get_object('clr').connect("clicked", clear, entry, builder)
    window = builder.get_object("window1")
    window.connect("key-press-event", on_key_pressed, entry, builder)
    window.connect("destroy", Gtk.main_quit)
    font_change = builder.get_object('font_change')
    font_change.connect("activate", font_select, builder)
    about = builder.get_object('about')
    about.connect("activate", about_show)
    exit_button = builder.get_object('exit')
    exit_button.connect("activate", Gtk.main_quit)


def font_select(self, builder):
    """ @brief open font select window
    @param self the caller of the function
    @param builder builder class for making gui from glade
    """
    del self
    dialog = Gtk.FontSelectionDialog("Prosím Vyberte Font")
    response = dialog.run()
    if response == -5:
        change_fonts(builder, dialog.get_font_name())
        dialog.close()
    else:
        dialog.close()


def about_show(self):
    """ @brief open about window
    @param self the caller of the function
    @param builder builder class for making gui from glade
    """
    del self
    about = Gtk.AboutDialog("O aplikaci")
    icon = GdkPixbuf.Pixbuf.new_from_file("../gui/icon.jpeg")
    about.set_logo(icon)
    about.set_comments("Jednoduchá aplikace kalkulačky.")
    about.set_version("1.0")
    about.set_program_name("Kalkulačka")
    about.set_license("Program je pod GNU GPL v3 licencí.\n"
                       "Kompletní znění licence je součástí zdrojových souborů, "
                       "popřípadě zde:\n"
                       "https://www.gnu.org/licenses/gpl-3.0.en.html")
    about.set_authors(["Vojtěch Bůbela",
                        "Vojtěch Fiala",
                        "Tadeáš Vintrlík"])
    response = about.run()
    if response == -4:
        about.close()


def connect_signal_grid(builder, grid_name, rows, columns):
    """ @brief connect all buttons in grid to callbacks
    @param builder builder class for making gui from glade
    @param grid_name name of the grid to use
    @param rows number of rows of the grid
    @param columns number of coulmns of the grid
    """
    exceptions = ["=", "REM", "CLR"]
    entry = builder.get_object("entry")
    grid = builder.get_object(grid_name)
    for i in range(0, columns):
        for j in range(0, rows):
            button = grid.get_child_at(i, j)
            if button.get_label() in exceptions:
                continue
            button.connect("clicked", user_input, entry, builder)


def change_font_grid(builder, grid_name, font, rows, columns):
    """ @brief change fonts in a grid
    Change fonts of all children in the GtkGrid element
    @param builder builder class for making gui from glade
    @param grid_name name of the grid to use
    @param font font to change it to
    @param rows number of rows of the grid
    @param columns number of coulmns of the grid
    """
    grid = builder.get_object(grid_name)
    for i in range(0, columns):
        for j in range(0, rows):
            button = grid.get_child_at(i, j)
            button.modify_font(font)


if __name__ == "__main__":
    APP = Gtk.Application(application_id='Calc')
    APP.connect('activate', main)
    APP.run(None)
    main()
