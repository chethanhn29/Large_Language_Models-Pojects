# [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
Document loaders load documents from many different sources. LangChain provides over 100 different document loaders as well as integrations with other major providers in the space, like AirByte and Unstructured. LangChain provides integrations to load all types of documents (HTML, PDF, code) from all types of locations (private S3 buckets, public websites).
## Overview
Document loaders designed to facilitate data retrieval and interaction within LangChain. These loaders serve to convert data from diverse sources and formats into a standardized document interface, enabling seamless manipulation and analysis.
![](https://python.langchain.com/assets/images/data_connection-c42d68c3d092b85f50d08d4cc171fc25.jpg)
## Purpose
The primary goal of these document loaders is to offer a means to interact with different data types such as PDFs, URLs, and proprietary sources (e.g., Notion databases) within the LangChain environment. These loaders aim to simplify the process of accessing and processing data for use in applications, particularly chat-based interfaces.

## Types of Loaders
### Unstructured Data Loaders
- Access text files from public sources like YouTube, Twitter, Hacker News.
- Fetch unstructured data from proprietary sources such as Figma, Notion.

### Structured Data Loaders
- Handle tabular data formats from sources like Airbyte, Stripe, Airtable.

## Usage
### PDF Document Loader
- Utilize the PyPDF loader to handle PDF files.
- Load multiple pages from a PDF, treating each page as an individual document.
- Each document consists of page content and associated metadata (source, page number).
```Python
from langchain.loaders import PyPDFLoader

# Load PDFs using PyPDFLoader
loader = PyPDFLoader()
documents = loader.load('path_to_pdf_file.pdf')

# Access content and metadata
for document in documents:
    print(document.content[:300])  # Display first 300 characters of content
    print(document.metadata)       # Display document metadata
```

### YouTube Document Loader
- Use the YouTube audio loader and OpenAI Whisper parser to convert YouTube video audio into text format.
- This transcription allows interaction or questioning related to video content.
```python
from langchain.loaders import YouTubeAudioLoader, OpenAIWhisperParser

# Use YouTubeAudioLoader and OpenAIWhisperParser
audio_loader = YouTubeAudioLoader()
whisper_parser = OpenAIWhisperParser()
loader = audio_loader + whisper_parser

# Load YouTube video content
loader.load('youtube_video_url')
# Access and work with the transcribed text
```
### Web-based Loader (URLs)
- Access educational content from URLs using the web-based loader.
- Examples from markdown files showcase the need for post-processing of loaded information.
```python
from langchain.loaders import WebBasedLoader

# Utilize WebBasedLoader for URLs
web_loader = WebBasedLoader()
documents = web_loader.load('url')

# Handle content with post-processing
```
### Notion Document Loader
- Retrieve data from Notion databases using the Notion directory loader.
- Notion data appears in markdown format, enabling interaction and analysis.
```python
from langchain.loaders import NotionDirectoryLoader

# Use NotionDirectoryLoader for Notion databases
notion_loader = NotionDirectoryLoader()
documents = notion_loader.load('notion_database_id')

# Analyze and interact with loaded Notion documents
```

## Post-Loading Processing and Challenges
- Importance of post-processing data after loading to make it usable.
- Documents can be extensive; therefore, splitting them into smaller, relevant chunks is crucial for effective retrieval and interaction.

## Future Considerations and Opportunities
- Consider sources not covered by existing loaders.
- Contribute by proposing new loaders to LangChain.
