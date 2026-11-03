%define pypi_name postorius

Name: python3-module-postorius
Version: 1.3.13
Release: alt1
Summary: Django web interface for GNU Mailman 3

License: GPL-3.0-or-later
Group: Development/Python3
URL: https://gitlab.com/mailman/postorius
# Source-url: %__pypi_url postorius
Source: %name-%version.tar

Patch0: postorius-django52.patch

Patch1: postorius-CVE-2026-44742.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pdm-backend

%description
A web user interface for GNU Mailman.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/postorius/tests

%files
%python3_sitelibdir/postorius/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1.3.13-alt1
- initial build for ALT Sisyphus

