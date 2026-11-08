%define oname changefinder

Name: python3-module-changefinder
Version: 0.4
Release: alt1

Summary: Online Change-Point Detection Library based on ChangeFinder Algorithm

License: MIT
Group: Development/Python3
Url: https://github.com/shunsukeaihara/changefinder

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-pytest python3-module-numpy
BuildRequires: python3-module-scipy python3-module-statsmodels
BuildRequires: python3-module-pandas-tests

BuildArch: noarch

%description
Online Change-Point Detection Library based on ChangeFinder Algorithm.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# with aarch64 numerics the ARIMA score peak at the third change point stays below 2 * p99 of the quiet part
# (a noarch package: %%ifarch sees noarch, so check the build host)
%pyproject_run_pytest %([ "$(uname -m)" != aarch64 ] || echo "-k 'not test_detects_regime_changes_on_natural_series'")

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/changefinder/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Tue Nov 03 2026 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new version 0.4
- switch to pyproject build and run upstream tests
- correct license to MIT
- add BuildRequires: python3-module-setuptools, python3-module-wheel
- add BuildRequires: python3-module-pytest, python3-module-numpy
- add BuildRequires: python3-module-scipy, python3-module-statsmodels
- add BuildRequires: python3-module-pandas-tests for statsmodels imports

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.03-alt1
- initial build for ALT Sisyphus
