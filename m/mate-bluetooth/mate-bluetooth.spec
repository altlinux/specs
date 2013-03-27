Group: Communications
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtk-update-icon-cache /usr/bin/gtkdocize /usr/bin/update-desktop-database /usr/bin/xmllint libgio-devel libgtk+2-gir-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gmodule-export-2.0) pkgconfig(gtk+-2.0) pkgconfig(x11) pkgconfig(xi)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-bluetooth
Version:        1.5.0
Release:        alt1_2
Summary:        MATE Desktop bluetooth applet
License:        GPLv2+
URL:            http://www.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  mate-panel-devel
BuildRequires:  mate-file-manager-sendto-devel
BuildRequires:  rarian-compat
BuildRequires:  gtk2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libunique-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  libmatenotify-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gsettings-desktop-schemas-devel

Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
Requires:  mate-panel
Requires:  mate-file-manager-sendto
Source44: import.info

%description
MATE Desktop bluetooth applet


%package libs
Group: System/Libraries
Summary:        Shared libraries for mate-bluetooth
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description libs
development files for mate-bluetooth


%package devel
Group: Communications
Summary:        Development file for mate-bluetooth
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
development files for mate-bluetooth

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static           \
           --disable-scrollkeeper     \
           --disable-schemas-compile  \
           --disable-icon-update      \
           --disable-desktop-update   \
           --enable-caja-sendto  

make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
%find_lang %{name} --all-name

desktop-file-install                               \
     --remove-category="MATE"                      \
     --add-category="X-Mate"                       \
     --delete-original                             \
     --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mate-bluetooth-properties.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_datadir}/icons/mate/*x*/status/*.png
%{_datadir}/icons/mate/*x*/apps/bluetooth.png
%{_datadir}/gtk-doc/html/mate-bluetooth
%{_datadir}/icons/mate/scalable/*/*.svg
%config %{_sysconfdir}/xdg/autostart/mate-bluetooth-applet.desktop
%{_bindir}/mate-bluetooth-applet
%{_bindir}/mate-bluetooth-properties
%{_bindir}/mate-bluetooth-sendto
%{_bindir}/mate-bluetooth-wizard
%{_datadir}/MateConf/gsettings/mate-bluetooth-nst
%{_datadir}/glib-2.0/schemas/org.mate.Bluetooth.nst.gschema.xml
%{_datadir}/MateConf/gsettings/mate-bluetooth
%{_datadir}/applications/mate-bluetooth-properties.desktop
%{_datadir}/glib-2.0/schemas/org.mate.Bluetooth.gschema.xml
%{_datadir}/mate/help/mate-bluetooth
%{_datadir}/omf/mate-bluetooth
%{_datadir}/mate-bluetooth

%files libs
%{_libdir}/libmate-bluetooth.so.8
%{_libdir}/libmate-bluetooth.so.8.0.0
%{_libdir}/girepository-1.0/MateBluetooth-1.0.typelib
%{_libdir}/mate-bluetooth/plugins/libgbtgeoclue.so
%{_libdir}/caja-sendto/plugins/libnstbluetooth.so

%files devel
%{_includedir}/mate-bluetooth
%{_libdir}/pkgconfig/mate-bluetooth-1.0.pc
%{_libdir}/libmate-bluetooth.so
%{_datadir}/gir-1.0/MateBluetooth-1.0.gir

%changelog
* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- mate 1.5

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

