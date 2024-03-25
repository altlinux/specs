%define pypi_name podman-py
%define mod_name podman

%def_with check

Name:    python3-module-%pypi_name
Version: 4.9.0
Release: alt1

Summary: Python bindings for Podman's RESTful API
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/containers/podman-py

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pyxdg
BuildRequires: python3-module-requests
BuildRequires: python3-module-requests-mock
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This python package is a library of bindings to use the RESTful API of Podman.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest podman/tests/unit

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Mon Feb 05 2024 Alexander Burmatov <thatman@altlinux.org> 4.9.0-alt1
- Initial build for Sisyphus.
