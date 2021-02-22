%define oname pyhacrf

Name: python3-module-%oname
Version: 0.1.2
Release: alt2
Summary: Hidden alignment conditional random field, discriminative string edit distance
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyhacrf

# https://github.com/dirko/pyhacrf.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-numpy-testing
BuildPreReq: python3-module-pylbfgs
BuildRequires: python3-module-pytest

%description
Hidden alignment conditional random field for classifying string pairs -
a learnable edit distance.

This package aims to implement the HACRF machine learning model with a
sklearn-like interface. It includes ways to fit a model to training
examples and score new example.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing

cython3 %oname/algorithms.pyx
%python3_build_debug

%install
%python3_install

%check
%ifnarch %ix86
python3 setup.py test -v
python3 setup.py build_ext -i
py.test3 -vv
%endif

%files
%doc *.rst examples
%python3_sitelibdir/*

%changelog
* Thu Feb 11 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.2-alt2
- Drop python2 support.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1.1.1.1
- Added missing dep on `numpy.testing`.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1
- Updated to upstream version 0.1.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.12-alt1.git20150818.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.12-alt1.git20150818
- Initial build for Sisyphus

