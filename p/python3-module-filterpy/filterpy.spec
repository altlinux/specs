%define oname filterpy

Name:       python3-module-%oname
Version:    1.1.0
Release:    alt4

Summary:    Kalman filtering and optimal estimation library
License:    MIT
Group:      Development/Python3
BuildArch:  noarch
Url:        https://pypi.python.org/pypi/filterpy/

#           https://github.com/rlabbe/filterpy.git
Source:     %name-%version.tar
Patch1:     %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpydoc xvfb-run
BuildRequires: python3-module-mock python3-module-pytest
BuildRequires: python3-module-matplotlib python3-module-scipy
BuildRequires: python3-module-numpy-testing


%description
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

rm -f requirements.txt

%check
rm -f filterpy/common/tests/test_discretization.py
%__python3 setup.py build_ext -i
PYTHONPATH=%buildroot%python3_sitelibdir xvfb-run py.test3 -vv

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Mon Aug 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt4
- Build requires fixed.

* Fri Feb 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt3
- Build for python2 disabled.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.1.0-alt2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream version 1.1.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.16-alt1.git20150217.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.16-alt1.git20150217.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150217
- Version 0.0.16

* Mon Dec 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20141130
- Version 0.0.7

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt2.git20141122
- Moved examples into tests subpackage

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141122
- Initial build for Sisyphus

