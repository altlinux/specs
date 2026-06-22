# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libUvula
Version: 1.0.1
Release: alt4.g3954db41.1

Summary: UV-unwrapper for potentially big meshes
License: LGPL-3.0-only
Group: Development/C++

URL: https://github.com/Ultimaker/libUvula
VCS: https://github.com/Ultimaker/libUvula
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
BuildRequires: libpolyclipping-devel

%description
This library is a standalone UV-unwrapper for potentially big meshes,
that provides grouped and non-overlapping patches of projected faces
on a texture.

%package devel
Summary: Development files for %name
Group:   Development/C++
Requires: %name = %EVR

%description devel
Development files for %name.

%package -n python3-module-pyUvula
Summary: %summary
Group:   Development/Python3
Requires: %name = %EVR

%description -n python3-module-pyUvula
This library is a standalone UV-unwrapper for potentially big meshes,
that provides grouped and non-overlapping patches of projected faces
on a texture.

%prep
%setup

%build
%cmake \
%ifarch %e2k
    -DCMAKE_C{_COMPILER=clang,XX_COMPILER=clang++} \
    -DCMAKE_C{,XX}_FLAGS_RELWITHDEBINFO="-O2 -DNDEBUG" \
%endif
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUVULA_VERSION=%version
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_libdir/libUvula.so.%version

%files devel
%_libdir/libUvula.so
%_includedir/Uvula

%files -n python3-module-pyUvula
%python3_sitelibdir/pyUvula.*.so

%changelog
* Mon Jun 22 2026 Valery Zabrovsky <brow@altlinux.org> 1.0.1-alt4.g3954db41.1
- Switch to more appropriate rolling tagging.

* Fri May 22 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.0.1-alt3
- e2k build fix

* Wed Apr 22 2026 Valery Zabrovsky <brow@altlinux.org> 1.0.1-alt2
- Enable debuginfo for pyUvula.

* Mon Apr 13 2026 Valery Zabrovsky <brow@altlinux.org> 1.0.1-alt1
- Initial build for ALT Sisyphus.
