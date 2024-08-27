%define _unpackaged_files_terminate_build 1
%define pypi_name uvloop

%def_with check

Name: python3-module-%pypi_name
Version: 0.20.0
Release: alt1

Summary: Ultra fast asyncio event loop
License: MIT and Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/uvloop/
Vcs: https://github.com/MagicStack/uvloop

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: setup.py
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libuv-devel

%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
BuildRequires: /proc
BuildRequires: /dev/pts
%endif

%description
uvloop is a fast, drop-in replacement of the built-in asyncio event loop.
uvloop is implemented in Cython and uses libuv under the hood.

%prep
%setup
%autopatch -p1
# Use own setup.py.
%__install %SOURCE2 setup.py
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
# Do not package a module for testing.
%__rm %buildroot%python3_sitelibdir/%pypi_name/_testbase.py

%check
# Tests 'test_write_buffer_full' disabled because of:
# https://github.com/MagicStack/uvloop/issues/576
%__rm -rf %pypi_name
%pyproject_run_pytest \
%ifarch ppc64le
    -k 'not test_write_buffer_full' \
%endif
    -vra

%files
%doc README.rst LICENSE-APACHE LICENSE-MIT
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

