%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-pywayland
Version: 0.4.7
Release: alt1

Summary: Python bindings for the libwayland library
License: Apache-2.0
Group: Development/Python3

Url: https://github.com/flacjacket/pywayland
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-cffi
BuildRequires: libwayland-server-devel
BuildRequires: libwayland-client-devel
BuildRequires: wayland-protocols

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
PyWayland provides a wrapper to the libwayland library using the CFFI
library to provide access to the Wayland library calls and written in
pure Python.

%prep
%setup
%patch0 -p1

%build
%__python3 ./pywayland/ffi_build.py
%__python3 -m pywayland.scanner
%python3_build

%install
%python3_install

%check
export XDG_RUNTIME_DIR="${PWD}/temp"
mkdir $XDG_RUNTIME_DIR
%__python3 -m pytest test

%files
%doc LICENSE README.rst
%_bindir/pywayland-scanner
%python3_sitelibdir/pywayland
%python3_sitelibdir/*.egg-info

%changelog
* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.4.7-alt1
- First build for ALT
