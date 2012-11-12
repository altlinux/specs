# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/mateconftool-2 libpopt-devel pkgconfig(audiofile) pkgconfig(esound) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
Group: System/Libraries
Requires: design-graphics
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
%global  schemas desktop_mate_accessibility_keyboard desktop_mate_accessibility_startup desktop_mate_applications_at_mobility desktop_mate_applications_at_visual desktop_mate_applications_browser desktop_mate_applications_office desktop_mate_applications_terminal desktop_mate_applications_window_manager desktop_mate_background desktop_mate_file_views desktop_mate_interface desktop_mate_lockdown desktop_mate_peripherals_keyboard desktop_mate_peripherals_mouse desktop_mate_sound desktop_mate_thumbnail_cache desktop_mate_thumbnailers desktop_mate_typing_break
 
Summary:	MATE Desktop base libraries
Name:	libmate
Version:	1.4.0
Release:	alt4_17
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License:	GPLv2+ and LGPLv2+

Buildrequires: mate-common mate-desktop-devel mate-corba-devel mate-vfs-devel mate-conf-devel mate-conf-gtk mate-conf libmatecomponent-devel libcanberra-devel mate-doc-utils popt-devel
Requires(pre):	mate-conf
Requires(post):	mate-conf
Requires(preun):	mate-conf
Requires: mate-conf
Source44: import.info
Patch33: libgnome-2.22.0-alt-default_gtk_theme.patch
Patch34: libgnome-alt-settings.patch
Patch35: libmate_default_background_path.patch
Patch36: libgnome-2.22.0-default-sound-effects.patch
Patch37: libgnome-2.24.1-default-noblink.patch
Patch38: libgnome-2.7.2-default-cursor.patch
Patch39: libmate-2.11.1-scoreloc.patch
Patch40: libmate-default-browser.patch
Patch41: libmate-im-settings.patch
Source45: alt-mate-default.xml
Source46: desktop_mate_peripherals_monitor.schemas

%description
MATE Desktop base libraries

%package devel
Summary: Development libraries, header files and utilities for libmate
Group: Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libs and headers for libmate

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1

%build
%configure -disable-static --disable-schemas-install --disable-esd
make %{?_smp_mflags} V=1


%install
export MATECONF_DISABLE_MAKE_FILE_SCHEMA INSTALL=1
make LIBTOOL="/usr/bin/libtool" DESTDIR=%{buildroot} install

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

%find_lang %{name}
cp -p %{SOURCE45} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/mate-default.xml
cp -p %{SOURCE46} $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas/


%pre
%mateconf_schema_prepare %{schemas}


%preun
%mateconf_schema_remove %{schemas}


%post
%mateconf_schema_upgrade %{schemas}


%files -f %{name}.lang
%doc AUTHORS README
%{_mandir}/man7/*
%{_bindir}/mate-open
%{_sysconfdir}/sound/events/mate.soundlist
%{_sysconfdir}/sound/events/gtk2-mate-events.soundlist
%{_sysconfdir}/mateconf/schemas/desktop_mate_accessibility_keyboard.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_accessibility_startup.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_at_mobility.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_at_visual.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_browser.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_office.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_terminal.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_window_manager.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_background.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_file_views.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_interface.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_lockdown.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_mouse.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_sound.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_thumbnail_cache.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_thumbnailers.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_typing_break.schemas
%{_datadir}/mate-background-properties/mate-default.xml
%{_libdir}/libmate-2.so.0.400.0
%{_libdir}/libmate-2.so.0
%{_libdir}/matecomponent/servers/MATE_Moniker_std.server
%{_libdir}/matecomponent/monikers/libmoniker_extra_2.so
%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_monitor.schemas

%files devel
%{_datadir}/gtk-doc/html/libmate/
%{_includedir}/libmate-2.0/
%{_libdir}/libmate-2.so
%{_libdir}/pkgconfig/libmate-2.0.pc

%changelog
* Mon Nov 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt4_17
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt4_1.1
- Build for Sisyphus

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt4_1
- adapted alt patches

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1
- drop Fedora icon theme patch (6)

* Wed Aug 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- use altlinux background

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

