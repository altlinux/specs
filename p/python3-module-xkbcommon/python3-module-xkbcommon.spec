%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-xkbcommon
Version: 0.8
Release: alt1

Summary: Python bindings for libxkbcommon using cffi
License: MIT
Group: Development/Python3

Url: https://github.com/sde1000/python-xkbcommon
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-cffi
BuildRequires: libxkbcommon-tools
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: xkeyboard-config
%endif

%description
Python bindings for libxkbcommon using cffi.

%prep
%setup
%patch0 -p1

%build
%__python3 ./xkbcommon/ffi_build.py
%python3_build


%install
%python3_install
# FIXME
mv %buildroot%python3_sitelibdir/xkbcommon/_ffi.abi3.so %buildroot%python3_sitelibdir/xkbcommon/_ffi.so

%check
%__python3 -m pytest -v tests

%files
%doc LICENSE README.rst
%python3_sitelibdir/xkbcommon
%python3_sitelibdir/*.egg-info

%changelog
* Sat Jan 14 2023 Egor Ignatov <egori@altlinux.org> 0.8-alt1
- new version 0.8

* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.4-alt1
- First build for ALT
