import os

import pandas as pd

from colorama import init,  Fore, Back


# Initialize colorama

init(autoreset=True)


error = False


class CustomError(Exception):

    def __init__(self, message):

        self.message = message


def print_error(message):

    print("\n" + Fore.RED + " " + message + "\n")

    error = True


def print_success(message):

    print("\n" + Fore.GREEN + " " + message + "\n")


def print_warning(message):

    print("\n" + Fore.YELLOW + " " + message + "\n")


def print_info(message):

    print("\n" + Fore.CYAN + " " + message + "\n")


def clear_screen():

    print("\033[H\033[J")


def print_normal(message):

    print("\n" + message + "\n")


def confirm_pause():

    input("\nPress any key to continue...")


def help():

    print_info("Usage: main.py [OPTION]")

    print_normal("Options:")

    print_normal(
        "  -d, --description    Start the program in description mode")

    print_normal("  -h, --help           Show this help message")

    print_info("Learn more about the program at: https://github.com/tensor35/Python-Prompt-Generator-Script/blob/master/README.md")


def main(description_mode: bool = False):

    clear_screen()

    # print_info mode of operation

    if description_mode:

        print_info("Generating Prompts in Description Mode")

    else:

        print_info("Generating Prompts in Normal Mode")

    # Checking requirements

    try:

        with open("prompt.txt", "r", encoding="utf-8") as template:

            template_data = template.read()

            if template_data == "":

                #  throw error

                raise CustomError(
                    "Template file is empty. Please add some text to it.")

        with open("key-values.csv", "r", encoding="utf-8") as csv_values:

            csv_data = csv_values.read()

            if csv_data == "":

                raise CustomError(
                    "CSV file is empty. Please add some data to it.")

    except Exception as e:

        print_error("Error:", e, "")

        return

    print_success("Checking Requirements")

    # Checking for key-value pairs

    print_info("Generating Prompts")

    try:

        df = pd.read_csv("key-values.csv")

        [row_count, column_count] = df.shape

        columns = df.columns.values

        if columns[0] != "City" or columns[1] != "Title":

            raise CustomError(
                "Invalid CSV Headers. Please make sure the CSV file has the correct format.")

        if column_count != 2:

            raise CustomError(
                "Invalid CSV columns count. Please make sure the CSV file has the correct format.")

        print_info(f"{row_count} records found in CSV file. {row_count} prompts will be generated ")
        confirm_pause()

        # Generate prompts

        if description_mode:

            for index, row in df.iterrows():

                prompt = template_data.replace(
                    "**/City/**", row["City"]).replace("**/Title/**", "")

                if not os.path.exists("prompts"):

                    os.makedirs("prompts")

                with open(f"prompts/{row['City']}_description.txt", "w", encoding="utf-8") as prompt_file:

                    prompt_file.write(prompt)

                    print_success(
                        f"{index + 1} out of {row_count} generated successfully.")

        else:

            for index, row in df.iterrows():

                prompt = template_data.replace(
                    "**/City/**", row["City"]).replace("**/Title/**", row["Title"])

                if not os.path.exists("prompts"):

                    os.makedirs("prompts")

                with open(f"prompts/{row['City']}_{row['Title']}.txt", "w", encoding="utf-8") as prompt_file:

                    prompt_file.write(prompt)

                    print_success(
                        f"{index + 1} out of {row_count} generated successfully.")

    except Exception as e:

        print_error("Error: ", e, "")

        return

    print_success("Prompts Generated Successfully")

    print_info("Prompts are saved in the prompts folder.")
