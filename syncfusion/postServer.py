import os
import io
import re
import sys
import urllib.parse
import uuid
import time
import http.server as server

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(405)

        def do_POST(self):
            filename="{}_{}".format("newfile",time.time())
            fileIn="/tmp/{}.docx".format(filename)
            fileOut="/tmp/{}.pdf".format(filename)
            
            try:
                if not self.headers['Content-Length']:
                    self.send_response(400)
                    
                file_length = int(self.headers['Content-Length'])
                read = 0
                with open(fileIn, 'wb+') as output_file:
                    while read < file_length:
                        new_read = self.rfile.read(min(66556, file_length - read))
                        if(len(new_read) > 0):
                            read = read + len(new_read)
                            output_file.write(new_read)
                        else:
                            break

                os.system('dotnet  WordToPDFDockerSample.dll {} {}'.format(fileIn,fileOut))
                self.send_response(200)
                self.send_header('Content-type', 'application/pdf')
                self.send_header('Content-Disposition', 'attachment; filename="file.pdf"')
                self.end_headers()
                
                with open(fileOut, 'rb') as file: 
                    self.wfile.write(file.read())
                    
            except Exception as e:
                self.send_response(500)
                print(e)
            finally:
                os.remove(fileIn)
                os.remove(fileOut)

if __name__ == '__main__':
    server = server.HTTPServer(("",8000), HTTPRequestHandler)
    server.serve_forever()
    server.server_close()