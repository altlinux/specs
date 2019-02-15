Name: gradio
Version: 7.2
Release: alt1
Summary: GTK3 app for finding and listening to internet radio stations
License: GPL-3.0+
Group: Sound
Url: https://github.com/haecker-felix/gradio
Source: %name-%version.tar
# Automatically added by buildreq on Thu Mar 16 2017
# optimized out: at-spi2-atk fontconfig glib2-devel gstreamer1.0-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgst-plugins1.0 libjson-glib libpango-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server perl perl-Encode perl-XML-Parser pkg-config python-base python-modules vala xml-utils
BuildRequires(Pre): meson
BuildRequires: libsqlite3-devel gst-plugins1.0-devel intltool libgtk+3-devel libjson-glib-devel libsoup-devel

%description
Gradio is a native GTK application. It lets you browse, search and find radio
stations, as well as listen to them, without needing to use a browser or enter
an internet radio stream URL. The application uses the Community Radio Browser
website for its database backend.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/gradio
%_datadir/appdata/de.haeckerfelix.gradio.appdata.xml
%_datadir/dbus-1/services/de.haeckerfelix.gradio.service
%_datadir/glib-2.0/schemas/de.haeckerfelix.gradio.gschema.xml
%_datadir/gnome-shell/search-providers/de.haeckerfelix.gradio.search-provider.ini
%_datadir/locale/cs/LC_MESSAGES/gradio.mo
%_datadir/locale/de/LC_MESSAGES/gradio.mo
%_datadir/locale/es/LC_MESSAGES/gradio.mo
%_datadir/locale/fr/LC_MESSAGES/gradio.mo
%_datadir/locale/hr/LC_MESSAGES/gradio.mo
%_datadir/locale/it/LC_MESSAGES/gradio.mo
%_datadir/locale/ka/LC_MESSAGES/gradio.mo
%_datadir/locale/nb/LC_MESSAGES/gradio.mo
%_datadir/locale/nl/LC_MESSAGES/gradio.mo
%_datadir/locale/pl/LC_MESSAGES/gradio.mo
%_datadir/locale/pt_BR/LC_MESSAGES/gradio.mo
%_datadir/locale/sk/LC_MESSAGES/gradio.mo
%_datadir/locale/sr/LC_MESSAGES/gradio.mo
%_datadir/locale/sr@latin/LC_MESSAGES/gradio.mo
%_datadir/locale/sv/LC_MESSAGES/gradio.mo
%_datadir/locale/tr/LC_MESSAGES/gradio.mo
%_desktopdir/de.haeckerfelix.gradio.desktop
%_iconsdir/hicolor/16x16/apps/de.haeckerfelix.gradio.png
%_iconsdir/hicolor/24x24/apps/de.haeckerfelix.gradio.png
%_iconsdir/hicolor/256x256/apps/de.haeckerfelix.gradio.png
%_iconsdir/hicolor/32x32/apps/de.haeckerfelix.gradio.png
%_iconsdir/hicolor/48x48/apps/de.haeckerfelix.gradio.png
%_iconsdir/hicolor/512x512/apps/de.haeckerfelix.gradio.png
%_iconsdir/hicolor/scalable/apps/de.haeckerfelix.gradio.svg
%_iconsdir/hicolor/symbolic/apps/de.haeckerfelix.gradio-symbolic.svg

%changelog
* Fri Feb 15 2019 Grigory Ustinov <grenka@altlinux.org> 7.2-alt1
- Build new version.

* Mon Jul 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 7.1-alt1
- new version 7.1

* Thu Mar 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.0-alt1
- first build for ALT Linux
