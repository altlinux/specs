%define _altdata_dir %_datadir/alterator

Name: alterator-ldap-users
Version: 0.8.6
Release: alt3

Summary: Alterator module for ldap users administration
License: GPLv2+
Group: System/Configuration/Other

Url: http://altlinux.org/alterator
Source: %name-%version.tar
Packager: Dmitriy Kruglikov <dkr@altlinux.org>

Requires: alterator >= 5.0
Requires: alterator-openldap-functions >= 0.2-alt2
Requires: alterator-auth >= 0.20-alt1
Requires: alterator-sh-functions >= 0.11-alt2
Requires: alterator-l10n >= 2.7-alt2
Requires: ldap-user-tools >= 0.2
Requires: passwdqc-utils >= 1.2.2-alt1

# Has to be optional: depens on Samba-DC.
#Recommends: netcmdplus

Requires: alterator-fbi >= 5.49.3

BuildRequires: guile-devel
BuildRequires: rpm-build >= 4.0.4-alt103
BuildRequires: alterator >= 5.0
BuildRequires: alterator-fbi >= 5.33-alt1

%description
Alterator module for local and LDAP user administration

%package -n alterator-usersource-functions
Summary: Common functions for user and group account data source management
License: GPLv2+
Group: Development/Other

%description -n alterator-usersource-functions
Common functions for user and group account data source management.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_libdir/ui/*/
%_alterator_datadir/type/*
%_alterator_libdir/type/*
%_alterator_backend3dir/*
%_alterator_datadir/design/images/ldap-users/*

%files -n alterator-usersource-functions
%_bindir/alterator-*-functions

%changelog
* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 0.8.6-alt3
- NMU:
  + clarify License:
  + minor spec cleanup

* Tue Apr 19 2022 Paul Wolneykien <manowar@altlinux.org> 0.8.6-alt2
- Switch to the branch's default version of Guile (guile-devel).

* Mon Dec 06 2021 Paul Wolneykien <manowar@altlinux.org> 0.8.6-alt1
- Require alterator-fbi >= 5.49.3 for upload and UI fixes.
- Hide the photo frame for AD (closes: 41391).
- Fix current user selection in the user list.
- Fix: Return error on trying to upload a photo for AD user.
- Display the unset login shell as 'Default shell' (closes: 41389).

* Sat May 25 2019 Michael Shigorin <mike@altlinux.org> 0.8.5-alt2
- minor spec fixup/cleanup

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.8.5-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Thu Aug 31 2017 Paul Wolneykien <manowar@altlinux.org> 0.8.5-alt1
- Fix: Disallow to modify the user full name fields for "CN=FullName"
  records.
- Fixed update of aux parameters for "CN=FullName" AD records.
- Fix: AD: Read the user patronym properly.
- Fix: Don\'t overtrim the error messages (closes: #33833).
- Fix: Output "(Active Directory)" comment when an AD source
  is selected.

* Mon May 22 2017 Paul Wolneykien <manowar@altlinux.org> 0.8.4-alt3
- Extract common functions for user and group account data source
  management in the separate package.
- Fixed: Pass the remote host when is listing remote bases.

* Wed May 17 2017 Paul Wolneykien <manowar@altlinux.org> 0.8.4-alt2
- Fixed "netcmdplus" package detection.

* Wed May 17 2017 Paul Wolneykien <manowar@altlinux.org> 0.8.4-alt1
- Support local Samba DC user administration with the help of netcmdplus package.

* Wed Nov 19 2014 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1
- Fix email list.

* Thu Nov 06 2014 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1
- Hide user settings if no user is selected.

* Thu Aug 07 2014 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Setup UID filter at start.
- Fix min_uid for regular users.

* Fri May 31 2013 Andrey Cherepanov <cas@altlinux.org> 0.8-alt8
- Fix button look by use standard definition

* Tue Apr 23 2013 Andrey Cherepanov <cas@altlinux.org> 0.8-alt7
- Support localization of ldap-user-tools helper scripts output

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.8-alt6
- Make photo replacemet picture more abstract
- Remove fixed size for file selector that made it truncated
- Don't distribute button in source selection

* Thu Dec 06 2012 Andrey Cherepanov <cas@altlinux.org> 0.8-alt5
- Perform direct group management without caching (ALT #27882)
- Fix behaviour in mode with tcb source

* Wed Dec 05 2012 Andrey Cherepanov <cas@altlinux.org> 0.8-alt4
- Show default user photo even no user selected
- Make interface more compact
- Fix small typo on Cancel button
- New default photo picture

* Wed Jul 20 2011 Paul Wolneykien <manowar@altlinux.ru> 0.8-alt3
- Mark the configuration file is present in the case of localhost
  based ldap/krb5 (closes 25932).
- Process 'krb5' mode the same way as 'ldap' (closes 25931).

* Tue Mar 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt2
- assume krb5 if server role=master
- set ENABLE_KRB at runtime

* Thu Mar 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- kerberos support resurrect
- support for ldap on localhost, but named differently

* Fri Feb 25 2011 Timur Aitov <timonbl4@altlinux.org> 0.7-alt3
- Added Department and Address fields
- Added lists for Title and Department
- Auto complete Organization field during creation user

* Wed Dec 15 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.7-alt2
- Fixed bugs: #24488

* Mon Nov 22 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.7-alt1
- Fixed bugs: #24276, #24488, #23224, #24486

* Wed Apr 14 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt3
- E-Mail editor returned to previous state

* Wed Apr 14 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt2
- Added Multisource (test)

* Fri Apr 02 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.6-alt1
- Added Migration tools (fot test reading data. Without write functions)
- Added filtration by UID

* Fri Mar 26 2010 Dmitriy Kruglikov <dkr@altlinux.org> 0.5-alt10
- Added Group's membership management (test)
- Added editable listbox for user's emails

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt9
- show message on successful update

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt8
- use file_list_add() and file_list_del() from latest alterator-sh-functions

* Mon Sep 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt7
- use telephone-number type
- use workflow 'none'
- redesign e-mail edition

* Wed Sep 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt6
- improve labels

* Wed Sep 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- improve html ui layout, use accordion widget

* Fri Sep 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- account creating: improve error messages
- e-mail edition: improve error messages (closes: #21399)

* Mon Aug 24 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt3.2
- fixed #21184 trying to init user homedir

* Fri Aug 21 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt3.1
- fixed #20986 check email address type

* Thu May 21 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt3
- improved user management
- added multiple user deletion
- added multiple user's email deletion

* Thu May 14 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt2.1
- fixed #19971
- fixed #19954

* Thu May 07 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt2
- fixed #19931 incorrect error reporting for new username
- removing user from all groups (action delete)

* Fri May 01 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt1
- new ldap-users (now using ajax)

* Thu Apr 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt2
- rewrote error handling

* Wed Apr 29 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt1
- fixed backend due to new ldap-user-tools and alterator-openldap-functions 

* Fri Feb 27 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt3
- added fixes due to changes in ldap-user-tools

* Tue Feb 10 2009 Sir Raorn <raorn@altlinux.ru> 0.3-alt2
- Fix typo in "is_active" parameter name

* Fri Feb 06 2009 Sir Raorn <raorn@altlinux.ru> 0.3-alt1
- [0.3]
 + Updated for 5.0 Office Server

* Wed Feb 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt1.M50.2
- added translation and help files

* Tue Feb 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt1.M50.1
- build for 5.0

* Tue Feb 03 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt1.M41.1
- fixed release

* Mon Feb 02 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt1.M41
- using alterator_api_version 1

* Fri Jan 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M41.1
- working version for school server

* Wed Jan 28 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M41
- removed alterator-users parts

* Wed Jan 28 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt1.M41
- clone of alterator-users
