# Listify

Turn photos of clothing into ready-to-post e-commerce listings: upload images, and a multimodal AI returns an SEO title, estimated price, colour, type, material and keywords.

<!-- screenshot: docs/listing.png -->

## Features

- Landing page plus an upload workspace: add or remove image rows, upload, preview
- AI listing generation from the product photo:
  - Amazon-style **listing title**
  - **Estimated price** in INR
  - **Colour, type and material**
  - **Keywords** for search and SEO
- Structured JSON response, typed out on the page
- `delete.py`: housekeeping script that clears uploaded files from the Gemini Files API

## How it works

```
Browser (main.html + upload.js) ──multipart POST /upload (images + fixed listing prompt)──► Flask backend
                                                                                           ▼
                                                                                     Gemini 1.5
```

The prompt pins the output to a JSON schema (`title, price, color, type, keywords`), so the result can go straight into a marketplace listing form.

## Tech stack

HTML · CSS · JavaScript · Python · Flask · Google Gemini (multimodal) · AWS EC2

## Run locally

Serve the folder (`python3 -m http.server`) and open `main.html`. The backend is a Flask service with an `/upload` endpoint that forwards images and prompt to Gemini; set `GOOGLE_API_KEY` in its environment and point the URL in `upload.js` at it.

## Team

Akshat Sharma, [maze0707](https://github.com/maze0707) · Site design based on an HTML5 UP template (see `LICENSE.txt`).
