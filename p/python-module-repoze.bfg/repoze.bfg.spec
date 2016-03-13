%define oname repoze.bfg

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt4.1
Summary: The repoze.bfg web application framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides repoze.bfg
%py_requires repoze chameleon paste paste.deploy paste.script webob
%py_requires repoze.lru zope.component zope.configuration
%py_requires zope.deprecation zope.interface venusian translationstring

%description
repoze.bfg is a small, fast, down-to-earth, open source Python web
development framework. It makes real-world web application development
and deployment more fun, more predictable, and more productive.

%package -n python3-module-%oname
Summary: The repoze.bfg web application framework
Group: Development/Python3
%py3_provides repoze.bfg
%py3_requires repoze chameleon paste paste.deploy paste.script webob
%py3_requires repoze.lru zope.component zope.configuration
%py3_requires zope.deprecation zope.interface venusian translationstring

%description -n python3-module-%oname
repoze.bfg is a small, fast, down-to-earth, open source Python web
development framework. It makes real-world web application development
and deployment more fun, more predictable, and more productive.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bfg
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires sphinx docutils coverage twill repoze.sphinx.autointerface

%description -n python3-module-%oname-tests
repoze.bfg is a small, fast, down-to-earth, open source Python web
development framework. It makes real-world web application development
and deployment more fun, more predictable, and more productive.

This package contains tests for repoze.bfg.

%package tests
Summary: Tests for repoze.bfg
Group: Development/Python
Requires: %name = %version-%release
%py_requires sphinx docutils coverage twill repoze.sphinx.autointerface

%description tests
repoze.bfg is a small, fast, down-to-earth, open source Python web
development framework. It makes real-world web application development
and deployment more fun, more predictable, and more productive.

This package contains tests for repoze.bfg.

%package docs
Summary: Documentation for repoze.bfg
Group: Development/Documentation
BuildArch: noarch

%description docs
repoze.bfg is a small, fast, down-to-earth, open source Python web
development framework. It makes real-world web application development
and deployment more fun, more predictable, and more productive.

This package contains documentation for repoze.bfg.

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
touch %buildroot%python_sitelibdir/repoze/bfg/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/repoze/bfg/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/*/tests.py*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/*/*/tests.py*

%files docs
%doc docs/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/tests.py*
#exclude %python3_sitelibdir/*/*/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/tests.py*
#python3_sitelibdir/*/*/*/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt4
- Added repoze/bfg/__init__.py

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

