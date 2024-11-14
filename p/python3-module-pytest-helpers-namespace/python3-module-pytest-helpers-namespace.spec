%define pypi_name pytest-helpers-namespace
%define mod_name pytest_helpers_namespace

%def_with check

Name:    python3-module-%pypi_name
Version: 2021.12.29
Release: alt1

Summary: PyTest Helpers Namespace
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/saltstack/pytest-helpers-namespace

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This plugin does not provide any helpers to pytest, it does, however, provide
a helpers namespace in pytest which enables you to register helper functions in
your conftest.py to be used within your tests without having to import them.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name-0.0.0.dist-info/

%changelog
* Mon Oct 14 2024 Alexander Burmatov <thatman@altlinux.org> 2021.12.29-alt1
- Initial build for Sisyphus.
