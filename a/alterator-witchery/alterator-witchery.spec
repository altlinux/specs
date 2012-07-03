Summary: demo steps for alterator-wizard

Name: alterator-witchery
Version: 0.3
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar

License: GPL
Group: System/Configuration/Other

Requires: alterator-wizardface >= 1.1-alt1

BuildPreReq: alterator >= 4.10-alt6

%description
demo steps for alterator-wizard

%prep
%setup -q

%install
%makeinstall

%files
%config(noreplace) %_sysconfdir/alterator/witchery
%_datadir/alterator/steps/*
%_datadir/alterator/ui/*
%_datadir/alterator/help/*/*

%changelog
* Thu Nov 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- remove unused html interfaces

* Thu May 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- move step definitions and step list to other place
- add samples for future installer with html UI

* Tue Aug 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- improve ui file layout

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- update to new wf

* Thu Jan 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- fix step description, remove unused help files

* Mon Oct 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
