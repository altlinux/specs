Name:    postgresql-deploy-cert
Version: 0.8
Release: alt6

Summary: deploy script for postgresql cert config
License: MIT
Group:   Other
Url:     https://git.altlinux.org/gears/p/postgresql-deploy-cert.git

Packager: "Denis Medvedev" <nbr@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
Requires: deploy
Requires: integalert-postgresql


%description
A module for deploy ansible configuration maker for postgresql config

%package scripts
Summary: scripts for blocking on integrity failure of db
Group: Other

%description scripts
Scripts to be installed on postgres db server with kerberos auth
that block logins on integrity failure.

%prep
%setup

%install
mkdir -p %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 postgresql-cert.yml %buildroot%_datadir/deploy/postgresql-cert.yml
install -Dm 0644 *.conf  %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 *.acl  %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 main.yml  %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 postgresql.pam  %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 postgresql.logrotate  %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 pw_blocker.sysconfig %buildroot/%_datadir/deploy/postgresql-cert/tasks
mkdir -p %buildroot/%_bindir
install -Dm 0750 pw_krb_blocker %buildroot/%_bindir
install -Dm 0750 pw_krb_unblocker %buildroot/%_bindir




%files
%_datadir/deploy/postgresql-cert.yml
%_datadir/deploy/postgresql-cert/tasks/*

%files scripts
%_bindir/pw_krb_blocker
%_bindir/pw_krb_unblocker


%changelog
* Tue Oct 15 2024 Denis Medvedev <nbr@altlinux.org> 0.8-alt6
- corrected pg_hba transport,
redesigned config for blocking script

* Wed Oct 02 2024 Denis Medvedev <nbr@altlinux.org> 0.8-alt5
- added missing logrotate feature

* Sun Sep 29 2024 Denis Medvedev <nbr@altlinux.org> 0.8-alt4
- dependency to integalert-postgresql

* Sun Sep 29 2024 Denis Medvedev <nbr@altlinux.org> 0.8-alt3
- copy instead of file statement used

* Sat Sep 28 2024 Denis Medvedev <nbr@altlinux.org> 0.8-alt2
- create dir for triggers if not exists

* Fri Sep 27 2024 Denis Medvedev <nbr@altlinux.org> 0.8-alt1
- added subpackage with scripts

* Wed Sep 25 2024 "Denis Medvedev" <nbr@altlinux.org> 0.7-alt1
- fixes and minor config changes

* Thu Jun 27 2024 "Denis Medvedev" <nbr@altlinux.org> 0.6-alt1
- added packages for cluster and checksums

* Mon Jun 03 2024 "Denis Medvedev" <nbr@altlinux.org> 0.5-alt1
- Initial build for ALT
