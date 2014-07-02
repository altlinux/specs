%define ver_major 0.6

Name: geary
Version: %ver_major.1
Release: alt1

Summary: Email client
License: LGPLv2.1+
Group: Networking/Mail
Url: https://wiki.gnome.org/Apps/Geary

Source: ftp://ftp.gnome.org/pub/sources/%name/%ver_major/%name-%version.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

%define vala_ver 0.22.1
%define gtk_ver 3.6.0
%define sqlite_ver 3.7.4

BuildPreReq: vala-tools >= %vala_ver libvala-devel
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libsqlite3-devel >= %sqlite_ver
BuildRequires: cmake intltool desktop-file-utils gnome-doc-utils
BuildRequires: libnotify-devel libcanberra-devel libgee0.8-devel
BuildRequires: libgmime-devel libgnome-keyring-devel libexpat-devel
BuildRequires: libpixman-devel libharfbuzz-devel libwebkitgtk3-devel
BuildRequires: libpng-devel libsecret-devel at-spi2-atk-devel libxml2-devel
BuildRequires: libXdmcp-devel libXdamage-devel libxshmfence-devel
BuildRequires: libXxf86vm-devel libXinerama-devel libXrandr-devel libXi-devel
BuildRequires: libXcursor-devel libXcomposite-devel libxkbcommon-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libsoup-gir-devel libwebkitgtk3-gir-devel libcanberra-vala

# TODO:
# -- Unity indicate support: OFF
# -- Unity messaging menu support: OFF
# -- Unity launcher support: OFF
# -- Reference tracking: OFF

%description
Geary is an email client built for the GNOME desktop environment.  It
allows you to read and send email with a simple, modern interface.

Visit http://www.yorba.org to read about the current state of.
Geary's development.

%prep
%setup

%build
%cmake
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS MAINTAINERS NEWS README THANKS
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.yorba.%name.gschema.xml
%_iconsdir/*/*/apps/*
%_datadir/appdata/%name.appdata.xml

%changelog
* Wed Jul 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Mar 03 2014 Igor Zubkov <icesik@altlinux.org> 0.4.3-alt1
- 0.4.3

* Sat Nov 23 2013 Igor Zubkov <icesik@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.4.1-alt1
- 0.4.1 trunk (r1119)

* Mon Aug 26 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt3
- Cleanup build requires

* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt2
- Fix desktop file

* Sat Apr 13 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Fri Mar 29 2013 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

