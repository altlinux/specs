BuildRequires: desktop-file-utils
Name: hugin
Version: 2011.4.0
Release: alt1.1

Group: Graphics
Summary: hugin - Goal: an easy to use cross-platform GUI for Panorama Tools.
License: GPL
Url: http://hugin.sourceforge.net/
Source0: %name-%version.tar
Source1: %name.desktop

BuildPreReq: libpano13-devel boost-devel >= 1.34 wxGTK-devel >= 2.8.0
BuildPreReq: libgtk+2-devel >= 2.0.3 boost-thread-devel >= 1.34 gcc-c++ gcc-fortran
BuildRequires: boost-devel boost-thread-devel boost-datetime-devel boost-regex-devel
BuildRequires: boost-filesystem-devel boost-iostreams-devel boost-system-devel
BuildRequires: boost-signals-devel libglew-devel libGLUT-devel libXi-devel libXmu-devel
BuildRequires: glib-devel libgtk+2-devel libjpeg-devel libpano13-devel perl-podlators
BuildRequires: libpng-devel libstdc++-devel libtiff-devel wxGTK-devel xorg-locales
BuildRequires: zlib-devel libpango-devel zip cmake openexr-devel libexiv2-devel libtclap-devel
Requires: enblend >= 3.2 libpano13 wxGTK >= 2.6.0  autopano-sift-C perl-Image-ExifTool make

%description
With hugin you can assemble a mosaic of photographs into a complete immersive
panorama, stitch any series of overlapping pictures and much more.

%prep
%setup -q

%build
###From CVS only
suffix=`echo %_libdir | sed s/[^0-9]*//`
cmake   -DCMAKE_INSTALL_PREFIX=%buildroot/usr/ -DINSTALL_XRC_DIR="/usr/share/hugin/xrc" -DLIB_SUFFIX="$suffix" .
make

%install
###Check line below
#/bin/ln -s %%_datadir/automake/mkinstalldirs config/mkinstalldirs

%makeinstall
###Check line below
%find_lang %name
###Check line below ???
%find_lang nona_gui
/bin/cat nona_gui.lang >>%name.lang

/bin/install -p -m644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
/bin/install -p -m644 -D src/hugin1/hugin/xrc/data/hugin.png %buildroot%_datadir/pixmaps/%name.png
/bin/install -p -m644 -D src/hugin1/hugin/xrc/data/hugin.png %buildroot%_niconsdir/%name.png
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Photography \
	%buildroot%_desktopdir/hugin.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Photography \
	%buildroot%_desktopdir/PTBatcherGUI.desktop


%files -f %name.lang
%doc AUTHORS COPYING LICENCE_VIGRA README
%_bindir/*
%dir %_datadir/hugin
%dir %_datadir/hugin/xrc
%_datadir/applications/*
%_datadir/hugin/
%_datadir/pixmaps/*
%_datadir/mime/packages/hugin.xml
%_libdir/*
%exclude /usr/lib/debug
%_niconsdir/*
%_desktopdir/*
%_man1dir/*
%_iconsdir/gnome/48x48/mimetypes/gnome-mime-application-x-ptoptimizer-script.png
/usr/share/icons/hicolor/32x32/apps/hugin.png

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.4.0-alt1.1
- Rebuilt with Boost 1.49.0

* Wed Dec 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.4.0-alt1
- 2011.4.0

* Tue Dec 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.2.0-alt1.1
- rebuild with boost 1.48

* Wed Nov 02 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.2.0-alt1
- 2011.2.0

* Fri Sep 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.0.0-alt2
- requires: make added

* Wed Jun 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2011.0.0-alt1
- 2011.0.0

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2010.4.0-alt1.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for hugin

* Sat Mar 26 2011 Ivan A. Melnikov <iv@altlinux.org> 2010.4.0-alt1.2
- rebuild with boost 1.46.1
- updated boost and xorg build-requires

* Wed Feb 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.4.0-alt1.1
- build fixed

* Thu Jan 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.4.0-alt1
- 2010.4.0

* Wed Dec 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.2.0-alt1.1
- rebuild with boost 1.45
- icon in desktop file fixed

* Tue Oct 12 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.2.0-alt1
- new upstream version
- (closes: #23822)

* Tue Jun 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.0.0-alt1.1
- Rebult with 0.20-alt1

* Wed Jun 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2010.0.0-alt1
- new upstream version

* Mon Jan 11 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2009.4.0-alt2
- Rebuit with exiv2-0.19

* Fri Dec 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2009.4.0-alt1
- new upstream version

* Mon Nov 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2009.2.0-alt1.1
- rebuild with libpano13

* Thu Oct 15 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2009.2.0-alt1
- new upstream version

* Tue Aug 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt2.2
- rebuild with wxGTK-2:2.8.10-alt2 (see 20451)

* Thu Jul 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt2.1
- rebuild with exiv2-0.18.2 

* Wed Jul 22 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt2
- 0.8.0 release (identical with rc5)
- requirement to exiftool added ( closes: #20843 )

* Fri Jul 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt1.rc5
- rc5
- some unpackaged files added

* Tue Jun 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0-alt1.rc3
- new version 
- wxGTK instead wxGTK2u

* Wed Jun 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt7
- build fixed 

* Thu Feb 26 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt6
- translated desktop file of batch stitcher 

* Fri Oct 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt5
- new version 

* Tue May 20 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt4.beta4
- added %_datadir/hugin/xrc to package

* Thu Apr 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt3.beta4
- fixed build 

* Tue Apr 08 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt2.1.beta4
- no real changes, fix conflict with tvb@ package 

* Tue Apr 08 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt2.beta4
- fixed build with new gettext-tools 

* Thu Jun 28 2007 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.0-alt1.beta4
- Fix build with new version of boost
- Add desktop file

* Wed Feb 14 2007 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.0-alt0.beta4
- New version

* Mon Sep 25 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.6.1-alt1
- New version
- Cleanup patches

* Fri May 19 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.6-alt0.0.cvs20060517
- Updating to CVS version
- Checking patches
- Checking dependencies

* Wed May 17 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt11
- Fixing code for gcc4.1
- Adding unpackaged files

* Tue Mar 07 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt10
- Cleanup spec

* Sat Feb 11 2006 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt9
- Removing stale require panorama-tools

* Wed Dec 28 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt8
- Correction of default settings for Linux

* Fri Dec 16 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt7
- First stable release of hugin at 11-12-2005

* Sat Dec 03 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt6.cvs20051203
- Updated to CVS version
- Compiled with wxGTK2u
- Added missed requires.

* Fri Sep 23 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt5.rc2
- Fixing build errors

* Fri Sep 23 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt4.rc2
- New RC.
- Some spec corrections.

* Fri Sep 09 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt3.rc1
- Adding menu entry for program

* Mon Sep 05 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.5-alt2.rc1
- Fixing for ALT Linux

* Tue Jul 26 2005 Sergei Epiphanov <serpiph@nikiet.ru> 0.5_rc1-alt1
-initial build
