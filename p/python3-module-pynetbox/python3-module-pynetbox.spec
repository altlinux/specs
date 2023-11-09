%define pypi_name pynetbox

%def_with check

Name:    python3-module-%pypi_name
Version: 7.2.0
Release: alt1

Summary: Python API client library for Netbox
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/netbox-community/pynetbox

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest-docker
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

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
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/pynetbox-0.0.0.dist-info/

%changelog
* Wed Nov 08 2023 Alexander Burmatov <thatman@altlinux.org> 7.2.0-alt1
- Initial build for Sisyphus.
