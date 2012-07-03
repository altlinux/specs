Name: alterator-distro-backup-server
Version: 0.6
Release: alt1

Source:%name-%version.tar

Summary: special alterator modules for ALT Linux Backup Server
License: GPL
Group: System/Configuration/Other

Requires: alterator >= 4.12-alt1
Requires: alterator-l10n >= 2.4-alt5
Requires: alterator-fbi >= 5.21-alt1
Requires: alterator-bacula >= 0.6-alt6
Requires: alterator-net-eth dhcpcd
Requires: alterator-root
Requires: alterator-datetime
Requires: alterator-logs >= 0.7-alt5
Requires: alterator-root
Requires: MySQL-server
Requires: MySQL-server-control 
Requires: MySQL-client
Requires(pre): bacula-director-mysql >= 3.0.2-alt6

BuildArch: noarch

BuildPreReq: alterator >= 4.12-alt1

%description
special alterator modules for ALT Linux Backup Server:
- management center
- network and storage setup
- log file

%prep
%setup -q

%build
%make_build

%install
%makeinstall

install -Dpm644 backup-server.dhcpcd %buildroot/lib/dhcpcd/dhcpcd-hooks/50-backup-server
install -d -m 755 %buildroot%_sysconfdir/alterator/
cp -a logs %buildroot%_sysconfdir/alterator/


%files
/lib/dhcpcd/dhcpcd-hooks/*
%_sysconfdir/alterator/logs/.order
%_sbindir/*
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_datadir/alterator/interfaces/guile/workflow/*
%_alterator_backend3dir/*

%changelog
* Wed May 23 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- use MySQL-server-control for password setting

* Tue Nov 23 2010 Radik Usupov <radik@altlinux.org> 0.5-alt1
- Build from sisyphus

* Wed Nov 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- use standard /logout ui

* Thu Nov 05 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- improve design
- fix menu localization

* Wed Oct 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- new menu design
- use 'Archive' screen as a default

* Wed Oct 07 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt9
- backup-server-storage: print ip only if ip address defined
- update for latest alterator-fbi

* Fri Oct 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- use separate screen for administrator setup (closes: #21789)

* Thu Oct 01 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt7
- remove bacula_backupcatalog_set_catalog_password (not needed for bacula >= 3.0.2-alt6) (ALT #21789)

* Mon Sep 28 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- optimize "System screen": get ip_string and date_string directly from backup-server-storage backend
- remove links for nonexistent common.js file

* Fri Sep 25 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- optimize menu generation

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- update workflow for latest alterator-fbi
- update javascript includes (closes: #21248)

* Fri Sep 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- update login page design for new branding

* Fri Sep 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- move bacula log definition into alterator-logs file

* Thu Aug 20 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- remove special ahttpd-backup-server service
- use common (alterator login) library for login and logout pages

* Fri Jun 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt6
- switch to bacula-director-mysql

* Thu Jun 25 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- i18n fixes

* Tue Jun 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- show error message if disk is full
- use standard classes from branding for messages

* Thu Jun 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- ahttpd-backup-server: use standard https port
- minimize number of daemon reloading
- add special logout page

* Mon Jun 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- made package noarch
- add special login page
- add log for ahttpd-backup-server
- backup-server/system UI: add administator's password and server's name edition

* Tue Jun 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
