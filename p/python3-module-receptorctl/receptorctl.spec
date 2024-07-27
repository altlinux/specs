%define _unpackaged_files_terminate_build 1
%define pypi_name receptorctl

%def_without check

Name: python3-module-%pypi_name
Version: 1.4.8
Release: alt1
Summary: Receptorctl is a front-end CLI and importable Python library that interacts with Receptor over its control socket interface
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/receptorctl
BuildArch: noarch
Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-click
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-yaml
%endif

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
%_bindir/receptorctl
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/tests

%changelog
* Tue Jul 23 2024 Anton Vyatkin <toni@altlinux.org> 1.4.8-alt1
- Initial build for Sisyphus.
