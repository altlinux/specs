%define _unpackaged_files_terminate_build 1
%define modulename pyUvula

Name: python3-module-%modulename
Version: 1.0.2
Release: alt1.g7559e5c3.1

Summary: UV-unwrapper for potentially big meshes
License: LGPL-3.0-only
Group: Development/Python3
URL: https://github.com/Ultimaker/libUvula
VCS: https://github.com/Ultimaker/libUvula

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
BuildRequires: libpolyclipping-devel

%py3_provides %modulename

%description
This library is a standalone UV-unwrapper for potentially big meshes,
that provides grouped and non-overlapping patches of projected faces
on a texture.

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
    -DUVULA_VERSION=%version
%cmake_build

%install
%cmake_install

%files
%doc README.md
%python3_sitelibdir/%modulename.*.so

%changelog
* Mon Aug 31 2026 Valery Zabrovsky <brow@altlinux.org> 1.0.2-alt1.g7559e5c3.1
- Build the Python package only.
- Update to latest snapshot.
- Minor spec cleanup.

* Mon Jun 22 2026 Valery Zabrovsky <brow@altlinux.org> 1.0.1-alt4.g3954db41.1
- Switch to more appropriate rolling tagging.

* Fri May 22 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.0.1-alt3
- e2k build fix

* Wed Apr 22 2026 Valery Zabrovsky <brow@altlinux.org> 1.0.1-alt2
- Enable debuginfo for pyUvula.

* Mon Apr 13 2026 Valery Zabrovsky <brow@altlinux.org> 1.0.1-alt1
- Initial build for ALT Sisyphus.
