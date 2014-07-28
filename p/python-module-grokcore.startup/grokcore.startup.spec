%define oname grokcore.startup

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt2
Summary: Paster support for Grok projects
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.startup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires grokcore zope.component zope.publisher zope.dottedname
%py_requires zope.app.wsgi zope.app.debug

%description
This package provides elements for starting a Grok project with paster
and WSGI.

%package -n python3-module-%oname
Summary: Paster support for Grok projects
Group: Development/Python3
%py3_requires grokcore zope.component zope.publisher zope.dottedname
%py3_requires zope.app.wsgi zope.app.debug

%description -n python3-module-%oname
This package provides elements for starting a Grok project with paster
and WSGI.

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.startup
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.appsetup zope.component zope.interface
%py3_requires zope.testing zope.security

%description -n python3-module-%oname-tests
This package provides elements for starting a Grok project with paster
and WSGI.

This package contains tests for grokcore.startup.

%package tests
Summary: Tests for grokcore.startup
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.appsetup zope.component zope.interface
%py_requires zope.testing zope.security

%description tests
This package provides elements for starting a Grok project with paster
and WSGI.

This package contains tests for grokcore.startup.

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
* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added module for Python 3

* Fri Feb 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

