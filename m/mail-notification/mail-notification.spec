%def_disable evolution
Name: mail-notification
Version: 5.4
Release: alt4.1

Summary: A mail notification icon for the system tray
License: GPL3
Group: Graphical desktop/GNOME
Url: http://www.nongnu.org/mailnotify

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://savannah.nongnu.org/download/mailnotify/%name-%version.tar
#.bz2
Patch: %name-alt-build.patch
Patch1: %name-gmime-2.4.patch
Patch2: %name-debian-typo-fixes.patch
Patch3: %name-debian-update-eds.patch
Patch4: %name-debian-update-gob2.patch
Patch5: %name-debian-update-icons.patch
Patch6: %name-alt-ru.patch

# Automatically added by buildreq on Tue Nov 29 2011
# optimized out: GConf ORBit2-devel fontconfig fontconfig-devel glib2-devel gnome-vfs gnome-vfs-devel libGConf-devel libICE-devel libSM-devel libX11-devel libart_lgpl-devel libatk-devel libavahi-glib libbonobo-devel libbonoboui-devel libcairo-devel libcom_err-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgnome-devel libgnome-keyring libgnome-keyring-devel libgnomecanvas-devel libgpg-error libgtk+2-devel libkrb5-devel libpango-devel libpopt-devel pkg-config xorg-xproto-devel
BuildRequires: libdbus-glib-devel libglade-devel libgmime-devel libgnomeui-devel libnotify-devel librarian libsasl2-devel libssl-devel libxml2-devel perl-XML-Parser

%if_enabled evolution
BuildRequires: evolution-devel
%endif

%description
Mail Notification monitors your mailboxes for new mail.

When new mail arrives, Mail Notification alerts you by displaying an icon
in the notification area. Moreover, a mail summary can be displayed in the
icon tooltip, a sound can be played, and notifications containing useful
action buttons can be popped up.

Mail Notification can monitor multiple mailboxes concurrently, and supports
Evolution, Gmail, IMAP, Maildir, mbox, MH, Mozilla products (Mozilla,
SeaMonkey, Thunderbird, ...), POP3, Sylpheed, Windows Live Hotmail and Yahoo!
Mail mailboxes. Moreover, since Mail Notification uses GnomeVFS, it
transparently supports remote (SSH, HTTP, ...) and compressed mailboxes.

Mail Notification supports advanced POP3 and IMAP features such as SSL/TLS
connections (in-band or on separate port), SASL and APOP authentication,
and the IMAP IDLE extension.

While its user interface is purposedly kept simple and straightforward,
advanced users are provided with ways to run commands in reaction to
events, customize the popup buttons, obtain a XML message list, modify the
appearance of the application, and so on.

When a mailbox supports it, Mail Notification listens for changes reported
by the mailbox rather than polling it periodically. This mode of operation
provides immediate notification of changes and reduces the system and
network resources used by Mail Notification.

%if_enabled evolution
%package -n evolution-plugin-mail-notification
Summary: Mail Notification plugin for Evolution
Group: Graphical desktop/GNOME
Requires: evolution >= 2.12
Requires: %name = %version-%release

%description -n evolution-plugin-mail-notification
This package contains an advanced mail notification plugin for Evolution,
that uses Mail Notification applet.
%endif

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
./jb configure prefix=/usr sysconfdir=/etc destdir=%buildroot \
	libs="-lX11"
touch build/src/* ||:
./jb build

%install
./jb install

subst '/^Encoding=/d;' \
	%buildroot%_desktopdir/*.desktop

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
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/*.desktop
%config %_sysconfdir/gconf/schemas/%name.schemas
%config %_sysconfdir/xdg/autostart/%name.desktop
#config %_sysconfdir/sound/events/*
%doc AUTHORS NEWS README TODO TRANSLATING

%if_enabled evolution
%files -n evolution-plugin-mail-notification
%_libdir/evolution/*/plugins/org-jylefort-%name.eplug
%_libdir/evolution/*/plugins/liborg-jylefort-%name.so

%endif

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4-alt4.1
- Fixed build

* Tue Nov 29 2011 Ildar Mulyukov <ildar@altlinux.ru> 5.4-alt4
- update ru.po by Evgeniya Sinichenkova (closes #26637)

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.4-alt3
- fix build

* Tue Nov 30 2010 Ildar Mulyukov <ildar@altlinux.ru> 5.4-alt2
- fix a small imperfection in desktop file

* Tue Aug 24 2010 Ildar Mulyukov <ildar@altlinux.ru> 5.4-alt1
- 5.4
- cache-crash-fix patch is no longer needed
- gmime-2.4 support added
- borrow some debian patches
- disable evolution plugin

* Thu Apr 10 2008 Ildar Mulyukov <ildar@altlinux.ru> 5.2-alt0.3
- added Fix made by Jean-Yves Lefort for bug #210915 (Patch1)
- a little fix in the spec

* Wed Apr 09 2008 Ildar Mulyukov <ildar@altlinux.ru> 5.2-alt0.2
- merged specfile of Alexey Rusakov <ktirf@>

* Wed Apr 09 2008 Ildar Mulyukov <ildar@altlinux.ru> 5.2-alt0.1
- 5.2
- %%name-alt-build.patch for as-needed env.
- new (ugly) build system by the author

* Mon Jan 14 2008 Alexey Rusakov <ktirf@altlinux.org> 5.0-alt1
- New version (5.0).
- Added an explicit dependency of evolution-plugin-m-n on the main package.

* Sat Dec 29 2007 Alexey Rusakov <ktirf@altlinux.org> 5.0-alt0.rc1
- New version (5.0-rc1).
- Removed Debian menu support.
- Specfile cleanup; removed %%__ macros; use more path macros.
- Updated description from the website.
- Use %%make_install instead of %%makeinstall.
- Introduced a subpackage with a plugin for Evolution.
- Added a hack to (un)install scripts to notify GConf daemons about a new
  schema (RPM macros of GConf should be fixed about this).

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.0-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Jan 26 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.0-alt2
- Corrected buildreqs for X.org 7.0

* Sun Aug 14 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0-alt1
- New upstream version.
- Removed excess BuildReqs.

* Wed Apr 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.1-alt1
- Initial Sisyphus package.

