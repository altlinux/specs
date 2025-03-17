%define _unpackaged_files_terminate_build 1

Name: qadwaitadecorations-activator-gnome
Version: 0.1.1
Release: alt1

Summary: Enables QT Adwaita decorations for GNOME on Wayland
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/Armatik/qadwaitadecorations-controller
VCS: https://gitlab.gnome.org/Armatik/qadwaitadecorations-controller

Source: %name-%version.tar

BuildArch: noarch

Requires: qadwaitadecorations-qt5
Requires: qadwaitadecorations-qt6

%description
Provides QT_WAYLAND_DECORATIONS environment variable with value 'adwaita'.

%prep
%setup

%install
install -Dpm755 qt_adwaita_decorations.sh %buildroot%_sysconfdir/profile.d/%name.sh

%files
%_sysconfdir/profile.d/%name.sh

%changelog
* Fri Mar 07 2025 Alexey Volkov <qualimock@altlinux.org> 0.1.1-alt1
- initial build for ALT
