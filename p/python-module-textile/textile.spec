%define version 2.1.8
%define release alt1
%setup_python_module textile

%def_with python3

Summary: This is Textile. A Humane Web Text Generator
Name: %packagename
Version: %version
Release: alt1.1
Source0: %modulename-%version.tar.gz
License: Freely Distributable
Group: Development/Python
BuildArch: noarch
URL: http://loopcore.com/python-textile/

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

%package tests
Summary: Tests for %modulename
Group: Development/Python
Requires: %name = %EVR

%description tests
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

This package contains tests for %modulename.

%package -n python3-module-%modulename
Summary: This is Textile. A Humane Web Text Generator
Group: Development/Python3

%description -n python3-module-%modulename
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

%package -n python3-module-%modulename-tests
Summary: Tests for %modulename
Group: Development/Python3
Requires: python3-module-%modulename = %EVR

%description -n python3-module-%modulename-tests
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

This package contains tests for %modulename.

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc PKG-INFO
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%modulename
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%modulename-tests
%python3_sitelibdir/*/tests
%endif

%changelog
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
