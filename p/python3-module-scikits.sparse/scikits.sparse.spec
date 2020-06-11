%define mname sksparse
%define oname scikits.sparse

%def_disable check

Name: python3-module-%oname
Version: 0.4.4
Release: alt1

Summary: Scikits sparse matrix package
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/scikits.sparse/

# https://github.com/njsmith/scikits-sparse.git
Source: %name-%version.tar
Patch0: fix-compilation-crash.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libsuitesparse-devel gcc-c++
BuildRequires: libnumpy-py3-devel python-tools-2to3
BuildRequires: python3-module-Cython python3-module-sphinx


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
%patch0 -p1

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	%mname/_version.py

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|np.get_include()|"./"|' setup.py

%build
ln -s $(%__python3 -c 'import numpy; print(numpy.get_include()+"/numpy-py3")') numpy

%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc pickle
%make -C doc html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
touch %buildroot%python3_sitelibdir/%mname/__init__.py
%__python3 setup.py test

%files
%doc README.md doc/_build/html
%python3_sitelibdir/%mname/*
%python3_sitelibdir/scikit_sparse-%version-py*.egg-info
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/test*

%files tests
%python3_sitelibdir/*/test*

%files pickles
%python3_sitelibdir/*/pickle


%changelog
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

