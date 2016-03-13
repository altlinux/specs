%define oname repoze.obob

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt3.1
Summary: Zope-like publisher as WSGI application
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.obob/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze paste.script WSGIUtils

%description
repoze.obob is a reconstruction of the "bobo" precursor of Zope (the
"object publisher" portion), stripped down to be used as a possible
application endpoint in the 'repoze' stack.

%package -n python3-module-%oname
Summary: Zope-like publisher as WSGI application
Group: Development/Python3
%py3_requires repoze paste.script WSGIUtils

%description -n python3-module-%oname
repoze.obob is a reconstruction of the "bobo" precursor of Zope (the
"object publisher" portion), stripped down to be used as a possible
application endpoint in the 'repoze' stack.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.obob
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.obob is a reconstruction of the "bobo" precursor of Zope (the
"object publisher" portion), stripped down to be used as a possible
application endpoint in the 'repoze' stack.

This package contains tests for repoze.obob.

%package tests
Summary: Tests for repoze.obob
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.obob is a reconstruction of the "bobo" precursor of Zope (the
"object publisher" portion), stripped down to be used as a possible
application endpoint in the 'repoze' stack.

This package contains tests for repoze.obob.

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
%doc *.txt doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/*/*/tests*

%if_with python3
%files -n python3-module-%oname
%doc *.txt doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/*/tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/*/*/tests*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

