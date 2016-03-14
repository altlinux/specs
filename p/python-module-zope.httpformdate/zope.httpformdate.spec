%define oname zope.httpformdate

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt3.1
Summary: Extension of zope.httpform for date support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.httpformdate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.httpform zope.datetime

%description
This is a small library that extends the zope.httpform library to
support date/time parsing. It provides a :date converter that uses the
parser from the zope.datetime library to convert a variety of date/time
formats to a standard datetime.datetime object.

%package -n python3-module-%oname
Summary: Extension of zope.httpform for date support
Group: Development/Python3
%py3_requires zope zope.httpform zope.datetime

%description -n python3-module-%oname
This is a small library that extends the zope.httpform library to
support date/time parsing. It provides a :date converter that uses the
parser from the zope.datetime library to convert a variety of date/time
formats to a standard datetime.datetime object.

%package -n python3-module-%oname-tests
Summary: Tests for zope.httpformdate
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This is a small library that extends the zope.httpform library to
support date/time parsing. It provides a :date converter that uses the
parser from the zope.datetime library to convert a variety of date/time
formats to a standard datetime.datetime object.

This package contains tests for zope.httpformdate.

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
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
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

