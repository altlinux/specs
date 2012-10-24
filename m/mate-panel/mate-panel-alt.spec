# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gio-querymodules /usr/bin/glib-genmarshal /usr/bin/gtkdocize /usr/bin/mateconftool-2 libgtk+2-gir-devel pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(gtk+-2.0) pkgconfig(ice) pkgconfig(libcanberra-gtk) pkgconfig(libecal-1.2) pkgconfig(libedataserver-1.2) pkgconfig(pango) pkgconfig(sm) python-devel
# END SourceDeps(oneline)
%define libwnck_version 1.0
%define mate_corba_version 1.0
%define _libexecdir %_prefix/libexec
%define gettext_package mate-panel-2.0

%define mate_desktop_version 1.1.0
%define glib2_version 2.25.12
%define gtk2_version 2.11.3
%define libmate_version 1.1.2
%define libmateui_version 1.1.2
%define libmatecomponentui_version 1.1.1
%define mate_cobra_version 1.1.0
%define libmatewnck_version 1.3.0
%define mate_conf_version 1.1.0
%define mate_menus_version 1.1.1
%define cairo_version 1.0.0
%define dbus_version 0.60
%define dbus_glib_version 0.60
%define mate_doc_utils_version 1.1.0
%define libmateweather_version 1.1.0


Summary: 			MATE panel
Name: 				mate-panel
Version: 			1.4.0
Release: 			alt3_1.1
URL: 				http://pub.mate-desktop.org
Source0: 			http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Source3: 			redhat-panel-default-setup.entries
Source4: 			gnome-compiler-flags.m4
Source5: 			redhat-panel-backwards-compat-config.schemas
Source6: 			add-translations.sh
License: 			GPLv2+ and LGPLv2+ and GFDL
Group: 				Graphical desktop/Other

Requires: 			mate-desktop >= %{mate_desktop_version}
Requires: 			libwnck >= %{libwnck_version}
Requires: 			mate-menus >= %{mate_menus_version}
Requires: 			mate-session-xsession
Requires: 			%{name}-libs = %{version}-%{release}

Requires(post): 	mate-conf >= %{mate_conf_version}
Requires(post): 	icon-theme-hicolor
Requires(pre): 		mate-conf >= %{mate_conf_version}
Requires(preun): 	mate-conf >= %{mate_conf_version}

BuildRequires: 		libxml2-python
BuildRequires: 		intltool
BuildRequires: 		gettext
BuildRequires: 		automake
BuildRequires: 		autoconf
BuildRequires: 		libtool
BuildRequires: 		scrollkeeper
BuildRequires: 		xsltproc libxslt
BuildRequires: 		libX11-devel
BuildRequires: 		libXt-devel
BuildRequires: 		mate-desktop-devel >= %{mate_desktop_version}
BuildRequires: 		glib2-devel >= %{glib2_version}
BuildRequires: 		gtk2-devel >= %{gtk2_version}
BuildRequires: 		libmate-devel >= %{libmate_version}
BuildRequires: 		libmateui-devel >= %{libmateui_version}
BuildRequires: 		libmatecomponentui-devel >= %{libmatecomponentui_version}
BuildRequires: 		libmatewnck-devel >= %{libmatewnck_version}
BuildRequires: 		mate-conf-devel >= %{mate_conf_version}
BuildRequires: 		mate-menus-devel >= %{mate_menus_version}
BuildRequires: 		libcairo-devel >= %{cairo_version}
BuildRequires: 		mate-doc-utils >= %{mate_doc_utils_version}
BuildRequires: 		libdbus-glib-devel >= %{dbus_glib_version}
BuildRequires: 		gtk-doc
BuildRequires: 		pango-devel
BuildRequires: 		libmatecomponent-devel
BuildRequires: 		libXau-devel
BuildRequires: 		libXrandr-devel
BuildRequires: 		libpolkit-devel >= 0.92
BuildRequires: 		libmateweather-devel >= %{libmateweather_version}
BuildRequires: 		librsvg-devel
BuildRequires:    	NetworkManager-devel
BuildRequires: 		intltool
BuildRequires: 		gettext-devel
BuildRequires: 		libtool
BuildRequires: 		libcanberra-devel
BuildRequires: 		mate-corba-devel >= %{mate_corba_version}}
BuildRequires:		libdbus-devel >= %{dbus_version}

