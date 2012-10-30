# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/mateconftool-2 /usr/bin/update-mime-database libICE-devel libSM-devel libX11-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libebook-1.2) pkgconfig(pango) pkgconfig(xft) pkgconfig(xi) xorg-kbproto-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define gettext_package mate-control-center-2.0

%define glib2_version 2.13.0
%define gtk2_version 2.21
%define mate_conf_version 1.1.0
%define mate_desktop_version 1.1.0
%define desktop_file_utils_version 0.9
%define xft_version 2.1.7
%define fontconfig_version 1.0.0
%define redhat_menus_version 0.50
%define marco_version 1.1.0
%define libxklavier_version 4.0
%define mate_menus_version 1.1.1
%define usermode_version 1.83
%define libmatekbd_version 1.1.0
%define libXrandr_version 1.2.99

Summary: 	Utilities to configure the Mate desktop
Name: 		mate-control-center
Version: 	1.4.0
Release: 	alt2_1.1
License: 	GPLv2+ and GFDL
Group: 		Graphical desktop/Other
Source: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
URL: 		http://pub.mate-desktop.org

Requires: mate-settings-daemon >= 1.1.0
Requires: altlinux-freedesktop-menu-common >= %{redhat_menus_version}
Requires: mate-icon-theme
Requires: libalsa
Requires: mate-menus >= %{mate_menus_version}
Requires: mate-desktop >= %{mate_desktop_version}
Requires: dbus-tools-gui
Requires: mate-control-center-filesystem = %{version}-%{release}
# we need XRRGetScreenResourcesCurrent
Requires: libXrandr >= %{libXrandr_version}

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: librsvg-devel
BuildRequires: mate-conf-devel >= %{mate_conf_version}
BuildRequires: mate-desktop-devel >= %{mate_desktop_version}
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: libxklavier-devel >= %{libxklavier_version}
BuildRequires: libXcursor-devel
BuildRequires: libXrandr-devel >= %{libXrandr_version}
BuildRequires: gettext
BuildRequires: mate-menus-devel >= %{mate_menus_version}
BuildRequires: libmatekbd-devel >= %{libmatekbd_version}
BuildRequires: mate-settings-daemon-devel
BuildRequires: intltool >= 0.37.1
BuildRequires: libXxf86misc-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: mate-doc-utils
BuildRequires: libglade2-devel
BuildRequires: libxml2-devel
BuildRequires: libdbus-devel >= 0.90
BuildRequires: libdbus-glib-devel >= 0.70
BuildRequires: scrollkeeper
BuildRequires: libcanberra-devel
BuildRequires: libunique-devel
BuildRequires: mate-window-manager-devel
BuildRequires: mate-common

Requires(preun): mate-conf
Requires(pre): mate-conf
Requires(post): mate-conf
Requires(post): desktop-file-utils >= %{desktop_file_utils_version}
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils >= %{desktop_file_utils_version}
Requires(postun): shared-mime-info

Provides: mate-control-center-extra = %{version}-%{release}
Patch33: gnome-control-center-2.22.1-alt-background-location.patch
Patch34: gnome-control-center-2.28.0-passwd.patch

%description
This package contains configuration utilities for the MATE desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.

%package devel
Summary: Development files for the MATE control-center
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
Th control-center package contains configuration utilities for the
MATE desktop.

This package contains libraries and header files needed for integrating
configuration of applications such as window managers with the control-center
utilities.

%package filesystem
Summary: MATE Control Center directories
Group: Development/C
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package an MUST not depend on the main package

%description filesystem
The MATE control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.


%prep
%setup -q -n mate-control-center-%{version}

NOCONFIGURE=1 ./autogen.sh
%patch33 -p1
%patch34 -p1

%build

%configure \
	--disable-scrollkeeper    \
    --disable-static \
    --disable-update-mimedb

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

make %{?_smp_mflags}

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

for i in apps_mate_settings_daemon_default_editor.schemas		\
	    apps_mate_settings_daemon_keybindings.schemas		\
	    apps_mate_settings_daemon_screensaver.schemas		\
	    desktop_mate_font_rendering.schemas ; do			\
	    rm -f $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas/$i ;	\
done

# we do want this
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mate/wm-properties

# we don't want these
#rm -rf $RPM_BUILD_ROOT%{_datadir}/mate/autostart
#rm -rf $RPM_BUILD_ROOT%{_datadir}/mate/cursor-fonts
rm $RPM_BUILD_ROOT%{_datadir}/applications/mimeinfo.cache

# remove useless libtool archive files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} \;

%find_lang %{gettext_package} --all-name

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/fontilus.schemas \
	%{_sysconfdir}/mateconf/schemas/mate-control-center.schemas \
	%{_sysconfdir}/mateconf/schemas/control-center.schemas \
	> /dev/null || :


%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/fontilus.schemas \
	%{_sysconfdir}/mateconf/schemas/mate-control-center.schemas \
	%{_sysconfdir}/mateconf/schemas/control-center.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/fontilus.schemas \
	%{_sysconfdir}/mateconf/schemas/mate-control-center.schemas \
	%{_sysconfdir}/mateconf/schemas/control-center.schemas \
	> /dev/null || :
fi


%files -f %{gettext_package}.lang
%doc AUTHORS COPYING NEWS README
%{_datadir}/mate-control-center/keybindings/*.xml
%{_datadir}/mate-control-center/ui
%{_datadir}/mate-control-center/pixmaps
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/polkit-1/actions/*
%{_datadir}/pkgconfig/mate-keybindings.pc
%{_datadir}/pkgconfig/mate-default-applications.pc
# list all binaries explicitly, so we notice if one goes missing
%{_bindir}/mate-at-mobility
%{_bindir}/mate-at-visual
%{_bindir}/mate-control-center
%{_bindir}/mate-typing-monitor
%{_bindir}/mate-font-viewer
%{_bindir}/mate-thumbnail-font
%{_bindir}/mate-appearance-properties
%{_bindir}/mate-at-properties
%{_bindir}/mate-default-applications-properties
%{_bindir}/mate-display-properties
%{_bindir}/mate-keybinding-properties
%{_bindir}/mate-keyboard-properties
%{_bindir}/mate-mouse-properties
%{_bindir}/mate-network-properties
%{_bindir}/mate-window-properties
%{_libdir}/*.so.*
%{_sysconfdir}/mateconf/schemas/control-center.schemas
%{_sysconfdir}/mateconf/schemas/mate-control-center.schemas
%{_sysconfdir}/mateconf/schemas/fontilus.schemas
%{_sysconfdir}/xdg/menus/matecc.menu
%{_sysconfdir}/xdg/autostart/mate-at-session.desktop
%{_libdir}/window-manager-settings
%{_sbindir}/mate-display-properties-install-systemwide
%{_datadir}/mime/packages/mate-theme-package.xml
%{_datadir}/mate/cursor-fonts/*
%{_datadir}/mate/help/mate-control-center/*/*.xml
%{_datadir}/omf/mate-control-center/*.omf

%files devel
%{_includedir}/mate-window-settings-2.0
%{_libdir}/libmate-window-settings.so
%{_libdir}/pkgconfig/*

%files filesystem
%dir %{_datadir}/mate/wm-properties
%dir %{_datadir}/mate-control-center
%dir %{_datadir}/mate-control-center/keybindings


%changelog
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

