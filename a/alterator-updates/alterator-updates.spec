Name: alterator-updates
Version: 0.2.2
Release: alt2

Summary: Module to configure automatic system updates
License: GPLv2+
Group: System/Configuration/Other

Url: http://altlinux.org/alterator
Source: %name-%version.tar
Packager: Stanislav Ievlev <inger@altlinux.org>

Requires: alterator >= 5.0
Requires: sisyphus-updates >= 0.1-alt4
Requires: alterator-l10n >= 2.1-alt7
Requires: altlinux-repos
Requires: avahi-tools

Conflicts: alterator-lookout < 1.6-alt6
Conflicts: alterator-fbi < 5.18-alt1

BuildRequires: guile22-devel
BuildRequires: rpm-build >= 4.0.4-alt103
BuildRequires: alterator >= 5.0
BuildRequires: alterator-fbi >= 5.33-alt1

%description
Module to configure automatic, schedule-based system updates.

%prep
%setup

%build
%make_build libdir=%_libdir

%install
%makeinstall DESTDIR=%buildroot

%files
%_alterator_datadir/ui/*
%_alterator_libdir/ui/*
%_alterator_datadir/type/*
%_alterator_libdir/type/*
%_alterator_backend3dir/*
%_alterator_datadir/applications/*

%changelog
* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 0.2.2-alt2
- NMU:
  + use guile22 on e2k too
  + clarify License:
  + minor spec cleanup

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Fri May 19 2017 Paul Wolneykien <manowar@altlinux.org> 0.2.2-alt1
- Enable and start crond when a new schedule is written (closes: 33450).

* Wed Mar 11 2015 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Replace shell-regexp with shell-quote.

* Mon Jun 03 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2-alt2
- add R: altlinux-repos

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
