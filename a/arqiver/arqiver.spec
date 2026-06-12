%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: arqiver
Version: 1.0.2
Release: alt1

Summary: Simple Qt archive manager; front-end for libarchive, gzip and 7z
License: GPL-3.0-or-later
Group: Archiving/Compression
Url: https://github.com/tsujan/Arqiver

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: qt6-tools
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)

Requires: tar
Requires: p7zip
Requires: /usr/bin/bsdtar

%description
Arqiver can extract, create and edit archives that are supported by its
back-ends.

It can open archives by drag-and-drop. With 7z, it also supports password
protection.

%prep
%setup
sed -i "s/Categories=.*/Categories=Utility;Archiving;Compression;FileTools;/" data/arqiver.desktop

%build
lrelease-qt6 arqiver.pro
qmake-qt6 \
          CONFIG+=nostrip \
          QMAKE_CXXFLAGS="%optflags"

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%find_lang %name --with-qt

%files -f %{name}.lang
%doc ChangeLog COPYING NEWS README.md
%_bindir/arqiver
%_desktopdir/arqiver.desktop
%_iconsdir/hicolor/scalable/apps/arqiver.svg

%changelog
* Fri Jun 12 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- New version 1.0.2.

* Sun Dec 07 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
