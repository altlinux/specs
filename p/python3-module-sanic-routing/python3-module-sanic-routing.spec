%define pypi_name sanic-routing
%define mod_name sanic_routing

%def_with check

Name:    python3-module-%pypi_name
Version: 23.12.0
Release: alt1

Summary: Internal handler routing for Sanic beginning with v21.3
License: MIT
Group:   Development/Python3
URL:     https://github.com/sanic-org/sanic-routing

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 23.12.0-alt1
- Initial build for Sisyphus.
