Name: synfigstudio
Version: 0.63.03
Release: alt1

Summary: Synfig studio - animation program
Group: Office
License: GPL
Url: http://synfig.com

Packager: Yuriy Shirokov <yushi@altlinux.org>

#Source: http://prdownloads.sf.net/synfig/%name-%version.tar.gz
Source: %name-%version.tar
#Patch0: synfigstudio-0.62.02-alt-gcc4.5.patch

# needed some font for synfig
BuildPreReq: fonts-ttf-liberation
# manually replaced: fonts-ttf-ms
# Automatically added by buildreq on Mon Jul 30 2007
BuildRequires: gcc-c++ libgtkmm2-devel libsynfig-devel

BuildPreReq: libsynfig-devel = %version
Requires: lib%name = %version-%release

%description
Synfig studio is a animation program.

%package -n lib%name
Summary: Library for Synfig studio
Group: Development/C++
Requires: libsynfig = %version

%description -n lib%name
Library for Synfig studio.

%package -n lib%name-devel
Summary: Header files for Synfig studio
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files for Synfig studio.

%prep
%setup -q
#%patch0 -p0

%build
%autoreconf
#export CPPFLAGS="-fno-inline"
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc INSTALL NEWS README TODO
%_bindir/*
%_pixmapsdir/*
%_iconsdir/*/*/*/*.png
%_iconsdir/*/*/*/*.svg
%_desktopdir/synfigstudio.desktop
%_datadir/mime-info/*

%files -n lib%name
%_libdir/libsynfigapp.*

%files -n lib%name-devel
%_includedir/synfigapp*/

%changelog
* Thu Jan 12 2012 Yuriy Shirokov <yushi@altlinux.org> 0.63.03-alt1
- new version 0.63.03

* Mon Oct 10 2011 Yuriy Shirokov <yushi@altlinux.org> 0.63.02-alt1
- new version 0.63.02

* Mon Jun 20 2011 Yuriy Shirokov <yushi@altlinux.org> 0.63.00-alt1
- new version 0.63.00

* Sat Dec 18 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.02-alt1
- new version 0.62.02

* Sun Nov 07 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.01-alt2
- patch for gcc-4.5

* Sun Jun 6 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.01-alt1
- new version 0.62.01

* Wed Apr 07 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.00-alt2
- spec cleanup

* Tue Mar 23 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.00-alt1
- new version 0.62.00

* Wed Oct 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.09-alt1
- new version 0.61.09 (with rpmrb script)

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.08-alt1
- new version 0.61.08 (with rpmrb script)

* Fri Oct 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.07-alt1
- new version 0.61.07 (with rpmrb script)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.06-alt2
- enable update/clean menus

* Sun Jul 01 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.06-alt1
- new version 0.61.06 (with rpmrb script)
- add dejavu font as needed during build

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.05-alt0.1
- initial build for ALT Linux Sisyphus

* Sun Dec 24 2006 - Manfred.Tremmel@iiv.de
- update to svn (Revision 229), seems, a lot of bugs where fixed inbetween
* Thu Dec 21 2006 - Manfred.Tremmel@iiv.de
- added --enable-optimization=1 to make it compile on SUSE 10.2
* Sat May 06 2006 - Manfred.Tremmel@iiv.de
- use -fno-inline with SUSE 10.1, because of a compiler bug in gcc 4.1
* Wed Mar 01 2006 - Manfred.Tremmel@iiv.de
- update to 0.61.05
* Mon Jan 23 2006 - Manfred.Tremmel@iiv.de
- recompile with new libffmpeg version
* Sun Jan 15 2006 - Manfred.Tremmel@iiv.de
- update to 0.61.04
* Thu Dec 15 2005 - Manfred.Tremmel@iiv.de
- first packman build, based on the spec-file
  from Robert B. Quattlebaum Jr. <darco@bigfoot.com>
