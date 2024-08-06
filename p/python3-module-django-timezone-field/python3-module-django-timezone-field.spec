%define pypi_name django-timezone-field

%def_with check

Name:    python3-module-%pypi_name
Version: 7.0
Release: alt1

Summary: A Django app providing DB, form, and REST framework fields for zoneinfo and pytz timezone objects
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/mfogel/django-timezone-field

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-pytest-lazy-fixture
BuildRequires: python3-module-pytz
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
%python3_sitelibdir/timezone_field/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 06 2024 Anton Vyatkin <toni@altlinux.org> 7.0-alt1
- New version 7.0.

* Mon Apr 15 2024 Anton Vyatkin <toni@altlinux.org> 6.1.0-alt2
- (NMU) Fixed FTBFS.

* Tue Dec 12 2023 Alexander Burmatov <thatman@altlinux.org> 6.1.0-alt1
- Update version to 6.1.0.

* Wed Oct 04 2023 Alexander Burmatov <thatman@altlinux.org> 6.0.1-alt1
- Initial build for Sisyphus.
