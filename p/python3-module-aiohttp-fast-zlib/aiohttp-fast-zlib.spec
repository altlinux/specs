Name: python3-module-aiohttp-fast-zlib
Version: 0.3.0
Release: alt1

Summary: Another nothingburger
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohttp-fast-zlib
VCS: https://github.com/bluetooth-devices/aiohttp-fast-zlib

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra isal
%pyproject_builddeps_metadata_extra zlib_ng
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/aiohttp_fast_zlib
%python3_sitelibdir/aiohttp_fast_zlib-%version.dist-info

%changelog
* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.0-alt1
- 0.3.0 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.1-alt1
- 0.1.1 released
