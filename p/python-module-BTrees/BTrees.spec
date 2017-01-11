%define _unpackaged_files_terminate_build 1
%define oname BTrees

%def_with python3
# very slow:
%def_disable check

Name: python-module-%oname
Version: 4.3.2
Release: alt1
Summary: Scalable persistent object containers
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/BTrees
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/BTrees.git
Source0: https://pypi.python.org/packages/f5/4d/206c8b5799e319c0138952b8d18cb4b2288d7dcc583598761f65ed8e416d/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zope.interface python-module-persistent
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface
#BuildPreReq: python-module-transaction
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zope.interface python3-module-persistent
%endif

%py_requires zope.interface 

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-repoze python-module-repoze.sphinx python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-dev python3-module-zope python3-module-zope.interface
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-persistent python-module-pytest python-module-repoze.sphinx.autointerface python-module-transaction python3-module-persistent python3-module-setuptools rpm-build-python3 time

%description
BTrees: scalable persistent components.

This package contains a set of persistent object containers built around
a modified BTree data structure. The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit
resolution of conflicts detected by that mechannism.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
BTrees: scalable persistent components.

This package contains a set of persistent object containers built around
a modified BTree data structure. The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit
resolution of conflicts detected by that mechannism.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
BTrees: scalable persistent components.

This package contains a set of persistent object containers built around
a modified BTree data structure. The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit
resolution of conflicts detected by that mechannism.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
BTrees: scalable persistent components.

This package contains a set of persistent object containers built around
a modified BTree data structure. The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit
resolution of conflicts detected by that mechannism.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Scalable persistent object containers
Group: Development/Python3

%description -n python3-module-%oname
BTrees: scalable persistent components.

This package contains a set of persistent object containers built around
a modified BTree data structure. The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit
resolution of conflicts detected by that mechannism.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
BTrees: scalable persistent components.

This package contains a set of persistent object containers built around
a modified BTree data structure. The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit
resolution of conflicts detected by that mechannism.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
exit 1

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.3.2-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.5-alt2.dev0.git20150602.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 4.1.5-alt2.dev0.git20150602.1
- NMU: Use buildreq for BR.

* Tue Jan 19 2016 Sergey Alembekov <rt@altlinux.ru> 4.1.5-alt2.dev0.git20150602
- remove ZODB cyrcular dependency

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.5-alt1.dev0.git20150602
- Version 4.1.5.dev0

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev0.git201411227
- Version 4.1.2.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.9-alt1.dev.git20141008
- Version 4.0.9dev

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt2
- Avoid conflict with ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Initial build for Sisyphus
