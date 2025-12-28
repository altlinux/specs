%define _unpackaged_files_terminate_build 1

%define appname com.github.akiraux.akira

%def_with check

Name: akira
Version: 0.0.16
Release: alt1

Summary: Native Linux App for UI and UX Design built in Vala and GTK
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/akiraux/Akira

Source: %name-%version.tar

# sync with version 0.0.16-2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(goocanvas-2.0)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: vapi(granite)

Requires: elementary-icon-theme

%if_with check
BuildRequires: /usr/bin/xvfb-run
%endif

%description
Akira is a native Linux Design application built in Vala and GTK.
Akira focuses on offering a modern and fast approach to UI and
UX Design, mainly targeting web designers and graphic designers.
The main goal is to offer a valid and professional solution for
designers who want to use Linux as their main OS.

%prep
%setup
sed -i "s|data/screenshots/||" README.md
sed -i "s|Categories=.*|Categories=GTK;Graphics;2DGraphics;|" data/com.github.akiraux.akira.desktop.in.in
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
xvfb-run %meson_test

%files -f %{appname}.lang
%doc AUTHORS COPYING README.md akira-logo-transparent.png data/screenshots/screenshot-1.png
%_bindir/%appname
%_desktopdir/com.github.akiraux.akira.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_iconsdir/hicolor/*/mimetypes/%{appname}.svg
%_datadir/metainfo/%{appname}.appdata.xml
%_datadir/mime/packages/%{appname}.mime.xml
%_pixmapsdir/%{appname}/akira-banner.jpg

%changelog
* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.0.16-alt1
- Initial build for Sisyphus
