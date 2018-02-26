%define oname repoze.catalog
Name: python-module-%oname
Version: 0.8.1
Release: alt1.git20110817
Summary: Python indexing and searching framework, useful outside Zope ecosystem
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.catalog
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.catalog.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-zope.component
BuildPreReq: python-module-zope.interface python-module-ZODB3
BuildPreReq: python-module-zope.event python-module-zdaemon
BuildPreReq: python-module-zconfig python-module-zc.lockfile
BuildPreReq: python-module-transaction python-module-nose

%py_requires repoze zope.component zope.index

%description
A Python indexing and searching system based on `zope.index`.

%package tests
Summary: Tests for repoze.catalog
Group: Development/Python
Requires: %name = %version-%release
%py_requires nose

%description tests
A Python indexing and searching system based on `zope.index`.

This package contains tests for repoze.catalog.

%package pickles
Summary: Pickles for repoze.catalog
Group: Development/Python

%description pickles
A Python indexing and searching system based on `zope.index`.

This package contains pickles for repoze.catalog.

%package docs
Summary: Documentation for repoze.catalog
Group: Development/Documentation
BuildArch: noarch

%description docs
A Python indexing and searching system based on `zope.index`.

This package contains documentation for repoze.catalog.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

export PYTHONPATH=$PWD
pushd docs
%make pickle
%make html
popd

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/benchmark
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/.build/html/*

%changelog
* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20110817
- Version 0.8.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt1.git20110323.2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20110323.2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20110323.1
- Moved all tests into tests package

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20110323
- Initial build for Sisyphus

