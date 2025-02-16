%define _unpackaged_files_terminate_build 1

Name: mate-wayland-session
Version: 1.28.3
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
Requires: firedecor
Requires: xorg-xwayland
Requires: wayfire-config-manager
Requires: wdisplays

# MATE components from session/mate-wayland-components.sh script
Requires: mate-polkit
Requires: mate-notification-daemon

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
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README TODO
%_bindir/mate-wayland.sh
%_bindir/mate-wayland-components.sh
%_datadir/doc/firedecor/firedecor.config
%dir %_datadir/firedecor/button-styles/mate
%_datadir/firedecor/button-styles/mate/*
%_datadir/glib-2.0/schemas/*.gschema.override
%_datadir/wayland-sessions/MATE.desktop

%changelog
* Sat Feb 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.28.3-alt1
- Initial build for Sisyphus
