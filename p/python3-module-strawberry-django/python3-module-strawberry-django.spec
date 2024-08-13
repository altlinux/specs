%define pypi_name strawberry-django
%define mod_name strawberry_django

%def_with check

Name:    python3-module-%pypi_name
Version: 0.47.1
Release: alt1

Summary: Strawberry GraphQL Django extension
License: MIT
Group:   Development/Python3
URL:     https://github.com/strawberry-graphql/strawberry-django

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-factory_boy
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-snapshot
BuildRequires: python3-module-strawberry-graphql
BuildRequires: python3-module-django
BuildRequires: python3-module-django-guardian
BuildRequires: python3-module-django-debug-toolbar
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-django-choices-field
BuildRequires: python3-module-django-polymorphic
BuildRequires: python3-module-django-mptt
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This package provides powerful tools to generate GraphQL types, queries,
mutations and resolvers from Django models.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export DJANGO_SETTINGS_MODULE=tests.django_settings
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo strawberry_graphql_django}

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 0.47.1-alt1
- Initial build for Sisyphus.
