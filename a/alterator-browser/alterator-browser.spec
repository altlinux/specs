%define _unpackaged_files_terminate_build 1

Name: alterator-browser
Version: 0.1.3
Release: alt1

Summary: Revised alterator
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-browser

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-base-common
BuildRequires: boost-devel-headers

Requires: alterator
Requires: alterator-manager
Requires: alterator-module-executor
Requires: alterator-module-legacy
Requires: alterator-module-categories
Requires: alterator-interface-application

Source0: %name-%version.tar

%description
Alterator operating via D-Bus.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/alterator-browser
%doc *.md
%_bindir/%name

%changelog
* Tue Apr 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- fix builder to comply with spec
- integrated with AMP
- brought up to specification
- update and combine docs into readme.md
- log outputs of application runs

* Fri Feb 16 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- closes window after running acc
- add toolbar with button running acc
- fix loadnig and installing translator
- add Ctrl+q shortcut to main window

* Sun Jan 28 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

* Wed Oct 25 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- added support for acc files

* Wed Jul 5 2023 Kozyrev Yuri <kozyrevid@altlinux.org> 0.0.1-alt1
- initial build
