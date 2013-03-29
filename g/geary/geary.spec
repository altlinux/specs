Name: geary
Version: 0.3.0
Release: alt1

Summary: Email client
License: LGPLv2.1+
Group: Networking/Mail
Url: http://www.yorba.org/projects/geary/

Source0: %name-%version.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Fri Mar 29 2013
# optimized out: at-spi2-atk cmake cmake-modules fontconfig fontconfig-devel glib2-devel gobject-introspection-devel libat-spi2-core libatk-devel libatk-gir-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libdbus-glib libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-gir-devel libgio-devel libgnome-keyring libgpg-error libgst-plugins1.0 libgtk+3-devel libjavascriptcoregtk3-devel libpango-devel libpango-gir-devel libsoup-devel libwayland-client libwayland-server perl-Encode pkg-config xz
BuildRequires: ctest intltool libcanberra-devel libcanberra-vala libfreetype-devel libgee-devel libgmime-devel libgnome-keyring-devel libgtk+3-gir-devel libjavascriptcoregtk3-gir-devel libnotify-devel libsoup-gir-devel libsqlite3-devel libunique3-devel libwebkitgtk3-devel vala

%description
Geary is an email client built for the GNOME desktop environment.  It
allows you to read and send email with a simple, modern interface.

Visit http://www.yorba.org to read about the current state of.
Geary's development.

%prep
%setup -q

%build
./configure --prefix=%_prefix
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS MAINTAINERS NEWS README THANKS
%_bindir/*
%dir %_datadir/geary
%_datadir/geary/
%_desktopdir/geary.desktop
%_datadir/glib-2.0/schemas/org.yorba.geary.gschema.xml
%dir %_datadir/gnome/help/geary/C
%_datadir/gnome/help/geary/C/
%_iconsdir/*/*/apps/*

%changelog
* Fri Mar 29 2013 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

