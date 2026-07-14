%define _unpackaged_files_terminate_build 1
%define soversion 2.1
%def_with check
%define ver_maj %(echo %version | awk -F. '{print $1}')

Name: libccd
Version: 2.1
Release: alt3

Summary: Library for collision detection between two convex shapes
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/danfis/libccd
Vcs: https://github.com/danfis/libccd

Source: %name-%version.tar
Patch0: libccd-2.1-ctest.patch
Patch1: libccd-2.1-pkgconfig.patch
Patch2: libccd-2.1-py3.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: gcc-c++

%if_with check
BuildRequires: ctest
BuildRequires: python3
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
BuildRequires: /proc
%endif

%description
libccd implements variation on Gilbert-Johnson-Keerthi algorithm plus Expand
Polytope Algorithm (EPA) and also implements algorithm Minkowski Portal
Refinement (MPR, a.k.a. XenoCollide) as described in Game Programming Gems 7.

%package -n libccd%soversion
Summary: %summary
Group: System/Libraries
Obsoletes: libccd

%description -n libccd%soversion
libccd implements variation on Gilbert-Johnson-Keerthi algorithm plus Expand
Polytope Algorithm (EPA) and also implements algorithm Minkowski Portal
Refinement (MPR, a.k.a. XenoCollide) as described in Game Programming Gems 7.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%summary

%prep
%setup
%autopatch -p1

%build
%cmake \
  -GNinja \
  -Wno-dev \
  -DENABLE_DOUBLE_PRECISION=ON \
  -DBUILD_TESTING=ON \
  #

%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
rm -f %buildroot%_defaultdocdir/ccd/BSD-LICENSE

%check
%ctest \
%ifnarch %valgrind_arches
  -E 'ccdtest-valgrind.*' \
%endif
  #

%files -n libccd%soversion
%doc BSD-LICENSE README.md
%_libdir/libccd.so.%ver_maj
%_libdir/libccd.so.%soversion

%files devel
%_includedir/ccd
%_libdir/libccd.so
%_libdir/pkgconfig/*.pc
%_libdir/ccd

%changelog
* Tue Jul 14 2026 Ivan A. Melnikov <iv@altlinux.org> 2.1-alt3
- NMU: Don't run valgrind tests on architectures that valgrind
  does not support (fixes FTBFS on loongarch64).

* Fri Dec 12 2025 Pavel Petrykin <silverducks@altlinux.org> 2.1-alt2
- Enable double precision.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- Initial build for Sisyphus.
