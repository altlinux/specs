# -*- mode: rpm-spec; coding: utf-8 -*-
%define version 0.9.9
%define release    alt1
%define source_version 0.9.9
%define oname Pyrex-Tests

Summary: Test suite and testing framework for Pyrex
Name: python-module-%oname
Version: %version
Release: %release.1
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
License: Public domain
Group: Development/Python
Url: http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/
BuildPreReq: rpm-build-python

%py_requires Pyrex

%description
Test suite and testing framework for Pyrex.

%package test-examples
Summary: Example tests for %oname
Group: Development/Documentation
BuildArch: noarch

%description test-examples
This package contains example tests for %oname.

%prep
%setup

%install
install -d %buildroot%_bindir
install -d %buildroot%python_sitelibdir/Pyrex
install -d %buildroot%_docdir/%name

install -p -m755 bin/run_tests %buildroot%_bindir/Pyrex.run_tests
cp -fR Pyrex/Testing %buildroot%python_sitelibdir/Pyrex/
cp -fR Tests %buildroot%_docdir/%name/

%files
%_bindir/Pyrex.run_tests
%python_sitelibdir/*
%exclude %python_sitelibdir/Pyrex/Testing/Mac*

%files test-examples
%_docdir/%name/

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.1
- Rebuild with Python-2.7

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1
- Version 0.9.9

* Tue Mar 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.6-alt1
- Version 0.9.8.6

* Tue Feb 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.5-alt4
- Initial build for ALT Linux

