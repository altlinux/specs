%define _unpackaged_files_terminate_build 1
%ifarch x86_64
%def_with check
%else
# Tests are unstable on another architecutres.
%def_without check	
%endif
%define pypi_name aiofile
%define module_name %pypi_name

Name: python3-module-%pypi_name
Version: 3.11.1
Release: alt1

Summary: Real asynchronous file operations with asyncio support
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aiofile/
Vcs: https://github.com/mosquito/aiofile

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

%prep
%setup
%autopatch -p1

# Fix version in pyproject.toml
sed -i '/^version/s/= .*$/= "%version"/' pyproject.toml

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 3.11.1-alt1
- Updated to 3.11.1.

* Wed Apr 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 3.9.0-alt1
- Initial build for ALT Sisyphus.

