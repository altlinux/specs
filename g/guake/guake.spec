Summary: guake - a drop-down terminal
Summary(ru.UTF-8):guake — выпадающий эмулятор терминала
Name: guake
Version: 0.4.2
Release: alt2.qa2
License: GPL v2+
Group: Terminals
URL: http://guake.org/
Source0: http://guake.org/files/%{name}-%{version}.tar.gz
Source1: guake.desktop

BuildRequires(pre): etersoft-build-utils libGConf-devel rpm-build-gnome
BuildRequires:  glibc-devel-static intltool libgtk+2-devel python-devel python-module-pygtk-devel python-module-vte python-modules-encodings

Requires: GConf
Requires: dbus
Requires: python-module-pygtk-libglade notification-daemon

Patch1: guake-add_tab-focus.patch
Patch2: guake-repocop-desktop.patch
Patch3: guake-0.4.2-alt-glib2.patch
BuildRequires: desktop-file-utils

%description
Guake is a drop-down terminal for Gnome Desktop Environment, so you
just need to press a key to invoke him, and press again to hide.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p2

%build
libtoolize
aclocal -I m4
autoconf
autoheader
automake
%configure \
--disable-static
%make

%install
%makeinstall 
#DESTDIR=%buildroot

rm -f %buildroot%_libdir/guake/*.la
#rm -r %buildroot%_datadir/locale/no_NB/
#install -d %buildroot%_datadir/locale/ru/LC_MESSAGES
#mv -f %buildroot%_datadir/locale/{ru_RU/LC_MESSAGES/guake.mo,ru/LC_MESSAGES/guake.mo}
mkdir -p -m 0777 %buildroot%gnome_autostartdir
cp %SOURCE1 %buildroot%gnome_autostartdir/guake.desktop


%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=System \
	%buildroot%_desktopdir/guake.desktop

%post
%gconf2_install guake

%preun
%gconf2_uninstall guake


%files -f %name.lang
%defattr(644,root,root,755)
%attr(755,root,root) %_bindir/*
%dir %_libdir/guake
%attr(755,root,root) %_libdir/guake/*.so
%_libdir/guake/*.py
%_datadir/guake
%_pixmapsdir/guake
%_desktopdir/*.desktop
%_datadir/dbus-1/services/org.guake.Guake.service
%_sysconfdir/gconf/schemas/guake.schemas
%_mandir/man1/guake.1*
%gnome_autostartdir/guake.desktop

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.qa2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.qa1.1
- Rebuild with Python-2.7

* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.2-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for guake
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Tue Sep 07 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.2-alt2
- Added patch: Ticket #248. The focus would change to the terminal after click on the new tab button.

* Fri Aug 13 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.2-alt1
- 0.4.2.20100801
- Added autostart guake

* Wed May 05 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Tue Jan 26 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 0.4.0-alt0.1
- initial build

