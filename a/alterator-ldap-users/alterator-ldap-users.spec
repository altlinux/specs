%define _altdata_dir %_datadir/alterator

Name: alterator-ldap-users
Version: 0.8
Release: alt3

Source: %name-%version.tar

Packager: Dmitriy Kruglikov <dkr@altlinux.org>

Summary: alterator module for ldap users administration
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Requires: alterator >= 4.11-alt1 ldap-user-tools >= 0.2 alterator-openldap-functions >= 0.2-alt2 alterator-auth >= 0.20-alt1
Requires: alterator-sh-functions >= 0.11-alt2
Requires: alterator-l10n >= 2.7-alt2
Requires: passwdqc-utils >= 1.2.2-alt1

Conflicts: alterator-fbi < 5.18-alt1

BuildPreReq: alterator >= 4.11-alt1

%description
alterator module for local and ldap users administration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_datadir/alterator/design/images/ldap-users/*
%_alterator_backend3dir/*
%_datadir/alterator/type/*

%changelog
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
