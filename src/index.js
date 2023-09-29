/**
 * Simple HTTP Server
 *
 * Run server: node index.js 9000
 * Access at: http://localhost:9000
 */

const http = require('http');

let server = http.createServer((request, response) => {
    let method = request.method;
    if ('GET' === method) {
        response.statusCode = 200;
        response.setHeader('Content-Type', 'text/html');
        response.write('Hello Node.js World');
        response.end();
    } else if ('POST' === method) {
        let body = '';
        request.on('data', (value) => {
            body += value;
        });

        request.on('end', function () {
            response.statusCode = 200;
            response.setHeader('Content-Type', 'text/html');

            response.write('<pre>' + body + '</pre>');
            response.end();
        });
    }
});

let port = parseInt(process.argv[2]) || 9000;
server.listen(port);

console.log(`Node.js web server at port ${port} is running...`);
