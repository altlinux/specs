Name: xiphos
Version: 4.1.0
Release: alt2
Summary: Bible Study Software
Url: http://xiphos.org/
Group: Text tools
License: GPL2
Source: https://github.com/crosswire/xiphos/releases/download/%version/%name-%version.tar.gz
Source44: %name.watch

Requires: sword yelp
Provides: gnomesword
Obsoletes: gnomesword
BuildRequires: biblesync-devel >= 1.2.0
BuildRequires: libsword-devel >= 1.8.0

# Automatically added by buildreq on Fri Sep 15 2017
# optimized out: at-spi2-atk biblesync docbook-dtds fontconfig glib2-devel gnome-doc-utils-xslt libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libdbus-devel libdbus-glib libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgst-plugins1.0 libgtk+3-devel libharfbuzz-icu libicu-devel libjavascriptcoregtk3-devel libpango-devel libsoup-devel libstdc++-devel libuuid-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server libxml2-devel perl perl-Encode pkg-config python-base python-module-libxml2 python-modules python-modules-compiler python-modules-ctypes python-modules-encodings python-modules-logging xml-common xorg-xproto-devel xsltproc
BuildRequires: biblesync-devel gcc-c++ gnome-doc-utils intltool libGConf-devel libdbus-glib-devel libgsf-devel libsword-devel libwebkitgtk3-devel time

%description
Xiphos (formerly known as GnomeSword) is a Bible study application for GNOME,
a graphical desktop environment which is available for Linux and UNIX. Xiphos
is based on The SWORD Project by the CrossWire Bible Society, a framework for
providing tools useful for studying the Bible and additional information like
commentaries, dictionaries, and other texts using your computer.

%prep
%setup
rm -rf src/biblesync

%build
%add_optflags -fpermissive
./waf configure \
	--prefix=%prefix \
	--enable-webkit-editor \
	--gtk=3 || tail build/config.log

./waf build

%install
./waf install --destdir=%buildroot

mv %buildroot%_docdir/xiphos/ doc-install
%find_lang %name --with-gnome

%files -f %name.lang
%doc doc-install/*
%_bindir/*
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name

%changelog
* Sun Jun 10 2018 Ildar Mulyukov <ildar@altlinux.ru> 4.1.0-alt2
- add dep on `sword` for in-sword localizaton

* Wed May 23 2018 Ildar Mulyukov <ildar@altlinux.ru> 4.1.0-alt1
- new version

* Fri Sep 15 2017 Ildar Mulyukov <ildar@altlinux.ru> 4.0.6a-alt1
- new version

* Tue Nov 20 2012 Ildar Mulyukov <ildar@altlinux.ru> 3.1.5-alt1
- new version

* Thu Oct 21 2010 Ildar Mulyukov <ildar@altlinux.ru> 3.1.3-alt2
- gtkhtml-editor requirement quick fix

* Thu Jun 24 2010 Ildar Mulyukov <ildar@altlinux.ru> 3.1.3-alt1
- new version 3.1.3
- disable GECKO
- clean up spec

* Sat Sep 05 2009 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Wed Jun 17 2009 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version 3.1 (with rpmrb script)

* Fri Dec 19 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Thu Jul 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.5-alt1
- new version 2.3.5
- update buildreq, build with libgtkhtml

* Mon Dec 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt2
- rebuild with new xulrunner

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)
- update buildreq
- build with xulrunner, new sword 1.5.10

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.10-alt0.1
- new version 2.1.10 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt0.1
- new version
- remove debian menu

* Tue Dec 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1cvs20051113
- new version

* Sun Nov 13 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.3cvs20050716
- fix %_datadir/%name owner

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.2cvs20050716
- try 2

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1cvs20050716
- new 2.1.2 from CVS
- build with new sword
- NOTE: remove ~/.gnomesword-2.0 if one crashed

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.5
- rebuild with GNOME 2.10
- set name of executable as gnomesword

* Sun Jan 23 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.4
- rebuild with gcc3.4

* Thu Nov 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.3
- menu file fixed

* Sun Oct 31 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.2
- rebuld with libgal 2.2.3

* Fri Jul 30 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.1
- first build for Sisyphus (unstable 2.1.1)

* Fri Mar 12 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.0-2mdk
- Rebuild with latest gtkhtml/gal

* Mon Jan 19 2004 Buchan Milne <bgmilne@linux-mandrake.com> 2.0.0-1mdk
- 2.0.0
- rebuild for sword

* Sun Apr 27 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.7.9-1mdk
 - 0.7.9
 - Rebuild for gal

* Thu Mar 13 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.7.8-1mdk
- 0.7.8
- Cleanups
- ->contrib

* Wed Oct 09 2002 David Abilleira <david1@abilleira.com> 0.7.6-1mdk
- Updated to 0.7.6

* Wed Oct 09 2002 David Abilleira <david1@abilleira.com> 0.7.5-1mdk
- First package
