%define pypi_name django-haystack

Name: python3-module-django-haystack
Version: 3.4.0
Release: alt1
Summary: Modular search integration for Django

License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/django-haystack/django-haystack
# Source-url: %__pypi_url django_haystack
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-setuptools_scm python3-module-wheel

%description
Pluggable search for Django..

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/haystack/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt1
- initial build for ALT Sisyphus

