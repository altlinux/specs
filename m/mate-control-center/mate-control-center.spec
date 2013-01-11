Serial: 1
Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/update-mime-database libICE-devel libSM-devel libX11-devel libXxf86misc-devel pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libmatekbdui) pkgconfig(libxml-2.0) pkgconfig(pango) pkgconfig(xcursor) pkgconfig(xft) pkgconfig(xi) xorg-kbproto-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define fedora 18
Name:           mate-control-center
%define _name   libslab
Version:        1.5.2
Release:        alt1_1
Summary:        MATE Desktop control-center
License:        LGPLv2+ and GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
Requires:       gsettings-desktop-schemas

BuildRequires: desktop-file-utils
BuildRequires: icon-naming-utils
BuildRequires: mate-common
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(dconf)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libmate-menu)
BuildRequires: pkgconfig(libmatekbd)
BuildRequires: pkgconfig(libmatenotify)
BuildRequires: pkgconfig(libmarco-private)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(mate-settings-daemon)
BuildRequires: pkgconfig(mate-desktop-2.0)
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(unique-1.0)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xxf86misc)
BuildRequires: pkgconfig(xkbfile)

# sample code block for handling distributions which cant provide
# pkgconfig() capabilities - according to Dan: %%{?fedora} < 17
%if 0%{?fedora} < 17
# BuildRequires: foobar-devel
%else
# BuildRequires: pkgconfig(foobar)
%endif
Source44: import.info
Patch33: gnome-control-center-2.22.1-alt-background-location.patch
Patch34: gnome-control-center-2.28.0-passwd.patch

%description
MATE Desktop Control Center


%package -n %{_name}
Group: Graphical desktop/Other
License:        LGPLv2+
Summary:        MATE Desktop libslab port

%description -n %{_name}
This package provides libslab which is used in MATE control panel and in
gnome-main-menu.


%package devel
Group: Development/C
Summary:        Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{?serial:%serial:}%{version}-%{release}
Requires: libslab-devel

%description devel
Development files for mate-control-center

%package -n libslab-devel
Group: Development/C
Summary:        Development files for libslab-devel
Requires: libslab = %{?serial:%serial:}%{version}-%{release}

%description -n libslab-devel
Development files for libslab-devel


%prep
%setup -q
%patch33 -p1
%patch34 -p1


%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static          \
           --disable-schemas-compile \
           --disable-update-mimedb   \
           --disable-scrollkeeper

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

desktop-file-install									\
	--remove-category="MATE"							\
	--add-category="X-Mate"								\
	--delete-original								\
	--dir=%{buildroot}%{_datadir}/applications					\
%{buildroot}%{_datadir}/applications/*.desktop

# delete mime cache
rm %{buildroot}%{_datadir}/applications/mimeinfo.cache

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%config %{_sysconfdir}/xdg/menus/matecc.menu
%{_bindir}/mate-*
%{_libdir}/libmate-window-settings.so.*
%{_libdir}/window-manager-settings/
%{_sbindir}/mate-display-properties-install-systemwide
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/matecc.directory
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-*.svg
%{_datadir}/glib-2.0/schemas/org.mate.*.xml
%{_datadir}/mate-control-center/
%{_datadir}/mate/cursor-fonts/*.pcf
%{_datadir}/mate/help/mate-control-center/
%{_datadir}/mime/packages/mate-theme-package.xml
%{_datadir}/thumbnailers/mate-font-viewer.thumbnailer
%{_datadir}/omf/mate-control-center/
%{_datadir}/polkit-1/actions/org.mate.randr.policy

%files -n %{_name}
%{_libdir}/libslab.so.*

%files devel
%{_includedir}/mate-window-settings-2.0/
%{_libdir}/pkgconfig/mate-window-settings-2.0.pc
%{_libdir}/libmate-window-settings.so
%{_datadir}/pkgconfig/mate-default-applications.pc
%{_datadir}/pkgconfig/mate-keybindings.pc

%files -n libslab-devel
# libslab
%{_includedir}/libslab/
%{_libdir}/libslab.so
%{_libdir}/pkgconfig/libslab.pc

%changelog
* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.2-alt1_1
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- use F19 import base

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1.1.1
- rebuild with new libmatekbd

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted background-location and passwd alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

