%define pypi_name django-tables2

%def_with check

Name:    python3-module-%pypi_name
Version: 2.6.0
Release: alt1

Summary: django-tables2 - An app for creating HTML tables
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/jieter/django-tables2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-django-filter
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-lxml
BuildRequires: python3-module-pytz
BuildRequires: python3-module-tablib
BuildRequires: python3-module-openpyxl
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
django-tables2 simplifies the task of turning sets of data into HTML tables.
It has native support for pagination and sorting. It does for HTML tables what
django.forms does for HTML forms. e.g.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%check
python3 manage.py test

%files -f %name.lang
%python3_sitelibdir/django_tables2/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 02 2023 Alexander Burmatov <thatman@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus.
