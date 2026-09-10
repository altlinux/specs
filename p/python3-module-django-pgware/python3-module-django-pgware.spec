%define pypi_name django-pgware
%define mod_name django_pg_utils

# PostgreSQL is needed to run tests
%def_with check

Name:    python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Useful PostgreSQL-specific Django utiites
License: PostgreSQL
Group:   Development/Python3
URL:     https://github.com/Xof/django-pgware

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
PostgreSQL utilities for Django: advisory locks, GUC management, and logging
suppression.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 09 2026 Alexander Burmatov <thatman@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
