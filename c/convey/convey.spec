%global _unpackaged_files_terminate_build 1
%define xdg_name net.donnybeelo.Convey
%def_with check

Name: convey
Version: 50.2
Release: alt1
Summary: Email application built around conversations
License: LGPL-2.1-or-later
Group: Networking/Mail
URL: https://gitlab.gnome.org/donnybeelo/convey
VCS: https://gitlab.gnome.org/donnybeelo/convey

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: appstream
BuildRequires: desktop-file-utils
BuildRequires: gcr4-libs-vala
BuildRequires: gobject-introspection-devel
BuildRequires: libfolks-vala
BuildRequires: libgtk4-gir-devel
BuildRequires: libstemmer-devel
BuildRequires: libwebkitgtk6.0-gir-devel
BuildRequires: pkgconfig(enchant-2)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(gcr-4)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmime-3.0)
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(gstreamer-play-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(libunwind)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libytnef)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: vala-tools
BuildRequires: yelp-tools

%description
Convey is an email application built around conversations,
for the GNOME desktop. It allows you to read, find and
send email with a straight-forward, modern interface.
Convey is a hard fork of Geary, and is not affiliated
with or endorsed by the GNOME Foundation.

%prep
%setup

%build
%add_optflags -I%_includedir/libytnef
%meson -Dprofile=release -Dstrip=true
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test \
		vala-unit:tests \
		desktop-file-validate \
		%xdg_name.metainfo.xml-validate \
		engine-tests

%files -f %name.lang
%_bindir/%name
%_libdir/%name
%_datadir/%name
%_desktopdir/%xdg_name.desktop
%_desktopdir/%name-autostart.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Sat Sep 26 2026 Alexander Makeenkov <amakeenk@altlinux.org> 50.2-alt1
- Initial build for ALT.
