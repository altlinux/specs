%define pypi_name openapi-pydantic
%define mod_name openapi_pydantic

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.1
Release: alt1

Summary: Pydantic OpenAPI schema implementation
License: MIT
Group:   Development/Python3
URL:     https://github.com/mike-oakley/openapi-pydantic

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-openapi-spec-validator
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
* Sat Aug 10 2024 Alexander Burmatov <thatman@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus.
