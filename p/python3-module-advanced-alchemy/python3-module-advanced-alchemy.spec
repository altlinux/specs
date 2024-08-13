%define pypi_name advanced-alchemy
%define mod_name advanced_alchemy

%def_without check

Name:    python3-module-%pypi_name
Version: 0.17.3
Release: alt1

Summary: A carefully crafted, thoroughly tested, optimized companion library for SQLAlchemy
License: MIT
Group:   Development/Python3
URL:     https://github.com/litestar-org/advanced-alchemy

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-asyncmy
BuildRequires: python3-module-asyncpg
BuildRequires: python3-module-psycopg
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
* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.17.3-alt1
- Initial build for Sisyphus.
