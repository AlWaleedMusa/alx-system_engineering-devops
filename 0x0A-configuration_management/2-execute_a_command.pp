# kill a process using

exec {'killmenow_process':
    command   => 'pkill killmenow',
    onlyif    => 'pgrep killmenow',
    provider  => 'shell',
    logoutput => true,
}
