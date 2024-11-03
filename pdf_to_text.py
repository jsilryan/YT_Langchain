from imports import *
from directory import * 

def remove_file_with_retry(file_path, retries=5, delay=1):
    for attempt in range(retries):
        try:
            os.remove(file_path)
            print(f"Successfully deleted: {file_path}")
            return True
        except PermissionError:
            print(f"PermissionError: {file_path} is in use. Retrying...")
            time.sleep(delay)
    print(f"Failed to delete: {file_path} after {retries} attempts.")
    return False

def remove_directory_with_retry(directory_path, retries=5, delay=1):
    for attempt in range(retries):
        try:
            shutil.rmtree(directory_path, onerror=remove_error)
            print(f"Successfully deleted directory: {directory_path}")
            return True
        except Exception as e:
            print(f"Error deleting directory: {e}. Retrying...")
            time.sleep(delay)
    print(f"Failed to delete directory: {directory_path} after {retries} attempts.")
    return False

def remove_error(func, path, exc_info):
    """Handle errors during rmtree."""
    if func == os.unlink:  # If it's a file
        remove_file_with_retry(path)
    elif func == os.rmdir:  # If it's a directory
        print(f"Directory still in use, cannot delete: {path}")

def convert_PDF_to_text(reader, image_path):
    # Create a folder to store the images
    image_folder = construct_folder_path(desktop_folder, "PDF_IMAGES")

    # Convert PDF to images and save them to the folder
    images = convert_from_path(image_path)
    image_files = []

    for i, image in enumerate(images):
        image_file = f"{image_folder}/page_{i}.png"
        image.save(image_file, "PNG")
        image_files.append(image_file)

    # Initialize a list to hold the OCR results and the extracted words
    all_texts = []

    # Iterate over saved images and extract text using the file name
    for image_file in image_files:
      ocr_result = reader.readtext(image_file)  # Extend to avoid nested lists

      words = []
      count = 0
      # Collect words from the OCR results
      for result in ocr_result:
          bbox, word, confidence = result  # Unpack the tuple
          if count < 3:
              print(result)
          words.append(word)
          count += 1

      # Join the list of words into a single string
      text = " ".join(words)
      all_texts.append(text)

    # Delete the images after processing
    remove_directory_with_retry(image_folder)

    # Return the extracted text
    all_texts_joined = " ".join(all_texts)
    return all_texts_joined
    