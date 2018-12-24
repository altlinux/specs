%define _unpackaged_files_terminate_build 1
%define modname libarchive-c
%def_with python3

Name: python-module-%modname
Version: 2.8
Release: alt1

Summary: Python interface to libarchive
Group: Development/Python
License: CC0
Url: https://github.com/Changaco/python-libarchive-c

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: libarchive-devel
BuildRequires: python-devel 
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python-module-six
BuildRequires: python-module-mock
BuildRequires: python-module-pytest-cov
BuildRequires: python-module-pytest-xdist

%if_with python3
BuildRequires: python3-devel
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-six
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-xdist
%endif

Requires: libarchive

%define _description The libarchive library provides a flexible interface for reading and writing   \
archives in various formats such as tar and cpio. libarchive also supports     \
reading and writing archives compressed using various compression filters such \
as gzip and bzip2.                                                             \
A Python interface to libarchive. It uses the standard ctypes module to        \
dynamically load and access the C library.

%description
%_description

%if_with python3
%package -n python3-module-%modname
Summary: %summary
Group: Development/Python3
Requires: libarchive
%description -n python3-module-%modname
%_description
%endif

%prep
%setup
%patch1 -p1

sed -i "s/@VERSION@/%version/" version.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --install-lib %python_sitelibdir

%if_with python3
pushd ../python3
%python3_install --install-lib %python3_sitelibdir
popd
%endif

%check
export LANG=en_US.UTF-8
export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH=%python_sitelibdir_noarch:%python_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py%{python_version_nodots python} -v

%if_with python3
pushd ../python3
export PYTHONPATH=%python3_sitelibdir_noarch:%python3_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py%{python_version_nodots python3} -v
popd
%endif

%files
%doc README.rst
%doc LICENSE.md
%python_sitelibdir/libarchive*

%if_with python3
%files -n python3-module-%modname
%doc README.rst
%doc LICENSE.md
%python3_sitelibdir/libarchive*
%endif

%changelog
* Mon Dec 24 2018 Slava Aseev <ptrnine@altlinux.org> 2.8-alt1
- Initial build for ALT
