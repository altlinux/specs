%define oname cssutils

Name: python3-module-cssutils
Version: 1.0.2
Release: alt2

Summary: CSS Cascading Style Sheets library for Python

Group: Development/Python3
License: LGPL
Url: https://pypi.python.org/pypi/cssutils

# Source-url: https://pypi.io/packages/source/c/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

# optional
%add_python3_req_skip google.appengine.api

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities!

%package doc
Summary: Documentation for CSS Cascading Style Sheets library for Python
Group: Development/Documentation

%description doc
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities!

This package contains documentation for %name.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%files
%_bindir/csscapture
%_bindir/csscombine
%_bindir/cssparse
%python3_sitelibdir_noarch/*

#files doc
#doc examples

%changelog
* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- build python3 package only

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- switch to build from tarball
- enable python3 module
- new version (1.0.2) with rpmgs script

* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt2
- exclude tests from package

* Tue Jul 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7b1-alt1.1
- Rebuild with Python-2.7

* Tue Jun 01 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.9.7b1-alt1
- 1st build for ALTLinux
- thanks to real@ fr spec skeleton
