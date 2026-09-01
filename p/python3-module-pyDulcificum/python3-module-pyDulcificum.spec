%define _unpackaged_files_terminate_build 1
%define modulename pyDulcificum

Name: python3-module-%modulename
Version: 5.11.0
Release: alt1.gf81c0ea9.1

Summary: Translation between the dialects of 3D printer commands
License: LGPL-3.0-only
Group: Development/Python3
URL: https://github.com/Ultimaker/synsepalum-dulcificum
VCS: https://github.com/Ultimaker/synsepalum-dulcificum

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-python3
%ifarch %e2k
BuildRequires: clang
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake
BuildRequires: %_bindir/python3
BuildRequires: pybind11-devel
BuildRequires: libspdlog-devel
BuildRequires: librange-v3-devel
BuildRequires: nlohmann-json-devel
BuildRequires: ctre-devel

%py3_provides %modulename

%description
Dulcificum changes the "flavor", or dialect of 3D printer commands.
Supported dialects include MiracleGrue jsontoolpath and UltiMaker GCode.

%prep
%setup
%autopatch -p1

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
%python3_sitelibdir/%modulename.*.so

%changelog
* Mon Aug 31 2026 Valery Zabrovsky <brow@altlinux.org> 5.11.0-alt1.gf81c0ea9.1
- Build the Python package only.
- Update to latest snapshot.
- Force set C++20 standard.
- Minor spec cleanup.

* Wed May 27 2026 Valery Zabrovsky <brow@altlinux.org> 5.10.2-alt3.gitdfaa4763
- Fix build for e2k (thx ilyakurdyukov@).
- Switch to more appropriate rolling tagging.

* Wed Apr 22 2026 Valery Zabrovsky <brow@altlinux.org> 5.10.2-alt2
- Enable debuginfo for pyDulcificum.

* Sun Apr 19 2026 Valery Zabrovsky <brow@altlinux.org> 5.10.2-alt1
- Initial build for ALT Sisyphus.
