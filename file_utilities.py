import pymupdf4llm
import os


def read_file(filepath: str) -> str:
    """
    This function takes a filepath as input and outputs the read text.
    Currently, accepts .txt and .pdf files.

    Args:
        filepath: The relative path to the input file.

    Returns:
        The read text from the file, or an empty string if the file cannot be read.
    """
    file_ext = os.path.splitext(filepath)[-1].lower()
    if file_ext == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    elif file_ext == '.pdf':
        text = pymupdf4llm.to_markdown(filepath)
    else:
        print("Filetype not supported.")
        return ""
    return text if text else ""
