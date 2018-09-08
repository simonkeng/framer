from livereload import Server, shell

server = Server()
server.watch('index.html')
server.serve(port=9876, host='localhost')

