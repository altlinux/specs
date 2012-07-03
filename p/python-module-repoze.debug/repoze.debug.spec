%define oname repoze.debug
Name: python-module-%oname
Version: 0.7.2
Release: alt1.git20110418.1.1
Summary: WSGI middleware: debugging utilities
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.debug
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.debug.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel

%py_requires repoze threadframe paste webob

%description
Middleware which can help with in-production forensic debugging.

%package tests
Summary: Tests for repoze.debug
Group: Development/Python
Requires: %name = %version-%release

%description tests
Middleware which can help with in-production forensic debugging.

This package contains tests for repoze.debug.

%package pickles
Summary: Pickles for repoze.debug
Group: Development/Python

%description pickles
Middleware which can help with in-production forensic debugging.

This package contains pickles for repoze.debug.

%package docs
Summary: Documentation for repoze.debug
Group: Development/Documentation
BuildArch: noarch

%description docs
Middleware which can help with in-production forensic debugging.

This package contains documentation for repoze.debug.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
%make pickle
%make html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/*/*/tests

%files tests
%exclude %python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.git20110418.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20110418.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20110418
- Initial build for Sisyphus

