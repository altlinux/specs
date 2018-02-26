Name: gossip
Version: 0.32
Release: alt4.git20090422

%def_enable dbus
%def_enable libnotify
%def_disable galago
%def_enable gnome_keyring
%def_disable ebook
%def_enable aspell
%def_disable peekaboo

Summary: Jabber client for GNOME
Group: Networking/Instant messaging
License: GPL
URL: http://developer.imendio.com/projects/gossip/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

%define intltool_version 0.35.0
%define loudmouth_version 1.4.1
%define libxml2_version 2.6.16
%define glib_version 2.12.0
%define gtk_version 2.14.0
%define gio_version 2.16.0
%define gconf_version 1.2.0
%define panel_version 2.10.0
%define dbus_version 0.61
%define galago_version 0.5.0
%define libnotify_version 0.4.1
%define libglade_version 2.0.0
%define libgnome_version 2.0.0
%define libcanberra_version 0.3

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

# For macros
BuildPreReq: GConf librarian

# from configure.in
BuildPreReq: intltool >= %intltool_version
BuildPreReq: desktop-file-utils >= 0.2.90
BuildPreReq: libloudmouth-devel >= %loudmouth_version
BuildPreReq: libxml2-devel >= %libxml2_version
BuildPreReq: glib2-devel >= %glib_version
BuildPreReq: libgtk+2-devel >= %gtk_version
BuildPreReq: libGConf-devel >= %gconf_version
%{?_enable_peekaboo:BuildPreReq: libgnome-panel-devel >= %panel_version}
BuildPreReq: libglade-devel >= %libglade_version
BuildPreReq: iso-codes-devel
BuildPreReq: libgio-devel >= %gio_version
BuildPreReq: libcanberra-devel >= %libcanberra_version libcanberra-gtk2-devel
BuildPreReq: libXScrnSaver-devel libXext-devel libX11-devel
%{?_enable_dbus:BuildPreReq: libdbus-devel >= %dbus_version libdbus-glib-devel}
%{?_enable_libnotify:BuildPreReq: libnotify-devel >= %libnotify_version}
%{?_enable_galago:BuildPreReq: libgalago-devel >= %galago_version}
%{?_enable_gnome_keyring:BuildPreReq: libgnome-keyring-devel}
%{?_enable_ebook:BuildPreReq: evolution-data-server-devel}
%{?_enable_aspell:BuildPreReq: libaspell-devel}

BuildRequires: gcc-c++ gnome-doc-utils

%description
Gossip is an instant messaging program for GNOME.
Gossip aims at making Instant Messaging with Jabber as easy as possible,
while giving users of the GNOME Desktop a user friendly way of keeping
in touch with their friends.

%package peekaboo
Summary: Peekaboo applet for Gossip
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description peekaboo
An applet to quickly show Gossip chat windows and some of the
more popular functions of Instant Messaging.

%prep
%setup -q

%patch0 -p1
rm -f COPYING
ln -s %_licensedir/GPL-2 COPYING
bzip2 -9k ChangeLog

%build
intltoolize --force
gnome-doc-prepare --copy --force
%autoreconf
%configure \
	%{subst_enable dbus} \
	%{subst_enable libnotify} \
	%{subst_enable galago} \
	%{?_enable_gnome_keyring:--enable-gnome-keyring=yes} \
	%{subst_enable ebook} \
	--disable-schemas-install \
	--disable-scrollkeeper
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_datadir/applications/*
%_datadir/icons/hicolor/*/apps/*
%_datadir/sounds/*
%config(noreplace) %_sysconfdir/sound/events/gossip.soundlist
%config %_sysconfdir/gconf/schemas/*
%doc AUTHORS ChangeLog.bz2 NEWS README
%doc --no-dereference COPYING

%if_enabled dbus
%if_enabled peekaboo
%files peekaboo
%_libexecdir/peekaboo-applet
%_libdir/bonobo/servers/*
%endif
%endif

%changelog
* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt4.git20090422
- fix build with libnotify-0.7

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt3.git20090422
- disable galago and ebook support
- disable applet

* Mon Oct 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt2.git20090422
- rebuild with libebook-1.2.so.10

* Tue May 12 2009 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt1.git20090422
- 0.32 git 20090422 version
- update BuildRequires
- removed libgnomeui and libgnomevfs deps, add libcanberra-gtk

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 0.31-alt2
- removed obsolete %%post{,in} scripts
- updated buildreqs

* Wed Oct 08 2008 Alexey Shabalin <shaba@altlinux.ru> 0.31-alt1
- 0.31
- rebuild with libgalago-0.5.2 (soname so.3)

* Sat Jul 12 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt3
- fix desktop file

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt2
- add Packager tag

* Sat May 10 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt1
- 0.28 -> 0.29

* Wed Apr 16 2008 Igor Zubkov <icesik@altlinux.org> 0.28-alt2
- Update Url
- add %%update_menus to %%post script
- add %%clean_menus to %%postun script

* Mon Mar 17 2008 Igor Zubkov <icesik@altlinux.org> 0.28-alt1
- 0.26 -> 0.28

* Tue Oct 23 2007 Igor Zubkov <icesik@altlinux.org> 0.26-alt2
- fix build with new intltool

* Tue Jun 19 2007 Igor Zubkov <icesik@altlinux.org> 0.26-alt1
- 0.17 -> 0.26
- buildreq and update build requires

* Wed Dec 27 2006 Igor Zubkov <icesik@altlinux.org> 0.17-alt1.1
- rebuild with new dbus

* Tue Sep 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.17-alt1
- Updated to 0.17
- Updated versioned dependencies
- Buildreq

* Thu Jul 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.12-alt1
- Release 0.12
- Patch0 is obsolete

* Fri Jun 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.2-alt1
- Release 0.11.2

* Tue Jun 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.1-alt2
- Patch0: port to libgalago 0.5, from GNOME bug 339333
- Rebuilt with libgalago 0.5

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.1-alt1
- Release 0.11.1

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11-alt1
- Release 0.11
- Enabled libnotify back
- Compressed ChangeLog

* Sun Mar 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.2-alt1
- Release 0.10.2
- Buildreq

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- Release 0.10.1
- Disabled libnotify support until the API stabilizes

* Sun Feb 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10-alt1
- 0.10
- Buildreq
- Optional Galago support, enabled by default
- Removed Debian-style menu

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.9-alt1
- New upstream release
- Patch0 is obsolete

* Fri Jul 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt3
- Patch for new dbus from Fedora (thanks Rider) [Patch0]
- Requires dbus 0.34

* Sun Jan 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt2
- Added the common menu entry (bug #5909)

* Tue Jan 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt1
- New upstream release

* Sat Dec 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt3
- Added /usr/share/gossip directory to the file list

* Mon Oct 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt2
- Stricter installtime versioned dependencies copied from the buildtime
  dependencies, which are in turn copied from configure dependencies
  (bug #5393)

* Sat Oct 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt1
- Updated to the new upstream release
- Conditionally build with dbus

* Tue May 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.5-alt1
- New upstream release

* Sat Mar 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.4-alt1
- New upstream release

* Sat Feb 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.2-alt1
- New upstream release
- Run automake

* Fri Jan 23 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.1-alt1
- New upstream release

* Sat Jan 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.6-alt1
- New upstream release

* Wed Aug 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.5-alt1
- New version

* Mon Jul 21 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.4-alt1
- Ported to ALT Linux
