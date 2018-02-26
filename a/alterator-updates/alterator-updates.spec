Name: alterator-updates
Version: 0.2
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Source:%name-%version.tar

Summary: dialog based interface for alterator
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.10-alt1
Requires: sisyphus-updates >= 0.1-alt4 avahi-tools
Requires: alterator-l10n >= 2.1-alt7
Conflicts: alterator-lookout < 1.6-alt4
Conflicts: alterator-fbi < 5.17-alt3

BuildArch: noarch

BuildPreReq: alterator >= 4.10-alt1


%description
dialog based interface for alterator

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall DESTDIR=%buildroot

%files
%_datadir/alterator/ui/*
%_datadir/alterator/type/*
%_alterator_backend3dir/*
%_datadir/alterator/applications/*

%changelog
* Mon Aug 03 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- use workflow 'none'
- share callbacks between qt and html ui

* Tue Apr 14 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt8
- move type definition to more convenient place

* Thu Apr 09 2009 Sir Raorn <raorn@altlinux.org> 0.1-alt7.1
- NMU:
 + backend3/updates: don't restart crond when changing autoupdate uptions

* Thu Apr 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- menu file: fix to group 'system'

* Mon Mar 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- fix module name

* Thu Feb 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- update interface for new behaviour of sisyphus-updates in local mode

* Thu Feb 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- fix url re

* Wed Feb 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- minor bugfixes
- add translations

* Mon Feb 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add html ui

* Fri Feb 06 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
