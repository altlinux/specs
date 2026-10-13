%define pypi_name bx_py_utils

Name: python3-module-%pypi_name
Version: 121
Release: alt1

Summary: Various Python utility functions

License: MIT
Group: Development/Python3
Url: https://github.com/boxine/bx_py_utils
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)

# optional AWS helper (bx_py_utils.aws.secret_manager)
%add_python3_req_skip boto3

%description
Various Python utility functions from Boxine:
string, dict, path, hashing and test helpers.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# the console script entry point refers to a missing __main__ module
rm -v %buildroot%_bindir/%pypi_name

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 121-alt1
- initial build for Sisyphus
