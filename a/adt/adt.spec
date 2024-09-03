%define _unpackaged_files_terminate_build 1

Name: adt
Version: 0.1.4
Release: alt1

Summary: ALT Diagnostic tool
License: GPLv2+
Group: Other
Url: https://gitlab.basealt.space/alt/adt

Provides: alterator-application-diagnostic-tool

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-base-common
BuildRequires: boost-devel-headers
BuildRequires: doxygen

BuildRequires: desktop-file-utils ImageMagick-tools

Requires: alterator-manager
Requires: alterator-module-executor
Requires: alterator-interface-diag

Source0: %name-%version.tar

%description
ADT (Alt Diagnostic Tool) is a utility for diagnosing software problems using the alterator-interface-diag1 interface.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%_datadir/alterator/applications
install -v -p -m 644 -D setup/adt.application %buildroot%_datadir/alterator/applications
install -p -D man/en/%name.man %buildroot%_mandir/man1/%name.1
install -p -D man/ru/%name.man %buildroot%_mandir/ru/man1/%name.1
%find_lang --with-man %name

%files -f %name.lang
%doc README.md
%doc INSTALL.md

%_bindir/adt
%_desktopdir/adt.desktop
%_datadir/alterator/applications/adt.application
%_iconsdir/hicolor/scalable/apps/adt.svg
%_datadir/alterator/backends/adt.backend
%_man1dir/%name.1*

%changelog
* Tue Sep 03 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.4-alt1
- session bus test support
- new UI design
- add manual
- fix run list of tests and display name

* Tue Apr 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt3
- add main icon
- fix exec field in .desktop file

* Wed Feb 28 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt2
- add the ability to use custom icons for the tools
- align with specification

* Fri Dec 15 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- add Report method for diagnostic tool
- adaptation for Alterator Entry

* Tue Oct 17 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- Changed method names for the interface alterator-manager 1.18
- fix alterator.interface.diag1 documentation

* Wed Jun 28 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- Use alterator-module-executor to get tools and tests

* Wed Dec 07 2022 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt1
- Initial build
