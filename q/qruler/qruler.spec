# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qruler
Version: 0.1.1
Release: alt2.20230818

Summary: A simple on-screen pixel meter, based on IRuler
License: GPL-2.0-or-later
Group: Graphical desktop/Other

Url: https://github.com/qtilities/qruler
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: qtilitools
BuildRequires: qt5-base-devel qt5-tools-devel

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_datadir/%name/
%_datadir/metainfo/io.github.qtilities.QRuler.appdata.xml
%_desktopdir/io.github.qtilities.QRuler.desktop
%doc COPYING README.md
%_iconsdir/hicolor/scalable/apps/io.github.qtilities.QRuler.svg

%changelog
* Tue Sep 05 2023 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt2.20230818
- Fix Url

* Sun Aug 20 2023 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1.20230818
- initial build
