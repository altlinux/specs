%define oname bluebream

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt4.1
Summary: The Zope Web Framework
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/bluebream/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zc.buildout python-module-PasteScript
BuildPreReq: python-module-PasteDeploy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zc.buildout python3-module-PasteScript
BuildPreReq: python3-module-PasteDeploy python-tools-2to3
%endif

%py_requires paste.script zc.buildout zope.app.wsgi zope.site
%py_requires zope.interface zope.schema zope.formlib zope.container
%py_requires zope.browserpage zope.app.debug

%description
BlueBream -- formerly known as Zope 3 -- is a web framework written in
the Python programming language.

%package -n python3-module-%oname
Summary: The Zope Web Framework
Group: Development/Python3
%py3_requires paste.script zc.buildout zope.app.wsgi zope.site
%py3_requires zope.interface zope.schema zope.formlib zope.container
%py3_requires zope.browserpage zope.app.debug

%description -n python3-module-%oname
BlueBream -- formerly known as Zope 3 -- is a web framework written in
the Python programming language.

%package -n python3-module-%oname-tests
Summary: Tests for BlueBream
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zc.buildout z3c.testsetup zope.testing

%description -n python3-module-%oname-tests
BlueBream -- formerly known as Zope 3 -- is a web framework written in
the Python programming language.

This package contains tests for BlueBream.

%package tests
Summary: Tests for BlueBream
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.buildout z3c.testsetup zope.testing

%description tests
BlueBream -- formerly known as Zope 3 -- is a web framework written in
the Python programming language.

This package contains tests for BlueBream.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Really added necessary requirements

* Mon Jun 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

