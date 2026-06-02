%define __name Pop
%define _name pop

Name: icon-theme-%_name
Version: 3.5.0
Release: alt1

Summary: System76 Pop icon theme for Linux
License: CC-BY-SA-4.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/icon-theme

Vcs: https://github.com/pop-os/icon-theme.git

Source: %url/archive/v%version/%name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

#Inherits=Pop-Extra,pop-os-branding,Adwaita,hicolor
Requires:  icon-theme-adwaita icon-theme-hicolor

%description
Pop_Icons is the icon theme for Pop!_OS. It uses a semi-flat design with
raised 3D motifs to help give depth to icons. Pop_Icons take inspiration
from the Adwaita GNOME Icons.

%prep
%setup -n icon-theme-%version

%build
%meson
%meson_build

%install
%meson_install

%files
%_iconsdir/%__name
%doc README.md

%changelog
* Tue Jun 02 2026 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- first build for Sisyphus


