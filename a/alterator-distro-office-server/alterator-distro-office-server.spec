Name: alterator-distro-office-server
Version: 1.0
Release: alt18

Provides: alterator-office-server = %version
Obsoletes: alterator-office-server

Source:%name-%version.tar

Packager: Vladislav Zavjalov <slazav@altlinux.org>

Summary: special alterator modules for ALT Linux Office Server
License: GPL
Group: System/Configuration/Other

Requires: alterator >= 4.7-alt3 alterator-sh-functions
Requires: alterator-net-iptables
Requires: alterator-net-domain >= 0.1-alt2
Requires: alterator-ca
Requires: alterator-root >= 0.7-alt1
Requires: alterator-l10n >= 2.4-alt2

Conflicts: alterator-net-eth < 4.3-alt5
Conflicts: alterator-fbi < 5.10-alt1

BuildPreReq: alterator >= 4.7-alt3

%description
special alterator modules for ALT Linux Office Server:
- firsttime settings
- hooks for administrator password

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%find_lang %name

%files
%config(noreplace) %_sysconfdir/alterator/logs/.order
%_bindir/*
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_libexecdir/alterator/hooks/*.d/*

%changelog
* Fri Dec 24 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt18
- revert for alterator

* Fri Dec 24 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt17
- build with new alterator

* Tue Dec 07 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt16
- ignore mandatory static net interface with startup param 'nostatic'

* Fri Oct 02 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt15
- be sure domain name is set (closed: #21806)
- locate commit-iptables near from read-iptables

* Thu Oct 01 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt14
- commit-iptables: use standard port list from alterator-net-iptables package

* Mon Sep 07 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt13
- commit-domain after all other operations

* Mon Aug 10 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt12
- ca-commit: fix language code calculation (closes: #20217)

* Mon Aug 10 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt11
- define logs order (closes: #20979)

* Thu Jun 11 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt10
- hardcode server role (closes: #20404)

* Thu Jun 04 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt9
- check that server role selected (closes: #20295)

* Tue May 26 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt8
- Added firsttime.d hook.

* Thu Apr 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt7
- improve CA support (closes: #19850)

* Fri Apr 17 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0-alt6
- Turn on CA autoupdate by default

* Tue Apr 14 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0-alt5
- alterator-ca support

* Wed Apr 08 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt4
- update for modern alterator

* Tue Apr 07 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt3
- add net-eth precommit hook

* Sat Apr 04 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- generate locale list automatically

* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- rename package to alterator-distro-office-server
- choose server role

* Wed Mar 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- setup common domain instead of ldap's base dn

* Fri Feb 27 2009 Lebedev Sergey <barabashka@altlinux.org> 0.8-alt1.2
- simple fix in ajax.scm for ldap backend

* Thu Feb 26 2009 Lebedev Sergey <barabashka@altlinux.org> 0.8-alt1.1
- fixed ldap support

* Thu Feb 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- remove office-server versions of alterator modules
- improve i18n

* Tue Feb 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- first build for sisyphus

* Tue Feb 17 2009 Lebedev Sergey <barabashka@altlinux.org> 0.6-alt5.M50.8
- removed po and help files

* Mon Feb 16 2009 Lebedev Sergey <barabashka@altlinux.org> 0.6-alt5.M50.7
- build for 5.0

* Mon Feb 16 2009 Lebedev Sergey <barabashka@altlinux.org> 0.6-alt5.M41.7
- simple fix in Makefile and spec files

* Thu Feb 12 2009 Lebedev Sergey <barabashka@altlinux.org> 0.6-alt5.M41.6
- removed domain support
- fixed tls support
- updated help and po files

* Thu Feb 05 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5.M41.5
- fix root password setting for mediawiki in backend

* Wed Feb 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5.M41.4
- rebuild with new alterator-l10n, add BuildPreReq: alterator-fbi

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5.M41.3
- removed rootpw settings (by barabashka@)

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5.M41.2
- use help and po from alterator-l10n
- add hidden desktop file for a-o-s-net

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5.M41.1
- build for 4.1

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt6
- write md5 as a ldap passwd
- fixed rootpw password change (by barabashka@)

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt4.M41.1
- build for 4.1

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5
- don't switch to ldap in backend
- change wiki and moodle admin names to root
- fix mysql_passwd_sum
- fix package description

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt3.M41.1
- build for 4.1

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt4
- fixed ldap uri, must be ldap:// (by barabashka@)

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt2.M41.1
- build for 4.1

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt3
- don't set passwords to mysql dumps
- don't require installed-db-school-server

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt1.M41.1
- build for 4.1

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt2
- add ru translations to desktop files
- fix backend for the installer
- update admin passwords in moodle and mediawiki databases

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt0.M41.1
- build for 4.1

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt1
- set root password for mysql
- add mysql_passwd_sum -- tool for calculating passwd hash for mysql
- add requires on openldap-servers and installed-db-school-server (fix #18586)

* Wed Jan 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt6.M41.1
- build for 4.1

* Wed Jan 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt7
- merge changes from barabashka@
  + removed alterator-auth Requires
  + removed symlink slapd.conf
  + included slapd-generated.conf into slapd.conf

* Tue Jan 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt5.M41.1
- build for 4.1

* Tue Jan 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt6
- merge ldap and net UI
- use tree structure for ui files
- change icons in install2 steps
- update po
- remove build requires on alterator-fbi (fix bug with po-files from l10n)

* Tue Jan 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt5
- merge changes from barabashka@
  + added switch_to_ldap + added Requires alterator-auth
  + added symlink slapd-generated.conf to slapd.conf
  + changed ldap ui

* Thu Jan 15 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt3.M41.1
- build for 4.1

* Wed Jan 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt4
- set passwords for moodle and mediawiki
- create .ssh dir if it does not exists

* Wed Jan 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt2.M41.1
- build for 4.1

* Wed Jan 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt3
- add install2/steps/office-server-root.desktop

* Mon Jan 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt2
- update po

* Mon Jan 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt0.M41.1
- build for 4.1

* Mon Jan 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- add office-server-ldap

* Mon Jan 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt0.M41.1
- build for 4.1

* Mon Jan 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt1
- show authorized key fingerprint in html UI

* Mon Jan 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt0.M41.1
- build for 4.1

* Mon Jan 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- add installer module for internal interfaces selecting

* Mon Jan 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt1
- add ssh key uploading

* Sun Jan 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt1
- first build from alterator-root-0.4-alt1.M41.4
