Name: alterator-net-bridge
Version: 0.2.2
Release: alt2

Url: http://altlinux.org/alterator
Source: %name-%version.tar

Summary: Alterator module for bridge interfaces
License: GPLv2+
Group: System/Configuration/Other

Requires: alterator >= 5.0
Requires: alterator-l10n
Requires: alterator-sh-functions >= 0.12-alt1
Requires: alterator-net-functions >= 2.0.0
Requires: alterator-net-eth >= 5.0.0
Requires: libshell >= 0.0.1-alt4
Requires: etcnet

BuildRequires(pre): alterator >= 5.0
BuildRequires: alterator-fbi
BuildRequires: guile22-devel

%define _unpackaged_files_terminate_build 1

%description
Alterator module for bridge network interfaces

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_libdir/ui/*
%_alterator_backend3dir/*

%changelog
* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 0.2.2-alt2
- NMU:
  + use guile22 on e2k too
  + clarify License:
  + minor spec cleanup

* Mon Sep 20 2021 Sergey V Turchin <zerg@altlinux.org> 0.2.2-alt1
- don't hardcode window size

* Mon Feb 10 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.1-alt1
- Add support of different bridge types

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Tue Apr 18 2017 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Changes for guile22.
- Add Qt UI.

* Wed Mar 23 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

