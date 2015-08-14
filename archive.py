def run_backup():

    # here is two functions, not listed here
    # both rerurns lists[] - with users 
    # like just username
    # and dirs 
    # like /var/www/vhosts/username
    userlist = arch_users_list(VHOSTSPATH)
    userpaths = arch_users_path(VHOSTSPATH, userlist)

    # day of week
    curday = time.strftime('%a')

    for hostdir, username in zip(userpaths, userlist):
        os.chdir(hostdir)
        print('\nWorking in: %s' % os.getcwd())
        print('Under user: %s' % username)

        # call first function, listed above

        backup_dir = back_dir_create(username, curday)

        if backup_dir:

            virtual_hosts = arch_vhosts_names(hostdir)

            for host in virtual_hosts:
                archname = (backup_dir + host + '.tar.bz2')

                # once in week I want have full backup
                # other time - 'incremental'

                if curday == 'Sun':
                    full_backup(host, archname)
                else:
                    inc_backup(host, archname)

        else:
            print('Backup already present, skip.')