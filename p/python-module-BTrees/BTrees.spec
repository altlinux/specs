%define oname BTrees

%def_with python3

Name: python-module-%oname
Version: 4.0.8
Release: alt2
Summary: Scalable persistent object containers
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/BTrees
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zope.interface python-module-persistent
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-repoze.sphinx.autointerface
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zope.interface python3-module-persistent
%endif

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
%setup

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
* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt2
- Avoid conflict with ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Initial build for Sisyphus

