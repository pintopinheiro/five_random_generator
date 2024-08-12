"""Main Process."""

import pandas as pd
from generate_numbers import generate_numbers


if __name__ == "__main__":
    while True:
        numbers = generate_numbers()
        df = pd.DataFrame(
            numbers,
            columns=["Random Numbers"]
        )

        # Save to an Excel file
        df.to_excel(
            "random_numbers.xlsx",
            index=False
        )
