%define pypi_name polyfactory

# tests work but cannot complete
%def_without check

Name:    python3-module-%pypi_name
Version: 3.2.0
Release: alt1

Summary: Simple and powerful factories for mock data generation
License: MIT
Group:   Development/Python3
URL:     https://github.com/litestar-org/polyfactory

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-msgspec
BuildRequires: python3-module-faker
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-pymongo
BuildRequires: python3-module-bson
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-aiosqlite
BuildRequires: python3-module-email-validator
BuildRequires: python3-module-beanie
BuildRequires: python3-module-mongomock-motor
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Polyfactory is a simple and powerful mock data generation library, based around
type hints and supporting dataclasses, typed-dicts, pydantic models, msgspec
structs and more.

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
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Dec 24 2025 Alexander Burmatov <thatman@altlinux.org> 3.2.0-alt1
- New 3.2.0 version.

* Tue Apr 29 2025 Alexander Burmatov <thatman@altlinux.org> 2.21.0-alt1
- New 2.21.0 version.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 2.18.1-alt1
- New 2.18.1 version.

* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 2.16.2-alt1
- Initial build for Sisyphus.
