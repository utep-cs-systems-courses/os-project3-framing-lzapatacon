import os

def archive_file(file_name):

    with open(file_name, "rb") as file:

        byte_array = bytearray()

        byte_array += file.read()

        return byte_array

    def unarchive_file(file_name, "w") as f:
        os.chdir("database")
        with open(file_name, "w") as f:
            f.write(encoded_data)
        os.chdir("..")
        f.write(encoded_data)
