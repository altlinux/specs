%define _unpackaged_files_terminate_build 1
%define oname zope.httpformdate

Name: python3-module-%oname
Version: 1.0.1
Release: alt4
Summary: Extension of zope.httpform for date support
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.httpformdate/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%py3_requires zope zope.httpform zope.datetime

%description
This is a small library that extends the zope.httpform library to
support date/time parsing. It provides a :date converter that uses the
parser from the zope.datetime library to convert a variety of date/time
formats to a standard datetime.datetime object.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This is a small library that extends the zope.httpform library to
support date/time parsing. It provides a :date converter that uses the
parser from the zope.datetime library to convert a variety of date/time
formats to a standard datetime.datetime object.

This package contains tests for %oname.

%prep
%setup

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
* Thu Dec 26 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.0.1-alt4
- NMU: remove python2 module build

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

