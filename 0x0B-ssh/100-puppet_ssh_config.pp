# puppet ssh config

file { '.ssh/config':
    ensure  => present,
    content => "
        Host *
            IdentityFile ~/.ssh/school
            PasswordAuthentication no
    ",
}
