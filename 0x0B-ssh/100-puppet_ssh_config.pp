# puppet ssh config

include stdlib

file_line { 'password_authentication':
    ensure  => present,
    path   => '.ssh/ssh_config',
    content => '
        Host *
            IdentityFile ~/.ssh/school
            PasswordAuthentication no
    ',
    replace => true,
}

file_line { 'identity':
  ensure => present,
  path   => '.ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}
