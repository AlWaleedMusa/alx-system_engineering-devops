# A manifest the debug an apache issue

# Ensure that the file '/etc/apache2/sites-available/your_site.conf' is present
file { '/etc/apache2/sites-available/your_site.conf':
    ensure  => present,
    content => '# Your corrected virtual host configuration content here',
    notify  => Service['apache2'],  # Notify the 'apache2' service when the file changes
}

# Ensure that the 'apache2' service is running and enabled
service { 'apache2':
    ensure  => running,
    enable  => true,
    require => File['/etc/apache2/sites-available/your_site.conf'],  # Require the file '/etc/apache2/sites-available/your_site.conf' to be present before starting the service
}
