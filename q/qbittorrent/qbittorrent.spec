Name: qbittorrent
Version: 2.9.3
Epoch: 1
Release: alt1.1

Summary: qBittorrent is a bittorrent client written in C++ / Qt4 using the good libtorrent library.
Summary(ru_RU.UTF-8): qBittorrent - bittorrent клиент написаный на C++ / Qt4, использующий библиотеку libtorrent.
License: GPL
Group: Networking/File transfer
Url: http://qbittorrent.org

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar
Source2: %{name}_ru.ts
Source3: %{name}_ru.qm

%define libtorrent_version 2:0.15.9-alt0.1.svn6292

BuildPreReq: desktop-file-utils

BuildRequires: boost-devel boost-filesystem boost-filesystem-devel boost-datetime boost-program-options-devel boost-asio-devel
BuildRequires: gcc-c++ libqt4-devel >= 4.4
BuildRequires: libtorrent-rasterbar-devel >= %libtorrent_version 
BuildRequires: GeoIP-Lite-Country
BuildRequires: libnotify-devel

Requires: libtorrent-rasterbar0.15 >= %libtorrent_version 
Requires: python-modules-ctypes
Requires: GeoIP-Lite-Country
Requires(post,postun): desktop-file-utils

%description
qBittorrent is a bittorrent client written in C++ / Qt4 using the good 
libtorrent-rasterbar library (By Arvid Nordberg). qBittorrent is 
free / open-source software released under the GNU GPL license. 
qBittorrent aims to be a good alternative to all other bittorrent 
clients. The Author is Christophe Dumez, French Student in 
computer science (IT).

%description -l ru_RU.UTF8
qBittorrent - клиент bittorrent написаный на C++ / Qt4, использующий 
библиотеку libtorrent-rasterbar (Arvid Nordberg). qBittorrent свободное 
ПО с открытм исходным кодом, распространяющийся под лицензией GNU GPL. 
qBittorrent стремиться быть хорошей альтернативой всем другим bittorrent 
клиентам. Автор Christophe Dumez, французский студент в области IT.
   
%prep
%setup -q
#cp -f %SOURCE2 %SOURCE3 src/lang/

