# syncfusion-pdf-converter-server
A sample dockerized server running syncfusion to convert docx files to PDF.</br>
This image is based on the example provided <a href="https://help.syncfusion.com/file-formats/docio/word-to-pdf-linux-docker">here</a> with the addition of a python server to receive documents to convert via HTTP POST requests.</br>
Once the server receives a new request the file in the body is stored in a temporary folder inside the container then the server invokes the convertion script and returns the generated PDF document.</br>
The server listens for POST requests with the raw file as the body. To send a file you can use Postman to generate the request or use curl as follows:
```
curl -X POST <url> --data-binary @<path to file>
```
## Installation
Execute the following commands to download, build and deploy the docker container. The server will listen on the specified port
```
git clone https://github.com/fborsani/syncfusion-pdf-converter-server/
cd syncfusion-pdf-converter-server/syncfusion
docker build --tag syncfusion-server
docker run -d -p <PORT>:8000 --name syncfusion-server syncfusion-server
```
