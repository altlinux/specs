Name:		flush
Summary:	GTK-based BitTorrent client
Version:	0.9.12
Release:	alt1.6
License:	GPLv3+
Group:		Networking/File transfer
Url:		http://flush.sourceforge.net/
Source0:	%name-%version.tar.bz2

BuildRequires: boost-asio-devel boost-filesystem-devel boost-signals-devel
BuildRequires: doxygen gcc-c++ libconfig-c++-devel libexpat-devel
BuildRequires: libglademm-devel libnotify-devel libssl-devel libtorrent-rasterbar-devel libdbus-devel

Patch0:		%name-0.9.11-magnet_mime_support.patch
Patch1: %name-%version-alt-build.patch

%description
Flush is a GTK-based BitTorrent client. You can use it to download files from
the BitTorrent network.

Features:
 * Controlling running instance by command line interface.
 * Running many instances with different configs from the same user.
 * Automatic copying finished downloads to specified directory.
 * Setting custom download path for each file of the torrent.
 * Ability to choose torrent file's character set encoding.
 * Automatic torrents loading from specified directory.
 * Automatic pausing and removing old torrents.
 * Temporary pausing and resuming torrents.
 * Overall and current session statistics.
 * Creating your own torrent files.
 * IP filter.

Flush uses Rasterbar's version of libtorrent.

%prep
%setup
%patch0 -p1
%patch1 -p2

%build
export CXXFLAGS+="--std=gnu++11 -DBOOST_FILESYSTEM_VERSION=3 -DGLIBMM_INCLUDED_FROM_WRAP_INIT_CC"
export CFLAGS+="--std=gnu++11 -DBOOST_FILESYSTEM_VERSION=3 -DGLIBMM_INCLUDED_FROM_WRAP_INIT_CC"
%configure --disable-bundle-package
%make_build

%install
%makeinstall
cd man/ru
make DESTDIR=%buildroot install
cd ../..

# icon and menu-entry
%__install -d -m 755 %buildroot%_datadir/pixmaps
%__install -m 644 icons/hicolor/48x48/apps/%name.png \
	%buildroot%_datadir/pixmaps

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING
%doc %_man1dir/%name.1.*
%doc %_mandir/*/*/%name.1.*
%_bindir/*
%dir %_datadir/%name
%dir %_datadir/%name/ui
%dir %_datadir/%name/icons
%_datadir/%name/ui/*.glade
%_desktopdir/*
%_iconsdir/*/*/apps/*
%_datadir/%name/icons
%_pixmapsdir/*

%changelog
* Fri Jan 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.12-alt1.6
- Fixed build.

* Tue Aug 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.12-alt1.5
- Rebuilt with new libtorrent-rasterbar.

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.12-alt1.4.qa4.1
- Rebuilt for gcc5 C++11 ABI.

* Fri May 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.12-alt1.4.qa4
- Rebuilt with new libtorrent-rasterbar8

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.9.12-alt1.4.qa3.1
- rebuild with boost 1.57.0

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.12-alt1.4.qa3
- Rebuilt with new libtorrent-rasterbar8

* Thu Jul 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.12-alt1.4.qa2
- Rebuilt with new libtorrent-rasterbar8

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.12-alt1.4.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.12-alt1.4
- Rebuilt with updated libtorrent-rasterbar

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.12-alt1.3
- Rebuilt with Boost 1.52.0

* Wed Sep 12 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.12-alt1.2
- fix BuildRequires for libtorrent-rasterbar7-devel

* Wed Sep 12 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.12-alt1.1
- fix build with new Boost 1.51

* Wed Sep 12 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Wed Aug 22 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.11-alt2
- add magnet support in desktop-file

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.11-alt1.1
- Rebuilt with Boost 1.49.0

* Fri Sep 30 2011 Motsyo Gennadi <drool@altlinux.ru> 0.9.11-alt1
- 0.9.11

* Tue Mar 22 2011 Motsyo Gennadi <drool@altlinux.ru> 0.9.10-alt2
- BuildRequires fixed for Sisyphus:
  + libdbus-devel added

* Mon Mar 07 2011 Motsyo Gennadi <drool@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Sun Jan 23 2011 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1
- build for ALT Linux (based OpenSUSE spec)
