Summary: Graphical network viewer modeled after etherman.
Name: etherape
Version: 0.9.12
Release: alt1
License: GPL
Group: Networking/Other
Packager: Ilya Mashkin <oddity at altlinux.ru>
Source: etherape-%version.tar.gz

URL: http://etherape.sourceforge.net

# Automatically added by buildreq on Tue Aug 16 2005
BuildRequires: ORBit2-devel esound fontconfig freetype2 glib2-devel gnome-vfs2-devel libGConf2-devel libart_lgpl-devel libatk-devel libbonobo2-devel libbonoboui-devel libglade2-devel libgnome-devel libgnome-keyring libgnomecanvas-devel libgnomeui-devel libgtk+2-devel libpango-devel libpcap-devel libpopt-devel libxml2-devel pkgconfig librarian gnome-doc-utils
BuildRequires: desktop-file-utils

%description
Etherape is a graphical network monitor for Unix modeled after
etherman. Featuring ether, ip and tcp modes, it displays network
activity graphically. Hosts and links change in size with traffic. 
Color coded protocols display. It supports ethernet, ppp and slip 
devices. It can filter traffic to be shown, and can read traffic 
from a file as well as live from the network.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall

%find_lang --with-gnome %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Monitor \
	%buildroot%_desktopdir/etherape.desktop


%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README FAQ README.bugs
%config %_sysconfdir/%name/*
%_bindir/*
%_datadir/locale/*/*/*
%_datadir/%name/*/*
%_datadir/applications/%name.desktop
#_datadir/gnome/*/*/*
%_datadir/pixmaps/*
%_man1dir/*
#_var/lib/scrollkeeper/*

%changelog
* Sat Jun 04 2011 Ilya Mashkin <oddity@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.10-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for etherape

* Sun May 01 2011 Ilya Mashkin <oddity@altlinux.ru> 0.9.10-alt2
- fix build

* Sun Feb 20 2011 Ilya Mashkin <oddity@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Sat Jan 16 2010 Ilya Mashkin <oddity@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Sat Oct 17 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1
- New version 0.9.8

* Sat Sep 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.7-alt2
- update requires, remove scrollkeeper

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 0.9.7-alt1
- New version 0.9.7
- spec fix, update requires

* Tue Aug 16 2005 Vitaly Erokhin <greyp@altlinux.org> 0.9.2-alt1
- New multithreaded name resolution using the standard resolver api. Works with dns, /etc/host, ...
- Small fixes for gcc 4

* Tue May 31 2005 Vitaly Erokhin <greyp@altlinux.org> 0.9.1-alt1
- First release (0.9.1)
