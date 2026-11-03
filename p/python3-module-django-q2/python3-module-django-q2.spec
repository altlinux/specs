%define pypi_name django-q2

# Optional IronMQ broker is not needed by the default ORM broker.
%add_python3_req_skip iron_mq

Name: python3-module-django-q2
Version: 1.11.1
Release: alt1
Summary: Multiprocessing distributed task queue for Django

License: MIT
Group: Development/Python3
URL: https://github.com/django-q2/django-q2
# Source-url: %__pypi_url django_q2
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-uv-build

%description
A multiprocessing distributed task queue for Django.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/django_q/tests

%files
%python3_sitelibdir/django_q/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1.11.1-alt1
- initial build for ALT Sisyphus

