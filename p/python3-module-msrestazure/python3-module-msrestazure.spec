%define pypi_name msrestazure

%def_without check

Name: python3-module-%pypi_name
Version: 0.6.4.post1
Release: alt1

Summary: AutoRest swagger generator Python client runtime
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/msrestazure

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 25 2024 Anton Vyatkin <toni@altlinux.org> 0.6.4.post1-alt1
- Initial build for Sisyphus.
