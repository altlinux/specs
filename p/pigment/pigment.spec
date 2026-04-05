%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: pigment
Version: 0.5.6
Release: alt1

Summary: Extract color palettes from your images
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/Jeffser/Pigment

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3

BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/appstreamcli
BuildRequires: /usr/bin/blueprint-compiler

Requires: libadwaita-gir
Requires: libportal-gir
Requires: python3-module-colorthief
Requires: python3-module-pygobject3
Requires: python3-module-pycairo
Requires: python3-module-pydbus

BuildArch: noarch

%description
Pigment allows you to extract a palette of colors from your
images offline. You can select the speed and accuracy by
modifying the number and quality of colors.

%prep
%setup
sed -i 's|^Categories=.*|Categories=Graphics;2DGraphics;|' data/com.jeffser.Pigment.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %{name}.lang
%doc CONTRIBUTING.md COPYING README.md
%_bindir/pigment
%_desktopdir/com.jeffser.Pigment.desktop
%_datadir/dbus-1/services/com.jeffser.Pigment.service
%_datadir/glib-2.0/schemas/com.jeffser.Pigment.gschema.xml
%_iconsdir/hicolor/scalable/apps/com.jeffser.Pigment.svg
%_iconsdir/hicolor/symbolic/apps/com.jeffser.Pigment-symbolic.svg
%_datadir/metainfo/com.jeffser.Pigment.metainfo.xml
%dir %_datadir/pigment
%_datadir/pigment/pigment.gresource
%dir %_datadir/pigment/pigment
%_datadir/pigment/pigment/__init__.py
%_datadir/pigment/pigment/main.py
%_datadir/pigment/pigment/widgets.py
%_datadir/pigment/pigment/window.py


%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.6-alt1
- Initial build for Sisyphus
