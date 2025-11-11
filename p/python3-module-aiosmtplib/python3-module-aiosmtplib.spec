%define _unpackaged_files_terminate_build 1
%define pypi_name aiosmtplib
%define mod_name aiosmtplib

%def_with check

Name: python3-module-%pypi_name
Version: 5.0.0
Release: alt1

Summary: asyncio SMTP client
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aiosmtplib/
Vcs: https://github.com/cole/aiosmtplib

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra uvloop
%pyproject_builddeps_check
%endif

%description
aiosmtplib is an asynchronous SMTP client for use with asyncio.
It is an async version of the smtplib module, with similar APIs.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc CHANGELOG.rst LICENSE.txt README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 11 2025 Anton Zhukharev <ancieg@altlinux.org> 5.0.0-alt1
- Packaged for ALT Sisyphus.
