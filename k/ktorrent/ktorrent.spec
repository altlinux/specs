Name:      ktorrent
Version:   2.2.8
Release:   alt5.1
License:   GPL
Summary:   KDE client for BitTorrent network 
URL:       http://ktorrent.org
Group:     Networking/File transfer
Source:   http://ktorrent.org/downloads/%version/%name-%version.tar.gz
Source1:  ktorrent.po

Patch0: ktorrent-2.2.8-link-fix.patch
# ALT BUG #19144
Patch1: ktorrent-2.2.8-uk.patch
Patch2: ktorrent-2.2.8-alt-DSO.patch

Packager: Damir Shayhutdinov <damir@altlinux.ru> 

# Automatically added by buildreq on Sun Jun 04 2006
BuildRequires: fontconfig gcc-c++ kdelibs-devel libgmp-devel libjpeg-devel libpng-devel libXext-devel libXt-devel qt3-designer xml-utils xorg-cf-files
BuildRequires: desktop-file-utils

%description
ktorrent - KDE BitTorrent client. It comes with many useful plugins.

%package plugin-webinterface
Group: Networking/File transfer
Summary: Web interface plugin for ktorrent
Requires: %name = %version-%release
Requires: %_bindir/php

%description plugin-webinterface
Web interface plugin for ktorrent

%prep
%setup
%patch0 -p1
# ALT BUG #19144
%patch1 -p1
%patch2 -p2
install %SOURCE1 translations/ru/messages/

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure
%make_build

%install
%K3install

%K3find_lang --with-kde %name

%files -f %name.lang
%_K3bindir/*
%_K3datadir/applications/kde/*
%_K3datadir/apps/%name/*
%_K3datadir/config.kcfg/*
%_kde3_iconsdir/hicolor/*/*/*.png
%_kde3_iconsdir/hicolor/scalable/apps/ktorrent.svgz
%_K3libdir/libktorrent-*.so
%_K3libdir/kde3/kt*.so
%_K3datadir/services/*.desktop
%_K3datadir/servicetypes/ktorrentplugin.desktop
%exclude %_K3libdir/kde3/kt*.la
%exclude %_K3libdir/libktorrent.so
%exclude %_K3libdir/kde3/ktwebinterfaceplugin.so

%files plugin-webinterface
%_K3libdir/kde3/ktwebinterfaceplugin.so

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt5.1
- Fixed build

* Mon Mar 12 2012 Roman Savochenko <rom_as@altlinux.ru> 2.2.8-alt5
- Revert to original version 2.2.8 build for work fix

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 2.2.8-alt4
- Build for TDE 3.5.13 release

* Wed Mar 02 2011 Timur Aitov <timonbl4@altlinux.org> 2.2.8-alt3
- move to alternate place

* Sat Mar 21 2009 Damir Shayhutdinov <damir@altlinux.ru> 2.2.8-alt2
- Fixed Ukrainian translation (#19144)
- Removed obsolete pre/postun scripts
- Web interface plugin moved to separate subpackage, ktorrent-plugin-webinterface
- Web interface plugin requires php (#19146)

* Wed Nov 12 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.2.8-alt1
- Updated to 2.2.8 (last release in 2.x series)

* Tue Nov 04 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.2.7-alt2
- Added desktop-file-utils to BuildReq (fixes build)

* Sat May 31 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.2.7-alt1
- Updated to 2.2.7 (bugfix release)

* Sun Apr 27 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.2.6-alt1
- Updated to 2.2.6
- Added %%post/un_ldconfig

* Sat Mar 29 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.2.5-alt3
- Add some more fixes from svn
  + Fix ktshell when there are multiple dcop sessions (KT#158115)
  + Fix stop all and start all from system tray menu (KT#157991)
  + ETA algorithm -> Time left estimation algorithm (KT#158277)
  + Ported DHT ping storm fix from KDE4 version
  + Fix infinite loop in DHT code

* Sat Mar 29 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.2.5-alt2
- Fix incorrect path when creating torrent with '#' in path (#12613)

* Sat Feb 02 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.2.5-alt1
- Updated to 2.2.5 bugfix release
  + fixes in zeroconf, DHT and web interface plugins

* Wed Dec 12 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.2.4-alt2
- Fix Russian translation (#13636)

* Wed Nov 21 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.2.4-alt1
- 2.2.4 bugfix release

* Sun Nov 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.2.3-alt1
- 2.2.3 bugfix release

* Sat Sep 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.2.2-alt1
- 2.2.2 bugfix release

* Wed Jul 25 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.2.1-alt1
- 2.2.1 bugfix release

* Wed Jul 04 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.2-alt1
- 2.2 release

* Mon Jun 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.2-alt0.rc1
- 2.2rc1

* Sat Jun 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.2-alt0.beta1
- 2.2beta1

* Tue Apr 24 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.1.4-alt1
- 2.1.4 bugfix release - fixes DHT crash

* Thu Apr 05 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.1.3-alt1
- 2.1.3 bugfix release

* Mon Mar 12 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.1.2-alt1
- 2.1.2 - fixed 2 vulnerabilities.

* Thu Mar 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.1.1-alt1
- 2.1.1 bugfix release
- Fix icons ownage (#10859)

* Tue Feb 06 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.1-alt1
- 2.1 release 

* Mon Jan 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.1-alt0.rc1
- 2.1 rc1

* Sun Dec 03 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.1-alt0.beta1
- 2.1 beta1

* Tue Oct 10 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0.3-alt1
- 2.0.3 bugfix release

* Fri Sep 01 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0.2-alt1
- 2.0.2 bugfix release

* Sun Aug 27 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0.1-alt1
- 2.0.1 bugfix release

* Wed Aug 16 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0-alt1
- 2.0 release

* Sat Aug 05 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0-alt0.rc1
- new version (2.0rc1)
- Patch0 gone upstream

* Sun Jun 04 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0-alt0.beta1
- NMU
- new version (2.0beta1)

* Wed Sep 07 2005 Nick S. Grechukh <gns@altlinux.ru> 1.1rc1-alt0.1
- initial build for ALTLinux Sisyphus

