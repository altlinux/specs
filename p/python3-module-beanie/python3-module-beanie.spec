%define pypi_name beanie

%def_without check

Name:    python3-module-%pypi_name
Version: 1.26.0
Release: alt1

Summary: Asynchronous Python ODM for MongoDB
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/BeanieODM/beanie

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-motor
BuildRequires: python3-module-lazy-model
BuildRequires: python3-module-pydantic-settings
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-asgi-lifespan
BuildRequires: python3-module-httpx
BuildRequires: python3-module-email-validator
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-toml
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pydantic-extra-types
BuildRequires: python-module-dns
BuildRequires: python3-module-bson
BuildRequires: python3-module-click
BuildRequires: python3-module-pydantic
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Beanie - is an asynchronous Python object-document mapper (ODM) for MongoDB.
Data models are based on Pydantic.

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
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 06 2024 Alexander Burmatov <thatman@altlinux.org> 1.26.0-alt1
- Initial build for Sisyphus.
