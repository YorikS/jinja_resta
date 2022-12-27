from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from jinja2 import Environment, select_autoescape, PackageLoader


class CustomHandler(SimpleHTTPRequestHandler):
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    def do_GET(self):
        if self.path.startswith('/media/'):
            super().do_GET()
        elif self.path == '/':
            self.render_index()
        elif self.path == '/about/':
            self.render_about()
        elif self.path == '/blog/':
            self.render_blog()
        elif self.path == '/contact/':
            self.render_contact()
        elif self.path == '/elements/':
            self.render_elements()
        elif self.path == '/menu/':
            self.render_menu()
        elif self.path == '/single_blog/':
            self.render_single_blog()
    
    def render_index(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('index.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_about(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('about.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_contact(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('contact.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_elements(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('elements.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_menu(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('menu.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_single_blog(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('single-blog.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Server starting')
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=CustomHandler)