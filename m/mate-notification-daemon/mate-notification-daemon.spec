Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize libgio-devel pkgconfig(dbus-1) pkgconfig(gdk-2.0) pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libcanberra-gtk) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-notification-daemon
Version:        1.5.1
Release:        alt1_1
Summary:        Notification daemon for MATE Desktop
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  icon-naming-utils
BuildRequires:  libcanberra-devel
BuildRequires:  libmatenotify-devel
BuildRequires:  libmatewnck-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-doc-utils
Source44: import.info

%description
Notification daemon for MATE Desktop

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-schemas-compile   \
           --with-gtk=2.0              \
           --with-gnu-ld               

make %{?_smp_mflags} V=1

%install
#Keeping this just in case, not needed anymore
#LIBTOOL="/usr/bin/libtool" 
make install DESTDIR=%{buildroot}

desktop-file-install                               \
        --remove-category="MATE"                   \
        --add-category="X-Mate"                    \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/mate-notification-properties.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-notification-properties
%{_datadir}/applications/mate-notification-properties.desktop
%{_datadir}/dbus-1/services/org.freedesktop.mate.Notifications.service
%{_datadir}/mate-notification-daemon/mate-notification-properties.ui
%{_libexecdir}/mate-notification-daemon
%{_datadir}/icons/hicolor/*/apps/mate-notification-properties.*
%{_datadir}/glib-2.0/schemas/org.mate.NotificationDaemon.gschema.xml
%{_datadir}/MateConf/gsettings/mate-notification-daemon.convert
%{_libdir}/mate-notification-daemon


%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

