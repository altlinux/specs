Name: corebird
Version: 1.4.2
Release: alt1.1

Summary: Native Gtk+ Twitter client for the Linux desktop

License: GPLv3
Group: Networking/Instant messaging
URL: http://corebird.baedert.org

Packager: Sergey Irupin <lamp@altlinux.org>
Source: %name-%version.tar

BuildRequires: vala pkgconfig(gtk+-3.0) pkgconfig(glib-2.0) pkgconfig(rest-0.7) pkgconfig(libsoup-2.4) pkgconfig(json-glib-1.0) pkgconfig(sqlite3) pkgconfig(gstreamer-video-1.0) pkgconfig(gspell-1)

%description
Native Gtk+ Twitter client for the Linux desktop

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc COPYING
%_bindir/%name
%_man1dir/%name.*
%_desktopdir/org.baedert.corebird.desktop
%_iconsdir/*/*/apps/corebird.png
%_datadir/appdata/org.baedert.corebird.appdata.xml
%_datadir/dbus-1/services/org.baedert.corebird.service
%_datadir/glib-2.0/schemas/org.baedert.corebird.gschema.xml

%changelog
* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1.1
- rebuilt against libgspell-1.so.2

* Mon Mar 20 2017 Sergey Iryupin <lamp@altlinux.org> 1.4.2-alt1
- Initial build
