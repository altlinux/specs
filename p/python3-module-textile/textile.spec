%define version 2.1.8
%define release alt1

%define modulename textile

Summary: This is Textile. A Humane Web Text Generator
Name: python3-module-%modulename
Version: %version
Release: alt2
Source0: %modulename-%version.tar.gz
License: Freely Distributable
Group: Development/Python3
BuildArch: noarch
URL: http://loopcore.com/python-textile/

BuildRequires(pre): rpm-build-python3

%description
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

%package tests
Summary: Tests for %modulename
Group: Development/Python3
Requires: %name = %EVR

%description tests
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

This package contains tests for %modulename.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.8-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1.8-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.8-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.8-alt1
- Version 2.1.8
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.4-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Version 2.1.4

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.10-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.0.10-alt1.1
- Rebuilt with python-2.5.

* Thu Apr 28 2005 Ivan Fedorov <ns@altlinux.ru> 2.0.10-alt1
- Initial build for ALT Linux