%build
%_configure_script --prefix=%buildroot%_usr --qtdir=%_qt4dir
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING INSTALL NEWS README TODO Changelog
%_bindir/*
%_datadir/applications/*
%_man1dir/*
%_datadir/icons/hicolor/*/*/*

%changelog
* Sat Jun 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.9.3-alt1.1
- Rebuilt with Boost 1.49.0

* Wed Dec 21 2011 Alexey Morsov <swi@altlinux.ru> 1:2.9.3-alt1
- new version

* Tue Oct 18 2011 Alexey Morsov <swi@altlinux.ru> 1:2.9.0-alt1.git20111016
- new git version (commit 33325cdfee2289f87c573d7ae8cb455fb324f202)
- 2.9.0 release

* Thu Sep 01 2011 Alexey Morsov <swi@altlinux.ru> 1:2.9.0-alt0.1.svn5623
- new svn trunk version

* Mon Apr 18 2011 Alexey Morsov <swi@altlinux.ru> 1:2.8.0-alt0.1.svn5489
- new svn trunk version

* Fri Mar 25 2011 Alexey Morsov <swi@altlinux.ru> 1:2.7.0-alt1
- release 2.7.0

* Sun Mar 13 2011 Alexey Morsov <swi@altlinux.ru> 1:2.7.0-alt0.1.svn5307
- new svn update

* Tue Jan 25 2011 Alexey Morsov <swi@altlinux.ru> 1:2.7.0-alt0.1.svn5159
- 2.7 alpha

* Fri Jan 07 2011 Alexey Morsov <swi@altlinux.ru> 1:2.6.0-alt0.1.svn5001
- rc2

* Tue Dec 28 2010 Alexey Morsov <swi@altlinux.ru> 1:2.6.0-alt0.1.svn4929
- new svn trunk version

* Fri Dec 17 2010 Alexey Morsov <swi@altlinux.ru> 1:2.6.0-alt0.1.svn4870
- new svn trunk version

* Tue Dec 07 2010 Alexey Morsov <swi@altlinux.ru> 1:2.6.0-alt0.1.svn4841
- new svn trunk version (2.6.0)

* Thu Nov 04 2010 Alexey Morsov <swi@altlinux.ru> 1:2.5.0-alt0.1.svn4657
- new svn trunk version (2.5.0)

* Sun Oct 17 2010 Alexey Morsov <swi@altlinux.ru> 1:2.5.0-alt0.1.svn4531
- new svn trunk version (2.5.0 alpha)

* Mon Aug 23 2010 Alexey Morsov <swi@altlinux.ru> 1:2.4.0-alt0.1.svn4402
- new svn trunk version (commit b2d556a1f287d9d7aafc3f5e3f22218953e2f660)

* Tue May 25 2010 Alexey Morsov <swi@altlinux.ru> 1:2.3.0-alt0.1.svn3936
- new svn trunk version (commit 4f4f6f857c65a3c37e7b1073ff0c6cdd8330d025)

* Tue May 25 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.8-alt1.svn3934
- new 2.2 svn branch version

* Mon Mar 15 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt1
- new release

* Sat Mar 13 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt0.1.svn3673
- new svn trunk version (now preferences columns resizable)

* Sat Mar 13 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt0.1.svn3672
- new svn trunk version

* Wed Feb 10 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt0.1.svn3565
- new svn trunk version

* Thu Feb 04 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt0.1.svn3534
- new svn trunk version
- add libnotify dependency

* Fri Jan 22 2010 Alexey Morsov <swi@altlinux.ru> 1:2.1.1-alt0.1.svn3460
- new version

* Thu Jan 14 2010 Alexey Morsov <swi@altlinux.ru> 1:2.1.1-alt0.1.svn3439
- new svn version (commit 9bb0e5ef935ddb9f60d88cecf9bcd95fc36324d1)
- clean requires
- update russian translation

* Wed Jan 06 2010 Alexey Morsov <swi@altlinux.ru> 1:2.0.6-alt1
- new release

* Thu Dec 31 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.5-alt1
- new release (critical bug fix)

* Wed Dec 30 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.4-alt1
- new release

* Wed Dec 23 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.3-alt1
- new release
- fix qt4 requires (qt >= 4.4)

* Sun Dec 20 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.2-alt0.2.svn3163
- add GeoIP-Lite-Country to BuildRequires

* Sat Dec 19 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.2-alt0.1.svn3163
- new svn branch version (commit 3f3aaf2b00cc819f7cbb84d3694972aa19501d20)

* Fri Nov 20 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.0-alt0.1.svn2870
- new svn version (commit 2055f3b6893f95721650acc322330b8c3aeb354c)

* Fri Oct 30 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2658
- new svn version (commit fd3f3b6b308173f538dca55c4fb685b988425891)

* Mon Oct 19 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2636
- new svn version (commit d15344bd5e02271f236354af353508c994dfd34e)

* Wed Oct 14 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2631
- new svn version (commit e00352dd5ea6226fe0e22dc3fbc2e9be26f51e1a)

* Tue Sep 22 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2616
- new svn version (commit ef193f0758af91058926b149742d6417e7319bd6)

* Mon Sep 07 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2608
- build svn r2608

* Fri Aug 28 2009 Alexey Morsov <swi@altlinux.ru> 1:1.5.0-alt0.2.svn2566
- build svn r2566
  + (fixed import 1.4 active torrens)
  + (desktop file fixed in upstream now)

* Wed Aug 26 2009 Alexey Morsov <swi@altlinux.ru> 1:1.5.0-alt0.2.beta4
- new version

* Tue Jun 09 2009 Alexey Morsov <swi@altlinux.ru> 1:1.4.0-alt0.3.beta2
- rebuild with new libtorrent-rasterbar

* Thu Apr 30 2009 Alexey Morsov <swi@altlinux.ru> 1:1.4.0-alt0.2.beta2
- add python-modules-ctypes to requires (for search engines)

* Wed Apr 22 2009 Alexey Morsov <swi@altlinux.ru> 1:1.4.0-alt0.1.beta2
- new beat version

* Wed Apr 22 2009 Alexey Morsov <swi@altlinux.ru> 1:1.3.3-alt1
- new version

* Sat Mar 21 2009 Alexey Morsov <swi@altlinux.ru> 1:1.3.2-alt1
- new version

* Wed Feb 25 2009 Alexey Morsov <swi@altlinux.ru> 1:1.3.1-alt2
- fix name for libtorrent-rasterbar-devel

* Sat Feb 07 2009 Alexey Morsov <swi@altlinux.ru> 1:1.3.1-alt1
- new version

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.1-alt1
- new version
- fix spec
  + remove deprecated call from post/postun

* Wed Oct 29 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.rc4.1
- fix build with boost1.36

* Mon Oct  6 2008 Alexey Morsov <swi@altlinux.org> 1:1.2.0-alt0.rc4
- new devel version

* Sun Aug 31 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.beta5
- new devel version

* Tue Aug 19 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.beta4
- new devel version 
- update russian translation

* Sat Aug 09 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.beta2
- new devel version

* Sat Aug 02 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.beta1
- new devel version

* Sat Aug 02 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.1-alt1
- new release
  + updated russian translation now in upstream

* Tue Jul 29 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.rc1.1
- update russian translation

* Thu Jul 24 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.rc1
- new version
- change requires
  + libtorrent changed to libtorrent-rasterbar (upstream renaming)

* Wed Jun 25 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.beta2
- 1.1.0 beta2

* Mon Jun 16 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.beta1.1
- svn r1793 (pre beta2)

* Sat Jun 07 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.beta1.0
- new beta version

* Sat May 17 2008 Alexey Morsov <swi@altlinux.ru> 1:1.0.0-alt3
- fix menus to correspond with policy
- patch desktop file to correspond standard

* Thu Apr 24 2008 Alexey Morsov <swi@altlinux.ru> 1:1.0.0-alt2
- put 1.0.0 tar to package (not 1.0.0rc11)

* Wed Apr 23 2008 Alexey Morsov <swi@altlinux.ru> 1:1.0.0-alt1
- 1.0.0 release
- Improved a lot the torrent creation module
- Bittorrent FAST extension support
- Added UPnP / NAT-PMP port forwarding support
- Brand new search engine plugins system
- IPv6 is now fully supported
- many other (see ChangeLog file)

* Tue Mar 25 2008 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt2.rc11
- rebuild with new libtorrent and boost-1.34.1

* Wed Jan 02 2008 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc11
- Bypass exit confirmation on system shutdown
- Download from urls are now able to follow redirections
- Fixed torrent creation from a directory
- Fixed save path when seeding automatically after torrent creation

* Mon Dec 10 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc10
- Filtered files don't appear on hard disk anymore
- Real torrent share ratio is now displayed in transfer list

* Sat Nov 24 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc9
- fix crash on add partial torrent

* Sat Nov 17 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc8
- 1.0.0rc8

* Sat Nov 03 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc7
- Filtered files are not allocated on the hard-drive anymore
- Torrent content is now displayed as a tree

* Thu Oct 25 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc6
- Bittorrent FAST extension support
- Allow to use  a proxy for trackers / web seeds / peers / DHT connections
- Allow to set upload/download limit per torrent (right click)
- Search engine is now using one thread per website for faster results
- Improved a lot the torrent creation module
- Improved unicode support

* Sat Oct 13 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc5
- version 1.0.0.rc5

* Sat Oct 06 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc3
- Added UPnP / NAT-PMP port forwarding support
- Added encryption support (compatible with Azureus)
- Added RSS support
- Brand new search engine plugins system
- Supports SOCKS5 proxies as well as HTTP ones
- ..and many more anchanced and some bug fixes

* Wed Aug 15 2007 Alexey Morsov <swi@altlinux.ru> 0.9.3-alt2
- rebuild with libtorrent-0.12-alt1

* Tue May 08 2007 Alexey Morsov <swi@altlinux.ru> 0.9.3-alt1
- new version

* Mon Apr 16 2007 Alexey Morsov <swi@altlinux.ru> 0.9.2-alt1
- new version (bug fixing)

* Tue Apr 10 2007 Alexey Morsov <swi@altlinux.ru> 0.9.1-alt1
- New version (lot of new features such as Peer Exchange (PeX) support,
  autocompletion, new system tray popups, better internationalization,
  a lot of code rewriting (optimized and cleaned). 
- based on latest libtorrent library by Arvid Norberg (v0.12) 
- spec cleanup

* Fri Dec 22 2006 Alexey Morsov <swi@altlinux.ru> 0.8.0-alt1
- Initial build for sisyphus

