

# CIS-117 Lab 3
# Task - Reads country information from a CSV file separating countries into individual CSV files by region.
# Group 69 Michael Strus, My Dad

import csv

def main():
    try:
        regions = {}

        with open("country_full.csv", "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                country = row["name"]
                region = row["region"]

                if not country or not region:
                    continue

                if region not in regions:
                    regions[region] = []

                regions[region].append([country, region])

        for region, countries in regions.items():
            filename = region + ".csv"

            with open(filename, "w", newline="", encoding="utf-8") as output:
                writer = csv.writer(output)
                writer.writerow(["name", "region"])
                writer.writerows(countries)

            print("Imported", filename)

        print("Heck Yeah Im Done!")

    except FileNotFoundError:
        print("Error: CSV file invalid.")

    except PermissionError:
        print("Error: Access Denied.")

    except IOError as error:
        print("File Error:", error)


if __name__ == "__main__":
    main()
