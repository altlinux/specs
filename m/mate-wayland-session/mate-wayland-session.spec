%define _unpackaged_files_terminate_build 1

Name: mate-wayland-session
Version: 1.28.5
Release: alt1

Summary: MATE wayland session manager
License: GPL-2.0
Group: Graphical desktop/MATE
Url: https://github.com/mate-desktop/mate-wayland-session

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: mate-common

# Wayland specifics (from README.md and by testing)
Requires: wayfire
Requires: xorg-xwayland
Requires: wayfire-config-manager
Requires: wdisplays

# MATE components from session/mate-wayland-components.sh script
Requires: mate-polkit
Requires: mate-notification-daemon
Requires: NetworkManager-applet-gtk
Requires: blueman
Requires: gnome-keyring
Requires: wf-shell
Requires: mate-panel
Requires: mate-file-manager
Requires: polkit
Requires: mate-settings-daemon

# Useful minimal set of packages
Requires: fonts-ttf-liberation
Requires: mate-menus
Requires: mate-terminal
Requires: caja-open-terminal
Requires: mate-icon-theme
Requires: icon-theme-hicolor

%description
mate-wayland-session contains the MATE wayland session manager, which
is running inside Wayfire Wayland compositor.

%prep
%setup
%patch -p1

%build
NOCONFIGURE=1 mate-autogen
%configure

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README.md TODO
%_bindir/mate-wayland.sh
%_bindir/mate-wayland-components.sh
%_datadir/glib-2.0/schemas/*.gschema.override
%_datadir/wayland-sessions/MATE.desktop

%changelog
* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 1.28.5-alt1
- New version 1.28.5.

* Mon Jan 12 2026 Nikolay Strelkov <snk@altlinux.org> 1.28.4-alt3
- Updated to the latest commit d2d8675.
- Adjusted dependencies and path to wayfire.ini.

* Thu Aug 28 2025 Nikolay Strelkov <snk@altlinux.org> 1.28.4-alt2
- Exclude leftovers of firedecor, as it is now stale and do not build.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.28.4-alt1
- New version 1.28.4.

* Sat Feb 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.28.3-alt1
- Initial build for Sisyphus
