%def_without clang

Name: util-dfm
Version: 1.2.24
Release: alt1

Summary: A Toolkits of libdfm-io, libdfm-mount and libdfm-burn

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/util-dfm

Source: %url/archive/%version/%name-%version.tar.gz
Patch: util-dfm-1.2.24-alt-pkgconfig-dqt5.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
# Automatically added by buildreq on Tue Oct 24 2023
# optimized out: cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libgio-devel libglvnd-devel libgpg-error libp11-kit libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-widgets libsasl2-3 libssl-devel libstdc++-devel libzen-devel pkg-config python3 python3-base sh5 zlib-devel
BuildRequires: cmake libisoburn-devel libmediainfo-devel libmount-devel libsecret-devel libudisks2-devel dqt5-base-devel
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

%package -n libdfm-io1
Summary: Library for %name
Group: System/Libraries

%description -n libdfm-io1
This package provides libdfm-io1 library for %name.

%package -n libdfm-io-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm-io-devel
This package provides development files for libdfm-io.

%package -n libdfm-mount1
Summary: Library for %name
Group: System/Libraries

%description -n libdfm-mount1
This package provides libdfm-mount1 library for %name.

%package -n libdfm-mount-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm-mount-devel
This package provides development files for libdfm-mount.

%package -n libdfm-burn1
Summary: Library for %name
Group: System/Libraries

%description -n libdfm-burn1
This package provides libdfm-burn1 library for %name.

%package -n libdfm-burn-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm-burn-devel
This package provides development files for libdfm-burn.

%prep
%setup
%patch -p1

%build
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files doc
%doc README.md LICENSE

%files -n libdfm-io1
%_libdir/libdfm-io.so.*

%files -n libdfm-io-devel
%_libdir/libdfm-io.so
%dir %_includedir/dfm-io/
%_includedir/dfm-io/dfm-io/
%_pkgconfigdir/dfm-io.pc
%dir %_libdir/cmake/dfm-io/
%_libdir/cmake/dfm-io/dfm-ioConfig.cmake

%files -n libdfm-mount1
%_libdir/libdfm-mount.so.*

%files -n libdfm-mount-devel
%_libdir/libdfm-mount.so
%dir %_includedir/dfm-mount/
%_includedir/dfm-mount/dfm-mount/
%_pkgconfigdir/dfm-mount.pc
%dir %_libdir/cmake/dfm-mount/
%_libdir/cmake/dfm-mount/dfm-mountConfig.cmake

%files -n libdfm-burn1
%_libdir/libdfm-burn.so.*

%files -n libdfm-burn-devel
%_libdir/libdfm-burn.so
%dir %_includedir/dfm-burn/
%_includedir/dfm-burn/dfm-burn/
%_pkgconfigdir/dfm-burn.pc
%dir %_libdir/cmake/dfm-burn/
%_libdir/cmake/dfm-burn/dfm-burnConfig.cmake

%changelog
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
