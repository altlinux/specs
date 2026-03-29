%define _unpackaged_files_terminate_build 1
%define pypi_name libarchive-c
%define mod_name libarchive

%def_with check

Name: python3-module-%pypi_name
Version: 5.3
Release: alt1.1
Summary: Python interface to libarchive
License: CC0
Group: Development/Python3
Url: https://pypi.org/project/libarchive-c/
Vcs: https://github.com/Changaco/python-libarchive-c
Source: %name-%version.tar
Patch1: %name-%version-alt.patch
Requires: libarchive

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: libarchive-devel

%if_with check
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-forked
%endif

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
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 5.3-alt1.1
- Demodernized packaging.

* Fri May 23 2025 Stanislav Levin <slev@altlinux.org> 5.3-alt1
- 5.2 -> 5.3.

* Mon Mar 17 2025 Stanislav Levin <slev@altlinux.org> 5.2-alt1
- 5.1 -> 5.2.

* Wed Mar 06 2024 Stanislav Levin <slev@altlinux.org> 5.1-alt1
- 4.0 -> 5.1.

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
