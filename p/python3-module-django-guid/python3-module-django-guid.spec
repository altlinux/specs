%define pypi_name django-guid

%def_with check

Name: python3-module-%pypi_name
Version: 3.5.0
Release: alt1

Summary: Middleware that enables single request-response cycle tracing by injecting a unique ID into project logs
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/django-guid
VCS: https://github.com/snok/django-guid

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django
BuildRequires: python3-module-celery
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-sentry-sdk
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-subtests
%endif

%description
Django GUID attaches a unique correlation ID/request ID to all your log outputs
for every request. In other words, all logs connected to a request now has
a unique ID attached to it, making debugging simple.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%python3_sitelibdir/django_guid
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/CHANGELOG.rst

%changelog
* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus.
