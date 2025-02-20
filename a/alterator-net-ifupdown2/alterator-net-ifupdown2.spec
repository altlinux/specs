%define _unpackaged_files_terminate_build 1


Name: alterator-net-ifupdown2
Version: 1.0.2
Release: alt2

Source:%name-%version.tar

Summary: Alterator module for PVE network setup
License: GPLv3
Group: System/Configuration/Other

BuildArch: noarch
Requires: alterator >= 5.0 libshell >= 0.1.3
Requires: alterator-l10n
Requires: alterator-sh-functions >= 0.12-alt1
Requires: alterator-hw-functions >= 0.7-alt2
Requires: libshell >= 0.1.3
Requires: ifupdown2

BuildRequires(pre): alterator >= 5.0
BuildRequires: alterator-fbi
BuildRequires: guile22-devel


%description
Alterator module for PVE network setup

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_backend3dir/*

%changelog
* Wed Feb 19 2025 Sergey Konev <darisishe@altlinux.org> 1.0.2-alt2
- Added localization and 'help' page (see alterator-l10n)
- Minor Makefile refactoring

* Fri Jan 17 2025 Sergey Konev <darisishe@altlinux.org> 1.0.2-alt1
- Provided functionality to set VLAN ID for bridge vmbr0 (optionally)
- Minor bug with interface's on-back button was fixed
- Got rid of web-interface (needless for this module)

* Wed Nov 20 2024 Alexey Shabalin <shaba@altlinux.org> 1.0.1-alt0.1
- Initial build package (based on alterator-net-eth)

