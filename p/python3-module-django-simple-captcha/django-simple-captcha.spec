%define _unpackaged_files_terminate_build 1
%define pypi_name django-simple-captcha
%define mod_name captcha

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: A very simple, yet powerful, Django captcha application

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/django-simple-captcha/

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

Conflicts: python3-module-django-recaptcha

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

# https://lists.altlinux.org/pipermail/devel/2024-July/218790.html
AutoProv: no


%description
Django Simple Captcha is an extremely simple,
yet highly customizable Django application to add captcha images to any Django form.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/


%changelog
* Fri Jun 28 2024 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- initial build for Sisyphus
- disable AutoProv due missed python module alternatives support
