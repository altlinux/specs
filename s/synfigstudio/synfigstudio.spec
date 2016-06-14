Name:    synfigstudio
Version: 1.1.9
Release: alt1

Summary: Synfig studio - animation program
Group:   Office
License: GPL
Url:     http://www.synfig.org
# VCS:	 https://github.com/synfig/synfig

Packager: Andrey Cherepanov <cas@altlinux.org>

#Source: http://prdownloads.sf.net/synfig/%name-%version.tar.gz
Source:  %name-%version.tar

BuildPreReq: fonts-ttf-liberation
BuildRequires: gcc-c++ libgtkmm2-devel
BuildRequires: libsynfig-devel >= %version
BuildRequires: intltool
BuildRequires: ImageMagick-tools
BuildRequires: libgtkmm3-devel
BuildRequires: libsigc++2-devel
BuildRequires: /proc

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

%build
%autoreconf
%add_optflags -std=c++11 -I%_includedir/sigc++-2.0 -I%_libdir/sigc++-2.0/include
%configure
%make_build

%install
%makeinstall_std

# Remove generated mime database
find %buildroot%_xdgmimedir/ -maxdepth 1 -a -type f -delete

%find_lang %name

%files -f %name.lang
%doc INSTALL NEWS README TODO
%_bindir/*
%_pixmapsdir/*
%_iconsdir/*/*/*/*.png
%_iconsdir/*/*/*/*.svg
%_desktopdir/%name.desktop
%_datadir/synfig/
%_datadir/mime-info/*
%_datadir/appdata/%name.appdata.xml
%_xdgmimedir/application/x-sif.xml
%_xdgmimedir/packages/%name.xml

%files -n lib%name
%_libdir/libsynfigapp.*

%files -n lib%name-devel
%_includedir/synfigapp*/

%changelog
* Sun Jun 05 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- New version

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version

* Fri Jul 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 29 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version

* Thu Mar 19 2015 Andrey Cherepanov <cas@altlinux.org> 0.64.3-alt2
- Apply patches from Fedora
- Drop obsoleted patches

* Fri Dec 26 2014 Andrey Cherepanov <cas@altlinux.org> 0.64.3-alt1
- New version

* Mon Nov 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.64.2-alt1
- New version
- Fix project URL

* Fri Nov 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.64.1-alt1
- New version

* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 0.64.0-alt1
- New version

* Mon Feb 11 2013 Andrey Cherepanov <cas@altlinux.org> 0.63.05-alt1
- New version 0.63.05

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
