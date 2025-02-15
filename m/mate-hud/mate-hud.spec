%define _unpackaged_files_terminate_build 1

Name: mate-hud
Version: 22.10.3
Release: alt1

Summary: Run menubar commands, much like the Unity 7 HUD
License: GPLv2
Group: Graphical desktop/MATE
URL: https://github.com/ubuntu-mate/mate-hud

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-distutils-extra

Requires: rofi
Requires: vala-panel-appmenu-gtk-module

BuildArch: noarch

Source: %name-%version.tar

%description
A Heads-Up Display (HUD) allows you to search through an application's
appmenu. So if you're trying to find that single filter in Gimp but
can't remember which filter category it fits into or if you can't
recall if preferences sits under File, Edit or Tools on your favourite
browser, you can just search for it rather than hunting through the
menus.

%prep
%setup

# add missed shebang
sed  -i '1i #!/usr/bin/python3' usr/lib/mate-hud/getkey_dialog.py

%build
%python3_build

%install
%python3_install

%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_libexecdir/%name/
%python3_sitelibdir/mate_hud-*/
%_datadir/glib-2.0/schemas/org.mate.hud.gschema.xml
%dir %_datadir/mate/
%dir %_datadir/mate/autostart/
%_datadir/applications/hud-settings.desktop
%_datadir/mate/autostart/%{name}.desktop
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/%{name}.*
%_datadir/rofi/themes/%{name}*.rasi

%changelog
* Sat Feb 15 2025 Nikolay Strelkov <snk@altlinux.org> 22.10.3-alt1
- Initial build for Sisyphus
