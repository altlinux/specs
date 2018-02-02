%define mname sksparse
%define oname scikits.sparse

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.2
Release: alt2.1
Summary: Scikits sparse matrix package
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.sparse/

# https://github.com/njsmith/scikits-sparse.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libsuitesparse-devel gcc-c++
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-Cython libnumpy-devel
BuildRequires: python-module-scipy python-module-nose
BuildRequires: python-module-alabaster python-module-html5lib python-module-notebook python-module-numpy-testing python-module-objects.inv python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-scipy python3-module-nose
BuildRequires: python3-module-html5lib python3-module-notebook python3-module-numpy-testing
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname numpy scipy

%description
This is a home for sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper. Usually this will be because it is released under the GPL.

So far we have a wrapper for the CHOLMOD library for sparse cholesky
decomposition.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a home for sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper. Usually this will be because it is released under the GPL.

So far we have a wrapper for the CHOLMOD library for sparse cholesky
decomposition.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Scikits sparse matrix package
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy

%description -n python3-module-%oname
This is a home for sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper. Usually this will be because it is released under the GPL.

So far we have a wrapper for the CHOLMOD library for sparse cholesky
decomposition.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a home for sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper. Usually this will be because it is released under the GPL.

So far we have a wrapper for the CHOLMOD library for sparse cholesky
decomposition.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This is a home for sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper. Usually this will be because it is released under the GPL.

So far we have a wrapper for the CHOLMOD library for sparse cholesky
decomposition.

This package contains pickles for %oname.

%prep
%setup

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	%mname/_version.py

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
touch %buildroot%python_sitelibdir/%mname/__init__.py
python setup.py test
%if_with python3
pushd ../python3
touch %buildroot%python3_sitelibdir/%mname/__init__.py
python3 setup.py test
popd
%endif

%files
%doc README.md doc/_build/html
%python_sitelibdir/%mname/*
%python_sitelibdir/scikit_sparse-%version-py*.egg-info
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc README.md doc/_build/html
%python3_sitelibdir/%mname/*
%python3_sitelibdir/scikit_sparse-%version-py*.egg-info
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt2
- Fixed version in egg-info.

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt1
- Updated to upstream version 0.4.2.
- Updated build dependencies.

* Wed Jul 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2-alt2.dev.git20140718.1.2
- Rebuilt with new libsuitesparse

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt2.dev.git20140718.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.dev.git20140718.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.dev.git20140718
- Rebuilt with updated NumPy

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev.git20140718
- Initial build for Sisyphus

