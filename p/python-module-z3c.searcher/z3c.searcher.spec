%define oname z3c.searcher

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt3.1
Summary: Persistent and session based search form for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.searcher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires z3c.form z3c.formui z3c.indexer z3c.template z3c.table
%py_requires zope.container zope.component zope.event zope.index
%py_requires zope.interface zope.location zope.schema zope.session

%description
This package provides an implementation for build z3c.indexer based
search forms for Zope3. The persistent search criteria can get stored in
a session or in an application as predefined filter query objects.

%package -n python3-module-%oname
Summary: Persistent and session based search form for Zope3
Group: Development/Python3
%py3_requires z3c.form z3c.formui z3c.indexer z3c.template z3c.table
%py3_requires zope.container zope.component zope.event zope.index
%py3_requires zope.interface zope.location zope.schema zope.session

%description -n python3-module-%oname
This package provides an implementation for build z3c.indexer based
search forms for Zope3. The persistent search criteria can get stored in
a session or in an application as predefined filter query objects.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.searcher
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.macro z3c.testing zope.app.authentication
%py3_requires zope.app.pagetemplate zope.app.testing zope.contentprovider
%py3_requires zope.intid zope.keyreference zope.publisher zope.session
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package provides an implementation for build z3c.indexer based
search forms for Zope3. The persistent search criteria can get stored in
a session or in an application as predefined filter query objects.

This package contains tests for z3c.searcher.

%package tests
Summary: Tests for z3c.searcher
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.macro z3c.testing zope.app.authentication
%py_requires zope.app.pagetemplate zope.app.testing zope.contentprovider
%py_requires zope.intid zope.keyreference zope.publisher zope.session
%py_requires zope.testing

%description tests
This package provides an implementation for build z3c.indexer based
search forms for Zope3. The persistent search criteria can get stored in
a session or in an application as predefined filter query objects.

This package contains tests for z3c.searcher.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

