# MS forms conversion to document

This repo contains a barebones template for converting Microsoft Forms spreadsheet output to an HTML document (that can then be converted into a range of other formats). 

## Dependencies

This uses Pandas to read the MS Forms spreadsheet and Jinja2 for templating. 

```pip install -r requirements.txt```

## How to run

Execute main python script ```convert.py``` with the command line parameters described in the table below. For example:

```
python convert.py -s exampleformoutput.xlsx -m columnmap.txt -t template.jinja
```

### Command line parameters

| Parameter | Function |
| --------- | -------- |
| -s | MS Forms spreadsheet (Excel xlsx format) |
| -m | Column mapping (tab-delimited text) with original column names from MS Forms spreadsheet in column one and short names (for Jinja template) in column 2. |
| -t | Jinja template specifying format of the pages using the shortnames from the column mapping file |