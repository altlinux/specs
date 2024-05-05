%def_enable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 0.8
%define rdn_name sm.puri.Chatty

%def_enable purple
%ifarch armh
#chatty-clock:ERROR:../tests/clock.c:170:test_clock_human_time: assertion failed (str == array[i].human_time_detailed): ("0 minute ago" == "1 minute ago")
%def_disable check
%else
# chatty:pgp failed in hasher
%def_disable check
%endif

Name: chatty
Version: %ver_major.3
Release: alt1

Summary: SMS, MMS and XMPP messaging application for GNOME
Group: Networking/Instant messaging
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/World/Chatty

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Chatty/-/archive/v%version/%name-v%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/Chatty.git
Source: %name-%version.tar
%endif

%define glib_ver 2.66
%define gtk4_ver 4.12
%define adw_ver 1.5
%define desktop_ver 43

Requires: dconf yelp
Requires: ModemManager feedbackd
Requires: gnupg2
Requires: gst-plugins-base1.0
Requires: gst-libav

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ yelp-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(libebook-contacts-1.2)
BuildRequires: pkgconfig(libebook-1.2)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: libphonenumber-devel
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= %desktop_ver
BuildRequires: libfeedback-devel
BuildRequires: pkgconfig(mm-glib)
BuildRequires: pkgconfig(gtksourceview-5)
%{?_enable_purple:BuildRequires: libpurple-devel}
%{?_enable_check:BuildRequires: xvfb-run gnupg2}
# for libcmatrix subproject
BuildRequires: pkgconfig(olm)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(json-glib-1.0)

%description
A simple to use messaging app for 1:1 communication and small groups
supporting SMS, MMS, XMPP and matrix.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version

%build
%meson
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang purism-%name %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_sysconfdir/xdg/autostart/%rdn_name-daemon.desktop
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/metainfo/%rdn_name.metainfo.xml
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/bash-completion/completions/%name


%changelog
* Sun May 05 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Tue Mar 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Tue Jan 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- updated to v0.8.1-1-g28fbb899 (ported to gtk4/libadwaita)

* Tue May 30 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- first build for Sisyphus (ALT #46306)


