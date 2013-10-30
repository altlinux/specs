%define ver_major 2.0
%define _libexecdir %_prefix/libexec
%def_enable systemd
%define _name cinnamon

Name: %{_name}-session
Version: %ver_major.3
Release: alt1

Summary: The cinnamon session programs for the Cinnamon GUI desktop environment
License: GPLv2+
Group: Graphical desktop/GNOME
URL: https://github.com/linuxmint/cinnamon-session
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar
Source1: %{_name}.session
Source2: %{_name}2d.session
Source3: start%{_name}-common
Source4: start%{_name}
Source5: start%{_name}2d
Source6: 02Cinnamon
Source7: 02Cinnamon2D

# From configure.in
%define glib_ver 2.33.4
%define gtk_ver 3.0.0
%define dbus_glib_ver 0.76
%define polkit_ver 0.91
%define upower_ver 0.9
%define systemd_ver 40

PreReq: xinitrc libcanberra-gnome libcanberra-gtk3
Requires: altlinux-freedesktop-menu-cinnamon
Requires: gstreamer dbus-tools-gui
Requires: gnome-filesystem
Requires: cinnamon-settings-daemon
Requires: nemo
Requires: upower polkit-gnome gcr

Requires: icon-theme-hicolor gnome-icon-theme-symbolic gnome-themes-standard

BuildPreReq: rpm-build-gnome >= 0.5
BuildPreReq: gnome-common

# From configure.in
BuildPreReq: intltool >= 0.35.0 libGConf-devel
BuildPreReq: libgio-devel glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libdbus-glib-devel >= %dbus_glib_ver
BuildPreReq: libupower-devel >= %upower_ver
BuildRequires: libpangox-compat-devel librsvg-devel libjson-glib-devel
BuildRequires: libX11-devel libXau-devel libXrandr-devel libXrender-devel libXt-devel
BuildRequires: libSM-devel libXext-devel libXtst-devel libXi-devel libXcomposite-devel libGL-devel
BuildRequires: GConf browser-plugins-npapi-devel perl-XML-Parser xorg-xtrans-devel
BuildRequires: libcinnamon-desktop-devel
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel libsystemd-daemon-devel libpolkit-devel}

%description
Cinnamon is a Linux desktop which provides advanced innovative features
and a traditional user experience. The desktop layout is similar to Gnome 2.
The underlying technology is forked from Gnome Shell. The emphasis is put on
making users feel at home and providing them with an easy to use and comfortable 
desktop experience.

This package provides the Cinnamon session manager.

%prep
%setup -q

[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure PATH=$PATH:/sbin \
    %{subst_enable systemd} \
    --enable-ipv6 \
    --disable-schemas-compile

%make_build

%install
%make_install install DESTDIR=%buildroot

install -pD -m655 %SOURCE1 %buildroot%_datadir/%name/sessions/%{_name}.session
install -pD -m655 %SOURCE2 %buildroot%_datadir/%name/sessions/%{_name}2d.session
install -pD -m755 %SOURCE3 %buildroot%_datadir/%name/start%{_name}-common
install -pD -m755 %SOURCE4 %buildroot%_bindir/start%{_name}
install -pD -m755 %SOURCE5 %buildroot%_bindir/start%{_name}2d

mkdir -p %buildroot%_x11sysconfdir/wmsession.d
install -pD -m655 %SOURCE6 %buildroot%_x11sysconfdir/wmsession.d
install -pD -m655 %SOURCE7 %buildroot%_x11sysconfdir/wmsession.d

rm -f %buildroot%_docdir/%name/dbus/cinnamon-session.html

%find_lang --with-gnome --output=%name.lang %name-3.0

%check
%make check

%files -f %name.lang
%_bindir/*
%_libexecdir/cinnamon-session-check-accelerated
%_libexecdir/cinnamon-session-check-accelerated-helper
%_desktopdir/*.desktop
%dir %_datadir/%name
%_datadir/%name/*.glade
%_datadir/%name/hardware-compatibility
%_datadir/%name/start%{_name}-common
%dir %_datadir/%name/sessions
%_datadir/%name/sessions/%{_name}.session
%_datadir/%name/sessions/%{_name}2d.session
%_iconsdir/hicolor/*/apps/cinnamon-session-properties.*
%config %_datadir/glib-2.0/schemas/org.cinnamon.SessionManager.gschema.xml
%_mandir/man?/*
%_x11sysconfdir/wmsession.d/*
%doc AUTHORS NEWS README

%changelog
* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt2
- add nemo and fallback-mount-helper as required components

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt3
- rebuild for GNOME-3.10

* Thu Sep 5 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt2
- load cinnamon-settings-daemon2d.desktop in 2d session

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- git20130824
- bump version

* Fri Aug 2 2013 Vladimir Didenko <cow@altlinux.org> 0.0.1-alt1
- Initial build - git20130723
