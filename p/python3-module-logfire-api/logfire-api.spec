%define _unpackaged_files_terminate_build 1
%define pypi_name logfire-api
%define module_name logfire_api

Name: python3-module-logfire-api
Version: 5.6.0
Release: alt1

Summary: Shim for the Logfire SDK which does nothing unless Logfire is installed
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/logfire-api/
VCS: https://github.com/pydantic/logfire
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
# The shim has no tests of its own: tests/test_logfire_api.py exercises
# it in python3-module-logfire-sdk.
%pyproject_configure_without_autodiscovery
%pyproject_configure_pypi_package

%description
%summary.

%prep
%setup
%autopatch -p1
cd logfire-api
%pyproject_setup_deps
cd -

%build
cd logfire-api
%pyproject_build
cd -

%install
cd logfire-api
%pyproject_install
cd -

%files
%doc logfire-api/README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.6.0-alt1
- Updated to 5.6.0.

* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.4.0-alt1
- Updated to 5.4.0.

* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.1.1-alt1
- Initial build for ALT Sisyphus.
