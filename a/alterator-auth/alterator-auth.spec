%define _hooksdir %_sysconfdir/hooks/hostname.d

Name: alterator-auth
Version: 0.44.10
Release: alt2

Summary: Alterator module for system wide auth settings
License: GPL-2.0+
Group: System/Configuration/Other

Requires: alterator >= 4.7-alt4
Requires: alterator-l10n >= 2.9.114-alt1
Requires: pam-config >= 1.7.0-alt1
Requires: pam_krb5
Requires: libnss-myhostname
Requires: libnss-role >= 0.5.6-alt1
Requires: avahi-daemon
Requires: settime-rfc867
Requires: bind-utils
Requires: local-policy >= 0.4.8-alt1
Requires: alterator-default-configs >= 0.0.2-alt1

Source: %name-%version.tar

BuildRequires(pre): alterator >= 5.0
BuildRequires(pre): alterator-lookout
BuildRequires: guile22-devel

%filter_from_requires /^samba-common$/d;/^systemd/d;/^gpupdate$/d;/gpupdate-setup/d

%description
Alterator module for system wide auth settings

%package -n task-auth-ad-winbind
Summary: Metapackage to authenticate in Active Directory domain by winbind
Group: System/Configuration/Other
Requires: alterator-auth
Requires: samba-winbind
Requires: samba-winbind-clients
Requires: samba-common-tools
Requires: krb5-kinit
Requires: pam_mount
Requires: libnss-role
Requires: alterator-datetime
Requires: pam_propperpwnam
Requires: samba-winbind-dnsupdate
Requires: system-report
Requires: diag-domain-client

%description -n task-auth-ad-winbind
Metapackage to authenticate in Active Directory domain by Winbind.

%package -n task-auth-ad-sssd
Summary: Metapackage to authenticate in Active Directory domain by sssd
Group: System/Configuration/Other
Requires: alterator-auth
Requires: sssd-ad
Requires: samba-common-tools
Requires: krb5-kinit
Requires: pam_mount
Requires: libnss-role
Requires: alterator-datetime
Requires: sssd-dbus
Requires: alterator-roles-common
Requires: samba-winbind-clients
Requires: sssd-tools
Requires: adcli
Requires: pam_propperpwnam
Requires: system-report
Requires: diag-domain-client

Provides:  task-auth-ad = %EVR
Obsoletes: task-auth-ad < %EVR

%description -n task-auth-ad-sssd
Metapackage to authenticate in Active Directory domain by SSSD.

%package -n task-auth-ldap-sssd
Summary: Metapackage to authenticate in LDAP domain by sssd
Group: System/Configuration/Other
Requires: alterator-auth
Requires: sssd-ldap
Requires: sssd-krb5
Requires: krb5-kinit
Requires: pam_mount
Requires: libnss-role
Requires: alterator-roles-common

Provides:  task-auth-ldap = %EVR
Obsoletes: task-auth-ldap < %EVR

%description -n task-auth-ldap-sssd
Metapackage to authenticate in LDAP domain by SSSD.

%package -n task-auth-freeipa
Summary: Metapackage to authenticate in FreeIPA domain
Group: System/Configuration/Other
Requires: alterator-auth
Requires: freeipa-client
Requires: krb5-kinit
Requires: pam_mount
Requires: libnss-role
Requires: libsss_sudo
Requires: alterator-datetime
Requires: alterator-roles-common
Requires: pam_propperpwnam

%description -n task-auth-freeipa
Metapackage to authenticate in FreeIPA domain.

%package -n alterator-roles-common
Summary: Common package with default roles and privileges
Group: System/Configuration/Other
Requires: libnss-role >= 0.5.1

%description -n alterator-roles-common
Common package with default roles and privileges.
Contains basic roles: users, power and localadmins.

%prep
%setup

%build
%make_build libdir=%_libdir

