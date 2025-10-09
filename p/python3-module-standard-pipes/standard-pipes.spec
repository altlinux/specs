%def_with check

%define srcname standard-pipes
%define modulename standard_pipes

Name:    python3-module-%srcname
Version: 3.13.0
Release: alt1

Summary: Standard library pipes redistribution. "dead battery"

License: Python-2.0.1
Group:   Development/Python3
URL:     https://pypi.org/project/standard-pipes

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-test
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/pipes/
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Fri Jul 18 2025 Grigory Ustinov <grenka@altlinux.org> 3.13.0-alt1
- Initial build for Sisyphus.
