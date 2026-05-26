%def_disable snapshot

%define _name gpu-profile-selector
%define __name GPU_profile_selector
%define ego_ver 26
%define ver_major %ego_ver
%define beta %nil
%define uuid %{__name}@lorenzo9904.gmail.com
%define xdg_name org.gnome.shell.extensions.%__name
%define gettext_domain %_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1
Epoch: 1

Summary: GPU profile selector extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/LorenzoMorelli/GPU_profile_selector

Vcs: https://github.com/LorenzoMorelli/GPU_profile_selector.git

BuildArch: noarch

%if_disabled snapshot
#Source: %url/archive/%version%beta/%__name-%version%beta.tar.gz
Source: %url/archive/v%version%beta/gnome-%version%beta.tar.gz
%else
Source: %__name-%version%beta.tar
%endif

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1
Requires: /usr/bin/pkexec envycontrol

%description
A simple gnome shell extension which provides a simple way to switch
between GPU profiles on Nvidia Optimus systems (i.e laptops with Intel +
Nvidia or AMD + Nvidia configurations) in a few clicks.

In particular this extension is a graphic interface for
[envycontrol](https://github.com/geminis3/envycontrol) program.

%prep
%setup -n %__name-%version%beta

%install
mkdir -p %buildroot%_datadir/{gnome-shell/extensions/%uuid,glib-2.0/schemas}
cp -ar *.js* img lib ui %buildroot%_datadir/gnome-shell/extensions/%uuid/
cp -a schemas/%xdg_name.gschema.xml %buildroot%_datadir/glib-2.0/schemas/

%files
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Mon May 25 2026 Yuri N. Sedunov <aris@altlinux.org> 1:26-alt1
- 26 (GNOME 50 supported)
- switched to ego versioning

* Wed Oct 15 2025 Yuri N. Sedunov <aris@altlinux.org> 49-alt1
- 49

* Wed Apr 30 2025 Yuri N. Sedunov <aris@altlinux.org> 48-alt1
- first build for Sisyphus

