%define _hooksdir %_libexecdir/alterator/hooks/firsttime.d

Name: alterator-ldap-groups-school-server
Version: 0.4
Release: alt6

Source: %name-%version.tar

Packager: Lebedev Sergey <barabashka@altlinux.org>

Summary: alterator module for ldap groups administration
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Requires: alterator >= 2.9 ldap-user-tools >= 0.2 alterator-auth >= 0.9-alt3
Requires: alterator-sh-functions >= 0.11-alt2
Requires: alterator-l10n >= 2.7-alt6
Conflicts: alterator-fbi < 0.16-alt2
Obsoletes: alterator-ldap-groups
Provides: alterator-ldap-groups = %version-%release

BuildPreReq: alterator >= 3.2-alt3 
BuildRequires: alterator-l10n alterator-fbi

%description
alterator module for ldap groups administration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%config(noreplace) %_sysconfdir/alterator/ldap-groups
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*
%_hooksdir/91-ldap-groups

%changelog
* Tue Dec 07 2010 Andrey Cherepanov <cas@altlinux.org> 0.4-alt6
- continue work on creation error (eg. group is exist)
- add ability to create non-system group

* Mon Dec 06 2010 Andrey Cherepanov <cas@altlinux.org> 0.4-alt5
- rebuild

* Wed Dec 01 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4-alt4
- Added Rujel groups
- Renamed to alterator-ldap-groups-school-server

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
