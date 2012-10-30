# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/mateconftool-2 /usr/bin/xmlto libICE-devel libSM-devel pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec

Summary: 	MATE Screensaver
Name: 		mate-screensaver
Version: 	1.4.0
Release: 	alt3
License: 	GPLv2+
Group: 		Toys
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
URL: 		http://pub.mate-desktop.org

Patch1: gnome-screensaver-2.20.0-default-theme.patch
#Patch2: gnome-screensaver-2.26.0-securitytoken.patch
Patch7: gnome-screensaver-2.20.0-blank-by-default.patch
Patch8: gnome-screensaver-2.20.0-selinux-permit.patch

BuildRequires: gtk2-devel
BuildRequires: libmateui-devel
BuildRequires: libdbus-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libxml2-devel
BuildRequires: mate-conf-devel
BuildRequires: mate-menus-devel
BuildRequires: mate-desktop-devel
BuildRequires: libexif-devel
BuildRequires: pam-devel
BuildRequires: libX11-devel libXScrnSaver-devel libXext-devel
BuildRequires: libXinerama-devel libXmu-devel
BuildRequires: libmatekbd-devel
BuildRequires: libmatenotify-devel
# this is here because the configure tests look for protocol headers
BuildRequires: xorg-x11-proto-devel
BuildRequires: gettext
BuildRequires: nss-devel
BuildRequires: automake autoconf libtool intltool mate-common
BuildRequires: libXxf86misc-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXtst-devel
BuildRequires: desktop-file-utils
BuildRequires: mate-common
Requires(pre): mate-conf
Requires(preun): mate-conf
Requires(post): mate-conf
Requires: altlinux-freedesktop-menu-common
# since we use it, and pam spams the log if a module is missing
Requires: mate-keyring-pam
#Requires: fedora-screensaver-theme
Conflicts: xscreensaver < 1:5.00-19
Patch33: gnome-screensaver-2.28.0-alt-pam.patch
Patch34: mate-screensaver-2.28.0-user_activity.patch
Source44: unix2_chkpwd.c


%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch1 -p1 -b .use-floaters-by-default
#%patch2 -p1 -b .securitytoken
%patch7 -p1 -b .blank-by-default
#patch8 -p1 -b .selinux-permit

autoreconf -f -i
%patch33 -p1
%patch34 -p1

%build

%configure \
	--disable-static \
	--with-xscreensaverdir=/usr/share/xscreensaver/config \
	--with-xscreensaverhackdir=/usr/libexec/xscreensaver  \
	--with-passwd-helper=/usr/libexec/mate-screensaver/mate-screensaver-chkpwd-helper  \
	--enable-locking \
	--disable-pam

make %{?_smp_mflags}
gcc -o %name-chkpwd-helper $RPM_OPT_FLAGS %SOURCE44 -lpam

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

#desktop-file-install --vendor="" --delete-original                   \
#  --dir $RPM_BUILD_ROOT%{_datadir}/applications                         \
#  --add-only-show-in X-MATE                                              \
#  $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%find_lang %{name}
install -m 755 %name-chkpwd-helper %buildroot%_libexecdir/%name/

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/mate-screensaver.schemas \
	> /dev/null || :
%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/mate-screensaver.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/mate-screensaver.schemas \
	> /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/*
%{_libexecdir}/*
# wildcard _libexecdir/*
%exclude %_prefix/lib/debug
%{_libdir}/pkgconfig/*
%{_datadir}/applications/mate-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/
%{_datadir}/mate-screensaver/
%{_datadir}/backgrounds/cosmos
%{_datadir}/pixmaps/mate-logo-white.svg
%{_datadir}/desktop-directories/mate-screensaver.directory
%dir %{_datadir}/mate-background-properties
%{_datadir}/mate-background-properties/cosmos.xml
%{_sysconfdir}/mateconf/schemas/*.schemas
%{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_sysconfdir}/pam.d/*
%{_sysconfdir}/xdg/autostart/mate-screensaver.desktop
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%doc %{_mandir}/man1/*.1.gz
%attr(2511,root,chkpwd) %_libexecdir/%name/%name-chkpwd-helper

%changelog
* Tue Oct 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3
- chkpwd usage and rights fixed

* Mon Oct 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Tue Aug 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

