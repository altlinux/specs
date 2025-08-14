Name:    ortp
Version: 5.4.37
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
* Thu Aug 14 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.37-alt1
- New version.

* Wed Aug 13 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.36-alt1
- New version.

* Fri Aug 01 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.33-alt1
- New version.

* Sat Jul 26 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.30-alt1
- New version.

* Thu Jul 24 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.29-alt1
- New version.

* Wed Jul 23 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.28-alt1
- New version.

* Wed Jun 25 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.24-alt1
- New version.

* Fri Jun 20 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.23-alt1
- New version.

* Sat Jun 07 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.21-alt1
- New version.

* Wed May 28 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.20-alt1
- New version.

* Tue May 20 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.18-alt1
- New version.

* Sat May 17 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.17-alt1
- New version.

* Thu May 15 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.16-alt1
- New version.

* Sat May 10 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.15-alt1
- New version.

* Wed May 07 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.14-alt1
- New version.

* Sat May 03 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.13-alt1
- New version.

* Wed Apr 30 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.12-alt1
- New version.

* Thu Apr 24 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.11-alt1
- New version.

* Fri Apr 18 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.9-alt1
- New version.

* Wed Apr 09 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.7-alt1
- New version.

* Fri Mar 21 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.2-alt1
- New version.

* Wed Mar 19 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version.

* Wed Mar 12 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version.

* Wed Mar 05 2025 Andrey Cherepanov <cas@altlinux.org> 5.3.106-alt1
- New version.

* Wed Feb 12 2025 Andrey Cherepanov <cas@altlinux.org> 5.3.105-alt1
- New version.

* Wed Jan 29 2025 Andrey Cherepanov <cas@altlinux.org> 5.3.104-alt1
- New version.

* Thu Dec 19 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.100-alt1
- New version.

* Tue Dec 17 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.99-alt1
- New version.

* Sat Dec 07 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.97-alt1
- New version.

* Sat Nov 30 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.96-alt1
- New version.

* Fri Nov 08 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.95-alt1
- New version.

* Tue Oct 29 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.94-alt1
- New version.

* Sat Oct 26 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.93-alt1
- New version.

* Wed Oct 23 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.92-alt1
- New version.

* Wed Oct 16 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.90-alt1
- New version.

* Thu Oct 10 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.89-alt1
- New version.

* Fri Oct 04 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.88-alt1
- New version.

* Thu Oct 03 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.87-alt1
- New version.

* Fri Sep 27 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.86-alt1
- New version.

* Fri Sep 20 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.85-alt1
- New version.

* Wed Sep 18 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.84-alt1
- New version.

* Fri Sep 13 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.83-alt1
- New version.

* Sat Sep 07 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.81-alt1
- New version.

* Tue Sep 03 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.79-alt1
- New version.

* Thu Aug 22 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.77-alt1
- New version.

* Mon Aug 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.74-alt2
- Fixed cmake config location.
- Fixed pkgconfig.

* Fri Aug 02 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.74-alt1
- Initial build for Sisyphus.
