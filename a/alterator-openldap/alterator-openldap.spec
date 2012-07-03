%define _altdata_dir %_datadir/alterator

Name: alterator-openldap
Version: 0.8
Release: alt2

Packager: Dmitriy Kruglikov <dkr@altlinux.ru>
BuildArch: noarch

Source:%name-%version.tar

Summary: alterator module for OpenLDAP server
License: GPL
Group: System/Configuration/Other
Requires: libshell 
Requires: alterator-services
Requires: ldap-user-tools >= 0.2-alt3.1
Requires: alterator-openldap-functions >= 0.2-alt2

Requires: alterator >= 3.5 gettext 
Requires: alterator-services

BuildPreReq: alterator >= 3.5-alt2, alterator-fbi >= 5.26-alt3


%description
Alterator module for OpenLDAP server.

%prep
%setup -q

%build
%make_build

%install
%makeinstall 

%find_lang %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/alterator/openldap
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_datadir/alterator/help/*/*
%_alterator_backend3dir/*

%changelog
* Mon Mar 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt2
- Management of TLS settings fixed (closes #25190)
- use samba.scheme from samba package due to set by installer

* Wed Dec 15 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.8-alt1
- Management of TLS settings.

* Wed Aug 18 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.7-alt2
- Bugfix, redesign, improvement.

* Tue Aug 17 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.7-alt1
- Added LDIF save/restore and schema upload.

* Wed Apr 14 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt4
- New requires. Closed bug #19368  -  UI improvement.

* Tue Apr 13 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt3
- Some changes in "Selected_DN" for test

* Tue Apr 13 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt2
- Impruved schema management

* Mon Apr 12 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt1
- Added schema management

* Fri Apr 02 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.4-alt1
- Added expert mode for BaseDN creation.
- Added multi-select for deletion of existen DN.
- Added check for system-auth bese.

* Thu Nov 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt6
- move openldap hook (specific for p5) out from package to appropriate installer-distro-*

* Mon Apr 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt5
- added openldap hook (enable_schema, enable_server)

* Thu Mar 12 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4.5
- simple fix around action write

* Fri Feb 27 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4.4
- fixed ui
- added help file
- fixed desktop file

* Thu Feb 26 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4.3
- added default_dn object for alterator-office-server

* Thu Feb 26 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4.2
- added fixes around creation dn

* Wed Feb 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4.1
- some simple fixes
- fixed code style
- fixed 'Accept local connections only'
- improved error messaging

* Wed Feb 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4
- added support for custom base dn
- added actions for dn
  + publish (avahi)
  + unpublish (avahi)
  + create
  + delete

* Mon Feb 16 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt2.M50.alt5
- updated due to building for M41

* Mon Feb 16 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt3
- updated due to building for M41

* Mon Feb 16 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt0.M41.6
- fixed Version and Release

* Thu Feb 12 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt2.M41.5
- removed domain support
- removed tls configuration (using default values)
- removed samba schema configuration (always enable)
- updated po and help files

* Wed Jan 24 2009 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt2.M41.4
- Uses alterator-services for slapd service management

* Fri Jan 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt2.M41.3
- fix help packaging

* Thu Jan 15 2009 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt2.M41.2
- Now requires alterator-chkconfig.
- Uses alterator-l10n for translations and help.

* Mon Dec 08 2008 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt1.M41.1
- Samba3 schema toggling.

* Fri Dec 05 2008 Paul Wolneykien <manowar@altlinux.ru> 0.2-alt2.M41.1
- Use "TRUE" value for ppolicy flags.

* Mon Dec 01 2008 Paul Wolneykien <manowar@altlinux.ru> 0.2-alt1.M41.1
- New release for branch 4.1.

* Tue Nov 11 2008 Paul Wolneykien <manowar@altlinux.ru> 0.1-alt2.M40.1
- Port for branch 4.0.

* Tue Sep 30 2008 Paul Wolneykien <manowar@altlinux.ru> 0.1-alt2.ism
- Adds replication module switch.

* Mon Sep 01 2008 Paul Wolneykien <manowar@altlinux.ru> 0.1-alt1.ism
- Add host container.

* Tue May 06 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt1.M40.3
- Simplify base DN dc:/o: split.

* Fri Apr 18 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt1.M40.2
- Grant anonymous access in default base config. 

* Fri Apr 11 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt1.M40.1
- Change base suffix description to "Base DN".
- Add host and port settings.

* Wed Mar 19 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial release.
