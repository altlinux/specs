%def_disable snapshot

%define _name pipewire-settings
%define ver_major 10
%define beta %nil
%define uuid %_name@gaheldev.github.com
%define gettext_domain %_name

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: Pipewire Settings extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/gaheldev/pipewire-settings

Vcs: https://github.com/gaheldev/pipewire-settings.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

Requires: gnome-shell >= 46
Requires: typelib(Adw) = 1

%description
GNOME extension to set Pipewire's buffer size and samplerate.

%prep
%setup -n %_name-%version%beta

%build

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/
cp -r %uuid %buildroot%_datadir/gnome-shell/extensions/

%files
%_datadir/gnome-shell/extensions/%uuid/
%doc README.md

%changelog
* Mon Jun 01 2026 Yuri N. Sedunov <aris@altlinux.org> 10-alt1
- 10

* Mon May 18 2026 Yuri N. Sedunov <aris@altlinux.org> 3-alt2
- updated to v3-23-g2f88bf1 (GNOME 50 supported)

* Sat Jan 10 2026 Yuri N. Sedunov <aris@altlinux.org> 3-alt1
- first build for Sisyphus (v3-22-g41bbf18)