BuildRequires: 		mate-common
BuildRequires: 		gobject-introspection-devel

Patch0: gnome-panel-vendor.patch
Patch1: gnome-panel-2.10.1-speak-to-us-ye-old-wise-fish.patch
Patch2: gnome-panel-search.patch
Patch3: gnome-panel-about.patch

# the next three patches belong together
# http://bugzilla.gnome.org/show_bug.cgi?id=470966
Patch8: launcher-desktop-files.patch
Patch9: desktop-file-monitoring.patch
Patch10: preferred-apps.patch

# don't pop up an error dialog if an applet from the
# default configuration is missing; we don't want to
# add a hard dependency on e.g. tomboy
Patch11: applet-error.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=520111
Patch24: gnome-panel-2.21.92-allow-spurious-view-done-signals.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=579092
Patch38: clock-network.patch

Patch40: clock-home.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=343436
Patch43: panel-padding.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=537798
Patch47: fix-clock-crash.patch

Patch49: mate-panel_rest_of_fedora_patches.patch
Requires: tzdata

%description
The MATE panel provides the window list, workspace switcher, menus, and other
features for the MATE desktop.

%package libs
Summary: Libraries for Panel Applets
License: LGPLv2+
Group: Development/C

%description libs
This package contains the libpanel-applet library that
is needed by Panel Applets.

%package devel
Summary: 	Headers and libraries for Panel Applet development
License: 	LGPLv2+
Group: 		Development/C
Requires: 	%{name}-libs = %{version}-%{release}

%description devel
Panel Applet development package. Contains files needed for developing
Panel Applets using the libpanel-applet library.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .vendor
#ALT#patch1 -p1 -b .speak-to-us-ye-old-wise-fish
#ALT#patch2 -p1 -b .search
#ALT#patch3 -p1 -b .about
%patch8 -p1 -b .launcher-desktop-files
%patch9 -p1 -b .desktop-file-monitoring
%patch10 -p1 -b .preferred-apps
%patch11 -p1 -b .applet-error
%patch24 -p1 -b .allow-spurious-view-done-signals
%patch38 -p1 -b .clock-network
%patch40 -p1 -b .clock-home
%patch43 -p1 -b .panel-padding
%patch47 -p1 -b .fix-clock-crash
%patch49 -p1 -b .mate-panel_rest_of_fedora_patches.patch

#ALT#cp -f %{SOURCE3} mate-panel/panel-default-setup.entries
cp -f %{SOURCE4} m4
#ALT#cp -f %{SOURCE5} mate-panel/panel-compatibility.schemas
NOCONFIGURE=1 ./autogen.sh


%build

%configure \
	--disable-static \
	--enable-introspection \
	--enable-matecomponent \
	--disable-scrollkeeper \
	--libexecdir=%{_libexecdir}/mate-panel \
	--enable-network-manager

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

make V=1 %{?_smp_mflags}


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

#
# Create pager and tasklist schemas for compatibility with older
# configurations which reference the old schema names
#
sed -e 's|/schemas/apps/window_list_applet/prefs/|/schemas/apps/tasklist_applet/prefs/|' $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas/window-list.schemas > $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas/tasklist.schemas
sed -e 's|/schemas/apps/workspace_switcher_applet/prefs/|/schemas/apps/pager_applet/prefs/|; s|<default>1</default>|<default>2</default>|' $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas/workspace-switcher.schemas > $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas/pager.schemas

## blow away stuff we don't want
rm -rf $RPM_BUILD_ROOT/var/scrollkeeper
rm -f $RPM_BUILD_ROOT%{_libdir}/libmate-panel-applet-2.*a
rm -f $RPM_BUILD_ROOT%{_libdir}/libmate-panel-applet-3.*a


