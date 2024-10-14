%define plugin hyprhook

Name: hyprland-plugin-%plugin
Version: 0.42.0
Release: alt1
License: MIT

Summary: A plugin for Hyprland that can call a script when an event occurs

Group: Graphical desktop/Other

Url: https://github.com/Hyprhook/Hyprhook

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: gcc-c++

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libglvnd)

%description
Hyprhook is a plugin for Hyprland that allows you to run scripts
when specific events occur. It acts as a proxy to make event
information available outside of C++ code, passing relevant
data as JSON parameters to your scripts.

%prep
%setup

%build
%make_build -C %plugin all

%install
install -d %buildroot%_libdir/hyprland

install %plugin/%plugin.so %buildroot%_libdir/hyprland/

%files
%_libdir/hyprland/%plugin.so

%changelog
* Mon Oct 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.42.0-alt1
- Initial build
