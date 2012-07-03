%define _altdata_dir %_datadir/alterator
%define _hooksdir %_sysconfdir/hooks/hostname.d

Name: alterator-auth
Version: 0.22
Release: alt5

BuildArch: noarch

Source:%name-%version.tar

Summary: alterator module for system wide auth settings
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.7-alt4
Requires: alterator-l10n >= 2.0-alt1
Requires: pam-config >= 1.4.0-alt1.1
Requires: pam_krb5
Requires: nss_ldap
Conflicts: alterator-fbi < 5.9-alt2
Conflicts: alterator-lookout < 1.6-alt6

Provides: alterator-nsswitch = %version
Obsoletes: alterator-nsswitch

BuildPreReq: alterator >= 4.7-alt4

%description
alterator module for system wide auth settings

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall
install -Dpm755 sbin/system-auth %buildroot/%_sbindir/system-auth
install -Dpm755 hooks/auth %buildroot/%_hooksdir/90-auth

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_sbindir/system-auth
%_hooksdir/90-auth
%_alterator_backend3dir/*

%changelog
* Thu Apr 19 2012 Mikhail Efremov <sem@altlinux.org> 0.22-alt5
- Add string for translation.
- Improve warning message.

* Wed Apr 18 2012 Mikhail Efremov <sem@altlinux.org> 0.22-alt4
- Always show warning message.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.22-alt3
- Show warning message about reboots necessity.

* Fri Mar 18 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.22-alt2
- alwais ldaps if kerberos

* Thu Mar 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.22-alt1
- set ldaps:// for kerberos domain
- requres on nss_ldap added

* Fri Oct 01 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.21-alt1
- fixed domain selection in acc

* Sun Apr 11 2010 Dmitriy L. Kruglikov <dkr@altlinux.org> 0.20-alt1
- Refabrisched after wf="form"->wf="none" migration.

* Wed Dec 02 2009 Dmitriy L. Kruglikov <dkr@altlinux.org> 0.10-alt3
- Added Local|LDAP|KRB5 support and LDAP base selection.

* Thu Jun 11 2009 Lebedev Sergey <barabashka@altlinux.org> 0.10-alt2
- removed write_krb5 (unnecessary function)
- merged with Anton V. Boyarshinov

* Thu Jun 11 2009 Lebedev Sergey <barabashka@altlinux.org> 0.9-alt3.2
- added support /etc/openldap/ldap.conf 

* Wed Apr 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.10-alt1
- removed /etc/krb5.conf filling (default is better) 

* Fri Apr 17 2009 Lebedev Sergey <barabashka@altlinux.org> 0.9-alt3.1
- fixed ui bug (installer) 

* Thu Apr 16 2009 Lebedev Sergey <barabashka@altlinux.org> 0.9-alt3
- rewrote qt interface
- synced html interface with qt interface
- fixed hook (now checking SERVER_ROLE)

* Thu Apr 09 2009 Lebedev Sergey <barabashka@altlinux.org> 0.9-alt2.1
- added role checking (hook)

* Wed Apr 08 2009 Lebedev Sergey <barabashka@altlinux.org> 0.9-alt2
- fixed nsswitch bug
- fixed simple error (auth hook)
- rewrote ui for domain auth

* Fri Apr 03 2009 Lebedev Sergey <barabashka@altlinux.org> 0.9-alt1
- added system-auth tool 
- rewrote backend and ui (now using system-auth tool)
- added /etc/hooks/hostname.d/90-auth (setting auth for servers) 

* Fri Mar 27 2009 Lebedev Sergey <barabashka@altlinux.org> 0.8-alt2.5
- removed alterator-kdc
- wrote fill_krb_conf
- fixed ui

* Thu Mar 26 2009 Lebedev Sergey <barabashka@altlinux.org> 0.8-alt2
- added krb5 support (krb5.conf)
- require alterator-kdc

* Fri Feb 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- move html ui definitions from templates to ui directory
- use help and translations directly from alterator-l10n

* Tue Dec 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt4
- use new help from l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt3
- update help (by azol@), rebuild with new alterator-l10n (add pt_BR.po)

* Fri Nov 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt2
- remove title and h1 from html template

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- replace constraints with types

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- use enumref

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- remove po-files
- use module.mak

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- rename: effect-update -> update-effect, effect-init -> init-effect

* Fri Jun 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- use effectShow
- update backend

* Tue Apr 29 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- update for new case-form algo

* Tue Apr 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- update help

* Tue Apr 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- join to common translation database

* Tue Apr 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- join alterator-auth and alterator-nsswitch
- remove html-messages.po
- improve UI according alterator HIG

* Wed Apr 02 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- fix hostname restrictions

* Wed Mar 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- remove template-*
- use alterator-sh-functions
- use libshell

* Tue Jan 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- update to new help system

* Thu Jun 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- fix backend

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add qt ui
- html ui improvements

* Fri Jun 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- help improvements from kirill@

* Tue Jun 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- comment out 'host' option to avoid conflict with uri

* Mon Jun 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add help

* Thu May 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- improve constraints

* Wed May 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- exclude ldap from list if appropriate nss module doesn't exists

* Tue May 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
