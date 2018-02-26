Name: libxprintutil
Summary: The XprintUtil Library
Version: 1.0.1
Release: alt2
Group: System/X11
License: MIT
Url: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/lib/libXprintUtil-%version.tar.bz2
Packager: Fr. Br. George <george@altlinux.ru>

BuildRequires: libX11-devel libXau-devel libXp-devel libXt-devel xorg-proto-devel xorg-util-macros gcc-c++
%description
The XprintUtil Library allows X11 application to print

%package -n libxprintutil-devel
Summary: Development files for %name
Group: System/X11

Requires: libxprintutil = %version-%release
Requires: libX11-devel
Requires: libXt-devel
Requires: xorg-x11-proto-devel
Provides: libxprintutil-devel = version-%release

%description -n libxprintutil-devel
Development files for %name

%files -n libxprintutil-devel
%_libdir/libXprintUtil.so
#%_libdir/libXprintUtil.la
%_pkgconfigdir/xprintutil.pc
%_includedir/X11/XprintUtil/xprintutil.h

#-----------------------------------------------------------

%package -n libxprintutil-static-devel
Summary: Static development files for %name
Group: System/X11
Requires: libxprintutil-devel = %version-%release
Provides: libxprintutil-static-devel = %version-%release

%description -n libxprintutil-static-devel
Static development files for %name

%files -n libxprintutil-static-devel
%_libdir/libXprintUtil.a

#-----------------------------------------------------------

%prep
%setup -q -n libXprintUtil-%version

%build
%configure
%make

%install
%make install DESTDIR=%buildroot

%files -n libxprintutil
%_libdir/libXprintUtil.so.1
%_libdir/libXprintUtil.so.1.0.0

%changelog
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
