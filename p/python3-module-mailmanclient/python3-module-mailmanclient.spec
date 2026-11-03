%define pypi_name mailmanclient

Name: python3-module-%pypi_name
Version: 3.3.5
Release: alt1
Summary: Python bindings for the GNU Mailman 3 REST API

License: LGPL-3.0-or-later
Group: Development/Python3
URL: https://gitlab.com/mailman/mailmanclient
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
The mailmanclient library provides official Python bindings for the GNU
Mailman 3 REST API, including list, domain and membership management.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/mailmanclient/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 3.3.5-alt1
- initial build for ALT Sisyphus