%install
export GUILE_LOAD_PATH=/usr/share/alterator/lookout
%makeinstall
install -Dpm644 etc/user-groups %buildroot%_sysconfdir/alterator/auth/user-groups
install -Dpm644 etc/admin-groups %buildroot%_sysconfdir/alterator/auth/admin-groups
install -Dpm644 etc/role.d/users.role %buildroot%_sysconfdir/role.d/users.role
install -Dpm644 etc/role.d/powerusers.role %buildroot%_sysconfdir/role.d/powerusers.role
install -Dpm644 etc/role.d/localadmins.role %buildroot%_sysconfdir/role.d/localadmins.role
install -Dpm755 sbin/system-auth %buildroot/%_sbindir/system-auth
install -Dpm755 hooks/auth %buildroot/%_hooksdir/90-auth
rm -f %buildroot%_libexecdir/alterator/hooks/auth

%pre -n alterator-roles-common
%_sbindir/groupadd -r -f -g 98 everyone 2> /dev/null ||:
#_sbindir/groupadd -r -f -g 99 nobody 2> /dev/null ||:
#_sbindir/groupadd -r -f -g 100 users 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 101 localadmins 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 102 powerusers 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 103 guests 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 104 accountops 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 105 serverops 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 106 printops 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 107 backupops 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 108 replicators 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 109 networkops 2> /dev/null ||:
%_sbindir/groupadd -r -f -g 110 remote 2> /dev/null ||:

