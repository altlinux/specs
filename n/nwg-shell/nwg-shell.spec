%define _unpackaged_files_terminate_build 1

Name: nwg-shell
Version: 0.5.50
Release: alt1

Summary: Meta-package for the nwg-shell project
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/nwg-piotr/nwg-shell

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: foot
Requires: gnome-themes-extra
Requires: ImageMagick
Requires: jq
Requires: typelib(AyatanaAppIndicator3)
Requires: NetworkManager-applet-gtk
Requires: papirus-icon-theme
Requires: playerctl
Requires: polkit-gnome
Requires: python3
Requires: swappy
Requires: sway
Requires: swayidle
Requires: swaylock
Requires: swaybg
Requires: wl-clipboard
Requires: xorg-xwayland
Requires: wlsunset
Requires: azote
Requires: gopsuinfo
Requires: nwg-dock
Requires: nwg-drawer
Requires: nwg-menu
Requires: nwg-look
Requires: nwg-panel
Requires: nwg-hello
Requires: nwg-shell-config
Requires: nwg-shell-wallpapers
Requires: nwg-displays
Requires: nwg-clipman
Requires: nwg-readme-browser
Requires: nwg-icon-picker
Requires: swaync
Requires: gtklock
Requires: gtklock-module-userinfo
Requires: gtklock-powerbar-module
Requires: gtklock-playerctl-module
Requires: xdg-user-dirs

%filter_from_requires /^.usr.bin.hyprctl/d
%filter_from_requires /grim/d
%filter_from_requires /slurp/d
%filter_from_requires /hyprland/d

%description
nwg-shell is a GTK3-based shell for sway and Hyprland Wayland
compositors. The project provides a common configuration
tool (nwg-shell-config) that allows you to configure the system in a
graphical UI, and a range of components such as nwg-panel (system panel),
nwg-drawer (application launcher), nwg-dock (system dock) or nwg-menu
(XDG-style menu). It also includes several native tools as nwg-look
(look and feel GTK settings editor), nwg-displays (display configuration
tool), Azote (wallpaper manager), nwg-clipman (clipboard history
manager), nwg-icon-picker (icon browser with textual search),
nwg-readme-browser (documentation viewer) and nwg-hello (login manager).

Scripts and utilities such as autotiling (script for sway to
automatically switch the horizontal / vertical window split orientation)
and gospuinfo (a command to display system usage info) are used in the
background. The shell also utilizes third party software as swaync
(notification center), gtklock / swaylock (screen lockers) and more.

The nwg-shell package itself acts as a metapackage and installer of
default configuration files.

User may want to install the following additional optional components:

* hyprland - supported alternative Wayland compositor;
* nwg-dock-hyprland - nwg-dock for Hyprland;
* firefox - suggested web browser;
* typobuster - suggested text editor;
* thunar - suggested file manager.

%prep
%setup
%patch -p1
sed -i 's|^Categories=.*|Categories=Utility;Documentation;|' nwg-readme.desktop

%build
%pyproject_build

%install
%pyproject_install
# NOTE renaming screenshot -> nwg-screenshot-cli
#      to prevent file conflict on /usr/bin/screenshot with mini-screenshoter package
mv -v scripts/screenshot scripts/nwg-screenshot-cli

# installing additional files
install -Dm 755 scripts/nwg-screenshot-cli -t %{buildroot}/%{_bindir}
install -Dm 644 %{name}.jpg %{buildroot}/%{_datadir}/backgrounds/%{name}.jpg
install -Dm 644 nwg-readme.desktop %{buildroot}/%_desktopdir/nwg-readme.desktop

%post
echo "NOTE: nwg-shell needs additional configuration for Sway and,"
echo "      optionally Hyprland."
echo "      Depending on your choice, run one of the below commands"
echo "      as normal user:"
echo "          nwg-shell-installer -a # Sway"
echo "          nwg-shell-installer -a -hypr # Hyprland"
echo "      Then logout and login back to Sway or Hyprland session."
echo "      More information is available at nwg-shell project website:"
echo "                https://nwg-piotr.github.io/nwg-shell/ ."

%files
%doc LICENSE README.md
%python3_sitelibdir/nwg_shell/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_bindir/nwg-shell
%_bindir/nwg-shell-installer
%_bindir/nwg-screenshot-cli
%_desktopdir/nwg-readme.desktop
%_datadir/backgrounds/*

%changelog
* Fri Apr 03 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.50-alt1
- New version 0.5.50.

* Wed Mar 04 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.49-alt3
- Use gtklock-module-userinfo instead of gtklock-userinfo-module.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.49-alt2
- Applied repocop fix for freedesktop-categories

* Sun Jun 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.49-alt1
- New version 0.5.49.

* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.48-alt1
- Initial build for Sisyphus
