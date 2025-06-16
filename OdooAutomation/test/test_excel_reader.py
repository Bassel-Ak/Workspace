from excel_io.excel_reader import ExcelReader

def test_load_and_get_credit_notes():
    # Path to your sample Excel sheet
    file_path = "data/credit_notes_test.xlsx"

    reader = ExcelReader(file_path)
    reader.load()  # Load and validate headers

    credit_notes = reader.get_credit_notes()  # Extract credit notes

    print(f"Extracted credit notes: {credit_notes}")
    assert len(credit_notes) > 0, "Credit notes list should not be empty"

if __name__ == "__main__":
    test_load_and_get_credit_notes()
