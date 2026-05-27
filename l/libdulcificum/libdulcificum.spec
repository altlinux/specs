# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libdulcificum
Version: 5.10.2
Release: alt3.gitdfaa4763

Summary: Translation between the dialects of 3D printer commands
License: LGPL-3.0-only
Group: Development/C++

URL: https://github.com/Ultimaker/synsepalum-dulcificum
VCS: https://github.com/Ultimaker/synsepalum-dulcificum
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-python3
BuildRequires: gcc-c++ cmake
%ifarch %e2k
BuildRequires: clang
%endif
BuildRequires: %_bindir/python3
BuildRequires: pybind11-devel
BuildRequires: libspdlog-devel
BuildRequires: librange-v3-devel
BuildRequires: nlohmann-json-devel
BuildRequires: ctre-devel

%description
Dulcificum changes the or dialect of 3D printer commands.
Supported dialects include MiracleGrue jsontoolpath and UltiMaker GCode.

%package devel
Summary: Development files for %name
Group:   Development/C++
Requires: %name = %EVR

%description devel
Development files for %name.

%package -n python3-module-pyDulcificum
Summary: %summary
Group:   Development/Python3
Requires: %name = %EVR
%py3_provides pyDulcificum

%description -n python3-module-pyDulcificum
Dulcificum changes the or dialect of 3D printer commands.
Supported dialects include MiracleGrue jsontoolpath and UltiMaker GCode.

%prep
%setup

%build
%cmake \
%ifarch %e2k
    -DCMAKE_C{_COMPILER=clang,XX_COMPILER=clang++} \
    -DCMAKE_C{,XX}_FLAGS_RELWITHDEBINFO="-O2 -DNDEBUG" \
%endif
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DDULCIFICUM_VERSION=%version \
    -DENABLE_TESTS=OFF \
    -DWITH_APPS=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_libdir/libdulcificum.so.%version

%files devel
%_libdir/libdulcificum.so
%_includedir/dulcificum.h
%_includedir/dulcificum

%files -n python3-module-pyDulcificum
%python3_sitelibdir/pyDulcificum.*.so

%changelog
* Wed May 27 2026 Valery Zabrovsky <brow@altlinux.org> 5.10.2-alt3.gitdfaa4763
- Fix build for e2k (thx ilyakurdyukov@).
- Switch to more appropriate rolling tagging.

* Wed Apr 22 2026 Valery Zabrovsky <brow@altlinux.org> 5.10.2-alt2
- Enable debuginfo for pyDulcificum.

* Sun Apr 19 2026 Valery Zabrovsky <brow@altlinux.org> 5.10.2-alt1
- Initial build for ALT Sisyphus.
