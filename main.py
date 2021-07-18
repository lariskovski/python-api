from fastapi import FastAPI

app = FastAPI()

in_memory_datastore = [
  {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
  {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
  {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
]

@app.get('/programming_languages')
def get_programming_languages():
   return {"programming_languages" : in_memory_datastore }

@app.get('/programming_languages/{programming_language_id}')
def get_programming_language(programming_language_id: int):
   return in_memory_datastore[programming_language_id]