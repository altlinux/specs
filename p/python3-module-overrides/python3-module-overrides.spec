%define pypi_name overrides

%def_with check

Name: python3-module-%pypi_name
Version: 7.3.1
Release: alt1

Summary: A decorator to automatically detect mismatch when overriding a method
License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/overrides/
VCS: https://github.com/mkorpela/overrides

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 14 2023 Anton Vyatkin <toni@altlinux.org> 7.3.1-alt1
- Initial build for Sisyphus
