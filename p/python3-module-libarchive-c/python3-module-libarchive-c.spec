%define _unpackaged_files_terminate_build 1
%define modname libarchive-c

Name: python3-module-%modname
Version: 3.1
Release: alt1

Summary: Python interface to libarchive
Group: Development/Python3
License: CC0
Url: https://github.com/Changaco/python-libarchive-c

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: libarchive-devel
BuildRequires: python3-devel
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-six
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-xdist

Requires: libarchive

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

sed -i "s/@VERSION@/%version/" version.py

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir

%check
export LANG=en_US.UTF-8
export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH=%python3_sitelibdir_noarch:%python3_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py%{python_version_nodots python3} -v

%files
%doc README.rst
%doc LICENSE.md
%python3_sitelibdir/libarchive*

%changelog
* Mon Oct 25 2021 Slava Aseev <ptrnine@altlinux.org> 3.1-alt1
- Update to upstream version 3.1

* Thu Mar 12 2020 Slava Aseev <ptrnine@altlinux.org> 2.9-alt1
- Update to upstream version 2.9
- Disable build for python2

* Mon Dec 24 2018 Slava Aseev <ptrnine@altlinux.org> 2.8-alt1
- Initial build for ALT
