%define pypi_name django_pgtrigger

Name: python3-module-django-pgtrigger
Version: 4.17.0
Release: alt1

Summary: Postgres trigger support integrated with Django models

License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/AmbitionEng/django-pgtrigger
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
Postgres trigger support integrated with Django models.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README*
%python3_sitelibdir/pgtrigger/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 4.17.0-alt1
- initial build for Sisyphus
