Name: efax-gtk
Version: 3.2.9
Release: alt1

Summary: GUI front end for the efax fax program
Summary(ru_RU.UTF-8): Графическая программа работы с факсами

License: GPL
Group: Communications
Url: http://efax-gtk.sourceforge.net/

Packager: Pavel Vainerman <pv@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.src.tar
Source1: %name-%version.ru.po
Source2: %name-%version.config
#Patch: %name-%version.patch

# Automatically added by buildreq on Wed Apr 25 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcxx-gtk-utils libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+3-devel libpango-devel libstdc++-devel libwayland-client libwayland-server pkg-config xorg-kbproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ libcxx-gtk-utils-devel libtiff-devel

Requires: efax

%description
Efax-gtk is a GUI front end for the efax fax program.  It
can be used to send and receive faxes with a fax modem, and to manage,
view and print faxes sent or received. It uses the scripts which
come with the efax package.

%description -l ru_RU.UTF-8
Efax-gtk - графическая факсовая программа. Она может быть использована
для отправки и получения факсовых сообщений через факс-модем.
Позволяет просматривать и распечатывать входящие или исходящие сообщения.
Использует скрипты входящие в пакет efax

%prep
%setup -q
#%patch -p0
cp -f %SOURCE1 po/ru.po
rm -rf  po/ru.gmo

%build
%__subst "s| install-data-hook||" efax-gtk-faxfilter/Makefile.in
%configure

# disable internal efax build
%__subst 's|SUBDIRS = src efax|SUBDIRS = src|' Makefile
# remove lpd filter build
%__subst 's|SUBDIRS = po efax-gtk-faxfilter|SUBDIRS = src|' Makefile

%__subst 's|stock_send-fax.png|%name.png|' %name.desktop

( cd po/ && %__make update-gmo )

%make_build

%install
%makeinstall_std
%find_lang %name

install -D -m644 %SOURCE2 %buildroot%_sysconfdir/efax-gtkrc
mkdir -p %buildroot%_niconsdir/
mv %buildroot%_datadir/pixmaps/%name.png %buildroot%_niconsdir/%name.png

# links for external efax progs
ln -sf efax %buildroot%_bindir/efax-0.9a
ln -sf efix %buildroot%_bindir/efix-0.9a

%files -f %name.lang
%doc AUTHORS README BUGS ChangeLog
%_bindir/*
%config /etc/efax-gtkrc
%_man1dir/*
%_desktopdir/*
%_niconsdir/*
%_spooldir/fax/%name-*

%changelog
* Wed Apr 25 2012 Vitaly Lipatov <lav@altlinux.ru> 3.2.9-alt1
- new version 3.2.9 (with rpmrb script)
- cleanup spec
- build with gtk+3

* Thu Nov 18 2010 Pavel Vainerman <pv@altlinux.ru> 3.2.6-alt1
- new version (3.2.6)
- update build requires

* Thu Jun 17 2010 Pavel Vainerman <pv@altlinux.ru> 3.2.1-alt1
- new version (3.2.1)

* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 3.0.16-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for efax-gtk
  * pixmap-in-deprecated-location for efax-gtk
  * postclean-05-filetriggers for spec file

* Mon Oct 27 2008 Pavel Vainerman <pv@altlinux.ru> 3.0.16-alt2
- fixed for new g++

* Thu Nov 15 2007 Pavel Vainerman <pv@altlinux.ru> 3.0.16-alt1
- new version (3.0.16)

* Thu Jul 19 2007 Pavel Vainerman <pv@altlinux.ru> 3.0.15-alt1
- new version (3.0.15)
- add patch: fix mode for creation directories
- update BuildRequires

* Sat Mar 17 2007 Pavel Vainerman <pv@altlinux.ru> 3.0.14-alt1
- new version (3.0.14)

* Sat Mar 10 2007 Pavel Vainerman <pv@altlinux.ru> 3.0.13-alt1
- new version

* Sun Feb 18 2007 Pavel Vainerman <pv@altlinux.ru> 3.0.12-alt2
- add icon for menu

* Fri Nov 10 2006 Pavel Vainerman <pv@altlinux.ru> 3.0.12-alt1
- new version (3.0.12)

* Sat Jan 28 2006 Vitaly Lipatov <lav@altlinux.ru> 3.0.8-alt2
- NMU: spec cleanup (fix URL in Source, fix macroses, summary)
- remove lpd filter build
- remove obsoleted man pages
- remove old style menu file
- remove scrollkeeper scripts (it is gtk only program)
- use tar.bz2 for tarball
- fix links to efax
- add patch for recoding to console charset

* Wed Jan 25 2006 Pavel Vainerman <pv@altlinux.ru> 3.0.8-alt1
- build new version
- update ru.po

* Mon Oct 17 2005 Pavel Vainerman <pv@altlinux.ru> 3.0.6-alt1
- build new version
- minor fixes in spec
- update ru.po

* Mon Sep 12 2005 Pavel Vainerman <pv@altlinux.ru> 3.0.5-alt1
- build new version
- update ru.po
- add patch for correct russian translate
- rebuild BuildRequires

* Sun Aug 14 2005 Pavel Vainerman <pv@altlinux.ru> 3.0.4-alt1
- build new version
- update ru.po

* Tue Jul 19 2005 Pavel Vainerman <pv@altlinux.ru> 3.0.3-alt1
- build new version

* Thu Jun 23 2005 Pavel Vainerman <pv@altlinux.ru> 3.0.2-alt2
- add patch for show date in fax journal
- rebuild BuildRequires

* Sun Jun 05 2005 Pavel Vainerman <pv@altlinux.ru> 3.0.2-alt1
- build new version

* Sun May 15 2005 Pavel Vainerman <pv@altlinux.ru> 3.0.1-alt1
- build new version

* Wed May 11 2005 Pavel Vainerman <pv@altlinux.ru> 2.2.15-alt3
- update spec-file (remove old comments)
- off 'pkg-config --recursive' option

* Mon Mar 07 2005 Pavel Vainerman <pv@altlinux.ru> 2.2.15-alt2
- update ru.po

* Sat Mar 05 2005 Pavel Vainerman <pv@altlinux.ru> 2.2.15-alt1
- build new version

* Tue Feb 15 2005 Pavel Vainerman <pv@altlinux.ru> 2.2.14-alt2
- update ru.po

* Mon Jan 03 2005 Pavel Vainerman <pv@altlinux.ru> 2.2.14-alt1
- build new version

* Mon Nov 01 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.12-alt2
- update ru.po

* Wed Oct 27 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.12-alt1
- build new version

* Mon Sep 06 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.10-alt1
- rebuild new version
- update ru.po
- add menu-icon

* Tue Jul 13 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.8a-alt2
- change default documents directory
- update patch

* Mon Jul 12 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.8a-alt1
- build new version
- update group
- update ru.po
- add patch for configure documents directory

* Wed Jun 16 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.7a-alt1
- new version
- add man files for efax-gtk-faxfilter, efax-gtk-send
- configure for use with standart efax program

* Sun Jun 06 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.7-alt2
- rebuild with new libs
- update ru.po

* Wed Jun 02 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.7-alt1
- new version

* Tue Apr 06 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.5a-alt1.1
- add BuildRequires

* Sat Apr 03 2004 Pavel Vainerman <pv@altlinux.ru> 2.2.5a-alt1
- Updated version
- fixing bug (segfault Settings 'OK')

* Thu Jan 15 2004 George Buravlyov <bor@etersoft.ru> 2.2.4-alt1
- First building for ALTLinux
