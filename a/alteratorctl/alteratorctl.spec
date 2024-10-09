%define _unpackaged_files_terminate_build 1

Name: alteratorctl
Version: 0.0.5
Release: alt3

Summary: CLI for alterator browser
License: GPL-2.0+
Group: System/Configuration/Other

BuildRequires: cmake gcc glib2-devel libdbus-glib-devel libgio-devel

Source0: %name-%version.tar

%description
A command line tool for using DBus objects

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name
%_datadir/alteratorctl/lang/ru/LC_MESSAGES/%name.mo

%changelog
* Wed Oct 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt3
- two ways of getting information about an object are implemented: plain text and keyed parsed content
- fix components and packages modules

* Fri Sep 27 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt2
- fix component module
- implement obtaining information about the object both in text and parsed form

* Mon Sep 16 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt1
- implement Alterator Entry parsing
- add diag module

* Thu Aug 22 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.4-alt1
- add common method
- refactor internal client modules to check objects and interfaces
- locale fix
- add translations

* Wed Jul 31 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.3-alt1
- refactor manager module
- implement diag module

* Tue Jul 23 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.2-alt1
- implement manager, packages and components modules

* Sun Jun 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.1-alt1
- initial build
