%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: kdevelop-python
Version: 26.04.3
Release: alt1

Summary: Python 3 language plugin for KDevelop
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/kdevelop/kdev-python

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt6-tools-devel
BuildRequires: python3-devel
BuildRequires: kdevelop-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-ki18n-devel

ExcludeArch: %ix86 riscv64

Requires: kdevelop

%description
KDevelop is an easy to use integrated development environment for KDE.
It supports a wide range of programming languages and features project
management, an advanced editor, a class browser and an integrated debugger.

This package contains the Python 3 language support plugin.

%prep
%setup
sed -i "s|^#!/usr/bin/env python$|#!/usr/bin/env python3|" documentation_src/pyqt/sip_to_xml5.py \
                                                           documentation_src/numpy/generate_numpy_doc.py \
                                                           documentation_src/introspection/introspect.py \
                                                           app_templates/django_project/manage.py

%build
%cmake \
       -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
# remove old obsolete stuff
rm -rv %buildroot%_datadir/kdevpythonsupport/documentation_files/{PyKDE4,PyQt4}
rm -v %buildroot%_datadir/kdevappwizard/templates/django_project.tar.bz2

%find_lang kdevpython

%files -f kdevpython.lang
%doc README
%_libdir/libkdevpythoncompletion.so
%_libdir/libkdevpythonduchain.so
%_libdir/libkdevpythonparser.so
%_libdir/qt6/plugins/kdevplatform/*/*.so
%_datadir/kdevappwizard/templates/qtdesigner_app.tar.bz2
%_datadir/kdevappwizard/templates/simple_pythonapp.tar.bz2
%dir %_datadir/kdevpythonsupport
%_datadir/kdevpythonsupport/*
%_datadir/metainfo/org.kde.kdev-python.metainfo.xml
%_datadir/qlogging-categories6/kdevpythonsupport.categories

%changelog
* Fri Jul 03 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.3-alt1
- New version 26.04.3.

* Wed Jun 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- Initial build for Sisyphus
