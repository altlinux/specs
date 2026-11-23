%define _unpackaged_files_terminate_build 1

%def_with check

Name: ant-renamer-qt
Version: 3.2.0
Release: alt1

Summary: Rename many files at once
License: GPL-2.0-or-later
Group: File tools
Url: https://github.com/morfredus/ant-renamer-qt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)

%if_with check
BuildRequires: ctest
%endif

%description
Ant Renamer Qt renames many files and folders in one go: replace,
insert, move or delete text, enumerate, change case, regular expressions,
names taken from a list, and tags read from MP3 files (ID3) and from
images (EXIF, IPTC, XMP).

It is the C++/Qt 6 port of Ant Renamer by Antoine Potten, developed alongside the original program, with its language files and help.

%prep
%setup
sed -i "s|docs/screenshots/English/||" README.md

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc LICENSE README.md SECURITY.md docs/screenshots/English/modern-ui-light-single-screen-bands.png
%_bindir/antrenamer-qt
%dir %_datadir/antrenamer-qt
%dir %_datadir/antrenamer-qt/Languages
%_datadir/antrenamer-qt/Languages/*.lng
%dir %_datadir/antrenamer-qt/help
%_datadir/antrenamer-qt/help/*.md
%dir %_datadir/antrenamer-qt/help/img
%_datadir/antrenamer-qt/help/img/*.png
%_desktopdir/antrenamer-qt.desktop
%_iconsdir/hicolor/256x256/apps/antrenamer-qt.png
%_iconsdir/hicolor/scalable/apps/antrenamer-qt.svg
%_datadir/metainfo/fr.morfredus.AntRenamerQt.metainfo.xml

%changelog
* Mon Nov 23 2026 Nikolay Strelkov <snk@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus
