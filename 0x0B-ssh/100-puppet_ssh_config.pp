# puppet ssh config

include stdlib

file_line { 'password_authentication':
    ensure  => present,
    path   => 'etc/ssh/ssh_config',
    content => '
        Host *
            IdentityFile ~/.ssh/school
            PasswordAuthentication no
    ',
    replace => true,
}
