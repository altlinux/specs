%define _stripped_files_terminate_build 1

%define rname kdev-php
%define sover 6
%define libkdevphpcompletion libkdevphpcompletion%sover
%define libkdevphpduchain libkdevphpduchain%sover
%define libkdevphpparser libkdevphpparser%sover

Name: kdevelop-php
Version: 26.04.3
Release: alt2
%K6init

Group: Development/Other
Summary: PHP language plugin for KDevelop
License: GPL-2.0-or-later
Url: https://invent.kde.org/kdevelop/kdev-php

ExcludeArch: %not_qt6_qtwebengine_arches
Requires: kdevelop

Source: %rname-%version.tar
Patch1: alt-soname.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: cmake extra-cmake-modules
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

%description
KDevelop is an easy to use integrated development environment for KDE.
It supports a wide range of programming languages and features project
management, an advanced editor, a class browser and an integrated debugger.

This package contains the PHP language support plugin.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkdevphpcompletion
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevphpcompletion
%name library.

%package -n %libkdevphpduchain
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevphpduchain
%name library.

%package -n %libkdevphpparser
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevphpparser
%name library.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #
#    -DINCLUDE_INSTALL_DIR=%_K6inc \

%install
%K6install
%find_lang kdevphp

%files common
%files -f kdevphp.lang
%_libdir/qt6/plugins/kdevplatform/*/kdevphpdocs.so
%_libdir/qt6/plugins/kdevplatform/*/kdevphplanguagesupport.so
%_libdir/qt6/plugins/kdevplatform/*/kdevphpunitprovider.so
%_datadir/kdevappwizard/templates/simple_phpapp.tar.bz2
%_datadir/kdevphpsupport/
%_datadir/metainfo/org.kde.kdev-php.metainfo.xml
%_datadir/qlogging-categories6/kdevphpsupport.categories

%files devel
%_K6inc/kdev-php/
%_libdir/cmake/KDevPHP/
%_K6link/lib*.so

%files -n %libkdevphpcompletion
%_K6lib/libkdevphpcompletion.so.%sover
%_K6lib/libkdevphpcompletion.so.*
%files -n %libkdevphpduchain
%_K6lib/libkdevphpduchain.so.%sover
%_K6lib/libkdevphpduchain.so.*
%files -n %libkdevphpparser
%_K6lib/libkdevphpparser.so.%sover
%_K6lib/libkdevphpparser.so.*

%changelog
* Tue Sep 15 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.3-alt2
- fix packaging

* Fri Jul 03 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.3-alt1
- New version 26.04.3.

* Wed Jun 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- Initial build for Sisyphus
