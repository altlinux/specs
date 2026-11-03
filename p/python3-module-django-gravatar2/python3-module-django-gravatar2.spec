%define pypi_name django-gravatar2

Name: python3-module-django-gravatar2
Version: 1.4.5
Release: alt1
Summary: Gravatar helpers and template tags for Django

License: MIT
Group: Development/Python3
URL: https://github.com/twaddington/django-gravatar
# Source-url: %__pypi_url django_gravatar2
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Essential Gravatar support for Django. Features helper methods, templatetags and a full test suite!.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/django_gravatar/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1.4.5-alt1
- initial build for ALT Sisyphus

