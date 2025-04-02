%def_without clang

Name: util-dfm
Version: 1.3.10
Release: alt1

Summary: A Toolkits of libdfm-io, libdfm-mount and libdfm-burn

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/util-dfm
Vcs: https://github.com/linuxdeepin/util-dfm.git

Source: %url/archive/%version/%name-%version.tar.gz
Patch: util-dfm-1.3.10-alt-pkgconfig-dqt6.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: cmake libisoburn-devel libmediainfo-devel libmount-devel libsecret-devel libudisks2-devel dqt6-base-devel
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

%package -n libdfm6-io1
Summary: Library for %name
Group: System/Libraries

%description -n libdfm6-io1
This package provides libdfm-io1 library for %name.

%package -n libdfm6-io-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm6-io-devel
This package provides development files for libdfm-io.

%package -n libdfm6-mount1
Summary: Library for %name
Group: System/Libraries

%description -n libdfm6-mount1
This package provides libdfm-mount1 library for %name.

%package -n libdfm6-mount-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm6-mount-devel
This package provides development files for libdfm-mount.

%package -n libdfm6-burn1
Summary: Library for %name
Group: System/Libraries

%description -n libdfm6-burn1
This package provides libdfm-burn1 library for %name.

%package -n libdfm6-burn-devel
Summary: Development files for %name
Group: Development/Other

%description -n libdfm6-burn-devel
This package provides development files for libdfm-burn.

%prep
%setup
%autopatch -p1
sed -i 's|Version: .*|Version: %version|g' \
  $(find ./misc -name '*.pc.in')

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
%doc README.md LICENSE

%files -n libdfm6-io1
%_libdir/libdfm6-io.so.1*

%files -n libdfm6-io-devel
%_libdir/libdfm6-io.so
%dir %_includedir/dfm6-io/
%_includedir/dfm6-io/dfm-io/
%_pkgconfigdir/dfm6-io.pc
%dir %_libdir/cmake/dfm6-io/
%_libdir/cmake/dfm6-io/dfm6-ioConfig.cmake

%files -n libdfm6-mount1
%_libdir/libdfm6-mount.so.1*

%files -n libdfm6-mount-devel
%_libdir/libdfm6-mount.so
%dir %_includedir/dfm6-mount/
%_includedir/dfm6-mount/dfm-mount/
%_pkgconfigdir/dfm6-mount.pc
%dir %_libdir/cmake/dfm6-mount/
%_libdir/cmake/dfm6-mount/dfm6-mountConfig.cmake

%files -n libdfm6-burn1
%_libdir/libdfm6-burn.so.1*

%files -n libdfm6-burn-devel
%_libdir/libdfm6-burn.so
%dir %_includedir/dfm6-burn/
%_includedir/dfm6-burn/dfm-burn/
%_pkgconfigdir/dfm6-burn.pc
%dir %_libdir/cmake/dfm6-burn/
%_libdir/cmake/dfm6-burn/dfm6-burnConfig.cmake

%changelog
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
