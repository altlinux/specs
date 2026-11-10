%define _unpackaged_files_terminate_build 1
%define pypi_name typesafe-sdk
%define mod_name typesafe_sdk

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.5
Release: alt1

Summary: Python SDK for TypeSafe AI API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/typesafe-sdk/
Vcs: https://github.com/typesafe-ai/typesafe-sdk-python

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%pyproject_configure_with_check_filter pyrefly
%pyproject_configure_with_check_filter tach
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
The official Python library for the TypeSafe API.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -k 'not (test_public_typing or test_wrap_bio_lock_only_on_affected_truststore)'

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 10 2026 Anton Zhukharev <ancieg@altlinux.org> 0.7.5-alt1
- Packaged for ALT Sisyphus.
