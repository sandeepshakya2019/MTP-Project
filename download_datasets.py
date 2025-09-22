import gdown
import zipfile
import os

# Correct direct download link
drive_url = "https://drive.google.com/uc?id=1fJshjFiK0LNfrLHbGPmhYm9b8WzUKDtY"
output_zip = "okutama_action.zip"

# Download from Google Drive
print("Downloading dataset...")
gdown.download(drive_url, output_zip, quiet=False)

# Extract if it's really a zip
if zipfile.is_zipfile(output_zip):
    print("Extracting...")
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall("okutama_action")
    os.remove(output_zip)
    print("Done! Files are extracted to 'okutama_action' folder.")
else:
    print("Downloaded file is not a zip archive. Maybe it’s already extracted or in another format.")
