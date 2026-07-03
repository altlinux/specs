%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: kdevelop-php
Version: 26.04.3
Release: alt1

Summary: PHP language plugin for KDevelop
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/kdevelop/kdev-php

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt6-tools-devel
BuildRequires: kdevelop-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-ktexteditor-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kdevelop-pg-qt

ExcludeArch: %ix86 riscv64

Requires: kdevelop

%description
KDevelop is an easy to use integrated development environment for KDE.
It supports a wide range of programming languages and features project
management, an advanced editor, a class browser and an integrated debugger.

This package contains the PHP language support plugin.

%prep
%setup

%build
%cmake \
       -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

# do not package the development stuff
rm -rfv %buildroot%_includedir
rm -rfv %buildroot%_libdir/cmake

%find_lang kdevphp

%files -f kdevphp.lang
%_libdir/libkdevphpcompletion.so
%_libdir/libkdevphpduchain.so
%_libdir/libkdevphpparser.so
%_libdir/qt6/plugins/kdevplatform/*/kdevphpdocs.so
%_libdir/qt6/plugins/kdevplatform/*/kdevphplanguagesupport.so
%_libdir/qt6/plugins/kdevplatform/*/kdevphpunitprovider.so
%_datadir/kdevappwizard/templates/simple_phpapp.tar.bz2
%dir %_datadir/kdevphpsupport
%_datadir/kdevphpsupport/*.php
%_datadir/metainfo/org.kde.kdev-php.metainfo.xml
%_datadir/qlogging-categories6/kdevphpsupport.categories

%changelog
* Fri Jul 03 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.3-alt1
- New version 26.04.3.

* Wed Jun 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- Initial build for Sisyphus
