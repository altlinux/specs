%define plugin Hyprspace

Name: hyprland-plugin-hyprspace
Version: 0.42.0
Release: alt1
License: GPL-2.0

Summary: Workspace overview plugin for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/KZDKM/Hyprspace

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: gcc-c++

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libglvnd)

%description
A plugin for Hyprland that implements a workspace overview feature 
similar to that of KDE Plasma, GNOME and macOS, aimed to provide 
a efficient way of workspace and window management.

%prep
%setup

%build
%make_build all 

%install
install -d %buildroot%_libdir/hyprland

install %plugin.so %buildroot%_libdir/hyprland/

%files
%_libdir/hyprland/%plugin.so

%changelog
* Sun Oct 13 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.42.0-alt1
- Initial build
