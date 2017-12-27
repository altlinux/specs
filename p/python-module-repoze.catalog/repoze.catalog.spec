%define _unpackaged_files_terminate_build 1
%define oname repoze.catalog

%def_without python3

Name: python-module-%oname
Version: 0.8.3
Release: alt2
Summary: Python indexing and searching framework, useful outside Zope ecosystem
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.catalog

# https://github.com/repoze/repoze.catalog.git
Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-zope.component
BuildRequires: python-module-nose
BuildRequires: python-module-ZEO python-module-docutils python-module-html5lib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

%py_requires repoze zope.component zope.index

%description
A Python indexing and searching system based on `zope.index`.

%if_with python3
%package -n python3-module-%oname
Summary: Python indexing and searching framework, useful outside Zope ecosystem
Group: Development/Python3
%py3_requires repoze zope.component zope.index

%description -n python3-module-%oname
A Python indexing and searching system based on `zope.index`.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.catalog
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires nose

%description -n python3-module-%oname-tests
A Python indexing and searching system based on `zope.index`.

This package contains tests for repoze.catalog.
%endif

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
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

#prepare_sphinx .
#ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

#export PYTHONPATH=$PWD
#pushd docs
#make pickle
#make html
#popd

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

#install -d %buildroot%python_sitelibdir/%oname
#cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/benchmark
#exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

#files pickles
#python_sitelibdir/%oname/pickle

#files docs
#doc docs/.build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/benchmark
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt2
- Disabled build for python-3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt2.git20130426.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt2.git20130426.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20130426.1
- NMU: Use buildreq for BR.

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt2.git20130426
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20130426
- New snapshot

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20130219
- Version 0.8.2

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

