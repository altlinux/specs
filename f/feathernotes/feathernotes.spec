%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: feathernotes
Version: 1.3.2
Release: alt1

Summary: Hierarchical notes-manager
License: GPL-3.0-or-later
Group: Editors
Url: https://github.com/tsujan/feathernotes

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(hunspell)

%description
FeatherNotes is a lightweight Qt hierarchical notes-manager for Linux.
It is independent of any desktop environment.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %{name}.lang
%doc ChangeLog COPYING NEWS README.md screenshots
%_bindir/feathernotes
%_desktopdir/feathernotes.desktop
%_iconsdir/hicolor/scalable/apps/feathernotes.svg
%_iconsdir/hicolor/scalable/mimetypes/text-feathernotes-fnx.svg
%_datadir/metainfo/feathernotes.metainfo.xml
%_datadir/mime/packages/feathernotes.xml

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus
