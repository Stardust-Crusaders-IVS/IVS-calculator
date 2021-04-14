""" @package gui
    @author: Tadeas Vintrlik <xvintr04>
    Documentation for main GUI package
"""
import gi
from gi.repository import Gtk
from gi.repository import Pango
gi.require_version("Gtk", "3.0")


def main():
    """ @brief Main gui function
        Start the cycle for gui drawing
    """
    builder = Gtk.Builder()
    builder.add_from_file("../gui/prototype1.glade")
    window = builder.get_object("window1")
    change_fonts(builder)
    window.show_all()
    Gtk.main()


def user_input(self, entry):
    """ @brief inputs the desired symbol into the entry
        @param self the caller of the function
        @param entry the entry where to add the new symbol
    """
    entry.set_text(entry.get_text() + self.get_label())


def user_result(self, entry):
    """ @brief calculates the result from the entry
        @param *self the caller of the function
        @param entry the entry where to show the result
    """
    del self  # Unused for now
    entry.set_text("This should show the result")


def rem_char(self, entry):
    """ @brief removes last character from entry
        @param *self the caller of the function
        @param entry the entry where to remove the character
    """
    del self  # Unused for now
    text = entry.get_text()
    entry.set_text(text[:-1])


def clear(self, entry):
    """ @brief clears the entry
        @param *self the caller of the function
        @param entry the entry which to clear
    """
    del self  # Unused for now
    entry.set_text("")


def change_fonts(builder):
    """ @brief change fonts of all elements
        @param builder builder class for making gui from glade
    """
    font = Pango.FontDescription('Sans Bold 18')
    change_font_grid(builder, 'numbers', font, 4, 3)
    change_font_grid(builder, 'operators', font, 4, 2)
    entry = builder.get_object('entry')
    entry.modify_font(font)
    connect_signal_grid(builder, 'numbers', 4, 3)
    connect_signal_grid(builder, 'operators', 5, 2)
    builder.get_object('equals').connect("clicked", user_result, entry)
    builder.get_object('rem').connect("clicked", rem_char, entry)
    builder.get_object('clr').connect("clicked", clear, entry)


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
            button.connect("clicked", user_input, entry)


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
