Name:    ortp
Version: 5.3.79
Release: alt1

Summary: oRTP is a C library implementing the RTP protocol (rfc3550)
License: AGPL-3.0
Group:   System/Libraries
URL: https://gitlab.linphone.org/BC/public/ortp

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch: ortp-5.3.74-alt-cmake-config-location.patch
Patch1: ortp-5.3.74-alt-pkgconfig-libdir-location.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libbctoolbox-devel

%description
%summary

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
%summary

%prep
%setup
%autopatch -p1

%build
%cmake -GNinja -Wno-dev -DBUILD_SHARED_LIBS=TRUE
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
rm -rf %buildroot%_defaultdocdir/ortp-5.3.0

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/ortp-tester
%_libdir/*.so
%_includedir/ortp
%_libdir/pkgconfig/%name.pc
%_libdir/cmake/Ortp/
%_datadir/ortp-tester

%changelog
* Tue Sep 03 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.79-alt1
- New version.

* Thu Aug 22 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.77-alt1
- New version.

* Mon Aug 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.74-alt2
- Fixed cmake config location.
- Fixed pkgconfig.

* Fri Aug 02 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.74-alt1
- Initial build for Sisyphus.
