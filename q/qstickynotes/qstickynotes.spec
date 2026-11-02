%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: qstickynotes
Version: 0.1
Release: alt2

Summary: Lightweight sticky notes application inspired by indicator-stickynotes
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/ivnish/QStickyNotes

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)

%description
QStickyNotes is a lightweight sticky notes application inspired by
indicator-stickynotes, but it is not a full clone.

%prep
%setup
%__subst 's|^Categories=.*|Categories=Utility;TextTools;|' QStickyNotes.desktop
%__subst 's|^Exec=.*|Exec=env QT_QPA_PLATFORM=xcb QStickyNotes|' QStickyNotes.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md screenshots
%_bindir/QStickyNotes
%_desktopdir/QStickyNotes.desktop
%dir %_datadir/QStickyNotes
%_datadir/QStickyNotes/*

%changelog
* Sun Nov 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.1-alt2
- Spec refined.

* Sat May 30 2026 Nikolay Strelkov <snk@altlinux.org> 0.1-alt1
- Initial build for Sisyphus
