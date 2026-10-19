%define pypi_name django_pglock

%def_with check

Name: python3-module-django-pglock
Version: 1.8.0
Release: alt1

Summary: Postgres locking routines and lock table access

License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/AmbitionEng/django-pglock
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-django-pgactivity
BuildRequires: python3-module-typing_extensions
%endif

# python3(pgactivity) is also provided by python3-module-pg_activity, which conflicts with django-pgactivity
%add_python3_req_skip pgactivity pgactivity.config pgactivity.utils

%description
Postgres locking routines and lock table access.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -c 'import pglock'

%files
%doc README*
%python3_sitelibdir/pglock/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- initial build for Sisyphus
