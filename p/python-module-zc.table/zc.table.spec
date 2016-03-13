%define oname zc.table

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt2.1
Summary: Zope 3 extension that helps with the construction of (HTML) tables
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.table/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zc.resourcelibrary zope.app.form zope.app.testing
%py_requires zope.cachedescriptors zope.component zope.formlib zope.i18n
%py_requires zope.interface zope.schema zope.testing

%description
This is a Zope 3 extension that helps with the construction of (HTML)
tables. Features include dynamic HTML table generation, batching and
sorting.

%package -n python3-module-%oname
Summary: Zope 3 extension that helps with the construction of (HTML) tables
Group: Development/Python3
%py3_requires zc zc.resourcelibrary zope.app.form zope.app.testing
%py3_requires zope.cachedescriptors zope.component zope.formlib zope.i18n
%py3_requires zope.interface zope.schema zope.testing

%description -n python3-module-%oname
This is a Zope 3 extension that helps with the construction of (HTML)
tables. Features include dynamic HTML table generation, batching and
sorting.

%package -n python3-module-%oname-tests
Summary: Tests for zc.table
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This is a Zope 3 extension that helps with the construction of (HTML)
tables. Features include dynamic HTML table generation, batching and
sorting.

This package contains tests for zc.table.

%package tests
Summary: Tests for zc.table
Group: Development/Python
Requires: %name = %version-%release

%description tests
This is a Zope 3 extension that helps with the construction of (HTML)
tables. Features include dynamic HTML table generation, batching and
sorting.

This package contains tests for zc.table.

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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Version 0.9.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus

