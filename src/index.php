<?php
/**
 * Simple HTTP Server
 *
 * Run server: php -S localhost:8000
 * Access at: http://localhost:8000
 */

$method = $_SERVER['REQUEST_METHOD'];
if ('GET' === $method) {
    echo 'Hello PHP World';
} else if ('POST' === $method) {
    echo '<pre>' . var_export($_POST, true) . '</pre>';
}
