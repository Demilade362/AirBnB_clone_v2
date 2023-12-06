# Setup the web servers for the deployment of web_static
exec { 'update_env' :
  command => '/usr/bin/env apt -y update',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
}
-> package { 'nginx':
  ensure => installed,
}
-> file { '/data':
  ensure  => 'directory'
}
-> file { '/data/web_static':
  ensure => 'directory'
}
-> file { '/data/web_static/releases':
  ensure => 'directory'
}
-> file { '/data/web_static/releases/test':
  ensure => 'directory'
}
-> file { '/data/web_static/shared':
  ensure => 'directory'
}
-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            background-color: #120607;
            color: aliceblue;
            text-align: center;
        }

        a {
            color: bisque;
            text-decoration: none;
            font-style: italic;
            font-family: "Courier New", Courier, monospace;
            border: 2px groove;
            padding: 10px;
            border-radius: 5px;
        }

        a:hover {
            animation: color-ray 2s infinite cubic-bezier(0.47, 0, 0.745, 0.715) alternate-reverse;
        }

        @keyframes color-ray {
            0% {
                color: red;
                border-color: red;
                text-shadow: 0 0 5px red;
            }

            20% {
                color: yellow;
                border-color: yellow;
                text-shadow: 0 0 10px yellow;
            }

            40% {
                color: blue;
                border-color: blue;
                text-shadow: 0 0 8px blue;
            }

            60% {
                color: magenta;
                border-color: magenta;
                text-shadow: 0 0 3px magenta;
            }

            80% {
                color: cyan;
                border-color: cyan;
                text-shadow: 0 0 7px cyan;
            }
        }
    </style>
</head>
<body>
    <h1>Hello World</h1>
    <a href="https://bio.link/olajide">Adeniji Olajide</a>
</body>
</html>'
}
-> file { '/data/web_static/current/':
  ensure => 'link',
  target => '/data/web_static/releases/test/'
}
-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

exec { 'nginx_configure':
  environment => ['n_alias=\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}'],
  command     => 'sed -i "/error_page 404 \\/404.html;/a\\$n_alias" /etc/nginx/sites-enabled/default',
  path        => '/usr/bin:/usr/sbin:/bin:/usr/local/bin'
}
-> service { 'nginx':
  ensure => running,
}
