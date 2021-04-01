Name: wine-grdwine
Version: 0.5.5.1
Release: alt1

Summary: Guardant usb dongle helper library for Wine
License: LGPLv2
Group: Emulators

Url: https://guardant.com
Packager: Konstantin Kondratyuk <kondratyuk@altlinux.org>

#Source-url: ftp://ftp.guardant.ru/support/linux/grdwine-%version.tar.gz
# Source-url: https://github.com/Etersoft/grdwine/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: libwine-devel

ExclusiveArch: %ix86 x86_64

%ifarch x86_64 aarch64
  %def_with build64
%else
  %def_without build64
%endif

%define winelibdir %_libdir/wine
%add_verify_elf_skiplist %winelibdir/grdwine.dll.so

%description
Guardant usb dongle helper library for Wine.
Implementation of the GrdWine is based on Linux USB Device
Filesystem and Linux USB HID Device Interface.

Supports Guardant Sign/Time and Guardant Code dongles.
Old keys Stealth II and Stealth III are not supported
(check WINE@Etersoft to get support).

%prep
%setup

%build
#autoreconf
./bootstrap.sh

%if_with build64
%configure \
	--enable-win64 \
%else
%configure \
%endif
	--with-wineincs=%_includedir \
	--with-winedlls=%buildroot/%winelibdir

%make_build

%install
mkdir -p %buildroot/%winelibdir/
%makeinstall_std

%files
%winelibdir/grdwine.dll.so

%changelog
* Thu Apr 01 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5.5.1-alt1
- new version 0.5.5.1 (with rpmrb script)
 + fix build with wine since 6.4
- change download URL

* Tue Jun 23 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5.5-alt2
- add AC_SYS_LARGEFILE to configure.ac

* Thu May 30 2019 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.5.5-alt1
- new version (0.5.5) with rpmgs script

