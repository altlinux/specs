%define oname lmoments3
Name: python3-module-%oname
Version: 1.0.2
Release: alt1.git20150211.1.1
Summary: Estimate linear moments for statistical distribution functions
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/lmoments3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/OpenHydrology/lmoments3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-numpy python3-module-scipy
BuildPreReq: python3-module-nose

%py3_provides %oname
%py3_requires numpy scipy

%description
This library was designed to use L-moments to calculate optimal
parameters for a number of distributions. This library extends a number
of scipy distributions and provides some additional distributions
frequently used in Extreme Value Analyses.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v

%files
%doc CHANGELOG.txt *.rst docs/source/*.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.git20150211.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150211
- Initial build for Sisyphus

