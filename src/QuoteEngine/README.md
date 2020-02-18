# Quote Engine Module

The Quote Engine Module is responsible for ingesting many types of files that contain quotes. A quote contains a body and an author (e.g. "this is a quote body" - Author). This module will be composed of many classes and demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

## Quote Format

Example quotes are provided in a variety of files, take a moment to review the file formats in `./_data/SimpleLines` and `./_data/DogQuotes`. Your task is to design a system to extract each quote line-by-line from these files.

## Ingestors

An abstract base class, IngestorInterface should define two methods with the following class method signatures:

```
def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
```

Separate strategy objects should realize IngestorInterface for each file type (csv, docx, pdf, txt).

**TIP:** *pdftotext may not be installed on your local machine (Mac or Windows). If this is the case, you can install using the open source XpdfReader utility.*

A final Ingestor class should realize the IngestorInterface abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.

## Requirements

This package requires the following packages:

- Pandas
- Python-docx

These dependencies are listed on the project's requirements.txt. They can be installed using
the following command:

```
pip install pillow
pip install python-docx
```