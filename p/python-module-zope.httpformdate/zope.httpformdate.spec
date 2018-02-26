%define oname zope.httpformdate
Name: python-module-%oname
Version: 1.0.1
Release: alt2.1
Summary: Extension of zope.httpform for date support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.httpformdate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.httpform zope.datetime

%description
This is a small library that extends the zope.httpform library to
support date/time parsing. It provides a :date converter that uses the
parser from the zope.datetime library to convert a variety of date/time
formats to a standard datetime.datetime object.

%package tests
Summary: Tests for zope.httpformdate
Group: Development/Python
Requires: %name = %version-%release

%description tests
This is a small library that extends the zope.httpform library to
support date/time parsing. It provides a :date converter that uses the
parser from the zope.datetime library to convert a variety of date/time
formats to a standard datetime.datetime object.

This package contains tests for zope.httpformdate.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

