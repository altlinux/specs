%define _unpackaged_files_terminate_build 1
%define pypi_name libarchive-c
%define mod_name libarchive

%def_with check

Name: python3-module-%pypi_name
Version: 4.0
Release: alt2
Summary: Python interface to libarchive
License: CC0
Group: Development/Python3
Url: https://pypi.org/project/libarchive-c/
Vcs: https://github.com/Changaco/python-libarchive-c
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: %name-%version-alt.patch
Requires: libarchive
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif
BuildRequires: libarchive-devel

%description
The libarchive library provides a flexible interface for reading and writing
archives in various formats such as tar and cpio. libarchive also supports
reading and writing archives compressed using various compression filters such
as gzip and bzip2.
A Python interface to libarchive. It uses the standard ctypes module to
dynamically load and access the C library.

%prep
%setup
%patch1 -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

# pure Python package depends on libarchive
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 4.0-alt2
- Modernized packaging.
- Fixed FTBFS (pytest-xdist 3).

* Thu Sep 15 2022 Slava Aseev <ptrnine@altlinux.org> 4.0-alt1
- new version

* Mon Oct 25 2021 Slava Aseev <ptrnine@altlinux.org> 3.1-alt1
- Update to upstream version 3.1

* Thu Mar 12 2020 Slava Aseev <ptrnine@altlinux.org> 2.9-alt1
- Update to upstream version 2.9
- Disable build for python2

* Mon Dec 24 2018 Slava Aseev <ptrnine@altlinux.org> 2.8-alt1
- Initial build for ALT
