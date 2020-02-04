%define oname vstat

%def_with python3

Name: python3-module-%oname
Version: 0.3
Release: alt2

Summary: Implementation of the v-statistic
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/vstat/
BuildArch: noarch

# https://github.com/dostodabsi/vstat.py.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-scipy python3-module-nose
BuildRequires: python3-module-repoze.lru

%py3_provides %oname


%description
Implements the v-statistic, a measure that compares the estimation
accuracy of the ordinary least squares estimator against a random
benchmark.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.git20150101.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20150101.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150101
- Version 0.3

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150101
- Initial build for Sisyphus

