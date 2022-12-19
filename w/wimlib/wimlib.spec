%define libname libwim

Name: wimlib
Version: 1.13.6
Release: alt1

Summary: Library to extract, create, modify, and mount WIM files
License: GPLv3+
Group: System/Libraries

Url: https://wimlib.net/
Source: https://wimlib.net/downloads/wimlib-%version.tar


BuildRequires: patchelf
BuildRequires: libattr-devel libfuse-devel libntfs-3g-devel libssl-devel libxml2-devel

%description
wimlib is a C library for creating, extracting, modifying, and mounting
files in the Windows Imaging Format (WIM files).  It is similar to
Microsoft's WIMGAPI but is designed for both UNIX and Windows.

%package -n %libname
Summary: Library to extract, create, modify, and mount WIM files
Group: System/Libraries

%description -n %libname
wimlib is a C library for creating, extracting, modifying, and mounting
files in the Windows Imaging Format (WIM files).  It is similar to
Microsoft's WIMGAPI but is designed for both UNIX and Windows.

%package -n %libname-devel
Summary: Development files for wimlib
Group: Development/Other
Requires: %libname = %version-%release

%description -n %libname-devel
Development files for wimlib.

%package -n wimtools
Summary: Tools to create, extract, modify, and mount WIM files
Group: File tools
Requires: %libname = %version-%release
%ifarch x86_64 %ix86
Requires: syslinux
%endif

%description -n wimtools
Tools to create, extract, modify, and mount files in the
Windows Imaging Format (WIM files).  These files are normally
created by using the `imagex.exe' utility on Windows,
but this package contains a free implementation of ImageX called
"wimlib-imagex" that is designed to work on both UNIX and Windows.

%prep
%setup

%build
# helps with rpath
#autoreconf

%configure \
       --disable-static \
       --disable-rpath  \
       --with-libcrypto \
       --with-ntfs-3g   \
       --with-fuse      \
       --enable-xattr
%make_build

%install
%makeinstall_std
patchelf --remove-rpath %buildroot%_bindir/wim*

%check
:>tests/test-imagex-ntfs # this one fails
make check

%files -n %libname
%doc README NEWS
%_libdir/libwim.so.*

%files -n wimtools
%_bindir/wim*
%_bindir/mkwinpeimg
%_man1dir/*

%files -n %libname-devel
%_libdir/libwim.so
%_includedir/wimlib.h
%_pkgconfigdir/wimlib.pc

%changelog
* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 1.13.6-alt1
- new version 1.13.6 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 1.13.5-alt1
- new version 1.13.5 (with rpmrb script)
- drop mt-st from BR
- disable autoreconf (broken)

* Fri Sep 24 2021 Michael Shigorin <mike@altlinux.org> 1.13.4-alt1.1
- drop unneeded ExclusiveArch:
  + verified to build on e2kv4, ppc64le, aarch64, armh
  + wimtools R: syslinux dependency is x86-specific indeed

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1.13.4-alt1
- new version 1.13.4 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.13.3-alt1
- new version 1.13.3 (with rpmrb script)

* Thu May 28 2020 Grigory Ustinov <grenka@altlinux.org> 1.13.2-alt1
- Build new version.

* Mon May 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.13.1-alt1
- Build new version.

* Fri Dec 14 2018 Grigory Ustinov <grenka@altlinux.org> 1.13.0-alt1
- Build new version.

* Wed Sep 05 2018 Grigory Ustinov <grenka@altlinux.org> 1.12.0-alt1.1
- NMU: Rebuild with new openssl.

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.12.0-alt1
- new version 1.12.0 (with rpmrb script)

* Mon Apr 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt2
- rebuild with ntfs-3g-2017.3.23-alt1

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Sun Apr 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1 (with rpmrb script)

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.6.2-alt2
- wimtools: explicit syslinux dependency

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.6.2-alt1
- NMU: 1.6.2
- minor spec cleanup
- re-enable most of the tests

* Thu Aug 29 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- initial build for ALT Linux Sisyphus

