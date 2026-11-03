%define pypi_name django-mailman3

Name: python3-module-django-mailman3
Version: 1.3.15
Release: alt1
Summary: Common Django applications and templates for Mailman 3

License: GPL-3.0-or-later
Group: Development/Python3
URL: https://gitlab.com/mailman/django-mailman3
# Source-url: %__pypi_url django_mailman3
Source: %name-%version.tar
Patch0: django-mailman3-django52.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pdm-backend

%description
Django library to help interaction with Mailman.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/django_mailman3/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1.3.15-alt1
- initial build for ALT Sisyphus

