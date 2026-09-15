%define _stripped_files_terminate_build 1

%define rname kdev-python
%define sover 6
%define libkdevpythoncompletion libkdevpythoncompletion%sover
%define libkdevpythonduchain libkdevpythonduchain%sover
%define libkdevpythonparser libkdevpythonparser%sover

Name: kdevelop-python
Version: 26.04.3
Release: alt3

Group: Development/Other
Summary: Python 3 language plugin for KDevelop
License: GPL-2.0-or-later
Url: https://invent.kde.org/kdevelop/kdev-python

ExcludeArch: %not_qt6_qtwebengine_arches
AutoReq: yes,nopython
Requires: kdevelop

Source: %rname-%version.tar
Patch1: alt-python-version.patch
Patch2: alt-soname.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules cmake
BuildRequires: qt6-tools-devel
BuildRequires: python3-devel
BuildRequires: kf6-kparts-devel kf6-kio-devel kf6-ki18n-devel kdevelop-devel

%description
KDevelop is an easy to use integrated development environment for KDE.
It supports a wide range of programming languages and features project
management, an advanced editor, a class browser and an integrated debugger.

This package contains the Python 3 language support plugin.

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

%package -n %libkdevpythoncompletion
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevpythoncompletion
%name library.

%package -n %libkdevpythonduchain
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevpythonduchain
%name library.

%package -n %libkdevpythonparser
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdevpythonparser
%name library.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

sed -i "s|^#!/usr/bin/env python$|#!/usr/bin/env python3|" documentation_src/pyqt/sip_to_xml5.py \
                                                           documentation_src/numpy/generate_numpy_doc.py \
                                                           documentation_src/introspection/introspect.py \
                                                           app_templates/django_project/manage.py

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
# remove old obsolete stuff
rm -rv %buildroot%_datadir/kdevpythonsupport/documentation_files/{PyKDE4,PyQt4}
rm -v %buildroot%_datadir/kdevappwizard/templates/django_project.tar.bz2

%find_lang kdevpython

%files common -f kdevpython.lang
%files
%doc README
%_libdir/qt6/plugins/kdevplatform/*/*.so
%_datadir/kdevappwizard/templates/qtdesigner_app.tar.bz2
%_datadir/kdevappwizard/templates/simple_pythonapp.tar.bz2
%_datadir/kdevpythonsupport/
%_datadir/metainfo/*kdev-python*.xml
%_datadir/qlogging-categories6/*kdevpython*.*categories

#%files devel
#%_K6inc/kdev-python/
#%_libdir/cmake/KDevPython/
#%_K6link/lib*.so

%files -n %libkdevpythoncompletion
%_K6lib/libkdevpythoncompletion.so.%sover
%_K6lib/libkdevpythoncompletion.so.*
%files -n %libkdevpythonduchain
%_K6lib/libkdevpythonduchain.so.%sover
%_K6lib/libkdevpythonduchain.so.*
%files -n %libkdevpythonparser
%_K6lib/libkdevpythonparser.so.%sover
%_K6lib/libkdevpythonparser.so.*

%changelog
* Tue Sep 15 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.3-alt3
- fix packaging

* Tue Jul 07 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 26.04.3-alt2
- Added support for Python 3.14 and 3.15.

* Fri Jul 03 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.3-alt1
- New version 26.04.3.

* Wed Jun 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- Initial build for Sisyphus
