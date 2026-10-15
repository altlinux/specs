%define pypi_name djangoql

%def_with check

Name: python3-module-djangoql
Version: 0.19.1
Release: alt1

Summary: Advanced search language for Django

License: MIT
Group: Development/Python3
URL: https://github.com/ivelum/djangoql
# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_disabled check
%else
BuildRequires: python3-module-ply
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
Advanced search language for Django.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
cd test_project
DJANGO_SETTINGS_MODULE=test_project.settings %__python3 manage.py test core

%files
%doc README*
%python3_sitelibdir/djangoql/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.19.1-alt1
- initial build for Sisyphus
