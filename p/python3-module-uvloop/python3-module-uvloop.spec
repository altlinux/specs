%define _unpackaged_files_terminate_build 1
%define pypi_name uvloop
%define mod_name uvloop

%def_with check

Name: python3-module-%pypi_name
Version: 0.22.1
Release: alt3.11.ga308f75

Summary: Ultra fast asyncio event loop
License: MIT and Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/uvloop/
Vcs: https://github.com/MagicStack/uvloop

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libuv-devel
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: /proc
BuildRequires: /dev/pts
%endif

%description
uvloop is a fast, drop-in replacement of the built-in asyncio event loop.
uvloop is implemented in Cython and uses libuv under the hood.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%global build_option "build_ext", "--cython-always","--use-system-libuv"
%pyproject_build \
  --backend-config-settings='{"--build-option": [%build_option]}'

%install
%pyproject_install
# Do not package a module for testing.
%__rm %buildroot%python3_sitelibdir/%mod_name/_testbase.py

%check
rm -rf %mod_name
%pyproject_run_unittest discover -v tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Anton Zhukharev <ancieg@altlinux.org> 0.22.1-alt3.11.ga308f75
- Fixed FTBFS (python>=3.13).

* Thu Dec 18 2025 Anton Zhukharev <ancieg@altlinux.org> 0.22.1-alt2
- Fixed FTBFS (fixed python version predicate in tests).

* Fri Oct 17 2025 Anton Zhukharev <ancieg@altlinux.org> 0.22.1-alt1
- Updated to 0.22.1.
- Reverted building scheme "fixing".

* Wed Oct 30 2024 Grigory Ustinov <grenka@altlinux.org> 0.21.0-alt2
- Fixed building scheme for backport to stable branches.

* Tue Oct 22 2024 Anton Zhukharev <ancieg@altlinux.org> 0.21.0-alt1
- Updated to 0.21.0.

* Tue Aug 27 2024 Anton Zhukharev <ancieg@altlinux.org> 0.20.0-alt1
- Updated to 0.20.0.

* Fri Apr 12 2024 Anton Zhukharev <ancieg@altlinux.org> 0.19.0-alt3
- Fixed FTBFS (libuv 1.48.0).

* Tue Dec 19 2023 Anton Zhukharev <ancieg@altlinux.org> 0.19.0-alt2
- Fixed building with cython>3.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.19.0-alt1
- Updated to 0.19.0.

* Sun Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.18.0-alt1
- Updated to 0.18.0.

* Sun Oct 15 2023 Anton Zhukharev <ancieg@altlinux.org> 0.17.0-alt2
- Enabled %%check.
- Cleaned up the package content.

* Sun Nov 06 2022 Anton Zhukharev <ancieg@altlinux.org> 0.17.0-alt1
- update to 0.17.0

* Thu Aug 11 2022 Anton Zhukharev <ancieg@altlinux.org> 0.16.0-alt1
- initial build for Sisyphus
