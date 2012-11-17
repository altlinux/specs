BuildRequires: libsystemd-login-devel
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xmlto libICE-devel libSM-devel libpam0-devel pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(x11)
# END SourceDeps(oneline)
Group: Toys
%define _libexecdir %_prefix/libexec
Name:           mate-screensaver
Version:        1.5.0
Release:        alt1_3
Summary:        MATE Screensaver

License:        GPLv2+ and LGPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# upstream commits
# https://github.com/mate-desktop/mate-screensaver/commit/8fbe2e552847b4ec1d5f49f35a2c2565cf3afeba
# https://github.com/mate-desktop/mate-screensaver/commit/49b028e85839da7006b4857cf323a7cbee91316c
# https://github.com/mate-desktop/mate-screensaver/commit/77ac5c607d0f0562aad4ab9573c4b85003216c0c
Patch0:         upstream_commits.patch

BuildRequires: gtk2-devel
BuildRequires: libmateui-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libxml2-devel
BuildRequires: mate-menus-devel
BuildRequires: mate-desktop-devel
BuildRequires: libexif-devel
BuildRequires: pam-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libmatekbd-devel
BuildRequires: libmatenotify-devel
BuildRequires: libGL-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: gettext
BuildRequires: nss-devel
BuildRequires: mate-common
BuildRequires: libXxf86misc-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXtst-devel
BuildRequires: desktop-file-utils
BuildRequires: mate-common
BuildRequires: pkgconfig(libsystemd-daemon)

Requires: altlinux-freedesktop-menu-common
Requires: mate-keyring-pam
Requires: mate-backgrounds
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
%patch0 -p1
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1
%patch34 -p1


%build
%configure \
        --disable-static \
        --with-xscreensaverdir=%{_datadir}/xscreensaver/config \
        --with-xscreensaverhackdir=%{_libexecdir}/xscreensaver  \
        --enable-locking \
	--with-passwd-helper=/usr/libexec/mate-screensaver/mate-screensaver-chkpwd-helper  \
	--disable-pam
#        --enable-pam

make V=1 %{?_smp_mflags}
gcc -o %name-chkpwd-helper $RPM_OPT_FLAGS %SOURCE45 -lpam


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome
install -m 755 %name-chkpwd-helper %buildroot%_libexecdir/%name/

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/mate-screensaver*
%{_sysconfdir}/pam.d/mate-screensaver
%{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_sysconfdir}/xdg/autostart/mate-screensaver.desktop
%{_libexecdir}/mate-screensaver-*
%{_libexecdir}/mate-screensaver/
%{_datadir}/applications/mate-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/*.desktop
%{_datadir}/mate-screensaver/
%{_datadir}/backgrounds/cosmos/
%{_datadir}/pixmaps/mate-logo-white.svg
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/MateConf/gsettings/org.mate.screensaver.gschema.migrate
%{_datadir}/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%{_datadir}/mate-background-properties/cosmos.xml
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_mandir}/man1/*.1.*
%attr(2511,root,chkpwd) %_libexecdir/%name/%name-chkpwd-helper

%files devel
%{_libdir}/pkgconfig/*


%changelog
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

