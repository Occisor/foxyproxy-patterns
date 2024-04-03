### VERSION - 0.3 ###

import os
import textwrap

# Get the current directory
current_directory = os.getcwd()

# Get a list of all files in the current directory
files_in_directory = os.listdir(current_directory)

# Filter out directories and keep only files without extension
files_to_process = [file for file in files_in_directory if os.path.isfile(file) and not os.path.splitext(file)[1]]

# Exclude the script file from the list
script_file = os.path.basename(__file__)
files_to_process = [file for file in files_to_process if file != script_file]

# Initialize an empty list to store processed words
words = []

# Process each file in the directory
for file_name in files_to_process:
    with open(file_name, "r") as f:
        words.clear()
        # Read the lines from the file and add them to the words list
        words.extend([line.strip() for line in f.readlines()])

        # Name of the output file with a .json extension
        output_file = f"{os.path.splitext(file_name)[0]}.json"

        # Template for creating a JSON object
        template_pre = textwrap.dedent("""\
        {
          "include": "include",
          "type": "wildcard",
          "title": "%s",
          "pattern": "*://*.%%s",
          "active": true
        }""" % file_name)
        template = textwrap.indent(template_pre, '  ')

        # Writing JSON objects to the file
        with open(output_file, "w") as f_out:
            f_out.write("[\n")
            for i, word in enumerate(words):
                f_out.write(template % word)
                if i < len(words) - 1:
                    f_out.write(",\n")
            f_out.write("\n]")
