# -*- coding: utf-8 -*-
%define name probstat
%define version 0.912
%define release alt3

%setup_python_module probstat

Summary: probability and statistics utils for Python
Name: %packagename
Version: %version
Release: %release.1
Source: %{modulename}_%version.tgz
License: GPL v2
Group: Development/Python
Url: http://probstat.sourceforge.net/
Packager: Python Development Team <python at packages.altlinux.org>

%description
A fast C implementation of various probability and statistical methods with
Python bindings, featuring combinations, permutations, Cartesians, products,
and priority queues.

This module is built for python %_python_version.

%prep

%setup -n %{modulename}_%version

%build
mkdir -p buildroot

%python_build_debug \
	install --optimize=2 \
		--root=`pwd`/buildroot \
		--record=INSTALLED_FILES

%install
cp -pr buildroot %buildroot
unset RPM_PYTHON

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.912-alt3.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.912-alt3
- Rebuilt for debuginfo

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.912-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 0.912-alt1.1
- Rebuilt with python-2.5.

* Sat Feb 25 2006 Alex V. Myltsev <avm@altlinux.ru> 0.912-alt1
- Initial build for Sisyphus.

