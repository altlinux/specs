%define oname repoze.session

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt3.1
Summary: Sessioning for web applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.session/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze zope.component zope.event ZODB3

%description
An HTTP sessioning system for web applications, based on code from the
faster http://agendaless.com/Members/tseaver/software/faster/ Zope 2
product. repoze.session uses ZODB as its persistence mechanism.

%package -n python3-module-%oname
Summary: Sessioning for web applications
Group: Development/Python3
%py3_requires repoze zope.component zope.event ZODB3

%description -n python3-module-%oname
An HTTP sessioning system for web applications, based on code from the
faster http://agendaless.com/Members/tseaver/software/faster/ Zope 2
product. repoze.session uses ZODB as its persistence mechanism.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.session
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
An HTTP sessioning system for web applications, based on code from the
faster http://agendaless.com/Members/tseaver/software/faster/ Zope 2
product. repoze.session uses ZODB as its persistence mechanism.

This package contains tests for repoze.session.

%package tests
Summary: Tests for repoze.session
Group: Development/Python
Requires: %name = %version-%release

%description tests
An HTTP sessioning system for web applications, based on code from the
faster http://agendaless.com/Members/tseaver/software/faster/ Zope 2
product. repoze.session uses ZODB as its persistence mechanism.

This package contains tests for repoze.session.

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
%doc *.txt docs/*.rst docs/code
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst docs/code
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

