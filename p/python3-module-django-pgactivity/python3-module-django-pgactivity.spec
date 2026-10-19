%define pypi_name django_pgactivity

Name: python3-module-django-pgactivity
Version: 1.8.0
Release: alt1

Summary: Monitor, kill, and analyze Postgres queries

License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/AmbitionEng/django-pgactivity
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch
Conflicts: python3-module-pg_activity
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
Monitor, kill, and analyze Postgres queries.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README*
%python3_sitelibdir/pgactivity/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- initial build for Sisyphus
