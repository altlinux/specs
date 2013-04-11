Group: Toys
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xmlto libICE-devel libSM-devel libgio-devel libpam0-devel pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(libsystemd-daemon) pkgconfig(libsystemd-login)
# END SourceDeps(oneline)
BuildRequires: libsystemd-login-devel
%define _libexecdir %_prefix/libexec
Name:           mate-screensaver
Version:        1.6.0
Release:        alt2
Summary:        MATE Screensaver
License:        GPLv2+ and LGPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
Requires:       altlinux-freedesktop-menu-common
Requires:       mate-keyring-pam
Requires:       mate-backgrounds
Requires:       mate-power-manager

BuildRequires:  gtk2-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  mate-menus-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  pam-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXmu-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libnotify-devel
BuildRequires:  libGL-devel
BuildRequires: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-evieproto-devel xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-pmproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcbproto-devel xorg-xcmiscproto-devel xorg-xextproto-devel xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel xorg-xf86rushproto-devel xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel
BuildRequires:  mate-common
BuildRequires:  libXxf86misc-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libXtst-devel
BuildRequires:  desktop-file-utils
BuildRequires:  mate-common
BuildRequires:  libX11-devel
BuildRequires:  systemd-devel
Buildrequires:  xmlto
Source44: import.info
Patch33: gnome-screensaver-2.28.0-alt-pam.patch
Patch34: mate-screensaver-2.28.0-user_activity.patch
Source45: unix2_chkpwd.c

%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.


%package devel
Group: Toys
Summary: Development files for mate-screensaver
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-screensaver


%prep
%setup -q
%patch33 -p1
%patch34 -p1


%build
NOCONFIGURE=1 ./autogen.sh
%configure \
            --with-x \
            --with-mit-ext \
            --with-xf86gamma-ext \
            --with-libgl \
            --with-shadow \
            --with-console-kit \
            --enable-docbook-docs \
            --enable-authentication-scheme=helper \
	    --with-passwd-helper=%_libexecdir/%name/%name-chkpwd-helper \
            --enable-locking

make %{?_smp_mflags} V=1
gcc -o %name-chkpwd-helper $RPM_OPT_FLAGS %SOURCE45 -lpam


%install
make DESTDIR=%{buildroot} install

desktop-file-install --delete-original             \
  --dir %{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mate-screensaver-preferences.desktop

desktop-file-install                                          \
   --delete-original                                          \
   --dir %{buildroot}%{_datadir}/applications/screensavers    \
%{buildroot}%{_datadir}/applications/screensavers/*.desktop

%find_lang %{name} --with-gnome
install -m 755 %name-chkpwd-helper %buildroot%_libexecdir/%name/

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/mate-screensaver*
%{_sysconfdir}/pam.d/mate-screensaver
%{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_sysconfdir}/xdg/autostart/mate-screensaver.desktop
%{_libexecdir}/mate-screensaver-*
%{_libexecdir}/mate-screensaver
%{_datadir}/applications/mate-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/*.desktop
%{_datadir}/mate-screensaver
%{_datadir}/backgrounds/cosmos/
%{_datadir}/pixmaps/mate-logo-white.svg
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/MateConf/gsettings/org.mate.screensaver.gschema.migrate
%{_datadir}/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%{_datadir}/mate-background-properties/cosmos.xml
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_mandir}/man1/*
%attr(2511,root,chkpwd) %_libexecdir/%name/%name-chkpwd-helper

%files devel
%{_libdir}/pkgconfig/*


%changelog
* Thu Apr 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- password check fixed: use setgid helper

* Sun Apr 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt3_3
- new fc release

* Tue Feb 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt3_2
- dropped obsolete dependencies

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_2
- new fc release

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_1
- bugfix release (closes: 28151)

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new version; updated ru translation

* Sat Nov 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- dropped gdialog compat script (conflicts with real gdialog)

* Tue Oct 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3
- chkpwd usage and rights fixed

* Mon Oct 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Tue Aug 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

