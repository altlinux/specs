%define pypi_name django-extra-views

%def_with check

Name: python3-module-%pypi_name
Version: 0.14.0
Release: alt1

Summary: Extra class-based views for Django
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/django-extra-views
VCS: https://github.com/AndrewIngram/django-extra-views

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch: merged_pr_233.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
Django-extra-views is a Django package which introduces additional class-based
views in order to simplify common design patterns such as those found in the
Django admin interface.

%prep
%setup -n %pypi_name-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "\
not test_create \
and not test_post \
and not test_get"

%files
%doc README.*
%python3_sitelibdir/extra_views
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 23 2024 Anton Vyatkin <toni@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus.
