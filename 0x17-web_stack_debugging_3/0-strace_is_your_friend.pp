file { '/etc/apache2/sites-available/your_site.conf':
    ensure  => present,
    content => '# Your corrected virtual host configuration content here',
    notify  => Service['apache2'],
}

service { 'apache2':
    ensure  => running,
    enable  => true,
    require => File['/etc/apache2/sites-available/your_site.conf'],
}
