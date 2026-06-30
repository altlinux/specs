%define _libexecdir %_prefix/libexec

%def_without clang

%define sover 1

Name: util-dfm
Version: 1.3.59
Release: alt1

Summary: A Toolkits of libdfm-io, libdfm-mount, libdfm-burn and libdfm-search

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/util-dfm
Vcs: https://github.com/linuxdeepin/util-dfm

# Source-url: https://github.com/linuxdeepin/util-dfm/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: util-dfm-1.3.43-alt-pkgconfig-dqt6.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: cmake libisoburn-devel libmediainfo-devel libmount-devel libsecret-devel libudisks2-devel dqt6-base-devel dtk6-common-devel libdtk6core-devel liblucene++-devel
BuildRequires: libdqt6-concurrent libdqt6-widgets libdqt6-test vulkan-headers
%if_enabled clang
BuildRequires: clang-devel
BuildRequires: lld-devel
BuildRequires: llvm-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package doc
Summary: Documentation for %name.
Group: Documentation
BuildArch: noarch

%description doc
This package provides documentation for %name.

%package -n libdfm6-io%sover
Summary: Library for %name
Group: System/Libraries

%description -n libdfm6-io%sover
This package provides libdfm-io library for %name.

%package -n libdfm6-io-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm6-io-devel
This package provides development files for libdfm-io.

%package -n libdfm6-mount%sover
Summary: Library for %name
Group: System/Libraries

%description -n libdfm6-mount%sover
This package provides libdfm-mount library for %name.

%package -n libdfm6-mount-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm6-mount-devel
This package provides development files for libdfm-mount.

%package -n dfm-burner
Summary: dfm6-burner-client by %name
Group: Graphical desktop/Other

%description -n dfm-burner
This package provides dfm6-burner-client aka dfm-burner.

%package -n libdfm6-burn%sover
Summary: Library for %name
Group: System/Libraries

%description -n libdfm6-burn%sover
This package provides libdfm-burn library for %name.

%package -n libdfm6-burn-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm6-burn-devel
This package provides development files for libdfm-burn.

%package -n dfm-searcher
Summary: dfm6-search-client by %name
Group: Graphical desktop/Other
Provides: dfm6-search-client = %EVR
Obsoletes: dfm6-search-client < %EVR

%description -n dfm-searcher
This package provides dfm6-search-client aka dfm-search.

%package -n libdfm6-search%sover
Summary: Library for %name
Group: System/Libraries

%description -n libdfm6-search%sover
This package provides libdfm-search library for %name.

%package -n libdfm6-search-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm6-search-devel
This package provides development files for libdfm-search.

%prep
%setup
%patch0 -p1
%patch1 -p2
sed -i 's|Version: .*|Version: %version|g' \
  $(find ./misc -name '*.pc.in')
# remove broken requires
sed -i 's| Boostsystem Threads||' \
  misc/dfm-search/dfm-search.pc.in

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build \
  -DPROJECT_VERSION=%version \
  -DVERSION=%version \
#

%install
%DQ6install

%files doc
%doc README.md LICENSE debian/changelog

%files -n libdfm6-io%sover
%_libdir/libdfm6-io.so.%sover
%_libdir/libdfm6-io.so.%version

%files -n libdfm6-io-devel
%_libdir/libdfm6-io.so
%dir %_includedir/dfm6-io/
%_includedir/dfm6-io/dfm-io/
%_pkgconfigdir/dfm6-io.pc
%dir %_libdir/cmake/dfm6-io/
%_libdir/cmake/dfm6-io/dfm6-ioConfig.cmake

%files -n libdfm6-mount%sover
%_libdir/libdfm6-mount.so.%sover
%_libdir/libdfm6-mount.so.%version

%files -n libdfm6-mount-devel
%_libdir/libdfm6-mount.so
%dir %_includedir/dfm6-mount/
%_includedir/dfm6-mount/dfm-mount/
%_pkgconfigdir/dfm6-mount.pc
%dir %_libdir/cmake/dfm6-mount/
%_libdir/cmake/dfm6-mount/dfm6-mountConfig.cmake

%files -n libdfm6-burn%sover
%_libdir/libdfm6-burn.so.%sover
%_libdir/libdfm6-burn.so.%version

%files -n dfm-burner
%_bindir/dfm-burner

%files -n libdfm6-burn-devel
%_libdir/libdfm6-burn.so
%dir %_includedir/dfm6-burn/
%_includedir/dfm6-burn/dfm-burn/
%_pkgconfigdir/dfm6-burn.pc
%dir %_libdir/cmake/dfm6-burn/
%_libdir/cmake/dfm6-burn/dfm6-burnConfig.cmake

%files -n dfm-searcher
%_bindir/dfm-searcher
%dir %_datadir/deepin/
%_datadir/deepin/dfm-search/

%files -n libdfm6-search%sover
%_libdir/libdfm6-search.so.%sover
%_libdir/libdfm6-search.so.%version

%files -n libdfm6-search-devel
%_libdir/libdfm6-search.so
%dir %_includedir/dfm6-search/
%_includedir/dfm6-search/dfm-search/
%_pkgconfigdir/dfm6-search.pc
%dir %_libdir/cmake/dfm6-search/
%_libdir/cmake/dfm6-search/dfm6-search*.cmake

%changelog
* Tue Jun 30 2026 Leontiy Volodin <lvol@altlinux.org> 1.3.59-alt1
- New version 1.3.59.
- Added: dfm-searcher.

* Wed Apr 29 2026 Leontiy Volodin <lvol@altlinux.org> 1.3.53-alt1
- New version 1.3.53.
- Renamed: dfm6-search-client -> dfm-searcher.

* Mon Apr 13 2026 Leontiy Volodin <lvol@altlinux.org> 1.3.51-alt1
- New version 1.3.51.

* Fri Feb 27 2026 Leontiy Volodin <lvol@altlinux.org> 1.3.43-alt2
- Fixed build on shrinked dqt6.

* Thu Dec 25 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.43-alt1
- New version 1.3.43.

* Wed Oct 22 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.39-alt1
- New version 1.3.39.

* Wed Sep 10 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.37-alt1
- New version 1.3.37.

* Wed Jul 30 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.34-alt1
- New version 1.3.34.

* Thu Jun 26 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.30-alt1
- New version 1.3.30.

* Mon Apr 14 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.15-alt1
- New version 1.3.15.
- Fixed build with cmake 4.0.0.

* Tue Mar 11 2025 Leontiy Volodin <lvol@altlinux.org> 1.3.10-alt1
- New version 1.3.10.
- Added vcs tag.
- Switched to dqt6.

* Thu May 16 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.24-alt1
- New version 1.2.24.
- Built via separate qt5 instead system (ALT #48138).

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.23-alt1
- New version 1.2.23.

* Fri Mar 01 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.22-alt1
- New version 1.2.22.
- No more needed libqt5-core = %%_qt5_version.

* Thu Jan 25 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.21-alt2
- Requires: libqt5-core = %%_qt5_version.

* Thu Jan 18 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.21-alt1
- New version 1.2.21.

* Tue Jan 09 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.20.0.3.2827-alt1
- New version 1.2.20-3-g2827d7b.

* Tue Oct 24 2023 Leontiy Volodin <lvol@altlinux.org> 1.2.17-alt1
- Initial build for ALT Sisyphus.
- Needed for deepin-file-manager 6.0.13.
