%define oname z3c.sharedmimeinfo

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt3.1
Summary: MIME type guessing framework for Zope, based on shared-mime-info
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.sharedmimeinfo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.i18n zope.i18nmessageid zope.interface zope.schema

%description
This package provides an utility for guessing MIME type from file name
and/or actual contents. It's based on freedesktop.org's shared-mime-info
database.

%package -n python3-module-%oname
Summary: MIME type guessing framework for Zope, based on shared-mime-info
Group: Development/Python3
%py3_requires zope.i18n zope.i18nmessageid zope.interface zope.schema

%description -n python3-module-%oname
This package provides an utility for guessing MIME type from file name
and/or actual contents. It's based on freedesktop.org's shared-mime-info
database.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.sharedmimeinfo
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.component

%description -n python3-module-%oname-tests
This package provides an utility for guessing MIME type from file name
and/or actual contents. It's based on freedesktop.org's shared-mime-info
database.

This package contains tests for z3c.sharedmimeinfo.

%package tests
Summary: Tests for z3c.sharedmimeinfo
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.component

%description tests
This package provides an utility for guessing MIME type from file name
and/or actual contents. It's based on freedesktop.org's shared-mime-info
database.

This package contains tests for z3c.sharedmimeinfo.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

