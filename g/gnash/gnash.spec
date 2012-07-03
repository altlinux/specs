Name: gnash
Version: 0.8.10
Release: alt2
Summary: GNU Flash player
License: GPLv3
Group: Video
Url: http://www.gnashdev.org/

Requires: libgnash = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): browser-plugins-npapi-devel
BuildRequires: boost-program_options-devel doxygen gcc-c++ kde4libs-devel libSDL-devel libXi-devel
BuildRequires: libXinerama-devel libXt-devel libXv-devel libcurl-devel libexpat-devel libgtk+2-devel libjpeg-devel
BuildRequires: libavformat-devel libavcodec-devel libswscale-devel
BuildRequires: libltdl-devel libspeex-devel libcairo-devel xulrunner-devel

%description
Standalone GNU Flash Player

%package klash
Group: Video
Summary: KDE Flash player
Requires: libgnash = %version-%release
Provides: %name-klash4 = %version-%release
Obsoletes: %name-klash4 < %version

%description klash
GNU Flash player for KDE

%package -n libgnash
Group: System/Libraries
Summary: Libraries for GNU Flash Player

%description -n libgnash
Libraries for GNU Flash Player

%package -n lib%name-devel
Group: Development/C++
Summary: Development files and libraries for %name
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files and library required to develop applications
that use gnash

%package -n mozilla-plugin-gnash
Group: Networking/WWW
Summary: GNU Flash Player plugin for Firefox and Mozilla
Requires: libgnash = %version-%release
Requires: gnash = %version-%release
Requires: browser-plugins-npapi

%description -n mozilla-plugin-gnash
GNU Flash Player plugin for Firefox and Mozilla

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--enable-hwaccel=none \
	--enable-renderer=cairo \
	--enable-media=ffmpeg \
	--with-npapi-plugindir=%browser_plugins_path \
	--enable-gui=gtk,kde4 \
	--with-kde4-lib=%_libdir/kde4/devel \
	--with-kde4-incl=%_includedir/kde4 \
	--without-gconf \
	--disable-testsuite \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install install-plugin

install -pD -m644 gui/%name.desktop %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_iconsdir
cp -r gui/icons/hicolor %buildroot%_iconsdir/

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/gtk-gnash
%dir %_datadir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/%name.1*
%_man1dir/gtk-gnash.1*

%files klash
%_bindir/qt4-gnash
%_libdir/kde4/libklashpart.so
%_datadir/kde4/apps/klash
%_datadir/kde4/services/klash_part.desktop
%_desktopdir/klash.desktop
%_iconsdir/hicolor/*/apps/klash.*
%_man1dir/qt4-gnash.1*

%files -n lib%name
%_sysconfdir/gnashrc
%_libdir/%name

%files -n lib%name-devel
%_includedir/%name
%_pkgconfigdir/*.pc

%files -n mozilla-plugin-%name
%_sysconfdir/gnashpluginrc
%browser_plugins_path/libgnashplugin.so

%changelog
* Wed Apr 18 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.10-alt2
- rebuilt with recent boost

* Sun Feb 05 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.10-alt1
- 0.8.10 released

* Thu Dec 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.9-alt3
- rebuilt with cairo as renderer

* Wed Dec 07 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.9-alt2
- rebuilt with libav

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.9-alt1.1
- Rebuilt with Boost 1.47.0

* Sun Mar 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.9-alt1
- 0.8.9

* Wed Mar 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.9-alt0.rc4
- 0.8.9 RC4

* Mon Mar 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.9-alt0.rc3
- 0.8.9 RC3

* Wed Dec 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt2
- rebuild with boost-1.45

* Mon Aug 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Tue Sep 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt2
- rebuild with browser-plugins-npapi-0.2

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Mon Sep 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5.11510-alt1
- bazaar revision 11510

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt7
- bazaar revision 11367

* Wed Jul 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt6
- bazaar revision 11259
- fixed build plugin for KDE3

* Tue Jul 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt5
- bazaar revision 11254

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt4
- rebuild with libpng12 1.2.37-alt2

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt3
- bazaar revision 10688

* Thu Mar 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt2
- 0.8.5 release

* Sun Mar 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt1.rc
- 0.8.5 RC

* Thu Feb 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt1.beta
- fixed plugin for KDE4

* Tue Feb 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt0.beta
- 0.8.5 beta

* Sun Nov 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt3
- klashpart: disabled debug messages

* Wed Nov 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- bazaar revision 10356

* Tue Oct 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Thu Jun 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Sun Apr 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Fri Oct 05 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.8.1-alt1
- New version.

* Wed Jun 13 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt1
- New version

* Sun Feb 25 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.7.2-alt2
- Added dependancy for gnash to mozilla plugin (thanks ab@ for notice)

* Wed Nov 29 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.7.2-alt1
- 0.7.2 release 

* Sat Jan 14 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.7-alt0.cvs.20051211
- Initial build for ALT Linux.
