Name: geary
Version: 0.3.1
Release: alt3

Summary: Email client
License: LGPLv2.1+
Group: Networking/Mail
Url: http://www.yorba.org/projects/geary/

Source0: %name-%version.tar.xz

Patch0: geary-0.3.1-alt-desktop-file.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake intltool vala glib2-devel libgio-devel
BuildRequires: libgtk+3-devel libgee-devel libunique3-devel
BuildRequires: libnotify-devel libcanberra-devel libsqlite3-devel
BuildRequires: libgmime-devel libgnome-keyring-devel
BuildRequires: libwebkitgtk3-devel libpixman-devel libXdmcp-devel
BuildRequires: libXdamage-devel libXxf86vm-devel libharfbuzz-devel
BuildRequires: libpng-devel libXinerama-devel libXi-devel
BuildRequires: libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: libxkbcommon-devel libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel libxml2-devel libcanberra-vala
BuildRequires: gobject-introspection-devel libatk-gir-devel
BuildRequires: libgtk+3-gir-devel libgdk-pixbuf-gir-devel
BuildRequires: libjavascriptcoregtk3-gir-devel libpango-gir-devel
BuildRequires: libsoup-gir-devel 

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
%setup -q
%patch0 -p1

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
* Mon Aug 26 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt3
- Cleanup build requires

* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt2
- Fix desktop file

* Sat Apr 13 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Fri Mar 29 2013 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

