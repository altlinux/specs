%define _unpackaged_files_terminate_build 1

Name: adt
Version: 0.1.13
Release: alt1

Summary: ALT Diagnostic tool
License: GPLv2+
Group: Other
Url: https://altlinux.space/alterator/adt

Provides: alterator-application-diagnostic-tool

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-base-common
BuildRequires: boost-devel-headers
BuildRequires: libtomlplusplus-devel
BuildRequires: doxygen

BuildRequires: desktop-file-utils ImageMagick-tools

Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.29
Requires: alterator-interface-diag >= 0.1.4
Requires: libtomlplusplus
Requires: icon-theme-adwaita-legacy

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
%_desktopdir/ru.basealt.adt.desktop
%_datadir/alterator/applications/adt.application
%_iconsdir/hicolor/scalable/apps/adt.svg
%_datadir/alterator/backends/adt.backend
%_man1dir/%name.1*

%changelog
* Fri Nov 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.13-alt1
- Add 'exit_status = true' for new version of executor.
- Rename desktop entry to be properly displayed in Gnome (thx Andrey Alekseev).
- Add report bus selection (thx Andrey Alekseev).

* Wed Aug 27 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.12-alt1
- fix size constraint of labels with tests on buses
- fix translation by system locale
- fix transparent tips in tool bar (closes: #55686)
- add --bus option (thx Andrey Alekseev)
- fix searching tool by path in cli (thx Andrey Alekseev)
- add margins and bold text to tool variable names (thx Andrey Alekseev)
- disable selection in variables table (thx Andrey Alekseev)
- add splitter margins (thx Andrey Alekseev)
- fix apply parameters immediately (thx Andrey Alekseev)
- fix wrap editors to prevent from text highlighting (thx Andrey Alekseev)
- fix set proper fonts to calculate elided text correctly (thx Andrey Alekseev)
- add menu bar (thx Andrey Alekseev)

* Mon Jul 07 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.11-alt2
- fix URL in .spec file

* Wed May 21 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.11-alt1
- implemented parameters for the tool

* Tue Apr 08 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.10-alt1
- fix tests filter

* Wed Feb 26 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.9-alt2
- fix test's log widget content
- fix tests status in testswidget
- fix tests translations

* Tue Feb 25 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.9-alt1
- move to qt6

* Wed Feb 19 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.8-alt1
- fix gui and cli
- model refactor
- add CHANGELOG.md

* Fri Dec 13 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.7-alt2
- fix model translation
- fix gui contoller
- fix cli controller
- fix .backend and .application file

* Wed Dec 11 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.7-alt1
- add journal save button
- add stop dialog
- add messages to status bar
- update translation
- move to toml

* Mon Oct 21 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.6-alt1
- change prefix from ru.basealt to org.altlinux

* Fri Oct 04 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.5-alt1
- remove horizontal scrollbar in test widget
- implement test status reset
- fix report suffix

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
