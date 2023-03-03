%define mname sksparse
%define oname scikits.sparse

%def_with check

Name: python3-module-%oname
Version: 0.4.8
Release: alt1

Summary: Sparse matrix tools extending scipy.sparse, but with incompatible licenses
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/scikit-sparse/
VCS: https://github.com/scikit-sparse/scikit-sparse.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-numpy
BuildRequires: python3-module-Cython
BuildRequires: libnumpy-py3-devel
BuildRequires: libsuitesparse-devel
BuildRequires: python3-module-sphinx
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
%endif

%description
This is a home for sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper. Usually this will be because it is released under the GPL.

So far we have a wrapper for the CHOLMOD library for sparse cholesky
decomposition.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This is a home for sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper. Usually this will be because it is released under the GPL.

So far we have a wrapper for the CHOLMOD library for sparse cholesky
decomposition.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
This is a home for sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper. Usually this will be because it is released under the GPL.

So far we have a wrapper for the CHOLMOD library for sparse cholesky
decomposition.

This package contains pickles for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

%build
%pyproject_build

%install
%pyproject_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc pickle
%make -C doc html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%ifnarch armh %ix86
%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -ra --pyargs sksparse
%endif

%files
%doc LICENSE.txt README.md doc/_build/html
%python3_sitelibdir/%mname
%python3_sitelibdir/%{pyproject_distinfo scikit_sparse}
%exclude %python3_sitelibdir/%oname/pickle
%exclude %python3_sitelibdir/%mname/test*

%files tests
%python3_sitelibdir/%mname/test*

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle


%changelog
* Fri Mar 03 2023 Anton Vyatkin <toni@altlinux.org> 0.4.8-alt1
- new version 0.4.8

* Thu Jun 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.4-alt1
- Version updated to 0.4.4.

* Fri Feb 28 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.2-alt3
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

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

