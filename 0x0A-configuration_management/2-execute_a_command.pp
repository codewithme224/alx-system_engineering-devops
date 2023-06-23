# Kills a process named killmenow
exec {'stop_process':
    command     => "pkill -f killmenow",
    path        => ['/bin', '/usr/bin/', '/usr/local/bin'],
    refreshonly => true,
}
