%define oname zExceptions

%def_with python3

Name: python-module-%oname
Version: 3.0
Release: alt1.dev0.git20150331.1
Summary: zExceptions contains common exceptions used in Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zExceptions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zExceptions.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.security
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
BuildPreReq: python3-module-zope.interface
BuildPreReq: python3-module-zope.publisher
BuildPreReq: python3-module-zope.security
%endif

%py_requires zope.interface zope.publisher zope.security

%description
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope 2.

%package -n python3-module-%oname
Summary: zExceptions contains common exceptions used in Zope2
Group: Development/Python3
%py3_requires zope.interface zope.publisher zope.security

%description -n python3-module-%oname
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope 2.

%package -n python3-module-%oname-tests
Summary: Tests for zExceptions
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope 2.

This package contains tests for zExceptions.

%package tests
Summary: Tests for zExceptions
Group: Development/Python
Requires: %name = %version-%release

%description tests
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope 2.

This package contains tests for zExceptions.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.dev0.git20150331.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.dev0.git20150331
- Version 3.0.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev
- Enabled testing

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.0-alt1.1
- Rebuild with Python-2.7

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

