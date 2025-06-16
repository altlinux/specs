%define _unpackaged_files_terminate_build 1

Name: gnome-console-keybind
Version: 0.1.3
Release: alt1

Summary: Setting the keyboard shortcut to launch the console 
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://altlinux.space/armatik/gnome-console-keybind
VCS: https://altlinux.space/armatik/gnome-console-keybind

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: dconf

%description
Sets the additional keyboard shortcut Ctrl+Alt+T to launch the console.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_sysconfdir/dconf/db/local.d/00-console-keybind

%changelog
* Thu Jun 05 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.3-alt1
- Initnal build.
