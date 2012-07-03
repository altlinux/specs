%define oname repoze.bfg
Name: python-module-%oname
Version: 1.3
Release: alt2.1
Summary: The repoze.bfg web application framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_provides repoze.bfg
%py_requires repoze chameleon paste paste.deploy paste.script webob
%py_requires repoze.lru zope.component zope.configuration
%py_requires zope.deprecation zope.interface venusian translationstring

%description
repoze.bfg is a small, fast, down-to-earth, open source Python web
development framework. It makes real-world web application development
and deployment more fun, more predictable, and more productive.

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

