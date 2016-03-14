%define real_name rope

Summary: python refactoring library
Name: python3-module-%real_name
Version: 0.9.4.1
Release: alt1.1
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/rope_py3k
BuildArch: noarch

Source: %real_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%description
%summary

%package tests
Summary: Tests for rope
Group: Development/Python
Requires: %name = %version-%release

%description tests
%summary

This package contains tests for rope.

%prep
%setup -n %real_name-%version

%build
%python3_build

%install
%python3_install -O1 --prefix="%prefix"

cp -fR ropetest %buildroot%python3_sitelibdir/

%files
%doc COPYING README.txt docs
%python3_sitelibdir/*
%exclude %python3_sitelibdir/ropetest

%files tests
%python3_sitelibdir/ropetest

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.1-alt1
- Version 0.9.4-1 (Python 3)

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.3-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Version 0.9.3

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2 (ALT #17977)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.1
- Rebuilt with python 2.6

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.8.2-alt1
- Initial ALT build
