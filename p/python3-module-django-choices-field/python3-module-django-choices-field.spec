%define pypi_name django-choices-field
%define mod_name django_choices_field

%def_with check

Name:    python3-module-%pypi_name
Version: 2.3.0
Release: alt1

Summary: Django field that set/get django's new TextChoices/IntegerChoices enum
License: MIT
Group:   Development/Python3
URL:     https://github.com/bellini666/django-choices-field

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
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
* Mon Aug 12 2024 Alexander Burmatov <thatman@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
