Name: gradio
Version: 5.0
Release: alt1
Summary: GTK3 app for finding and listening to internet radio stations
License: GPL-3.0+
Group: Sound
Url: https://github.com/haecker-felix/gradio
Source: %name-%version.tar
# Automatically added by buildreq on Thu Mar 16 2017
# optimized out: at-spi2-atk fontconfig glib2-devel gstreamer1.0-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgst-plugins1.0 libjson-glib libpango-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server perl perl-Encode perl-XML-Parser pkg-config python-base python-modules vala xml-utils
BuildRequires: gst-plugins1.0-devel intltool libgtk+3-devel libjson-glib-devel libsoup-devel

%description
Gradio is a native GTK application. It lets you browse, search and find radio
stations, as well as listen to them, without needing to use a browser or enter
an internet radio stream URL. The application uses the Community Radio Browser
website for its database backend.

%prep
%setup

%build
%define _configure_script ./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md COPYING
%_bindir/gradio
%_desktopdir/de.haeckerfelix.gradio.desktop
%_datadir/gradio/
%_iconsdir/hicolor/*/apps/de.haeckerfelix.gradio.png
%_iconsdir/hicolor/scalable/categories/*.svg
%_datadir/icons/hicolor/symbolic/apps/de.haeckerfelix.gradio-symbolic.svg
%_datadir/glib-2.0/schemas/de.haecker-felix.gradio.gschema.xml

%changelog
* Thu Mar 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.0-alt1
- first build for ALT Linux
