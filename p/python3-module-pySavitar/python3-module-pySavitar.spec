%define _unpackaged_files_terminate_build 1
%define modulename pySavitar

Name: python3-module-%modulename
Version: 5.12.0
Release: alt1.g74cbe2bd.1

Summary: Python bindings for C++ implementation of 3mf loading
License: LGPL-3.0-or-later AND BSD-3-Clause
Group: Development/Python3
URL: https://github.com/Ultimaker/pySavitar
VCS: https://github.com/Ultimaker/pySavitar

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libpugixml-devel
BuildRequires: python3-dev
BuildRequires: libsavitar-devel = 5.12.0
BuildRequires: python3-module-sip6
BuildRequires: python3-module-PyQt6-sip

Requires: libsavitar = 5.12.0
Requires: python3-module-PyQt6-sip

%py3_provides %modulename
Provides: python3-module-savitar = %EVR
Obsoletes: python3-module-savitar

%description
%summary.

%prep
%setup
%autopatch -p1

%build
# Decode PyQt6.sip ABI version from bytewise value
export PyQt6_SIP_ABI_VERSION=$(python3 <<__EOF__
from PyQt6.sip import SIP_ABI_VERSION as abi
print(f'{abi >> 16}.{abi >> 8 & 0xff}')
__EOF__
)

%cmake -DPyQt6_SIP_ABI_VERSION=$PyQt6_SIP_ABI_VERSION
%cmake_build

%install
%cmake_install

%files
%python3_sitelibdir/%modulename.so
%python3_sitelibdir/%modulename.pyi

%changelog
* Mon Aug 31 2026 Valery Zabrovsky <brow@altlinux.org> 5.12.0-alt1.g74cbe2bd.1
- Initial build for ALT Sisyphus (as a separate package).
