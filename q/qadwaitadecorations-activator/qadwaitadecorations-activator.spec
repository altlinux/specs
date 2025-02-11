%define _unpackaged_files_terminate_build 1

Name: qadwaitadecorations-activator
Version: 0.1.0
Release: alt1

Summary: Enables QT Adwaita decorations for Wayland
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/Armatik/qadwaitadecorations-controller
VCS: https://gitlab.gnome.org/Armatik/qadwaitadecorations-controller

Source0: %name-%version.tar

BuildArch: noarch

Requires: qadwaitadecorations-qt5
Requires: qadwaitadecorations-qt6

%description
Provides QT_WAYLAND_DECORATIONS environment variable with value 'adwaita'.

%prep
%setup

%install
install -Dpm755 qt_adwaita_decorations.sh %buildroot%_sysconfdir/profile.d/qt_adwaita_decorations.sh

%files
%_sysconfdir/*

%changelog
* Mon Feb 10 2025 Alexey Volkov <qualimock@altlinux.org> 0.1.0-alt1
- Initial build for ALT
