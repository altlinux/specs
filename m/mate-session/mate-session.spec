# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/mateconftool-2 /usr/bin/xmlto /usr/bin/xsltproc libICE-devel libSM-devel libXext-devel libwrap-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(ice) pkgconfig(sm) pkgconfig(xext) pkgconfig(xrender)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define gtk_version 2.20
%define dbus_glib_version 0.70
%define dbus_version 0.90
%define mate_keyring_version 1.1.0
%define mate_conf_version 1.1.0
%define libmatenotify_version 1.1.0

#different version for fc17

Summary: 	MATE session manager
Name: 		mate-session
Version: 	1.4.0
Release: 	alt2_5.1
URL: 		http://pub.mate-desktop.org
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 	GPLv2+
Group: 		Graphical desktop/Other

# required to get mateconf-sanity-check-2 in the right place
Requires: mate-conf-gtk >= %{mate_conf_version}
# Needed for mate-settings-daemon
Requires: mate-control-center

# pull in dbus-x11, see bug 209924
Requires: dbus-tools-gui
# we need an authentication agent in the session
Requires: mate-polkit
# and we want good defaults
Requires: polkit
# for fc17
Requires: ConsoleKit
Requires: ConsoleKit-x11

BuildRequires: gtk2-devel >= %{gtk_version}
BuildRequires: libdbus-devel >= %{dbus_version}
BuildRequires: libdbus-glib-devel >= %{dbus_glib_version}
BuildRequires: mate-keyring-devel >= %{mate_keyring_version}
BuildRequires: libmatenotify-devel >= %{libmatenotify_version}
BuildRequires: mate-conf-devel >= %{mate_conf_version}
BuildRequires: mate-conf-gtk >= %{mate_conf_version}
BuildRequires: pango-devel
BuildRequires: mate-settings-daemon-devel
BuildRequires: desktop-file-utils
BuildRequires: libXau-devel
BuildRequires: libXrandr-devel
BuildRequires: xorg-xtrans-devel

# this is so the configure checks find /usr/bin/halt etc.
BuildRequires: consolehelper

BuildRequires: intltool
BuildRequires: libX11-devel libXt-devel
BuildRequires: libXtst-devel
BuildRequires: xmlto
BuildRequires: libupower-devel
BuildRequires: mate-common
#only for bad mate-common from fedora
BuildRequires: 	libtool

# for patch3
BuildRequires: libmatenotify-devel

Requires(pre): mate-conf >= %{mate_conf_version}
Requires(post): mate-conf >= %{mate_conf_version}
Requires(preun): mate-conf >= %{mate_conf_version}

# https://bugzilla.gnome.org/show_bug.cgi?id=597030
Patch3: 0001-Add-ability-to-perform-actions-after-a-period-of-idl.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=607094
Patch4: nag-root-user.patch

Patch7: gnome-session-cflags.patch
Source44: import.info
Provides: mate-session-manager = %version-%release
Patch33: gnome-session-2.31.6-alt-autosave_session.patch
Patch34: mate-session-g_debug.patch
Source45: MATE64.png

%description
mate-session manages a MATE desktop or GDM / MDM login session. It starts up
the other core MATE components and handles logout and saving the session.

%package xsession
Summary: mate-session desktop file
Group: Graphical desktop/Other
Requires: mate-session = %{version}-%{release}

%description xsession
Desktop file to add MATE to display manager session menu.

%prep
%setup -q
%patch3 -p1 -b .max-idle
%patch4 -p1 -b .nag-root-user
%patch7 -p1 -b .cflags
NOCONFIGURE=1 ./autogen.sh
%patch33 -p0
%patch34 -p1

%build

%configure \
    --disable-static \
	--with-default-wm=marco \
	--enable-ipv6 \

make %{?_smp_mflags}

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

mkdir -p $RPM_BUILD_ROOT%{_datadir}/mate/autostart

cp AUTHORS COPYING NEWS README $RPM_BUILD_ROOT%{_datadir}/doc/mate-session

%find_lang mate-session --all-name

cat <<__START_MATE__ >startmate
#!/bin/sh

# turn on fonts antialiasing
export GDK_USE_XFT=1

# TODO
# set default browser to whatever MATE user likes
#export BROWSER=mate-open

# tell restored browsers where plugins are
export MOZ_PLUGIN_PATH="\${MOZ_PLUGIN_PATH:+"\$MOZ_PLUGIN_PATH:"}\${HOME:+"\$HOME/.mozilla/plugins:"}%_libdir/mozilla/plugins:%_libdir/netscape/plugins:%browser_plugins_path"

# TODO
# export HELP_BROWSER=yelp

# use prefixed .menu files
#export XDG_MENU_PREFIX="mate-"

#### use /usr/share/mate as a part of XDG_DATA_DIRS
#### export XDG_DATA_DIRS="\${XDG_DATA_DIRS:+"\$XDG_DATA_DIRS:"}%_datadir/mate"

# Since shared-mime-info-0.90-alt3 XDG_DATA_DIRS not exported. We need to define
# the set of base directories explicitly.

export XDG_DATA_DIRS="%_datadir/mate:%_datadir:/usr/local/share"

exec %_bindir/mate-session "\$@"
__START_MATE__

install -pD -m755 startmate %buildroot%_bindir/startmate

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d/
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/02Mate
NAME=Mate
ICON=%_iconsdir/hicolor/64x64/apps/mate.png
DESC=Mate (Gnome 2) Environment
EXEC=%_bindir/startmate
SCRIPT:
exec %_bindir/startmate
__EOF__

install -pD -m644 %SOURCE45 %buildroot%_iconsdir/hicolor/64x64/apps/mate.png


%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule %{_sysconfdir}/mateconf/schemas/mate-session.schemas >& /dev/null || :
#for fc17

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/mate-session.schemas >& /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/mate-session.schemas >& /dev/null || :
fi

%files xsession
%{_datadir}/xsessions/*

%files -f mate-session.lang
%doc %dir %{_datadir}/doc/mate-session
%doc %{_datadir}/doc/mate-session/AUTHORS
%doc %{_datadir}/doc/mate-session/COPYING
%doc %{_datadir}/doc/mate-session/NEWS
%doc %{_datadir}/doc/mate-session/README
%doc %dir %{_datadir}/doc/mate-session/dbus
%doc %{_datadir}/doc/mate-session/dbus/*
%doc %{_mandir}/man*/*
%{_datadir}/applications/mate-session-properties.desktop
%dir %{_datadir}/mate-session
%{_datadir}/mate/autostart
%{_bindir}/*
%{_sysconfdir}/mateconf/schemas/*.schemas
%{_datadir}/mate-session/gsm-inhibit-dialog.ui
%{_datadir}/mate-session/session-properties.ui
%{_datadir}/icons/hicolor/*/apps/mate-session-properties.png
%{_datadir}/icons/hicolor/scalable/apps/mate-session-properties.svg

%_bindir/*
%_iconsdir/hicolor/64x64/apps/mate.png
%config %_sysconfdir/X11/wmsession.d/*Mate*
#exclude %_datadir/xsessions/mate.desktop
#exclude %_bindir/mate-wm



%changelog
* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_5.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_5
- adapted alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_5
- new release

* Wed May 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

