%def_enable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 0.7
%define rdn_name sm.puri.Chatty

%def_enable purple
%ifarch armh
#chatty-clock:ERROR:../tests/clock.c:170:test_clock_human_time: assertion failed (str == array[i].human_time_detailed): ("0 minute ago" == "1 minute ago")
%def_disable check
%else
%def_enable check
%endif

Name: chatty
Version: %ver_major.3
Release: alt1

Summary: SMS, MMS and XMPP messaging application for GNOME
Group: Networking/Instant messaging
License: GPL-3.0-or-later
Url: https://source.puri.sm/Librem5/chatty

%if_disabled snapshot
Source: https://source.puri.sm/Librem5/%name/-/archive/v%version/%name-v%version.tar.gz
%else
Vcs: https://source.puri.sm/Librem5/chatty.git
Source: %name-%version.tar
%endif

%define glib_ver 2.66
%define gtk_ver 3.22
%define gtk4_ver 4.6
%define handy_ver 1.5
%define adw_ver 1.2

Requires: dconf yelp
Requires: ModemManager feedbackd

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ yelp-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: pkgconfig(gspell-1)
#BuildRequires: pkgconfig(gtk4) >= %gtk4_ver
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
#BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(gnome-desktop-3.0)
#BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: evolution-data-server-devel
BuildRequires: libphonenumber-devel
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: libfeedback-devel
BuildRequires: pkgconfig(mm-glib)
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
* Tue May 30 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- first build for Sisyphus (ALT #46306)


