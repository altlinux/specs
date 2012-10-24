# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/mateconftool-2 pkgconfig(dbus-glib-1) pkgconfig(gdk-2.0) pkgconfig(gdk-pixbuf-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libcanberra-gtk) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define dbus_version            0.90

Summary: 	Desktop Mate Notification Daemon
Name: 		mate-notification-daemon
Version: 	1.4.0
Release: 	alt1_1.1
URL: 		http://mate-desktop.org
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 	GPLv2+
Group: 		System/Libraries
Provides: 	desktop-notification-daemon

BuildRequires: libdbus-devel >= %{dbus_version}
BuildRequires: libmatenotify-devel
BuildRequires: libcanberra-devel
BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: mate-conf-devel
BuildRequires: libmatewnck-devel
BuildRequires: gtk2-devel

Provides: mate-notification-daemon
Provides: mate-notification-daemon-engine-slider = %{version}-%{release}

%description
mate-notification-daemon is the server implementation of the freedesktop.org
desktop notification specification. Notifications can be used to inform
the user about an event or display some form of information without getting
in the user's way.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--disable-static \
	--with-gtk=2.0

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/mate-notification-daemon.schemas \
	> /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/mate-notification-daemon.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/mate-notification-daemon.schemas \
	> /dev/null || :
fi



%files -f %{name}.lang
%doc COPYING AUTHORS NEWS

%{_libexecdir}/mate-notification-daemon
%{_datadir}/applications/mate-notification-properties.desktop
%{_sysconfdir}/mateconf/schemas/mate-notification-daemon.schemas
%{_bindir}/mate-notification-properties
%{_libdir}/mate-notification-daemon/engines/*
%{_datadir}/dbus-1/services/org.freedesktop.mate.Notifications.service
%_iconsdir/hicolor/*/*/*
%{_datadir}/mate-notification-daemon/mate-notification-properties.ui


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

