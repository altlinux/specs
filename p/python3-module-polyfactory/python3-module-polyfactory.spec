%define pypi_name polyfactory

%def_with check

Name:    python3-module-%pypi_name
Version: 2.18.1
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
donttest="test_handle_constrained_date[ge-le]"
donttest="$donttest or test_handle_constrained_date[gt-lt]"
donttest="$donttest or test_handle_constrained_date[ge-lt]"
donttest="$donttest or test_handle_constrained_date[gt-le]"
donttest="$donttest or test_optional_url_field_parsed_correctly"
donttest="$donttest or test_type_property_parsing"
py.test-3 -v -k "not ($donttest)"

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 2.18.1-alt1
- New 2.18.1 version.

* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 2.16.2-alt1
- Initial build for Sisyphus.
