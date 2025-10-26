%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.suzie97.communique

Name: communique
Version: 1.2.0
Release: alt1

Summary: Featureful RSS Reader for elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/ellie-commons/communique

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gumbo)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(rest-0.7)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: vapi(granite)

%description
%summary

Subscribe to and read RSS/Atom feeds with cross-platform synchronization.
Communique is a feed reader with support for a lot of RSS services,
like Feedbin, Tiny Tiny RSS, Nextcloud News etc. And ofcourse, you can
use Communique to subscribe to and read RSS feeds locally, without
logging in to anything.

%prep
%setup
# we have no net in hasher!
sed -i "s|plugin_test])|plugin_test], should_fail: true)|" plugins/backend/feedbin/meson.build
sed -i "s|plugin_test)|plugin_test, should_fail: true)|" plugins/backend/feedbin/meson.build

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc COPYING FUZZ_TESTING.md README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_iconsdir/hicolor/scalable/apps/%{appname}-symbolic.svg
%dir %_libdir/%appname
%_libdir/%appname/*
%_libdir/libFeedReader.so
%dir %_datadir/%appname
%_datadir/%appname/*
%_datadir/glib-2.0/schemas/%{appname}*.gschema.xml
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
