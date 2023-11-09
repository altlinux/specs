%define pypi_name pytest-docker
%define mod_name pytest_docker

# Need docker-compose version >=1.27.3 <2.0
%def_without check

Name:    python3-module-%pypi_name
Version: 2.0.1
Release: alt1

Summary: Docker-based integration tests
License: MIT
Group:   Development/Python3
URL:     https://github.com/avast/pytest-docker

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-attrs
BuildRequires: python3-module-requests
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch1: remove-broken-arguments-from-tests.patch

%description
Simple pytest fixtures that help you write integration tests with Docker
and Docker Compose. Specify all necessary containers in a docker-compose.yml
file and and pytest-docker will spin them up for the duration of your tests.

%prep
%setup -n %pypi_name-%version
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 08 2023 Alexander Burmatov <thatman@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus.
