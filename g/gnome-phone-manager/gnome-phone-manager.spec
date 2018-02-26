%define ver_major 0.69

Name: gnome-phone-manager
Version: %ver_major
Release: alt1

Summary: GNOME Cellular Phone Manager
Group: Communications
Url: http://live.gnome.org/PhoneManager
License: GPLv2+

#git://git.gnome.org/phonemgr
Source: ftp://ftp.gnome.org/pub/gnome/sources/gnome-phone-manager/%version/%name-%version.tar
Patch: %name-0.69-gthread.patch

Requires(post,preun): GConf

BuildRequires: evolution-data-server-devel intltool libbluez-devel libgtk+3-devel
BuildRequires: libcanberra-gtk3-devel libGConf-devel libgnokii-devel
BuildRequires: libgnome-bluetooth-devel >= 3.4 libgtkspell-devel libtelepathy-glib-devel
BuildRequires: libdbus-glib-devel gnome-icon-theme gnome-common
BuildRequires: desktop-file-utils

%description
Phone Manager allows you to control aspects of your mobile phone from the
GNOME desktop.

Current features include:
    * Runs in the background; indicates status on the panel notification area.
    * Display on-screen alert when text message (SMS) arrives
    * Text message (SMS) sending facility
    * Evolution Addressbook integration when sending messages

Phone Manager supports any mobile phone that can connect to your computer as a
serial port: via Bluetooth, IrDA, or a serial cable.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=System \
	--remove-category=Telephony \
	--add-category=TelephonyTools \
	--add-category=Utility \
	%buildroot%_desktopdir/gnome-phone-manager.desktop

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/*
%_datadir/applications/*.desktop
%_datadir/%name
%_mandir/man1/*
%_libexecdir/telepathy-phoney
%_libdir/gnome-bluetooth/plugins/libphonemgr.so
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.phoney.service
%_datadir/telepathy/managers/phoney.manager
%config %_sysconfdir/gconf/schemas/%name.schemas
%doc README AUTHORS NEWS

%exclude %_libdir/gnome-bluetooth/plugins/libphonemgr.la

%changelog
* Sat Apr 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.69-alt1
- 0.69 snapshot

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.68-alt1
- 0.68

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.66-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gnome-phone-manager

* Mon Feb 21 2011 Yuri N. Sedunov <aris@altlinux.org> 0.66-alt1
- 0.66

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.65-alt5
- rebuild against libgnome-bluetooth.so.8

* Thu Oct 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.65-alt4
- rebuild against libedataserver-1.2.so.14 (e-d-s-2.32.0)

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.65-alt3
- rebuild against libgnokii.so.6

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.65-alt2
- rebuild against libedataserver-1.2.so.13 (e-d-s-2.30.2)

* Sat Mar 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.65-alt1
- first build for Sisyphus

