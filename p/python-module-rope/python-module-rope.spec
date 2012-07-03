%define real_name rope

Summary: python refactoring library
Name: python-module-%real_name
Version: 0.9.3
Release: alt1.1
License: GPL
Group: Development/Python
Url: http://rope.sf.net
Packager: Python Development Team <python at packages.altlinux.org>
BuildArch: noarch

Source: %real_name-%version.tar.gz

# Automatically added by buildreq on Sat May 10 2008
BuildRequires: python-devel

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
%python_build

%install
%python_install -O1 --prefix="%prefix"

cp -fR ropetest %buildroot%python_sitelibdir/

%files
%doc COPYING README.txt docs
%python_sitelibdir/*
%exclude %python_sitelibdir/ropetest

%files tests
%python_sitelibdir/ropetest

%changelog
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
