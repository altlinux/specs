Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtkdocize libXau-devel libgio-devel libgtk+2-gir-devel pkgconfig(NetworkManager) pkgconfig(cairo) pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(ice) pkgconfig(libcanberra-gtk) pkgconfig(pango) pkgconfig(xau) pkgconfig(xrandr) python-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-panel
Version:        1.5.4
Release:        alt1_1
Summary:        MATE Desktop panel applets
#libs are LGPLv2+ applications GPLv2+
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gsettings-desktop-schemas
# needed as nothing else requires it
Requires:       mate-session-manager
#for fish
Requires:       fortune-mod

BuildRequires:  libdbus-glib-devel
BuildRequires:  libdconf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk2-devel
BuildRequires:  icon-naming-utils
BuildRequires:  libcanberra-devel
BuildRequires:  libmateweather-devel
BuildRequires:  libmatewnck-devel
BuildRequires:  libnm-gtk-devel
BuildRequires:  librsvg-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-doc-utils
BuildRequires:  mate-menus-devel
BuildRequires:  pango-devel
BuildRequires:  popt-devel
Source44: import.info
Requires: tzdata

%description
MATE Desktop panel applets


%package libs
Group: Development/C
Summary:        Shared libraries for mate-panel
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description libs
Shared libraries for libmate-desktop

%package devel
Group: Development/C
Summary:        Development files for mate-panel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-panel

%prep
%setup -q


%build
NOCONFIGURE=1 ./autogen.sh
#libexecdir needed for gnome conflicts
%configure --disable-scrollkeeper                 \
           --disable-static                       \
           --disable-schemas-compile              \
           --with-x                               \
           --enable-network-manager               \
           --libexecdir=%{_libexecdir}/mate-panel \
           --enable-introspection
make  %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install

rm -fv %{buildroot}%{_libdir}/lib*.la

desktop-file-install \
        --remove-category="MATE" \
        --add-category="X-Mate" \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/mate-panel.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/mate-desktop-item-edit
%{_bindir}/mate-panel
%{_bindir}/mate-panel-test-applets
%{_libdir}/girepository-1.0/MatePanelApplet-4.0.typelib
%{_libexecdir}/mate-panel/
%{_datadir}/glib-2.0/schemas/org.mate.panel.*.xml
%{_datadir}/applications/mate-panel.desktop
%{_datadir}/dbus-1/services/org.mate.panel.*.service
%{_datadir}/omf/mate-applet-fish/
%{_datadir}/omf/mate-applet-clock/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mate/help/mate-applet-clock/
%{_datadir}/mate/help/mate-applet-fish/
%{_datadir}/mate-panel
%{_datadir}/mate-panelrc
%{_datadir}/MateConf/gsettings/mate-panel.convert

%files libs
%doc COPYING.LIB
%{_libdir}/libmate-panel-applet-4.so.1*

%files devel
%{_libdir}/libmate-panel-applet-4.so
%{_includedir}/mate-panel-4.0/
%{_libdir}/pkgconfig/libmatepanelapplet-4.0.pc
%{_datadir}/gir-1.0/MatePanelApplet-4.0.gir
%{_datadir}/gtk-doc/html/mate-panel-applet/


%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new fc release

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt4_1.1
- rebuild with mate-desktop

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3_1.1
- Build for Sisyphus

* Fri Oct 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1
- adapted alt patches, dropped some fedora patches

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- added Requires: iso-codes

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2
- converted by srpmconvert script

