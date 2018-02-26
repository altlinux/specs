Name: sane-frontends
Version: 1.0.14
Release: alt4.1

Summary: Graphical frontend to SANE
Summary(ru_RU.UTF-8): Графическая оболочка для SANE
Url: http://www.sane-project.org/

Source: ftp://ftp.sane-project.org/pub/sane/%name-%version/%name-%version.tar
License: GPL
Group: Graphics

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildPreReq: libusb-devel

# Automatically added by buildreq on Sat Feb 24 2007
BuildRequires: libgimp2-devel libgphoto2-devel libieee1284-devel libjpeg-devel libsane-devel libtiff-devel

Provides: xscanimage
Patch0: sane-frontends-1.0.14-badcode.patch
Patch1: sane-frontends-1.0.14-newsane.patch

%description
This is the xscanimage program, used to scan images using SANE, either
standalone or as a gimp plugin. Also includes xcam.

Note: Use xsane program instead.

%description -l ru_RU.UTF-8
Пакет содержит программу xscanimage, используемую для сканирования
изображений через SANE, либо самостоятельно, либо как модуль для
GIMP. Также в пакете присутствует программа xcam.

Рекомендуется использовать программу xsane вместо данного пакета

%prep
%setup -q
%patch0 -p1 -b .badcode
%patch1

%build
%configure

%make_build

%install
%makeinstall
%define gimpplugdir %buildroot%_libdir/gimp/2.0/plug-ins
mkdir -p %gimpplugdir
ln -s -f %_bindir/xscanimage %gimpplugdir/xscanimage

%files
%doc NEWS README AUTHORS
%_bindir/*
%_libdir/gimp/2.0/plug-ins/xscanimage
%config(noreplace) %_datadir/sane/sane-style.rc
%_man1dir/*

%changelog
* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.14-alt4.1
- Fixed build

* Tue Dec 20 2011 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt4
- cleanup spec
- rebuild with RPATH free sane

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt3
- fix build with new sane 1.0.20 (which introduced incompat. with SANE 1.0)
- add fix patch from Fedora

* Sat Feb 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt2
- update buildreq, small cleanup spec

* Mon Sep 19 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt1
- new version

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.13-alt1
- new version

* Fri Jun 11 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.12-alt2
- change URL

* Mon May 17 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.12-alt1
- new version
- build with gimp2

* Mon Jan 12 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt2
- make link for gimp plig-in directly in package
- rebuild with gcc3.3
- remove COPYING from doc

* Mon Oct 06 2003 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt1
- new version

* Mon Mar 24 2003 Vitaly Lipatov <lav@altlinux.ru> 1.0.10-alt1
- release of 1.0.10
- Caution: sane-style.rc moved from datadir to datadir/sane

* Mon Oct 28 2002 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- release of 1.0.9
- add russian translation in spec

* Thu Sep 19 2002 AEN <aen@altlinux.ru> 1.0.9-alt0.2
- buildreq fixed

* Mon Sep 09 2002 AEN <aen@altlinux.ru> 1.0.9-alt0.1
- built sources from cvs for J2.1/HomePC

* Mon Jun 03 2002 AEN <aen@logic.ru> 1.0.8-alt1
- new version

* Wed Feb 13 2002 AEN <aen@logic.ru> 1.0.7-alt1
- new version

* Fri Jan 18 2002 AEN <aen@logic.ru> 1.0.6-alt1
- new version

* Fri Aug 10 2001 AEN <aen@logic.ru> 1.0.5-alt1
- new version

* Thu Jan 09 2001 AEN <aen@logic.ru>
- adopted for RE

* Mon Jan 08 2001 Francis Galiegue <fg@mandrakesoft.com> 1.0.4-2mdk

- Summary now capitalised
- BuildRequires: sane (for sane-config)

