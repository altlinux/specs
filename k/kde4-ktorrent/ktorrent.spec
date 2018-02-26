
%define rname ktorrent
%define libktorrent libktorrent1

%add_findreq_skiplist %_K4apps/%rname/scripts/*.py

Name: kde4-%rname
Version: 4.2.1
Release: alt1

Group:     Networking/File transfer
Summary:   KDE client for BitTorrent network 
License:   GPL
URL:       http://ktorrent.org

Conflicts: ktorrent <= 2.2.8-alt2
Requires: kde4-kross-python

Source:   http://ktorrent.org/downloads/%version/%rname-%version.tar.gz
Patch1: ktorrent-3.2beta1-alt-find-plasma.patch

# Automatically added by buildreq on Tue Jun 01 2010 (-bi)
#BuildRequires: gcc-c++ glib2-devel glibc-devel-static kde4base-workspace-devel kde4pimlibs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libktorrent-devel libqt3-devel libtag-devel libxkbfile-devel qt4-assistant qt4-designer rpm-build-ruby
BuildRequires(pre): libktorrent-devel kde4base-runtime-devel kde4base-workspace-devel kde4pimlibs-devel
BuildRequires: gcc-c++ glib2-devel glibc-devel libtag-devel

%description
ktorrent - KDE BitTorrent client. It comes with many useful plugins.


%prep
%setup -q -n %rname-%version
#%patch1 -p1


%build
%K4build
#    -DENABLE_DHT_SUPPORT=false


%install
%K4install
%K4find_lang --with-kde %rname


%files -f %rname.lang
%_K4bindir/*
%_K4iconsdir/hicolor/*/*/kt*.*
%_K4xdg_apps/%rname.desktop
%_K4apps/%rname/
%_K4libdir/libktcore.so.*
#%_K4libdir/libktupnp.so.*
%_K4lib/*kt*.so
#%_K4lib/kio_magnet.so
%_K4srv/*.desktop
%_K4srv/magnet.protocol
%_K4srvtyp/ktorrentplugin.desktop
#%_K4cfg/magnetsettings.kcfg


%changelog
* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.2.0-alt0.M60P.1
- built for M60P

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.2.0-alt1
- release 4.2.0

* Thu Feb 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.2.0-alt0.1
- 4.2rc1

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.1.3-alt0.M60P.1
- built for M60P

* Mon Dec 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.1.3-alt1
- new version

* Thu Nov 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.1.2-alt2
- fix requires

* Thu Sep 22 2011 Sergey V Turchin <zerg@altlinux.org> 4.1.2-alt0.M60P.1
- built for M60P

* Thu Sep 22 2011 Sergey V Turchin <zerg@altlinux.org> 4.1.2-alt1
- new version

* Mon May 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.1.1-alt1
- new version

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 4.1.0-alt2
- fix build requires

* Wed Mar 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.1.0-alt1
- new version
- move to standart place

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.0.5-alt2
- rebuilt with kde-4.6

* Fri Jan 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.0.5-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.4-alt0.M51.1
- built for M51

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.4-alt1
- new version

* Fri Sep 17 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.3-alt0.M51.1
- built for M51

* Fri Sep 17 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.3-alt1
- new version

* Mon Jul 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.2-alt0.M51.1
- built for M51

* Mon Jul 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.2-alt1
- new version

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt1
- new version

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 3.3.4-alt0.M51.1
- built for M51

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 3.3.4-alt1
- new version

* Fri Jan 22 2010 Sergey V Turchin <zerg@altlinux.org> 3.3.3-alt0.M51.1
- built for M51

* Fri Jan 22 2010 Sergey V Turchin <zerg@altlinux.org> 3.3.3-alt1
- new version

* Fri Dec 25 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.2-alt0.M51.1
- built for M51

* Fri Dec 25 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.2-alt1
- new version

* Wed Dec 16 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.1-alt2
- fix to build really 3.3.1 instead of old release

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.1-alt0.M51.1
- built for M51

* Mon Dec 07 2009 Sergey V Turchin <zerg@altlinux.org> 3.3.1-alt1
- new version

* Wed Nov 11 2009 Sergey V Turchin <zerg@altlinux.org> 3.3-alt1
- new version

* Wed Nov 11 2009 Sergey V Turchin <zerg@altlinux.org> 3.2.5-alt1
- new version

* Fri Oct 02 2009 Sergey V Turchin <zerg@altlinux.org> 3.2.4-alt1
- new version

* Tue Aug 11 2009 Sergey V Turchin <zerg@altlinux.org> 3.2.3-alt0.M50.1
- built for M50

* Tue Aug 11 2009 Sergey V Turchin <zerg@altlinux.org> 3.2.3-alt1
- new version

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 3.2.2-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 3.2.2-alt1
- new version

* Mon Apr 13 2009 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt0.M50.1
- built for M50

* Mon Apr 13 2009 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt1
- new release

* Thu Feb 19 2009 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt1
- 3.2 release

* Thu Feb 05 2009 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt0.5.rc1
- 3.2-RC1

* Mon Jan 26 2009 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt0.4.beta1
- fix compile with new KDE

* Thu Dec 25 2008 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt0.3.beta1
- built for Sisyphus

* Thu Dec 11 2008 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt0.2.beta1
- built for M41

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

