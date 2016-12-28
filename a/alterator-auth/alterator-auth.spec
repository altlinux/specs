%define _altdata_dir %_datadir/alterator
%define _hooksdir %_sysconfdir/hooks/hostname.d

Name: alterator-auth
Version: 0.30.2
Release: alt1

BuildArch: noarch

%filter_from_requires /^samba-common$/d

Source:%name-%version.tar

Summary: Alterator module for system wide auth settings
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.7-alt4
Requires: alterator-l10n >= 2.0-alt1
Requires: pam-config >= 1.7.0-alt1
Requires: pam_krb5
Requires: nss-ldap
Requires: libnss-myhostname
Requires: avahi-daemon
Requires: settime-rfc867
Requires: bind-utils

Conflicts: alterator-fbi < 5.9-alt2
Conflicts: alterator-lookout < 1.6-alt6

Provides: alterator-nsswitch = %version
Obsoletes: alterator-nsswitch

BuildPreReq: alterator >= 4.7-alt4

%description
Alterator module for system wide auth settings

%package -n task-auth-ad
Summary: Metapackage to authenticate in Active Directory domain
Group: System/Configuration/Other
Requires: alterator-auth
Requires: samba-winbind
Requires: samba-winbind-clients
Requires: samba-common-tools
Requires: krb5-kinit
Requires: pam_mount
Requires: libnss-role
Requires: alterator-datetime
Requires: gvfs-shares

%description -n task-auth-ad
Metapackage to authenticate in Active Directory domain.

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall
install -Dpm644 etc/user-groups %buildroot%_sysconfdir/alterator/auth/user-groups
install -Dpm644 etc/admin-groups %buildroot%_sysconfdir/alterator/auth/admin-groups
install -Dpm755 sbin/system-auth %buildroot/%_sbindir/system-auth
install -Dpm755 hooks/auth %buildroot/%_hooksdir/90-auth

%files
%config(noreplace) %_sysconfdir/alterator/auth/user-groups
%config(noreplace) %_sysconfdir/alterator/auth/admin-groups
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_sbindir/system-auth
%_hooksdir/90-auth
%_alterator_backend3dir/*

%files -n task-auth-ad

%changelog
* Wed Dec 28 2016 Andrey Cherepanov <cas@altlinux.org> 0.30.2-alt1
- Set local hostname and set krb5_ccache_type to KEYRING
- Require gvfs-shares in task-auth-ad

* Tue Dec 27 2016 Andrey Cherepanov <cas@altlinux.org> 0.30.1-alt1
- Fix nss role behaviour (use domain names and place in nsswitch.conf)

* Mon Dec 26 2016 Andrey Cherepanov <cas@altlinux.org> 0.30.0-alt1
- Edit existing Kerberos configuration instead of use winbind to
  retrieve Kerberos config (ALT #32342, #32937)
- Set winbind enum users and groups to `no` to prevent lags in large
  networks
- Check task-auth-ad package installed instead of winbind service to
  get complete list of requirements
- Map domain groups to local Unix groups
- Add gvfs stuff to task-auth-ad for shares mount
- Set time sync from dc for client
- Adapt LightDM for too many domain users: remove user list and language
  chooser (such as Windows login screen)

* Fri Nov 18 2016 Andrey Cherepanov <cas@altlinux.org> 0.29.7-alt1
- Wait 10 seconds for winbind to create krb5.conf file (ALT #32759)

* Fri Oct 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.29.6-alt1
- Support offline login and set more usable parameters for pam_winbind
- Register machine in domain DNS during Active Directory join
- Show real error from system-auth if it exists
- Fix domain name detection in resolvconf
- Add bind-utils for troubleshooting

* Mon Aug 01 2016 Andrey Cherepanov <cas@altlinux.org> 0.29.5-alt2
- Add metapackage task-auth-ad to setup authentication in Active
  Directory domain

* Mon Jul 11 2016 Andrey Cherepanov <cas@altlinux.org> 0.29.5-alt1
- Fix join to Active Directory domain in some cases:
  - Increase available idmap range from 10.000 to 20 millions
  - Use system keytab for share files to domain users
  - Require libnss-myhostname to prevent "DNS update failed!" error
    (see https://lists.samba.org/archive/samba/2009-June/148869.html)
  - Check Nebios name length (shoud not be more 15 chars) both in script
    and form
- Inform user to succesful join to Active Directory domain

* Fri Jun 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.29.4-alt1
- "group: files [SUCCESS=merge] ldap" for glibc groups merging

* Wed Jun 01 2016 Andrey Cherepanov <cas@altlinux.org> 0.29.3-alt1
- Fix Kerberos environment prepare by winbind
- Comment out unused parameters
- Support WINS in Samba config file

* Fri Nov 27 2015 Andrey Cherepanov <cas@altlinux.org> 0.29.2-alt1
- Replace entire section [global] in /etc/samba/smb.conf by new config
- Support mapping parameters both for Samba 3.x and 4.x

* Fri Sep 25 2015 Andrey Cherepanov <cas@altlinux.org> 0.29.1-alt1
- Read domain name from domain parameter of resolvconf -l

* Thu Apr 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.29-alt1
- Enable service settime-rfc867 for ALT domain
- Add settime-rfc867 to requirements
- Support both sysvinit and systemd services


* Wed Apr 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.28-alt1
- Sync time with DC before join to Active Directory domain
- Check available of /usr/bin/net for join to AD
- Set idmap range to 10000-20000 and disable master role by default for
  Active Directory auth (useful for KDM using MaxShowUID=29999)
- Autofill Active Directory domain name from DNS information
- Usability improvements
- system-auth: show usage infomation and program version

* Fri Mar 13 2015 Andrey Cherepanov <cas@altlinux.org> 0.27-alt1
- Support Active Directory authentication in GUI (ALT #30021)

* Tue Mar 03 2015 Andrey Cherepanov <cas@altlinux.org> 0.26.1-alt1
- [system-auth] Disable old scheme services only on scheme change

* Thu Feb 19 2015 Andrey Cherepanov <cas@altlinux.org> 0.26-alt1
- Add support of Active Directory auth in system-auth
- Do not require ldap-user-tools for list local configured LDAP DNs (ALT #24180)
- Fix fatal exit in backend if avahi-daemon is not running
- Fix typo (ALT #25930)
- Package ini-config helper for set parameters in ini files

* Thu Jan 24 2013 Andrey Cherepanov <cas@altlinux.org> 0.25-alt3
- Fix system-auth write with nss-ldapd

* Fri Nov 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.25-alt2
- setting ccreds checkbox state added

* Thu Nov 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.25-alt1
- add simple pam_ccreds support (without status and constraints)

* Tue Nov 13 2012 Andrey Cherepanov <cas@altlinux.org> 0.24-alt4
- Fix check avahi-daemon under systemd

* Mon Nov 12 2012 Andrey Cherepanov <cas@altlinux.org> 0.24-alt3
- Check avahi-daemon activity in more convinent way compatible with systemd

* Sat Nov 03 2012 Andrey Cherepanov <cas@altlinux.org> 0.24-alt2
- Don't hide local base selection if avahi-daemon is stopped

* Wed Oct 31 2012 Andrey Cherepanov <cas@altlinux.org> 0.24-alt1
- Autostart nslcd daemon if ldap or krb5 authentication is used
- Warning about stopped avahi-daemon
- Add avahi-daemon in requires

* Thu Oct 04 2012 Andrey Cherepanov <cas@altlinux.org> 0.23-alt1
- Support nss-ldapd

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
