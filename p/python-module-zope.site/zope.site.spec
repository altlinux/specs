%define oname zope.site

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 4.0.1
Release: alt2.dev0.git20150608
Summary: Local registries for zope component architecture
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.site/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-%oname-tests
BuildPreReq: python-module-zope.annotation python-module-zope.container-tests
BuildPreReq: python-module-zope.security python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent python-module-zope.location
BuildPreReq: python-module-zope.testing python-module-zope.traversing-tests
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.size
BuildPreReq: python-module-ZODB-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-%oname-tests
BuildPreReq: python3-module-zope.annotation python3-module-zope.container-tests
BuildPreReq: python3-module-zope.security python3-module-zope.event
BuildPreReq: python3-module-zope.lifecycleevent python3-module-zope.location
BuildPreReq: python3-module-zope.testing python3-module-zope.traversing-tests
BuildPreReq: python3-module-zope.component-tests
BuildPreReq: python3-module-zope.size python3-module-zodbpickle
BuildPreReq: python3-module-ZODB-tests
BuildPreReq: python3-module-zope.filerepresentation
%endif

%py_requires zope.annotation zope.container zope.security
%py_requires zope.component zope.event zope.interface
%py_requires zope.lifecycleevent zope.location

%description
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

%package -n python3-module-%oname
Summary: Local registries for zope component architecture
Group: Development/Python3
%py3_requires zope.annotation zope.container zope.security
%py3_requires zope.component zope.event zope.interface
%py3_requires zope.lifecycleevent zope.location

%description -n python3-module-%oname
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

%package -n python3-module-%oname-tests
Summary: Tests for zope.site
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.configuration zope.testing

%description -n python3-module-%oname-tests
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

This package contains tests for zope.site.

%package tests
Summary: Tests for zope.site
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.configuration zope.testing

%description tests
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

This package contains tests for zope.site.

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

%check
export PYTHONPATH=$PWD/src
python setup.py test -v
#if_with python3
%if 0
pushd ../python3
export PYTHONPATH=$PWD/src
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2.dev0.git20150608
- Enabled check

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20150608
- Version 4.0.1.dev0

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.2-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt1
- Initial build for Sisyphus

