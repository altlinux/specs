%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-pywayland
Version: 0.4.15
Release: alt1

Summary: Python bindings for the libwayland library
License: Apache-2.0
Group: Development/Python3

Url: https://github.com/flacjacket/pywayland
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
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

sed -i -e 's/pywayland_scanner/scanner/' setup.cfg

%build
%__python3 ./pywayland/ffi_build.py
%__python3 -m pywayland.scanner
%pyproject_build

%install
%pyproject_install

# hack to drop .abi3 from binaries
find %buildroot -name '*.abi3*' -exec rename '.abi3' '' {} \;

%check
export TOX_TESTENV_PASSENV="XDG_RUNTIME_DIR"
export XDG_RUNTIME_DIR="${PWD}/temp"
mkdir -p $XDG_RUNTIME_DIR
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.rst
%_bindir/pywayland-scanner
%python3_sitelibdir/pywayland
%python3_sitelibdir/%{pyproject_distinfo pywayland}

%changelog
* Wed Jan 11 2023 Egor Ignatov <egori@altlinux.org> 0.4.15-alt1
- new version 0.4.15

* Tue Jul 26 2022 Egor Ignatov <egori@altlinux.org> 0.4.14-alt1
- new version 0.4.14

* Wed Jul 06 2022 Egor Ignatov <egori@altlinux.org> 0.4.13-alt1
- new version 0.4.13

* Tue Apr 19 2022 Egor Ignatov <egori@altlinux.org> 0.4.12-alt1
- hack to drop .abi3 from binaries
- new version 0.4.12

* Thu Feb 24 2022 Egor Ignatov <egori@altlinux.org> 0.4.11-alt1
- new version 0.4.11

* Fri Jan 21 2022 Stanislav Levin <slev@altlinux.org> 0.4.8-alt2
- Fixed FTBFS (setuptools 60+).

* Thu Jan 13 2022 Egor Ignatov <egori@altlinux.org> 0.4.8-alt1
- new version 0.4.8

* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.4.7-alt1
- First build for ALT
