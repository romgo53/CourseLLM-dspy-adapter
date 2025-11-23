# import os
# from typing import List, Dict

# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaIoBaseDownload
# import io

# SCOPES = [
#     "https://www.googleapis.com/auth/drive.readonly",
# ]

# def _get_drive_service():
#     keyfile = os.environ.get("GOOGLE_SERVICE_ACCOUNT_FILE")
#     if not keyfile:
#         raise RuntimeError("GOOGLE_SERVICE_ACCOUNT_FILE environment variable not set")
#     creds = service_account.Credentials.from_service_account_file(keyfile, scopes=SCOPES)
#     service = build("drive", "v3", credentials=creds, cache_discovery=False)
#     return service

# def fetch_markdown_files(file_ids: List[str]) -> Dict[str, str]:
#     """Download files by id. Returns dict of id->utf-8 content for .md files.

#     If a file cannot be fetched, it's omitted from the result.
#     """
#     service = _get_drive_service()
#     out = {}
#     for fid in file_ids:
#         try:
#             # Try to export as text if it's a Google Doc, otherwise get media
#             # First, get metadata to inspect mimeType
#             meta = service.files().get(fileId=fid, fields="id,name,mimeType").execute()
#             mime = meta.get("mimeType", "")
#             if mime == "application/vnd.google-apps.document":
#                 # export as plain text
#                 request = service.files().export_media(fileId=fid, mimeType="text/plain")
#                 fh = io.BytesIO()
#                 downloader = MediaIoBaseDownload(fh, request)
#                 done = False
#                 while not done:
#                     status, done = downloader.next_chunk()
#                 content = fh.getvalue().decode("utf-8")
#             else:
#                 # Regular file (like .md) - use media().get
#                 request = service.files().get_media(fileId=fid)
#                 fh = io.BytesIO()
#                 downloader = MediaIoBaseDownload(fh, request)
#                 done = False
#                 while not done:
#                     status, done = downloader.next_chunk()
#                 content = fh.getvalue().decode("utf-8")
#             out[fid] = content
#         except Exception:
#             # skip failures silently for now
#             continue
#     return out
