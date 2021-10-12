Name: libxprintutil
Summary: The XprintUtil Library
Version: 1.0.1
Release: alt6
Group: System/X11
License: MIT
Url: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/lib/libXprintUtil-%version.tar.bz2

# Automatically added by buildreq on Thu Mar 07 2013
# optimized out: gnu-config libX11-devel libXau-devel libstdc++-devel pkg-config xorg-printproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ libXp-devel libXt-devel

%description
The XprintUtil Library allows X11 application to print

%package devel
Summary: Development files for %name
Group: System/X11
Requires: libxprintutil = %version-%release

%description devel
Development files for %name

%files devel
%_libdir/libXprintUtil.so
%_pkgconfigdir/xprintutil.pc
%_includedir/X11/XprintUtil/xprintutil.h

%prep
%setup -q -n libXprintUtil-%version

%build
%configure
%make

%install
%make install DESTDIR=%buildroot

rm -fv %buildroot%_libdir/*.a

%files -n libxprintutil
%_libdir/libXprintUtil.so.1
%_libdir/libXprintUtil.so.1.0.0

%changelog
* Tue Oct 12 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt6
- Remove devel-static subpackage.

* Mon Jul 29 2019 Fr. Br. George <george@altlinux.ru> 1.0.1-alt5
- Fix devel-tatic package name (Closes: #36964)

* Thu Mar 07 2013 Fr. Br. George <george@altlinux.ru> 1.0.1-alt4
- Remove xorg-x11-proto-devel from requirements

* Thu Mar 07 2013 Fr. Br. George <george@altlinux.ru> 1.0.1-alt3
- Rebuild with new buildreq

* Mon Apr 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2
- fix build

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libxprintutil
  * postun_ldconfig for libxprintutil
  * postclean-05-filetriggers for spec file

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

