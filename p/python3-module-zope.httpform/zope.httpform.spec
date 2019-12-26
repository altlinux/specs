%define oname zope.httpform

Name: python3-module-%oname
Version: 1.0.2
Release: alt4
Summary: HTTP Form Data Parser
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.httpform/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python-tools-2to3

%py3_requires zope zope.interface

%description
zope.httpform is a library that, given a WSGI or CGI environment
dictionary, will return a dictionary back containing converted
form/query string elements. The form and query string elements contained
in the environment are converted into simple Python types when the form
element names are decorated with special suffixes.

%package tests
Summary: Tests for HTTP Form Data Parser
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
zope.httpform is a library that, given a WSGI or CGI environment
dictionary, will return a dictionary back containing converted
form/query string elements. The form and query string elements contained
in the environment are converted into simple Python types when the form
element names are decorated with special suffixes.

This package contains tests for HTTP Form Data Parser.

%prep
%setup
find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%changelog
* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.0.2-alt4
- NMU: Remove python2 module build

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

