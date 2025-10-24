import azure.functions as func
import datetime
import json
import logging
import codecs
import csv

app = func.FunctionApp()


@app.function_name('FirstHTTPFunction')
@app.route(route="myroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    response = {"message": "Wow, this first HTTP Function works!"}
    return func.HttpResponse(json.dumps(response), status_code=200)


@app.function_name('SecondHTTPFunction')
@app.route(route="newroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Starting the second HTTP Function request.')

    name = req.params.get('name')
    if name:
        response_data = {"message": f"Hello, {name}, so glad this Function worked!!"}
    else:
        response_data = {"message": "Hello, so glad this Function worked!!"}

    return func.HttpResponse(json.dumps(response_data), status_code=200)


@app.function_name(name="MyFirstBlobFunction")
@app.blob_trigger(
    arg_name="readfile",
    path="demoblob/People.csv",
    connection="AzureWebJobsStorage"
)
def main(readfile: func.InputStream):
    reader = csv.reader(codecs.iterdecode(readfile, 'utf-8'))
    for row in reader:
        logging.info(f"Row: {row}")