%find_lang %{gettext_package} --all-name

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`

#
# Clear out the old defaults
#
mateconftool-2 --direct --config-source=$MATECONF_CONFIG_SOURCE --recursive-unset /apps/panel > /dev/null || :
mateconftool-2 --direct --config-source=$MATECONF_CONFIG_SOURCE --recursive-unset /schemas/apps/panel > /dev/null || :

#
# Install the schemas
#
mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/clock.schemas \
	%{_sysconfdir}/mateconf/schemas/fish.schemas \
	%{_sysconfdir}/mateconf/schemas/pager.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-compatibility.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-general.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-global.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-object.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-toplevel.schemas \
	%{_sysconfdir}/mateconf/schemas/tasklist.schemas \
	%{_sysconfdir}/mateconf/schemas/window-list.schemas \
	%{_sysconfdir}/mateconf/schemas/workspace-switcher.schemas \
  > /dev/null || :

#
# Install the default setup into /apps/panel and /apps/panel/default_setup
#
mateconftool-2 --direct --config-source=$MATECONF_CONFIG_SOURCE --load %{_sysconfdir}/mateconf/schemas/panel-default-setup.entries > /dev/null || :
mateconftool-2 --direct --config-source=$MATECONF_CONFIG_SOURCE --load %{_sysconfdir}/mateconf/schemas/panel-default-setup.entries /apps/panel > /dev/null || :

: 

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/clock.schemas \
	%{_sysconfdir}/mateconf/schemas/fish.schemas \
	%{_sysconfdir}/mateconf/schemas/pager.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-compatibility.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-general.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-global.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-object.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-toplevel.schemas \
	%{_sysconfdir}/mateconf/schemas/tasklist.schemas \
	%{_sysconfdir}/mateconf/schemas/window-list.schemas \
	%{_sysconfdir}/mateconf/schemas/workspace-switcher.schemas \
  > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/clock.schemas \
	%{_sysconfdir}/mateconf/schemas/fish.schemas \
	%{_sysconfdir}/mateconf/schemas/pager.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-compatibility.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-general.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-global.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-object.schemas \
	%{_sysconfdir}/mateconf/schemas/panel-toplevel.schemas \
	%{_sysconfdir}/mateconf/schemas/tasklist.schemas \
	%{_sysconfdir}/mateconf/schemas/window-list.schemas \
	%{_sysconfdir}/mateconf/schemas/workspace-switcher.schemas \
  > /dev/null || :
fi

%files -f %{gettext_package}.lang
%doc AUTHORS COPYING COPYING.LIB COPYING-DOCS NEWS README
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/mate-panel
%exclude %{_datadir}/mate-panelrc
%{_datadir}/idl/mate-panel-2.0
%{_datadir}/mate-2.0/ui/*.xml
%{_datadir}/man/man*/*
%{_datadir}/applications/mate-panel.desktop
%{_bindir}/mate-panel
%{_bindir}/mate-desktop-item-edit
%{_libexecdir}/mate-panel/*
%{_sysconfdir}/mateconf/schemas/*.schemas
%{_sysconfdir}/mateconf/schemas/*.entries
%{_libdir}/mate-panel
%{_libdir}/girepository-1.0/MatePanelApplet-3.0.typelib
%{_datadir}/mate/help/*
%{_datadir}/omf/*
%{_datadir}/dbus-1/services/org.mate.panel.applet.ClockAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.FishAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.NotificationAreaAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.WnckletFactory.service

%files libs
%{_libdir}/*.so.*

%files devel
%{_bindir}/mate-panel-test-applets
%{_bindir}/panel-test-applets-matecomponent
%{_libdir}/pkgconfig/*
%{_includedir}/mate-panel-3.0/libmate-panel-applet/*
%{_includedir}/panel-2.0
%{_libdir}/*.so
%{_datadir}/gtk-doc
%{_datadir}/gir-1.0/MatePanelApplet-3.0.gir


%changelog
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

