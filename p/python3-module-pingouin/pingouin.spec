#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename pingouin

%def_with check

Name: python3-module-%modulename
Version: 0.5.5
Release: alt1
Summary: A python statistical library based on Pandas
Group: Development/Python3
License: GPL-3.0

URL: https://pypi.org/project/pingouin/
VCS: https://github.com/raphaelvallat/pingouin

Source: %name-%version.tar
BuildArch: noarch

Buildrequires(pre): rpm-macros-python3
Buildrequires: rpm-build-python3
Buildrequires: python3-module-setuptools

%if_with check
Buildrequires: python3-module-pytest-cov
Buildrequires: python3-module-pandas-tests
Buildrequires: python3-module-pytest
Buildrequires: python3-module-tabulate
Buildrequires: python3-module-pandas_flavor
Buildrequires: python3-module-seaborn
Buildrequires: python3-module-statsmodels
Buildrequires: python3-module-scikit-learn
%endif

%description
Pingouin is an open-source statistical package written in Python 3
and based mostly on Pandas and NumPy.
Pingouin is designed for users who want simple yet exhaustive
statistical functions.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python3 -m pytest -k 'not (TestRegression and test_logistic_regression)' -v

%files
%doc README.rst CODE_OF_CONDUCT.md LICENSE
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/%modulename-%version.dist-info

%changelog
* Mon Jan 05 2026 Polina Poidenko <polipoki@altlinux.org> 0.5.5-alt1
- Initial build for Sisyphus (Closes: 56503).
