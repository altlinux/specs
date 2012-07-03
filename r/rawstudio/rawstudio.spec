Name: rawstudio
Version: 2.0
Release: alt4

Summary: Rawstudio is an open source raw-image converter written in GTK+
License: GPLv2+
Group: Graphics

URL: http://rawstudio.org/
Source: http://rawstudio.org/files/release/rawstudio-%version.tar.gz

Patch1: rawstudio-2.0-glibthreads.patch

BuildRequires: chrpath
# Automatically added by buildreq on Wed Apr 13 2011
BuildRequires: gcc-c++ libGConf libGConf-devel libdbus-devel libexiv2-devel libfftw3-devel libflickcurl-devel libgphoto2-devel libgtk+2-devel libjpeg-devel liblcms-devel liblensfun-devel libpng-devel libsqlite3-devel libssl-devel libtiff-devel

%description
Rawstudio can read and convert RAW-images from most digital cameras.

%prep
%setup
%patch1 -p1

# Relocates plugins directory:
subst 's@PACKAGE_DATA_DIR@"%_libdir"@' librawstudio/rs-plugin-manager.c

%build
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot icondir=%_liconsdir install

# This icon does not installed by Makefile but accessed by rawstudio.
# See also ALT bug #21439.
install -Dpm644 pixmaps/rawstudio.png %buildroot%_iconsdir/rawstudio.png

rm -f %buildroot%_datadir/rawstudio/plugins/*.{a,la}
mkdir -p %buildroot%_libdir/rawstudio/plugins
mv %buildroot%_datadir/rawstudio/plugins %buildroot%_libdir/rawstudio/

chrpath --delete %buildroot%_bindir/rawstudio

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/rawstudio
%_libdir/rawstudio
%_libdir/*.so.*
%_datadir/rawspeed
%_pixmapsdir/*
%_iconsdir/rawstudio.png
%_liconsdir/*
%_desktopdir/*
%exclude %_includedir
%exclude %_pkgconfigdir

%changelog
* Fri Apr 06 2012 Victor Forsiuk <force@altlinux.org> 2.0-alt4
- Fix g_thread_init() issue with glib 2.32+.

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 2.0-alt3
- Fix RPATH issue.

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt2
- rebuilt against libexiv2.so.11

* Fri Apr 08 2011 Victor Forsiuk <force@altlinux.org> 2.0-alt1
- 2.0

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 1.2-alt5
- Rebuild with libexiv2.so.9.

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 1.2-alt4
- Rebuild with libexiv2.so.6.

* Fri Nov 13 2009 Victor Forsyuk <force@altlinux.org> 1.2-alt3
- Package icon that accessed by rawstudio but does not installed by Makefile.

* Mon Jul 20 2009 Victor Forsyuk <force@altlinux.org> 1.2-alt2
- Rebuild with libexiv2.so.5.

* Tue Jun 09 2009 Victor Forsyuk <force@altlinux.org> 1.2-alt1
- 1.2

* Thu Oct 23 2008 Victor Forsyuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Sep 16 2008 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- 1.1

* Wed Apr 30 2008 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- 1.0

* Mon Apr 14 2008 Victor Forsyuk <force@altlinux.org> 0.7-alt2
- Desktop file mime entry fix.

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.7-alt1
- 0.7

* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 0.6-alt1
- 0.6

* Wed Mar 21 2007 Victor Forsyuk <force@altlinux.org> 0.5.1-alt1
- 0.5.1

* Thu Feb 08 2007 Victor Forsyuk <force@altlinux.org> 0.5-alt1
- 0.5

* Fri Sep 29 2006 Victor Forsyuk <force@altlinux.ru> 0.4.1-alt1
- Initial build.
