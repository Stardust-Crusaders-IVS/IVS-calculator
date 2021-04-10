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


def change_fonts(builder):
    """ @brief change fonts of all elements
        @param builder builder class for making gui from glade
    """
    font = Pango.FontDescription('Sans Bold 18')
    # TODO: magical constants
    change_font_grid(builder, 'numbers', font, 4, 3)
    change_font_grid(builder, 'operators', font, 4, 2)
    builder.get_object('entry').modify_font(font)


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
