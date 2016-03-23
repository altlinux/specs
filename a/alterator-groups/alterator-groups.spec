Name:    alterator-groups
Version: 0.6
Release: alt1

Summary: Alterator module for system groups administration
License: GPL
Group:   System/Configuration/Other

Source:  %name-%version.tar
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch

Requires: gettext
Requires: alterator-sh-functions >= 0.6-alt1

# we need alterator-read-desktop from alterator >= 3.6-alt7
Requires: alterator >= 3.6-alt7

BuildPreReq: alterator >= 3.6-alt7
Conflicts: alterator-fbi < 0.15-alt1
Conflicts: alterator-lookout < 1.0

%description
%summary

%prep
%setup -q

%build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_sysconfdir/alterator/*/
%_alterator_backend3dir/*

%changelog
* Wed Mar 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1
- Refactoring interface: manage members in two lists
- Simplify group filter

* Mon Jun 01 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- change module name to "Local groups" (closes: #19930)
- fix spec to avoid ownerless dirs
- update translations in groups.desktop

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt4
- move templates/* to ui/
- move help and translations to alterator-l10n

* Wed Sep 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt3
- rebuild with new alterator-l10n

* Wed Sep 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt2
- sort group list
- tune labels
- use explicit widget attributes (qt ui)
- change Add Group button (qt ui)

* Tue Sep 23 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt1
- remove _* groups from the list
- fix help
- fix empty list crash (qt ui)
- remove group counter (qt ui)
- move add group dialog on top (qt ui)
- tune labels
- add html ui

* Wed Sep 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- merge simple and expert interfaces

* Tue Sep 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt12
- change default values in checkboxes in expert ui

* Tue Sep 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt11
- fix labels in expert ui

* Mon Sep 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt10
- fix empty list crash

* Mon Sep 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt9
- fix #16570 (use alterator-dump-desktop)

* Thu Jul 31 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt8
- fix #16483 (crashes on empty group lists)

* Wed Jul 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt7
- add help

* Wed Jul 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt6
- fixes in backend and ui

* Wed Jul 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt5
- rebuild with alterator-l10n

* Wed Jul 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt4
- error on adding existing group
- sort groups by gid in simple mode

* Wed Jul 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt3
- simple mode
  - add users from the list
  - create/delete user groups
- changes in simple and expert interfaces

* Tue Jul 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt2
- expert mode:
  - add primary group filter
  - fix system group filter (use /etc/login.defs)
  - change group filter ui

* Mon Jul 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt1
- use desktop-files (simple and expert qt interfaces)

* Fri Jul 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt2
- rebuild with alterator-l10n

* Wed Jul 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt1
- initial version

