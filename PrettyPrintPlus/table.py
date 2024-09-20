class Table:
    def __init__(self, headers):
        """
        Initialize the table with headers (columns).
        """
        self.headers = headers
        self.rows = []
        self.column_widths = [len(header) for header in headers]

    def add_row(self, row):
        """
        Add a row to the table. Ensure it matches the number of headers.
        """
        if len(row) != len(self.headers):
            raise ValueError(f"Row length {len(row)} does not match the number of columns {len(self.headers)}")
        
        # Update column widths based on the new row data
        for i, cell in enumerate(row):
            self.column_widths[i] = max(self.column_widths[i], len(str(cell)))
        
        self.rows.append(row)

    def _create_border(self, left, mid, right, fill):
        """
        Create the top, middle, and bottom borders.
        """
        border = left
        for i, width in enumerate(self.column_widths):
            border += fill * (width + 2)  # +2 for padding
            if i < len(self.column_widths) - 1:
                border += mid
        border += right
        return border

    def _format_row(self, row, bold=False):
        """
        Format a single row with proper column widths and padding.
        Optionally make the row bold.
        """
        formatted_row = "│"
        for i, cell in enumerate(row):
            # Apply bold if needed
            cell_str = f"{str(cell).ljust(self.column_widths[i])}"
            if bold:
                cell_str = f"\033[1m{cell_str}\033[0m"  # ANSI escape for bold text
            formatted_row += f" {cell_str} │"
        return formatted_row

    def print(self):
        """
        Print the table with solid borders and formatted rows, including bold headers.
        """
        # Top border
        top_border = self._create_border('┌', '┬', '┐', '─')
        print(top_border)

        # Header row (with bold formatting)
        print(self._format_row(self.headers, bold=True))

        # Separator between header and rows
        middle_border = self._create_border('├', '┼', '┤', '─')
        print(middle_border)

        # Data rows
        for row in self.rows:
            print(self._format_row(row))

        # Bottom border
        bottom_border = self._create_border('└', '┴', '┘', '─')
        print(bottom_border)

    ### New Methods to Access Specific Rows, Columns, and Cells ###
    
    def get_row(self, index):
        """
        Access a specific row by its index.
        """
        if index < 0 or index >= len(self.rows):
            raise IndexError("Row index out of range.")
        return self.rows[index]

    def get_column(self, column_name):
        """
        Access a specific column by its header name.
        """
        if column_name not in self.headers:
            raise ValueError(f"Column '{column_name}' does not exist.")
        
        col_index = self.headers.index(column_name)
        return [row[col_index] for row in self.rows]

    def get_cell(self, row_index, column_name):
        """
        Access a specific cell by its row index and column name.
        """
        row = self.get_row(row_index)
        col_index = self.headers.index(column_name)
        return row[col_index]
    
    ### Optional: Update Rows, Columns, and Cells ###

    def update_cell(self, row_index, column_name, new_value):
        """
        Update a specific cell by its row index and column name.
        """
        row = self.get_row(row_index)
        col_index = self.headers.index(column_name)
        row[col_index] = new_value
        # Update column width to handle the new value's length
        self.column_widths[col_index] = max(self.column_widths[col_index], len(str(new_value)))

    def update_row(self, index, new_row):
        """
        Update a specific row by its index.
        """
        if len(new_row) != len(self.headers):
            raise ValueError(f"New row length does not match the number of columns {len(self.headers)}.")
        self.rows[index] = new_row
        # Update column widths
        for i, cell in enumerate(new_row):
            self.column_widths[i] = max(self.column_widths[i], len(str(cell)))

    def update_column(self, column_name, new_values):
        """
        Update an entire column by its header name.
        """
        if column_name not in self.headers:
            raise ValueError(f"Column '{column_name}' does not exist.")
        
        col_index = self.headers.index(column_name)
        
        if len(new_values) != len(self.rows):
            raise ValueError("Number of new values must match the number of rows in the table.")
        
        for i, new_value in enumerate(new_values):
            self.rows[i][col_index] = new_value
            # Update column width to handle the new value's length
            self.column_widths[col_index] = max(self.column_widths[col_index], len(str(new_value)))
    

table = Table(["Name", "Age", "City"])
table.add_row(["John Doe", 30, "New York"])
table.add_row(["Jane Smith", 25, "London"])
table.add_row(["Bob Johnson", 35, "Paris"])
table.add_row(["Alice Williams", 28, "Tokyo"])
table.print()

print("Row 1:", table.get_row(1))