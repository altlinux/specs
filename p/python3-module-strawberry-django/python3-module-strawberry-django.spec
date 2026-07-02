%define pypi_name strawberry-django
%define mod_name strawberry_django

%def_with check

Name:    python3-module-%pypi_name
Version: 0.86.4
Release: alt1

Summary: Strawberry GraphQL Django extension
License: MIT
Group:   Development/Python3
URL:     https://github.com/strawberry-graphql/strawberry-django

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

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
BuildRequires: python3-module-django-tree-queries
BuildRequires: python3-module-django-model-utils
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This package provides powerful tools to generate GraphQL types, queries,
mutations and resolvers from Django models.

%prep
%setup -n %pypi_name-%version
sed -i 's/version = "0.86.3"/version = "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
export DJANGO_SETTINGS_MODULE=tests.django_settings
echo 'STATIC_URL = "/static/"' >> tests/django_settings.py
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo strawberry_graphql_django}

%changelog
* Wed Jul 01 2026 Alexander Burmatov <thatman@altlinux.org> 0.86.4-alt1
- New 0.86.4 version.

* Mon Jun 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.86.0-alt1
- New 0.86.0 version.

* Tue May 05 2026 Alexander Burmatov <thatman@altlinux.org> 0.84.0-alt1
- New 0.84.0 version.

* Mon Apr 13 2026 Alexander Burmatov <thatman@altlinux.org> 0.82.1-alt1
- New 0.82.1 version.

* Wed Mar 18 2026 Alexander Burmatov <thatman@altlinux.org> 0.82.0-alt1
- New 0.82.0 version.

* Wed Mar 04 2026 Alexander Burmatov <thatman@altlinux.org> 0.79.1-alt1
- New 0.79.1 version.

* Wed Feb 04 2026 Alexander Burmatov <thatman@altlinux.org> 0.75.0-alt1
- New 0.75.0 version.

* Wed Jan 21 2026 Alexander Burmatov <thatman@altlinux.org> 0.74.1-alt1
- New 0.74.1 version.

* Mon Jan 12 2026 Alexander Burmatov <thatman@altlinux.org> 0.73.1-alt1
- New 0.73.1 version.

* Wed Dec 10 2025 Alexander Burmatov <thatman@altlinux.org> 0.70.1-alt1
- New 0.70.1 version.

* Wed Nov 26 2025 Alexander Burmatov <thatman@altlinux.org> 0.67.2-alt1
- New 0.67.2 version.

* Thu Oct 30 2025 Alexander Burmatov <thatman@altlinux.org> 0.67.0-alt1
- New 0.67.0 version.

* Wed Oct 15 2025 Alexander Burmatov <thatman@altlinux.org> 0.66.2-alt1
- New 0.66.2 version.

* Wed Jul 30 2025 Alexander Burmatov <thatman@altlinux.org> 0.65.1-alt1
- New 0.65.1 version.

* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.60.0-alt1
- New 0.60.0 version.

* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.59.1-alt1
- New 0.59.1 version.

* Sat Apr 26 2025 Alexander Burmatov <thatman@altlinux.org> 0.58.0-alt1
- New 0.58.0 version.

* Tue Mar 18 2025 Alexander Burmatov <thatman@altlinux.org> 0.57.0-alt1
- New 0.57.0 version.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.52.1-alt1
- New 0.52.1 version.

* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 0.50.0-alt1
- New 0.50.0 version.

* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 0.47.1-alt1
- Initial build for Sisyphus.