%files
%config(noreplace) %_sysconfdir/alterator/auth/user-groups
%config(noreplace) %_sysconfdir/alterator/auth/admin-groups
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_libdir/ui/auth/*.go
%_sbindir/system-auth
%_hooksdir/90-auth
%_alterator_backend3dir/*

%files -n alterator-roles-common
%config(noreplace) %_sysconfdir/role.d/users.role
%config(noreplace) %_sysconfdir/role.d/powerusers.role
%config(noreplace) %_sysconfdir/role.d/localadmins.role

%files -n task-auth-ad-winbind

%files -n task-auth-ad-sssd

%files -n task-auth-ldap-sssd

%files -n task-auth-freeipa

%changelog
* Wed Sep 18 2024 Andrey Cherepanov <cas@altlinux.org> 0.44.10-alt2
- task-auth-ad*: added diagnostic tools.
- task-auth-ad-winbind: added samba-winbind-dnsupdate.

* Thu May 30 2024 Andrey Limachko <liannnix@altlinux.org> 0.44.10-alt1
- system-auth: ad: change from admin credential to host for correct
  ACL issuance during DNS registration (thx Sozonov Evgenii)

* Sun Feb 25 2024 Andrey Limachko <liannnix@altlinux.org> 0.44.9-alt1
- system-auth: ad: enable winbind service in sssd mode

* Fri Feb 02 2024 Andrey Cherepanov <cas@altlinux.org> 0.44.8-alt1
- system-auth: ad: disabled conflicted auth service.

* Thu Nov 23 2023 Andrey Cherepanov <cas@altlinux.org> 0.44.7-alt1
- system-auth: remove extra quote in usage output (ALT #48139)

* Thu Oct 19 2023 Andrey Cherepanov <cas@altlinux.org> 0.44.6-alt1
- system-auth: fix join to sub OU (ALT #44924)

* Fri Oct 13 2023 Andrey Cherepanov <cas@altlinux.org> 0.44.5-alt3
- Fix autoreq filters: hostnamectl is in systemd package
- Remove orphaned hook file
- Specified license with version.

* Wed Oct 11 2023 Michael Shigorin <mike@altlinux.org> 0.44.5-alt2
- E2K: move to guile22 too
- minor spec cleanup (see also ALT#46206)

* Tue Sep 19 2023 Andrey Cherepanov <cas@altlinux.org> 0.44.5-alt1
- Requires pam_propperpwnam for join to AD and FreeIPA to ignore login name in different forms.
- system-auth: add --gpo to use GPO after join machine to Active Directory.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 0.44.4-alt1
- Fix join with passwords beginning from - symbol

* Sat May 27 2023 Andrey Limachko <liannnix@altlinux.org> 0.44.3-alt1
- Fix missing OS version for Sisyphus Regular builds

* Sun May 07 2023 Andrey Cherepanov <cas@altlinux.org> 0.44.2-alt1
- Pass OS name and version diring join to Active Directory (ALT #46071). Thanks Sergey Sysoev.

* Wed Mar 01 2023 Andrey Cherepanov <cas@altlinux.org> 0.44.1-alt1
- Fix auth in Active Directory with task-auth-ad-winbind without task-auth-ad-sssd.

* Mon Feb 20 2023 Andrey Cherepanov <cas@altlinux.org> 0.44.0-alt1
- Many improvements by sin@ and kaa@:
- Disable Username and Password edit boxes activity when kerberos ccache using.
- Add support for switching between sssd and winbind during join to AD.
- Avoid to use default credential cache with password authentication and place login/password credential pair as command line option to net utility.
- Add support of using default kerberos credential cache during join to AD.
- Don't show gpupdate checkbox for ipa join (ALT#45154).
- Check Active Directory computer name condition by RFC952 and fix regression with not changing static hostname after reboot.
- Computer name and static hostname restrictions when typing into a domain.

* Wed Sep 28 2022 Andrey Cherepanov <cas@altlinux.org> 0.43.15-alt1
- Support custom computer OU and Windows 2003 during join to Active Directory.

* Tue Jul 12 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.43.14-alt2
- task-auth-ad-sssd: add requires for sssd-tools and adcli for machine password

* Mon Jul 11 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.43.14-alt1
- Added functionality related to adding roles for domain groups.

* Mon Jul 04 2022 Ivan Savin <svn17@altlinux.org> 0.43.13-alt1
- Add new parameters when setting up AD.

* Wed Jun 08 2022 Ivan Savin <svn17@altlinux.org> 0.43.12-alt1
- Add ability to restore default configuration files.

* Wed Apr 27 2022 Ivan Savin <svn17@altlinux.org> 0.43.11-alt1
- Enlarged sssd settings window (ALT #42008)
- Replacing the apply button with ok in the sssd settings.

* Wed Aug 25 2021 Ivan Savin <svn17@altlinux.org> 0.43.10-alt1
- Add sssd settings.
- Add use of control libnss-role instead of write_nsswitch

* Tue Jul 27 2021 Lenar Shakirov <snejok@altlinux.org> 0.43.9-alt5
- backend: fix list ldap local_bases (namingContexts) (ALT #40569)
- sbin/system-auth: fix sssd package check, old LDAP auth scheme
  work again (ALT #40570)

* Sun Jul 04 2021 Andrey Cherepanov <cas@altlinux.org> 0.43.9-alt4
- Add libsss_sudo to task-auth-freeipa.

* Fri Nov 13 2020 Ivan Savin <svn17@altlinux.org> 0.43.9-alt3
- Fix an error message (the password is expired).

* Wed Oct 07 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.43.9-alt2
- Avoid dependency to gpupdate-setup due gpupdate mechanism is not mandatory.

* Wed Sep 30 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.43.9-alt1
- Enable Winbind with SSSD idmap for Active Directory secure channel.
- Synchronize SSSD and Winbind configuaration during join to AD.

* Sat Sep 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.43.8-alt2
- Add requires samba-winbind-clients to task-auth-ad-sssd metapackage

* Thu Sep 10 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.43.8-alt1
- Improve gpupdate enable/disable process

* Wed Jul 15 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.43.7-alt1
- Add default libnss-role roles for users, powerusers and localadmins in separated
  package: alterator-roles-common - common files for alterator-roles (not implemented yet).
- user-groups and admin-groups saved temporary for compatibility.
- Create aditional groups during alterator-roles-common install:
 + everyone (with prefered guid 98)
 + localadmins (with prefered guid 101)
 + powerusers (with prefered guid 102)
 + guests (with prefered guid 103)
 + accountops (with prefered guid 104)
 + serverops (with prefered guid 105)
 + printops (with prefered guid 106)
 + backupops (with prefered guid 107)
 + replicators (with prefered guid 108)
 + networkops (with prefered guid 109)
 + remote (with prefered guid 110)

* Sat Jul 04 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.43.6-alt1
- Add ad_gpo_access_control default as permissive for sssd.conf

* Wed Jul 01 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.43.5-alt1
- Add ad_gpo_ignore_unreadable and cache_credentials defaults for sssd.conf

* Fri Jun 19 2020 Andrey Cherepanov <cas@altlinux.org> 0.43.4-alt2
- Add changelog from p9 allows copy from sisyphus to p9.

* Tue Jun 09 2020 Andrey Cherepanov <cas@altlinux.org> 0.41-alt1.3.p9
- Place dns source immediately after files instead of disabling avahi-daemon service (ALT #37082).

* Tue Jun 09 2020 Andrey Cherepanov <cas@altlinux.org> 0.43.4-alt1
- Place dns source immediately after files instead of disabling avahi-daemon service (ALT #37082).

* Fri Jun 05 2020 Andrey Cherepanov <cas@altlinux.org> 0.43.3-alt1
- Disable avahi-daemon if login to .local domain is requested (ALT #37082).

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.43.2-alt1
- join_ipa_domain(): adapt dm and delete obsoleted fix for nsswitch.conf.

* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 0.43.1-alt1
- Fix hide user list for new version of lightdm.
- Do not remove local DNS from resolvconf.

* Mon Jun 01 2020 Andrey Cherepanov <cas@altlinux.org> 0.43-alt1
- Hide user list in Lightdm for domain login.

* Sat Apr 18 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.42-alt1
- task-auth-ad-sssd now depends on sssd-dbus allowing AD domain users
  to access D-Bus services like `systemctl` and etc.
- system-auth now display correctly message in case of wrong password or
  preauth failed.
- Add Enable Group Policy checkbox in credential dialog during join to AD.

* Wed Sep 11 2019 Andrey Cherepanov <cas@altlinux.org> 0.41-alt1
- Suppress error message during LDAP server check.

* Thu Apr 18 2019 Andrey Cherepanov <cas@altlinux.org> 0.40-alt1
- Do not require nss-ldap by default.
- Disable nscd if sssd is used.

* Wed Mar 20 2019 Andrey Cherepanov <cas@altlinux.org> 0.39-alt1
- Add package task-auth-ldap-sssd.
- Fix here-document blocks in system-auth for bash4.

* Fri Mar 15 2019 Andrey Cherepanov <cas@altlinux.org> 0.38-alt2
- Do not hide user in lightdm-gtk-greeter because it hides they at all.

* Wed Mar 13 2019 Andrey Cherepanov <cas@altlinux.org> 0.38-alt1
- Make ldap/krb5 authentication by SSSD instead on nss-ldapd.
- Use own parser to set values in /etc/krb5.conf.

* Wed Oct 03 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.37-alt1
- AD: configure sssd to obey the group policy
- AD: correctly update the (A) DNS record of the newly joined host

* Tue May 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.36-alt1
- Change entry files for ALT Domain from combobox to inputbox to support
  Astra Linux Directory.
- Check domain name in DNS first in AD and FreeIPA join.
- Add -d option for system-auth to show debug output.
- Do not change hostname during join process (ALT #33723).
- Fix typo in service file name (ALT #33224).

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.35-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Wed May 17 2017 Andrey Cherepanov <cas@altlinux.org> 0.35-alt1
- Remove gvfs-shares from task-auth-* metapackages (ALT #33481)
- Hide non-existing services list (ALT #33371)
- Hide roleadd warnings about non-existing groups (ALT #33372)

* Thu Apr 06 2017 Andrey Cherepanov <cas@altlinux.org> 0.34-alt1
- task-auth-ad now is provided by task-auth-ad-sssd
- Samba config cleanup, disable wins support
- Disable service nscd for sssd

* Wed Mar 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.33.1-alt1
- Wrap long line in warning

* Wed Mar 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.33-alt1
- Package task-auth-ad is not enough to auth with Active Directory
  because it uses non-recommended winbind
- [Active Directory] Fix DNS and Kerberos configuration
- Supress grep output in ipa_domain check

* Wed Mar 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.32.1-alt1
- Do not strict require ipa-client-install

* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.32-alt1
- Support join to FreeIPA domain

* Mon Feb 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.31-alt1
- Add new metapackage task-auth-ad-sssd for configure auth by SSSD
- Support SSSD for auth in Active Directory

* Tue Jan 31 2017 Andrey Cherepanov <cas@altlinux.org> 0.30.3-alt1
- Workaround to fix https://bugs.altlinux.org/32139 for system with old
  libshell 
- [SUCCESS=merge] in nsswitch.conf is supported only in 
  glibc-core >= 2.23. Remove this option for earlier version

* Thu Dec 29 2016 Andrey Cherepanov <cas@altlinux.org> 0.30.2-alt2
- Remove hostnamectl (systemd-services) from requirements

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
