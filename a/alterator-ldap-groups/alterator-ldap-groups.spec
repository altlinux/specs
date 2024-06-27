%define _hooksdir %_sysconfdir/hooks/hostname.d

Name: alterator-ldap-groups
Version: 0.6.7
Release: alt2

Url: http://altlinux.org/alterator
Source: %name-%version.tar
Packager: Andrey Cherepanov <cas@altlinux.org>

Summary: Alterator module for LDAP groups administration
License: GPLv2
Group: System/Configuration/Other

Requires: alterator >= 5.0
Requires: alterator-auth >= 0.9-alt3
Requires: alterator-sh-functions >= 0.11-alt2
Requires: alterator-l10n >= 2.7-alt6
Requires: ldap-user-tools >= 0.2
Requires: shadow-groups >= 4.0.4.1-alt9

Conflicts: alterator-fbi < 5.18-alt1
Conflicts: netcmdplus < 0.1.1

Obsoletes: alterator-ldap-groups-school-server < %version
Provides:  alterator-ldap-groups-school-server = %version-%release

BuildRequires: guile22-devel
BuildRequires: alterator >= 5.0
BuildRequires: alterator-fbi >= 5.33-alt1

%description
Alterator module for LDAP groups administration

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%config(noreplace) %_sysconfdir/alterator/ldap-groups
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_libdir/ui/*/
%_alterator_datadir/type/*
%_alterator_libdir/type/*
%_alterator_backend3dir/*
%_hooksdir/91-ldap-groups

%changelog
* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 0.6.7-alt2
- NMU:
  + use guile22 on e2k too
  + clarify License:
  + add Url:
  + minor spec cleanup

* Tue Aug 21 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.7-alt1
- Use strict data types for the "group", "member_in" and "member_out"
  parameters.

* Thu May 31 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.6-alt3
- Don't require a particular rpm-build version.

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.6-alt2.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Thu Aug 31 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.6-alt2
- Fix: Output "(Active Directory)" comment when an AD source
  is selected.
- Fix: Switch to the selected AD database (closes: #33834).
  
* Mon May 22 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.6-alt1
- Support Samba DC group management.

* Tue Jul 08 2014 Mikhail Efremov <sem@altlinux.org> 0.6.5-alt1
- Fix addition/removal local groups.

* Mon Jun 10 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1
- No wrap checkbox text
- Localization support for system group combobox

* Thu Jun 06 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.3-alt1
- Add mapping to system UNIX and Samba group

* Fri May 31 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt3
- Fix button look by use standard definition

* Tue Apr 23 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt2
- Disable show of group flags (default, local)
- Don't distribute button in source selection

* Thu Nov 01 2012 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt1
- Support empty lines and comments beginning from # in group-init-list
- Add groups 'users' and 'admins' for NT domain

* Thu Oct 25 2012 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- Move init script from firsttime.d to hostname.d hooks directory.
  Please, run /etc/hooks/hostname.d/91-ldap-groups manually
  to create initial groups for existing domain (ALT #24494)
- Obsoletes alterator-ldap-groups-school-server package
- Hide registered workstations groups (with trailing $)
- Support School Server specific default groups. If they are
  unnecessary, just remove it manually

* Wed Dec 15 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt2
- Released as  0.6-alt2 for test

* Wed Nov 24 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt1
- Manage local and LDAP groups.

* Fri Apr 02 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.5-alt1
- Redesigned membership.
- Fixed bug with space in group name.

* Mon Oct 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- fix typo in desktop file

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- show message on successful update

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- redesign email and member edition
- use workflow 'none'

* Wed Sep 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- move hook into firsttime.d
- improve html ui (closes: #21566)
- use constraints for e-mail (closes: #21400)

* Wed Sep 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add initial group list (closes: #21222)

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt5.1
- added requires alterator-l10n and alterator-fbi
- fixed group_del

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt5
- improved ui management
- added multiple group deletion

* Thu May 14 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt4.1
- fixed #19971
- fixed #19954

* Thu May 07 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt4
- fixed #19932: multiple select of users

* Mon May 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt3
- fixed #19880 (ldap groups with space in name)

* Thu Apr 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2
- rewrote error handling

* Mon Apr 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt1
- initial build
