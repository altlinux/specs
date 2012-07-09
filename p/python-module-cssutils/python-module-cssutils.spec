%define oname cssutils
Name: python-module-cssutils
Version: 0.9.9
Release: alt2
Summary: CSS Cascading Style Sheets library for Python

Group: Development/Python
License: LGPL
Url: http://%oname.googlecode.com/
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://%oname.googlecode.com/files/%oname-%version.zip
BuildArch: noarch

# Automatically added by buildreq on Tue Jun 01 2010 (-bi)
BuildRequires: python-module-mechanize python-module-setuptools python-modules-encodings unzip

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
%setup -n %oname-%version

%build
%python_build

%install
%python_install -O1

%files
%doc *.txt PKG-INFO
%_bindir/*
%python_sitelibdir_noarch/*
%exclude %python_sitelibdir_noarch/tests

%files doc
%doc examples docs/*

%changelog
* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt2
- exclude tests from package

* Tue Jul 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7b1-alt1.1
- Rebuild with Python-2.7

* Tue Jun 01 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.9.7b1-alt1
- 1st build for ALTLinux
- thanks to real@ fr spec skeleton
