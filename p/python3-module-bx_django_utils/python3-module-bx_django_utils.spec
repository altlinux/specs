%define pypi_name bx_django_utils

Name: python3-module-%pypi_name
Version: 101
Release: alt1

Summary: Various Django utility functions

License: MIT
Group: Development/Python3
Url: https://github.com/boxine/bx_django_utils
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)

# optional test helper, playwright is not packaged
%add_python3_req_skip playwright.sync_api

%description
Various Django utility functions from Boxine:
model, admin, view, data type and test helpers.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# the console script entry point refers to a missing __main__ module
rm -v %buildroot%_bindir/%pypi_name
# upstream unit tests need the development test project
find %buildroot%python3_sitelibdir/%pypi_name -depth -type d -name tests -exec rm -rv {} +

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 101-alt1
- initial build for Sisyphus
