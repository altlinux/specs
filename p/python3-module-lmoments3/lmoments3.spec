%define _unpackaged_files_terminate_build 1
%define oname lmoments3

%def_with check

Name: python3-module-%oname
Version: 1.0.5
Release: alt1
Summary: Estimate linear moments for statistical distribution functions
License: GPLv3
Group: Development/Python3
Url: https://pypi.org/project/lmoments3/

# https://github.com/OpenHydrology/lmoments3.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildPreReq: python3(numpy)
BuildPreReq: python3(numpy.testing)
BuildPreReq: python3(scipy)
%endif

%description
This library was designed to use L-moments to calculate optimal
parameters for a number of distributions. This library extends a number
of scipy distributions and provides some additional distributions
frequently used in Extreme Value Analyses.

%prep
%setup

sed -i 's|"version": "0+unknown"|"version": "%version"|' versioneer.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst docs/source/*.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt1
- Automatically updated to 1.0.5.
- Build with check.
- Moved on modern pyproject macros.

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.4-alt3
- Fixed FTBFS by disabling tests, which use obsoleted api.

* Tue Sep 29 2020 Stanislav Levin <slev@altlinux.org> 1.0.4-alt2
- Fixed FTBFS.

* Thu Oct 03 2019 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- 1.0.2 -> 1.0.4.
- Fixed testing.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.git20150211.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150211
- Initial build for Sisyphus

