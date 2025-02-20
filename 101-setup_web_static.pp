# A puppet manifest that sets up my web servers for the deployment of web_static

exec {"update":
  provider => shell,
  command  => "sudo apt-get -y update",
  before   => Exec["install Nginx"],
}

exec {"install Nginx":
  provider => shell,
  command  => "sudo apt-get -y install nginx",
}

-> file { '/data/':
  ensure => "directory"
}

-> file { '/data/web_static/':
  ensure => 'directory'
}

-> file { '/data/web_static/releases/test/':
  ensure => 'directory'
}

-> file { '/data/web_static/releases/test/':
  ensure => "directory"
}

-> file { '/data/web_static/shared/':
  ensure => "directory"
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => "present",
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"
}

-> exec {"symbolic link":
  provider => shell,
  command  => "sudo ln -sf /data/web_static/releases/test/ /data/web_static/current",
  before   => Exec['add hbnb_static']
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

-> exec {'add hbnb_static':
  provider => shell,
  command  => "sudo sed -i '/^[^#]*location \/ {/ { :a; N; /}/!ba; s/}/&\n\n        location \/hbnb_static {\n                alias \/data\/web_static\/current\/;\n        }/; }' /etc/nginx/sites-available/default",
  before   => Exec['restart Nginx']
}

-> exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart'
}
