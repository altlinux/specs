%define oname z3c.resourceinclude

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt3
Summary: Machinery to include web resources based on request layer
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.resourceinclude/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app.publisher zope.app.cache zope.contentprovider
%py_requires plone.memoize chameleon.zpt

%description
The package is able to include the following types of resources:

* Cascading stylesheets (.css)
* Kinetic stylesheets (.kss)
* Javascript (.js)

%package -n python3-module-%oname
Summary: Machinery to include web resources based on request layer
Group: Development/Python3
%py3_requires zope.app.publisher zope.app.cache zope.contentprovider
%py3_requires plone.memoize chameleon.zpt

%description -n python3-module-%oname
The package is able to include the following types of resources:

* Cascading stylesheets (.css)
* Kinetic stylesheets (.kss)
* Javascript (.js)

%package -n python3-module-%oname-tests
Summary: Tests for z3c.resourceinclude
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The package is able to include the following types of resources:

* Cascading stylesheets (.css)
* Kinetic stylesheets (.kss)
* Javascript (.js)

This package contains tests for z3c.resourceinclude.

%package tests
Summary: Tests for z3c.resourceinclude
Group: Development/Python
Requires: %name = %version-%release

%description tests
The package is able to include the following types of resources:

* Cascading stylesheets (.css)
* Kinetic stylesheets (.kss)
* Javascript (.js)

This package contains tests for z3c.resourceinclude.

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
* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

