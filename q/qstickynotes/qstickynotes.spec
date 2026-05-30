%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: qstickynotes
Version: 0.1
Release: alt1

Summary: Lightweight sticky notes application inspired by indicator-stickynotes
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/ivnish/QStickyNotes

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)

%description
QStickyNotes is a lightweight sticky notes application inspired by
indicator-stickynotes, but it is not a full clone.

%prep
%setup
sed -i 's|^Categories=.*|Categories=Utility;TextTools;|' QStickyNotes.desktop
sed -i 's|^Exec=.*|Exec=env QT_QPA_PLATFORM=xcb QStickyNotes|' QStickyNotes.desktop

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
* Sat May 30 2026 Nikolay Strelkov <snk@altlinux.org> 0.1-alt1
- Initial build for Sisyphus
